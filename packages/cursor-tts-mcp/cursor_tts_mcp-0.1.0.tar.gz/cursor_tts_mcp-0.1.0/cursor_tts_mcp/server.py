from flask import Flask, request, render_template, jsonify
from gtts import gTTS
import os
import pygame
import tempfile
import threading
import time
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TTSServer:
    def __init__(self):
        self.app = Flask(__name__)
        self.setup_routes()
        pygame.mixer.init()
        
        # Load configuration from environment
        self.port = int(os.getenv('TTS_PORT', 5000))
        self.lang = os.getenv('TTS_LANG', 'en')
        self.voice_speed = float(os.getenv('TTS_VOICE_SPEED', 1.0))
        
        # Ensure temp directory exists
        self.temp_dir = Path(tempfile.gettempdir()) / 'cursor_tts_mcp'
        self.temp_dir.mkdir(exist_ok=True)

    def setup_routes(self):
        self.app.route('/')(self.home)
        self.app.route('/speak', methods=['POST'])(self.speak)
        self.app.route('/mcp/tts', methods=['POST'])(self.mcp_tts)

    def home(self):
        return render_template('index.html')

    def play_audio(self, audio_file):
        try:
            pygame.mixer.music.load(audio_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
        except Exception as e:
            logger.error(f"Error playing audio: {e}")
        finally:
            try:
                os.unlink(audio_file)
            except:
                pass

    def speak(self):
        try:
            text = request.json.get('text', '')
            if not text:
                return jsonify({'error': 'No text provided'}), 400

            # Create a temporary file
            temp_file = tempfile.NamedTemporaryFile(
                suffix='.mp3',
                dir=self.temp_dir,
                delete=False
            )
            temp_filename = temp_file.name
            temp_file.close()

            # Generate speech
            tts = gTTS(text=text, lang=self.lang)
            tts.save(temp_filename)

            # Play audio in a separate thread
            thread = threading.Thread(target=self.play_audio, args=(temp_filename,))
            thread.daemon = True
            thread.start()

            return jsonify({'success': True, 'message': 'Audio playing'})

        except Exception as e:
            logger.error(f"Error in speak endpoint: {e}")
            return jsonify({'error': str(e)}), 500

    def mcp_tts(self):
        """MCP endpoint for text-to-speech conversion"""
        try:
            data = request.json
            if not data or 'response' not in data:
                return jsonify({'error': 'Invalid MCP request'}), 400

            # Extract text from MCP response
            text = data['response']
            
            # Create a temporary file
            temp_file = tempfile.NamedTemporaryFile(
                suffix='.mp3',
                dir=self.temp_dir,
                delete=False
            )
            temp_filename = temp_file.name
            temp_file.close()

            # Generate speech
            tts = gTTS(text=text, lang=self.lang)
            tts.save(temp_filename)

            # Play audio in a separate thread
            thread = threading.Thread(target=self.play_audio, args=(temp_filename,))
            thread.daemon = True
            thread.start()

            return jsonify({
                'success': True,
                'message': 'Converting response to speech'
            })

        except Exception as e:
            logger.error(f"Error in MCP endpoint: {e}")
            return jsonify({'error': str(e)}), 500

    def run(self):
        logger.info(f"Starting TTS MCP server on port {self.port}")
        self.app.run(port=self.port, debug=True)

def main():
    server = TTSServer()
    server.run()

if __name__ == '__main__':
    main() 