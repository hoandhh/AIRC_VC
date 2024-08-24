import time
import models.yolo_llm.get_person as get_person
import models.yolo_llm.get_data as get_data
import models.yolo_llm.gemini_api as gemini_api
import cv2

# cap = cv2.VideoCapture('')
# if (cap.isOpened()== False): 
#   print("Error opening video stream or file")
  
# count = 0
# while(cap.isOpened()):
#     _, image = cap.read()
#     count += 1
#     if count % 125 == 0:
image = "testimg.png"

start_time = time.time()
get_person.get(image)
end_time1 = time.time()

get_action = get_data.get()
end_time2 = time.time()

result = gemini_api.get_response(get_action)
end_time3 = time.time()

# Tính thời gian chạy
# time_get_person = end_time1-start_time
# time_classifi = end_time2-end_time1
# time_get_prompt = end_time3-end_time2
# time_total = end_time3-start_time
# print(f"Thời gian phát hiện người: {time_get_person:.2f} giây")
# print(f"Thời gian phân loại hành động: {time_classifi:.2f} giây")
# print(f"Thời gian lấy câu nhận xét: {time_get_prompt:.2f} giây")
# print(f"Tổng thời gian: {time_total:.2f} giây")

# In kết quả
print(result)
    # else:
    #     continue