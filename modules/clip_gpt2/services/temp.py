# @title Imports

import clip
import os
import numpy as np
import torch
from typing import Tuple, List, Union, Optional
from transformers import (
    GPT2Tokenizer,
    GPT2LMHeadModel,
    AdamW,
    get_linear_schedule_with_warmup,
)
import skimage.io as io
import PIL.Image

from skimage import io
import PIL
import json
from models.model import ClipCaptionPrefix
from utils.generate_normal import generate2
from utils.generate_beam import generate_beam


N = type(None)
V = np.array
ARRAY = np.ndarray
ARRAYS = Union[Tuple[ARRAY, ...], List[ARRAY]]
VS = Union[Tuple[V, ...], List[V]]
VN = Union[V, N]
VNS = Union[VS, N]
T = torch.Tensor
TS = Union[Tuple[T, ...], List[T]]
TN = Optional[T]
TNS = Union[Tuple[TN, ...], List[TN]]
TSN = Optional[TS]
TA = Union[T, ARRAY]


D = torch.device
CPU = torch.device("cpu")


def get_device(device_id: int) -> D:
    if not torch.cuda.is_available():
        return CPU
    device_id = min(torch.cuda.device_count() - 1, device_id)
    return torch.device(f"cuda:{device_id}")


CUDA = get_device

current_directory = os.getcwd()
save_path = os.path.join(os.path.dirname(current_directory), "pretrained_models")
os.makedirs(save_path, exist_ok=True)
# model_path = "./pretrained_models/resnet50tooth.pt"

# Lấy đường dẫn tuyệt đối của thư mục hiện tại
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, "../"))
model_path = os.path.join(parent_dir, "output", "transformer_weights.pt")

# @title Model


is_gpu = True  # @param {type:"boolean"}

# @title CLIP model + GPT2 tokenizer

device = CUDA(0) if is_gpu else "cpu"
clip_model, preprocess = clip.load("RN50x4", device=device, jit=False)
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# @title Load model weights

prefix_length = 40

model = ClipCaptionPrefix(
    prefix_length,
    clip_length=40,
    prefix_size=640,
    num_layers=8,
    mapping_type="transformer",
)
# Load state dictionary with strict=False to ignore unexpected keys
model.load_state_dict(torch.load(model_path, map_location=CPU), strict=False)

model = model.eval()
device = CUDA(0) if is_gpu else "cpu"
model = model.to(device)

# Print a summary of the loaded model to inspect its structure
# print(model)


image_dir = "./images"
captions_data = []


def get_all_caption(image_dir, captions_data):
    for filename in os.listdir(image_dir):
        if filename.endswith(".jpg") or filename.endswith(
            ".JPG"
        ):  # Add other image extensions if needed
            file_path = os.path.join(image_dir, filename)

            # Extract image ID from filename (assuming filename format is like "000000000123.jpg")
            image_id = os.path.splitext(filename)[0]

            image = io.imread(file_path)
            pil_image = PIL.Image.fromarray(image)
            display(pil_image)

            image = preprocess(pil_image).unsqueeze(0).to(device)

            with torch.no_grad():
                prefix = clip_model.encode_image(image).to(device, dtype=torch.float32)
                prefix = prefix / prefix.norm(2, -1).item()
                prefix_embed = model.clip_project(prefix).reshape(1, prefix_length, -1)

                generated_text_prefix = generate2(model, tokenizer, embed=prefix_embed)

            # Store both image ID and caption
            captions_data.append({"id": image_id, "caption": generated_text_prefix})

    output_file = "captionsval.json"
    with open(output_file, "w") as f:
        json.dump(captions_data, f, indent=4)


def get_single_caption(path):

    use_beam_search = False  # @param {type:"boolean"}

    image = io.imread(path)
    pil_image = PIL.Image.fromarray(image)
    # pil_img = Image(filename=UPLOADED_FILE)
    # display(pil_image)

    image = preprocess(pil_image).unsqueeze(0).to(device)
    with torch.no_grad():
        # if type(model) is ClipCaptionE2E:
        #     prefix_embed = model.forward_image(image)
        # else:
        prefix = clip_model.encode_image(image).to(device, dtype=torch.float32)
        prefix_embed = model.clip_project(prefix).reshape(1, prefix_length, -1)
    if use_beam_search:
        generated_text_prefix = generate_beam(model, tokenizer, embed=prefix_embed)[0]
    else:
        generated_text_prefix = generate2(model, tokenizer, embed=prefix_embed)
    return generated_text_prefix
