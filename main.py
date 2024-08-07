import sys
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import logging
import time
from threading import Thread
from queue import Queue
import socket
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'services')))
from extract_keyframes import extract_key_frames  # Nhập hàm từ module mới

application = Flask(__name__)
CORS(application)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

sessions = {}

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0)
        s.connect(("8.8.8.8", 1))
        IP_CONNECT = s.getsockname()[0]
        s.close()
    except Exception:
        IP_CONNECT = "127.0.0.1"
    return IP_CONNECT

@application.route('/upload_video', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return jsonify({"error": "No video file provided"}), 400

    video_file = request.files['video']
    if video_file.filename == '':
        return jsonify({"error": "No video file selected"}), 400

    session_id = request.form.get('session_id')
    if not session_id:
        return jsonify({"error": "No session ID provided"}), 400

    video_path = f"temp_video_{session_id}.mp4"
    video_file.save(video_path)
    output_folder = f'result_{session_id}'

    sessions[session_id] = {
        "captions": Queue()
    }

    # Gọi hàm extract_key_frames từ module video_processing
    Thread(target=extract_key_frames, args=(video_path, output_folder, 2, session_id, "tooth_captioning")).start()
    return jsonify({"status": "Processing video", "session_id": session_id}), 202

@application.route('/get_captions/<session_id>', methods=['GET'])
def get_captions(session_id):
    if session_id not in sessions:
        return jsonify({"error": "Invalid session ID"}), 400

    try:
        caption = sessions[session_id]["captions"].get(timeout=30)
        if caption == "[DONE]":
            del sessions[session_id]
        return jsonify({"caption": caption})
    except:
        return jsonify({"caption": None}), 204

if __name__ == '__main__':
    HOST_CONNECT = get_local_ip()
    PORT_CONNECT = 5000
    application.run(host=HOST_CONNECT, port=PORT_CONNECT, debug=True)
