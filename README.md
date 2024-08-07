# AIRC_Video_Captioning

#  Chú Thích Hình Ảnh Trong Nha Khoa, Hành Động Trong Lớp Học

Dự án này nhằm phát triển một hệ thống chú thích hình ảnh cho nha khoa, hoặc các hành động trong lớp học, tập trung vào việc tạo ra các chú thích cho hình ảnh và video liên quan đến răng hoặc các hành động trong lớp học. Hệ thống sẽ sử dụng các kỹ thuật học sâu để tự động mô tả nội dung của hình ảnh và video nha khoa, cung cấp các chú thích thông tin để hỗ trợ việc giảng dạy và học tập.

## Table of Contents / Mục Lục
- [Introduction / Giới Thiệu](#introduction)
- [Installation / Cài Đặt](#installation)
  - [Installing Python / Cài Đặt Python](#installing-python)
  - [Installing Git / Cài Đặt Git](#installing-git)
  - [Creating a Virtual Environment / Tạo Môi Trường Ảo](#creating-a-virtual-environment)
  - [Installing Required Packages / Cài Đặt Các Gói Cần Thiết](#installing-required-packages)
- [Usage / Cách Sử Dụng](#usage)
- [Contributing / Đóng Góp](#contributing)
- [License / Giấy Phép](#license)

## Introduction / Giới Thiệu
Chú thích hình ảnh là một nhiệm vụ kết hợp giữa thị giác máy tính và xử lý ngôn ngữ tự nhiên để tạo ra các mô tả văn bản cho hình ảnh. Trong bối cảnh giáo dục nha khoa, dự án này nhằm áp dụng các kỹ thuật chú thích hình ảnh để tự động tạo ra các chú thích cho hình ảnh và video nha khoa, chẳng hạn như:

- Hình ảnh về răng và bệnh về răng
- Các hoạt động trong lớp học 

Bằng cách cung cấp các chú thích thông tin cho những tài liệu hình ảnh này, dự án nhằm nâng cao khả năng 

## Installation / Cài Đặt

### Installing Python / Cài Đặt Python
1. Cài đặt Python và môi trường ảo:

   ```bash
   sudo apt-get update
   sudo apt-get upgrade
   sudo apt install software-properties-common
   sudo add-apt-repository ppa:deadsnakes/ppa
   sudo apt update
   sudo apt install python3.11
   sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1
   sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 2
   sudo update-alternatives --config python3
   sudo apt install python3-pip
   python3 -m pip install virtualenv
   sudo apt install python3.11-venv

Thêm đường dẫn cho virtualenv:
```sh
nano ~/.bashrc
```

Thêm dòng sau vào cuối tệp:
```sh
export PATH="$PATH:/home/visual/.local/bin"
```
Áp dụng các thay đổi:
```sh
source ~/.bashrc
```
2.  Installing Git / Cài Đặt Git

Cài đặt Git bằng cách sử dụng lệnh sau:
```sh
sudo apt-get install git
```

Creating a Virtual Environment / Tạo Môi Trường Ảo
Clone dự án từ GitHub:
Mở terminal (hoặc Command Prompt trên Windows) và chạy lệnh sau để clone dự án:
bash
```sh
git clone https://github.com/leodqk/CLIP_Captioning.git
```
Tạo thư mục pretrained_models:
Sau khi clone xong, bạn cần chuyển vào thư mục dự án và tạo thư mục pretrained_models:

```sh
cd CLIP_Captioning
mkdir pretrained_models
```

Tải model từ Google Drive và lưu vào trong thư mục pretrained_models này: Tải Model.

3. Installing Required Packages / Cài Đặt Các Gói Cần Thiết

Cài đặt các gói từ requirements.txt:
```sh
pip install -r requirements.txt
```
Nếu gặp lỗi với scikit_image, làm theo các bước sau:

Cài đặt các gói phụ thuộc:
```sh
sudo apt-get install build-essential python3-dev python3-pip
sudo apt-get install libatlas-base-dev
```

Cập nhật pip:
```sh
python3 -m pip install --upgrade pip
```

Cài đặt lại scikit-image:
```sh
pip install scikit-image
```

Sử dụng phiên bản pre-built:
Nếu bạn gặp khó khăn trong việc cài đặt từ mã nguồn, bạn có thể thử cài đặt phiên bản pre-built của scikit-image từ PyPI:
```sh
pip install --upgrade scikit-image
```

Cài đặt các gói bổ sung:
```sh
pip3 install git+https://github.com/openai/CLIP.git
pip3 install scikit-image
pip3 install transformers
pip3 install ipython
pip3 install gdown
```

# # Usage / Cách Sử Dụng
Hướng dẫn sử dụng sẽ được cập nhật trong các phiên bản sau của dự án.
Contributing / Đóng Góp
Chúng tôi hoan nghênh mọi đóng góp từ cộng đồng. Vui lòng mở một vấn đề hoặc gửi yêu cầu kéo nếu bạn có ý tưởng hoặc cải tiến nào.
License / Giấy Phép
Dự án này được cấp phép theo Giấy phép MIT.
text
