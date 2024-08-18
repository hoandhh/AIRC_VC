import os
import sys

__dir__ = os.path.dirname(__file__)
sys.path.append(os.path.join(__dir__, "../"))

from queue import Queue
from flask import request, jsonify, send_file
from services.caption_service import extract_key_frames
from services.video_processing_service import extract_key_frames_from_url
from services.youtube_service import download_youtube_video_as_bytes
from utils.global_vars import sessions
from threading import Thread
import logging
from utils.function_global import is_youtube_url

def upload_video(application):
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

    Thread(target=extract_key_frames, args=(application, video_path, output_folder, session_id)).start()
    return jsonify({"status": "Processing video", "session_id": session_id}), 202

def upload_url(application):
    url = request.form.get('url')  
    session_id = request.form.get('session_id')

    if not url or not session_id:
        return jsonify({"error": "URL and session ID are required"}), 400

    sessions[session_id] = {
        "captions": Queue(),
        "youtube_video_downloaded": False
    }

    if is_youtube_url(url):
        Thread(target=process_youtube_video, args=(url, session_id)).start()
        return jsonify({"status": "Downloading YouTube video", "session_id": session_id}), 202
    else:
        Thread(target=extract_key_frames_from_url, args=(application, url, f'result_{session_id}', session_id)).start()
        return jsonify({"status": "Processing regular video", "session_id": session_id}), 202

def process_youtube_video(url, session_id):
    video_bytes = download_youtube_video_as_bytes(url)
    if video_bytes:
        video_file_path = f"downloaded_video_{session_id}.mp4"
        with open(video_file_path, "wb") as f:
            f.write(video_bytes.getvalue())

        sessions[session_id]["youtube_video_downloaded"] = True
    else:
        logging.error("Failed to download YouTube video.")

def get_video(session_id):
    video_file_path = f"downloaded_video_{session_id}.mp4"
    
    if os.path.exists(video_file_path):
        return send_file(video_file_path, as_attachment=True)
    else:
        return jsonify({"error": "Video not found."}), 404

def start_captioning(application, session_id):
    if session_id not in sessions:
        return jsonify({"error": "Invalid session ID"}), 400
    
    if sessions[session_id].get("youtube_video_downloaded", False):
        video_file_path = f"downloaded_video_{session_id}.mp4"
        output_folder = f'result_{session_id}'
        
        Thread(target=extract_key_frames, args=(application, video_file_path, output_folder, session_id)).start()
        return jsonify({"status": "Captioning started", "session_id": session_id}), 202
    else:
        return jsonify({"error": "Video not downloaded yet."}), 404

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
