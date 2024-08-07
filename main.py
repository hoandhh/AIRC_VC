import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'services/extract_keyframes')))
import extract_keyframes

extract_keyframes.extract_key_frames("E:/AIRC2024/AIRC_VC/services/test2.mp4", "output", 2, "test1", "tooth_captioning")