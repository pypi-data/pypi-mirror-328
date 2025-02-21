# pmsh-ocr

Primary Math Screen Handwriting OCR (pmsh-ocr) is a Python package for recognizing primary school mathematical expressions handwritten on screen.

## Features

- Recognize primary mathematical expressions handwritten on screen
- Vocabulary: `['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '-', '<', '=', '>', '\frac', '{', '}']`
- Support recognizing expression with input reference text, e.g. answer
- Model trained with max token length 40

## Installation

```bash
pip install pmsh-ocr
```

## Usage

```python
import cv2

from pmsh import PMSHOCR

ocr = PMSHOCR()

image = cv2.imread('path_to_image')
ref_text = 'some reference txt'
result = ocr.inference(image, ref_text)
print(result)
```

example of result:

```json
{
    "box": [0, 0, 384, 288], # [x1, y1, x2, y2]
    "ctc_text": "-15",       # text not referring the input ref_text
    "ctc_prob": 0.999,
    # if the input ref_text is None, the following keys will not output
    "ar_text": "-15",        # text referring the input ref_text
    "ar_prob": 0.92
}
```

## License

This project is licensed under the MIT License.
