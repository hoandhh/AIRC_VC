import os
import sys

__dir__ = os.path.dirname(__file__)
sys.path.append(os.path.join(__dir__, "../services"))
import time
import modules.get_captions.models.yolo_llm.get_person as get_person
import modules.get_captions.models.yolo_llm.get_data as get_data
import modules.get_captions.models.yolo_llm.gemini_api as gemini_api

def caption_image(image_path):
    """
    Xử lý hình ảnh để phát hiện người, phân loại hành động và lấy câu nhận xét.

    Parameters:
    - image_path (str): Đường dẫn tới hình ảnh cần xử lý.

    Returns:
    - result (str): Kết quả từ Gemini API.
    """

    # Bắt đầu tính thời gian cho bước phát hiện người
    # start_time = time.time()
    get_person.get(image_path)
    # end_time1 = time.time()

    # Bắt đầu tính thời gian cho bước phân loại hành động
    get_action = get_data.get()
    # end_time2 = time.time()

    # Bắt đầu tính thời gian cho bước lấy câu nhận xét
    result = gemini_api.get_response(get_action)
    # end_time3 = time.time()

    # Chỉ trả về caption
    return result
