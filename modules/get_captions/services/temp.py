import os
import sys

__dir__ = os.path.dirname(__file__)
sys.path.append(os.path.abspath(os.path.join(__dir__, "../models")))
sys.path.append(os.path.abspath(os.path.join(__dir__, "../utils")))

import clip
import numpy as np
import torch
from models import ClipCaptionPrefix
from utils import generate2, generate_beam
from transformers import GPT2Tokenizer
from skimage import io
import PIL.Image
import json

def get_device(device_id: int) -> torch.device:
    if not torch.cuda.is_available():
        return torch.device("cpu")
    device_id = min(torch.cuda.device_count() - 1, device_id)
    return torch.device(f"cuda:{device_id}")

def main():
    current_directory = os.getcwd()
    save_path = os.path.join(os.path.dirname(current_directory), "pretrained_models")
    os.makedirs(save_path, exist_ok=True)

    model_path = os.path.join(os.path.dirname(__file__), "..", "output", "transformer_weights.pt")

    is_gpu = True
    device = get_device(0) if is_gpu else "cpu"

    clip_model, preprocess = clip.load("RN50x4", device=device, jit=False)
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

    prefix_length = 40

    model = ClipCaptionPrefix(
        prefix_length,
        clip_length=40,
        prefix_size=640,
        num_layers=8,
        mapping_type="transformer",
    )

    model.load_state_dict(torch.load(model_path, map_location=torch.device("cpu")), strict=False)
    model = model.eval().to(device)

    image_dir = "./images"
    captions_data = []

    def get_all_caption(image_dir, captions_data):
        for filename in os.listdir(image_dir):
            if filename.endswith(".jpg") or filename.endswith(".JPG"):
                file_path = os.path.join(image_dir, filename)

                image_id = os.path.splitext(filename)[0]

                image = io.imread(file_path)
                pil_image = PIL.Image.fromarray(image)
                image = preprocess(pil_image).unsqueeze(0).to(device)

                with torch.no_grad():
                    prefix = clip_model.encode_image(image).to(device, dtype=torch.float32)
                    prefix = prefix / prefix.norm(2, -1).item()
                    prefix_embed = model.clip_project(prefix).reshape(1, prefix_length, -1)

                    generated_text_prefix = generate2(model, tokenizer, embed=prefix_embed)

                captions_data.append({"id": image_id, "caption": generated_text_prefix})

        output_file = "captionsval.json"
        with open(output_file, "w") as f:
            json.dump(captions_data, f, indent=4)

    def get_single_caption(path):
        use_beam_search = False

        image = io.imread(path)
        pil_image = PIL.Image.fromarray(image)
        image = preprocess(pil_image).unsqueeze(0).to(device)

        with torch.no_grad():
            prefix = clip_model.encode_image(image).to(device, dtype=torch.float32)
            prefix_embed = model.clip_project(prefix).reshape(1, prefix_length, -1)
        
        if use_beam_search:
            return generate_beam(model, tokenizer, embed=prefix_embed)[0]
        else:
            return generate2(model, tokenizer, embed=prefix_embed)

if __name__ == "__main__":
    main()
