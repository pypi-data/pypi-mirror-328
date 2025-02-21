import re
from abc import ABC, abstractmethod
from typing import Union

import numpy as np


class BaseTokenizer(ABC):

    def __init__(self, vocabulary_tokens: list[str], specials_first: tuple = (), specials_last: tuple = ()) -> None:
        """Base class for tokenizers. Token may be characters, subwords, or words.

        Args:
            vocabulary_tokens: List of tokens in the vocabulary.
            specials_first: Special tokens to prepend to the list.
            specials_last: Special tokens to append to the list.
        """
        self._itos = specials_first + tuple(vocabulary_tokens) + specials_last
        self._stoi = {s: i for i, s in enumerate(self._itos)}

        long_tokens = [t for t in self._itos if len(t) > 1]
        long_tokens.sort(key=len, reverse=True)
        self.text_separator_regex = re.compile(f'{"|".join(map(re.escape, long_tokens))}' + '|.')

    def __len__(self):
        return len(self._itos)

    def _tokens2ids(self, tokens: list[str]) -> list[int]:
        token_ids = []
        for token in tokens:
            # ignore unknown tokens
            if token in self._stoi:
                token_ids.append(self._stoi[token])
        
        return token_ids

    def _ids2tokens(self, token_ids: list[int], join: bool = True) -> Union[str, list[str]]:
        tokens = [self._itos[i] for i in token_ids]
        return ''.join(tokens) if join else tokens

    @abstractmethod
    def encode(self, labels: list[str]) -> tuple[np.ndarray, np.ndarray]:
        """Encode a batch of labels to a representation suitable for the model.

        Args:
            labels: List of labels. Each can be of arbitrary length.

        Returns:
            padded_batch: np.ndarray, batch representation padded to the max label length. Shape: (N, L)
            seq_lens: np.ndarray, lengths of each label in the batch, not acount BOS EOS. Shape: (N, )
        """
        raise NotImplementedError

    @abstractmethod
    def _filter(self, probs: np.ndarray, ids: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        """Internal method which performs the necessary filtering prior to decoding."""
        raise NotImplementedError

    def decode(self, batch_probs: np.ndarray, batch_ids: np.ndarray, raw: bool = False) -> tuple[list[str], list[float]]:
        """Decode a batch of token distributions.

        Args:
            batch_probs: the probabilities of batch tokens every step in greedy decode, Shape: N, L
            batch_ids: the ids of batch tokens every step in greedy decode, Shape: N, L
            raw: return unprocessed labels (will return list of list of strings)

        Returns:
            batch_tokens: list of string labels (arbitrary length) and
            batch_return_probs: their corresponding sequence probability as a list of float
        """
        batch_tokens = []
        batch_return_probs = []
        for probs, ids in zip(batch_probs, batch_ids):
            if not raw:
                probs, ids = self._filter(probs, ids)
            tokens = self._ids2tokens(ids, not raw)
            if raw:
                return_probs = probs.tolist()
            else:
                return_probs = np.mean(probs).tolist() if len(probs) > 0 else 1.0
            batch_tokens.append(tokens)
            batch_return_probs.append(return_probs)
        return batch_tokens, batch_return_probs


class ARTokenizer(BaseTokenizer):
    BOS = '[BOS]'
    EOS = '[EOS]'
    PAD = '[PAD]'

    def __init__(self, vocabulary_tokens: list[str]) -> None:
        specials_first = (self.EOS,)
        specials_last = (self.BOS, self.PAD)
        super().__init__(vocabulary_tokens, specials_first, specials_last)
        self.eos_id, self.bos_id, self.pad_id = [self._stoi[s] for s in specials_first + specials_last]

    def encode(self, labels: list[str], pad_with_eos: bool = False) -> tuple[np.ndarray, np.ndarray]:
        real_pad_id = self.eos_id if pad_with_eos else self.pad_id
        batch = []
        for label in labels:
            tokens = self.text_separator_regex.findall(label)
            token_ids = self._tokens2ids(tokens)
            # add BOS and EOS token id
            token_ids = [self.bos_id] + token_ids + [self.eos_id]
            batch.append(token_ids)
        seq_lens = [len(ids) for ids in batch]
        max_len = max(seq_lens)
        padded_batch = np.full((len(batch), max_len), real_pad_id)
        for i, ids in enumerate(batch):
            padded_batch[i, :len(ids)] = ids
        seq_lens = np.array(seq_lens) - 2 # exclude BOS and EOS

        return padded_batch, seq_lens

    def _filter(self, probs: np.ndarray, ids: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        eos_idx_arr = np.nonzero(ids == self.eos_id)[0]
        if eos_idx_arr.size > 0:
            eos_idx = eos_idx_arr[0]
        else:
            eos_idx = len(ids) # Nothing to truncate.
        
        # Truncate after EOS
        probs = probs[:eos_idx] # :eos_idx+1 whether include prob. for EOS (if it exists)
        ids = ids[:eos_idx]
        return probs, ids
    
        # ids = ids.tolist()
        # try:
        #     eos_idx = ids.index(self.eos_id)
        # except ValueError:
        #     eos_idx = len(ids)  # Nothing to truncate.
        # # Truncate after EOS
        # ids = ids[:eos_idx]
        # probs = probs[: eos_idx]  # but include prob. for EOS (if it exists)
        # return probs.tolist(), ids


class CTCTokenizer(BaseTokenizer):
    BLANK = '[BLANK]'

    def __init__(self, vocabulary_tokens: list[str]) -> None:
        # BLANK uses index == 0 by default
        super().__init__(vocabulary_tokens, specials_first=(self.BLANK,))
        self.blank_id = self._stoi[self.BLANK]

    def encode(self, labels: list[str]) -> tuple[np.ndarray, np.ndarray]:
        # We use a padded representation since we don't want to use CUDNN's CTC implementation
        batch = []
        for label in labels:
            tokens = self.text_separator_regex.findall(label)
            token_ids = self._tokens2ids(tokens)
            batch.append(token_ids)
        seq_lens = [len(ids) for ids in batch]
        max_len = max(seq_lens)
        padded_batch = np.full((len(batch), max_len), self.blank_id)
        for i, ids in enumerate(batch):
            padded_batch[i, :len(ids)] = ids
        seq_lens = np.array(seq_lens)

        return padded_batch, seq_lens

    def _filter(self, probs: np.ndarray, ids: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        selection = np.ones(len(ids), dtype=bool)
        selection[1:] = ids[1:] != ids[:-1]  # Remove duplicate tokens
        selection &= ids != self.blank_id  # Remove BLANKs
        probs = probs[selection]
        ids = ids[selection]
        return probs, ids
