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
        └── video_controller.py
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
        └── 📁Yolo_LLM   # Bổ sung sau
        └── 📁Clip_Gpt2
            └── 📁models
                └── __init__.py
                └── model.py    # Các model cần sử dụng
            └── 📁output
                └── temp.txt
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
        └── routes.py
    └── 📁scripts
        └── automation_script.py
        └── performance_measurement.py
        └── project_management.py
    └── 📁services
        └── __init__.py
        └── caption_service.py
        └── video_processing_service.py
        └── youtube_service.py
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
