from ultralytics import YOLO
import os
from collections import Counter
import shutil

def get():
    
    # Load mô hình YOLO đã huấn luyện
    model = YOLO('best.pt')  # Thay thế bằng mô hình bạn muốn sử dụng

    folder_path = 'runs/detect'
    subfolders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
    latest_subfolder = max(subfolders, key=lambda x: os.path.getctime(os.path.join(folder_path, x)))
    image_folder = './runs/detect/' + latest_subfolder + '/' + 'crops/person'

    # Khởi tạo danh sách để lưu nhãn của ảnh
    labels = []
    results = []

    # Duyệt qua tất cả các ảnh trong thư mục
    for image_file in os.listdir(image_folder):
        if image_file.lower().endswith(('.png', '.jpg', '.jpeg')):  # Thay đổi các định dạng nếu cần
            image_path = os.path.join(image_folder, image_file)
            
            # Phân loại ảnh
            results.append(model.predict(source=image_path))

    name = []
    for result in results:
        name.append(model.names[int(result[0].probs.top1)])
    label_counts = Counter(name)
    label_counts_string = ','.join(f"{label}: {count}" for label, count in label_counts.items())
    # shutil.rmtree("./runs/detect")
    return label_counts_string




        





