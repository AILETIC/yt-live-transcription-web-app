# WebApp Audio Transcription

This web application allows you to transcribe audio locally on your computer in real-time, without the need to upload a file. You can simply press the Start button and the app will provide live audio transcriptions. The application is built using Flask for the backend and JavaScript for the frontend.

## Installation

To install and run the application, follow these steps:

1. Clone the repository: `git clone https://github.com/AILETIC/yt-live-transcription-web-app.git`
2. Install the required dependencies using pip: `pip install -r requirements.txt`

## Usage

1. Run the Flask server by executing the following command:
   ```bash
   python app.py
   ```
2. Open your web browser and enter the following URL: `http://localhost:8000`
3. On the web page, you will see a Start button and a Stop button. Click the Start button to begin audio recording.
4. While the audio is being recorded, transcriptions will be displayed in the text area below.
5. Click the Stop button to end the audio recording.

## API Interface

The application also provides an API endpoint to transcribe audio. To use this API, follow these steps:

1. Send a POST request to the following endpoint: `http://localhost:8000/api/transcribe/`
2. Include the audio file in the request body as a form-data parameter with the key `audio`.
3. The audio file must be in WAV format.
4. The API will respond with a JSON object containing the transcribed text.

Here is an example using cURL:

```bash
curl -X POST -F "audio=@/path/to/audio.wav" http://localhost:8000/api/transcribe/
```

The API response will be in the following format:
```json
{
  "success": true,
  "data": "<transcribed-text>"
}
```

Note: Replace `http://localhost:8000` with the appropriate URL if the application is hosted elsewhere.
