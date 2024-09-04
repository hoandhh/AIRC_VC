```
└── 📁AIRC_VC
    └── 📁.git
    └── 📁configs
        └── __init__.py
        └── app_config.py
        └── config.py
        └── db_config.py
        └── logging_config.py
    └── 📁controllers
        └── __init__.py
        └── order_controller.py
        └── product_controller.py
        └── user_controller.py
        └── video_controller.py # thực hiện logic xử lý với video, và trả về phản hồi thích hợp
    └── 📁database
        └── 📁database_access
            └── product_access.py
            └── user_access.py
        └── 📁database_connection
            └── mongo_connection.py
            └── sql_connection.py
        └── 📁database_migration
            └── 001_initial_setup.py
            └── 002_user_table.py
        └── 📁database_models
            └── product_model.py
            └── user_model.py
    └── 📁docs
        └── database.md
        └── design_patterns.md
        └── oop.md
    └── 📁logger
        └── log_formatter.py
        └── logger.py
    └── 📁models
        └── __init__.py
        └── user_model.py
    └── 📁modules   # 2 mô hình khác nhau
        └── 📁yolo_llm   # Bổ sung sau
        └── 📁clip_gpt2
            └── 📁models
                └── __init__.py
                └── model.py    # Transformer, GPT2, Mapping network
            └── 📁output        # Các file pretrained theo từng chủ đề
                └── tooth_caption.pt
                └── classroom_caption.pt
                └── action_caption.pt
            └── 📁services
                └── __init__.py
                └── getcaption.py   # Lấy nhiều caption và lấy một caption
            └── 📁utils
                └── __init__.py
                └── generate_beam.py  # Sinh ngôn ngữ sử dụng beam search
                └── generate_normal.py  # Không dùng beam search
            └── __init__.py
            └── main.py     # Chạy module
        └── __init__.py
    └── 📁output
        └── .gitignore
    └── 📁patterns
        └── base_controller.py
        └── base_model.py
        └── base_object.py
        └── base_service.py
    └── 📁routes
        └── __init__.py
        └── routes.py # các route để quản lý việc tải video lên, xử lý video, tạo phụ đề, và truy xuất phụ đề.
    └── 📁scripts
        └── automation_script.py
        └── performance_measurement.py
        └── project_management.py
    └── 📁services
        └── __init__.py
        └── caption_image_yolo_llm.py # Tạo caption cho ảnh bằng yolo và model mới
        └── caption_service.py #Tạo caption cho mỗi key_frame của video 
        └── video_processing_service.py #Xử lý tạo captions cho video url
        └── youtube_service.py #Tải video từ youtube
    └── 📁tests
        └── __init__.py
        └── test_order.py
        └── test_product.py
        └── test_user.py
        └── test.py
    └── 📁utils
        └── __init__.py
        └── date_utils.py
        └── file_utils.py
        └── function_global.py
        └── global_vars.py
        └── number_utils.py
        └── string_utils.py
    └── .gitignore
    └── main.py
    └── README.md
    └── requirements.txt
    └── setup.py
    └── test.py
```
