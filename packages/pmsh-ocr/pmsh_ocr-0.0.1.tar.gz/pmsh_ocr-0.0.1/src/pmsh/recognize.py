import math

import cv2
import numpy as np
import onnxruntime as ort

from .tokenize import ARTokenizer, CTCTokenizer


RAW_VOCABULARY = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    ".",
    "-",
    "<",
    "=",
    ">",
    "\\frac",
    "{",
    "}",
]

def resize_image_cv(image, dst_shape=(64, 256)):
    imgH, imgW = dst_shape
    h, w = image.shape[:2]
    
    ratio = w / float(h)
    if math.ceil(imgH * ratio) > imgW:
        resized_w = imgW
    else:
        resized_w = int(math.ceil(imgH * ratio))
    real_interpolation = cv2.INTER_AREA if h > imgH else cv2.INTER_LINEAR
    resized_image = cv2.resize(image, (resized_w, imgH), interpolation=real_interpolation)
    # for gray
    if len(resized_image.shape) == 2:
        resized_image = np.expand_dims(resized_image, axis=-1)

    if resized_w < imgW:
        channel = resized_image.shape[2]
        padded_image = np.ones((imgH, imgW, channel), dtype=np.uint8) * 255
        padded_image = padded_image.astype(np.uint8)
        padded_image[:, :resized_w] = resized_image
    else:
        padded_image = resized_image
    return padded_image


class Recognizer:
    def __init__(self, model_dir, vocabulary=RAW_VOCABULARY, input_shape=(64, 256)):
        self.model_dir = model_dir
        self.ctc_model_path = model_dir + "/encoder_ctc.onnx"
        self.ctc_model_session = ort.InferenceSession(self.ctc_model_path)
        self.ar_model_path = model_dir + "/decoder_loop.onnx"
        self.ar_model_session = ort.InferenceSession(self.ar_model_path)

        self.raw_vocabulary = vocabulary
        self.ctc_tokenizer = CTCTokenizer(vocabulary)
        self.ar_tokenizer = ARTokenizer(vocabulary)

        self.input_shape = input_shape

    def inference(self, image, ref_text=None):
        norm_image = resize_image_cv(image, self.input_shape)
        norm_image = norm_image.transpose(2, 0, 1)
        norm_image = np.expand_dims(norm_image, axis=0).astype(np.float32)

        ctc_output_ids, ctc_output_probs, output_feature = self.ctc_model_session.run(
            ["output_ids", "output_probs", "output_feature"], 
            {"input_image": norm_image}
        )
        ctc_final_text, ctc_final_prob = self.ctc_tokenizer.decode(ctc_output_probs, ctc_output_ids)
        result = {"ctc_text": ctc_final_text[0], "ctc_prob": ctc_final_prob[0]}

        if ref_text:
            batch_ref_ids, seq_lens = self.ar_tokenizer.encode([ref_text], pad_with_eos=True)
            batch_ref_ids = batch_ref_ids[:, 1:seq_lens[0] + 1] # exclude BOS and EOS
            # batch size is 1, so ref_key_padding_mask all zeros, has no effect
            ref_key_padding_mask = np.zeros((1, 1, 1, seq_lens[0]), dtype=np.float32)
            ar_output_ids, ar_output_probs = self.ar_model_session.run(
                ["output_tgt_ids", "output_tgt_probs"],
                {
                    "input_feature": output_feature,
                    "input_ref_ids": batch_ref_ids,
                    "input_ref_key_padding_mask": ref_key_padding_mask,
                },
            )
            ar_final_text, ar_final_prob = self.ar_tokenizer.decode(ar_output_probs, ar_output_ids)
            result["ar_text"] = ar_final_text[0]
            result["ar_prob"] = ar_final_prob[0]
        
        return result
