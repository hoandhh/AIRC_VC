from services.temp import get_single_caption, get_all_caption


def get_caption(image_path):
    return get_single_caption(image_path)


captions_data = []


def get_all_captions(image_path, captions_data):
    return get_all_caption(image_path, captions_data)

print(get_single_caption("C:/Users/ASUS/Documents/AIRC_VC/modules/clip_gpt2/run.jpg"))