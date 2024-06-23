from flask import request, send_file, jsonify, current_app as app
from .transcribe import transcribe_audio
from .respond import generate_speech_response
import os

@app.route('/upload', methods=['POST'])
def upload_audio():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    transcription = transcribe_audio(file_path)
    response_audio_path = generate_speech_response(transcription)

    return send_file(response_audio_path, mimetype='audio/wav')
