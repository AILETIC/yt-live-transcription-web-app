from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests, time
import whisper
from io import BytesIO

app = Flask(__name__)
CORS(app)

model = whisper.load_model("base")
def transcribe_audio(audio_file, language="en"):
    output = model.transcribe(
        audio_file, 
        fp16=False, # cpu
        word_timestamps=False, # word timestamps
        condition_on_previous_text=False, # refresh each time
        initial_prompt="", # refresh each time
        language=language
    )
    return output["text"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/api/transcribe/', methods=['POST'])
def transcribe():
    
    if 'audio' not in request.files:
        return jsonify({"error": "Invalid data!"}), 400

    audio = request.files['audio']
    audio.save("audio.wav")
    text = transcribe_audio("audio.wav") 

    return jsonify({"success": True, "data": text}), 200

if __name__ == "__main__":
    app.run(debug=True, port=8000)