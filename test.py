import os
import sys

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "services/extract_keyframes")
    )
)
import extract_keyframes
import datetime

input_path = ""
output_path = "output"
option = ""

session_id = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

if option == "tooth_captioning":
    extract_keyframes(input_path, output_path, 2, session_id, option)
elif option == "class_captioning":
    extract_keyframes(input_path, output_path, 2, session_id, option)
elif option == "action_captioning":
    extract_keyframes(input_path, output_path, 2, session_id, option)
else:
    print("Invalid option")
