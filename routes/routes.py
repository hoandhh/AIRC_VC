from controllers.video_controller import (
    upload_video,
    upload_url,
    get_video,
    start_captioning,
    get_captions
)

def register_routes(app):
    @app.route('/upload_video', methods=['POST'])
    def handle_upload_video():
        return upload_video(app)
    
    @app.route('/upload_url', methods=['POST'])
    def handle_upload_url():
        return upload_url(app)

    app.route('/get_video/<session_id>', methods=['GET'])(get_video)

    @app.route('/start_captioning/<session_id>', methods=['POST'])
    def handle_start_captioning(session_id):
        return start_captioning(app, session_id)
    
    app.route('/get_captions/<session_id>', methods=['GET'])(get_captions)
