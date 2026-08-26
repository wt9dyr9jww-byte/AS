"""
JARVIS Web Server - Iron Man Style AI Assistant
Web-based interface running on localhost
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser
import subprocess
import threading
import requests
from urllib.parse import quote
import os
import sys

app = Flask(__name__)
CORS(app)

class JARVISWebAssistant:
    def __init__(self):
        """Initialize JARVIS web assistant"""
        try:
            self.recognizer = sr.Recognizer()
            self.engine = pyttsx3.init()
            self.setup_voice()
            self.master_name = "Sir"
            print("✓ JARVIS voice engine initialized")
        except Exception as e:
            print(f"⚠️  Voice initialization warning: {e}")
        
    def setup_voice(self):
        """Configure JARVIS voice"""
        try:
            self.engine.setProperty('rate', 150)
            self.engine.setProperty('volume', 0.9)
            voices = self.engine.getProperty('voices')
            
            # Try to find a British or male voice
            selected = False
            for voice in voices:
                voice_name = voice.name.lower()
                if any(keyword in voice_name for keyword in ['british', 'uk', 'david', 'male']):
                    self.engine.setProperty('voice', voice.id)
                    print(f"✓ Voice selected: {voice.name}")
                    selected = True
                    break
            
            if not selected and len(voices) > 0:
                self.engine.setProperty('voice', voices[0].id)
                print(f"✓ Voice selected: {voices[0].name}")
        except Exception as e:
            print(f"⚠️  Voice setup warning: {e}")
    
    def speak(self, text):
        """Speak text"""
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            print(f"Speech error: {e}")
    
    def listen(self):
        """Listen for voice commands"""
        try:
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=8)
                command = self.recognizer.recognize_google(audio)
                return command.lower()
        except sr.UnknownValueError:
            return "Could not understand"
        except sr.RequestError as e:
            return f"Microphone error: {str(e)}"
        except Exception as e:
            return f"Error: {str(e)}"
    
    def search_web(self, query):
        """Search the web"""
        try:
            search_url = f"https://www.google.com/search?q={quote(query)}"
            webbrowser.open(search_url)
            return f"Searching for {query}"
        except Exception as e:
            return f"Search error: {str(e)}"
    
    def open_youtube(self, search_term=None):
        """Open YouTube"""
        try:
            if search_term:
                youtube_url = f"https://www.youtube.com/results?search_query={quote(search_term)}"
                webbrowser.open(youtube_url)
                return f"Opening YouTube - searching for {search_term}"
            else:
                youtube_url = "https://www.youtube.com"
                webbrowser.open(youtube_url)
                return "Opening YouTube"
        except Exception as e:
            return f"YouTube error: {str(e)}"
    
    def open_website(self, website):
        """Open a website"""
        try:
            if not website.startswith('http'):
                website = f"https://{website}"
            webbrowser.open(website)
            return f"Opening {website}"
        except Exception as e:
            return f"Website error: {str(e)}"
    
    def open_application(self, app_name):
        """Open applications"""
        app_commands = {
            'chrome': ['google-chrome', 'chrome.exe', 'open -a "Google Chrome"'],
            'firefox': ['firefox', 'firefox.exe'],
            'edge': ['msedge.exe', 'microsoft-edge'],
            'notepad': ['notepad', 'gedit', 'nano'],
            'calculator': ['calc.exe', 'gnome-calculator', 'open -a "Calculator"'],
            'spotify': ['spotify'],
            'vscode': ['code', 'code.exe'],
        }
        
        for cmd in app_commands.get(app_name.lower(), []):
            try:
                subprocess.Popen(cmd)
                return f"Opening {app_name}"
            except:
                continue
        return f"Cannot find {app_name} on this system"
    
    def get_time(self):
        """Get current time"""
        try:
            current_time = datetime.now().strftime("%H:%M:%S")
            current_date = datetime.now().strftime("%A, %B %d, %Y")
            return f"The current time is {current_time}. Today is {current_date}"
        except Exception as e:
            return f"Time error: {str(e)}"
    
    def get_weather(self):
        """Get weather information"""
        try:
            response = requests.get('https://wttr.in/?format=%t+%w', timeout=5)
            if response.status_code == 200:
                return f"Current weather: {response.text}"
            else:
                return "Weather service temporarily unavailable"
        except:
            return "Unable to fetch weather information at this time"
    
    def process_command(self, command):
        """Process voice commands"""
        if not command:
            return "No command received, Sir"
        
        response = ""
        
        try:
            # Greetings
            if any(word in command for word in ['hello', 'hi', 'wake up', 'hey jarvis', 'jarvis']):
                response = f"Good day, {self.master_name}. I am fully operational and ready to serve."
            
            # Search
            elif 'search' in command or 'google' in command:
                query = command.replace('search', '').replace('google', '').strip()
                if query:
                    response = self.search_web(query)
                else:
                    response = "What would you like me to search for, Sir?"
            
            # YouTube
            elif 'youtube' in command:
                query = command.replace('youtube', '').replace('search', '').strip()
                if query:
                    response = self.open_youtube(query)
                else:
                    response = self.open_youtube()
            
            # Open app/website
            elif 'open' in command:
                app_or_site = command.replace('open', '').strip()
                if app_or_site:
                    app_result = self.open_application(app_or_site)
                    if "Cannot" not in app_result:
                        response = app_result
                    else:
                        response = self.open_website(app_or_site)
            
            # Time and date
            elif 'time' in command or 'date' in command:
                response = self.get_time()
            
            # Weather
            elif 'weather' in command:
                response = self.get_weather()
            
            # Help
            elif 'help' in command:
                response = "I can search the web, open YouTube, open applications and websites, tell you the time, and check the weather. What would you like me to do?"
            
            # Default
            else:
                response = f"I received your command: '{command}'. I'm processing that for you, Sir."
        
        except Exception as e:
            response = f"Error processing command: {str(e)}"
        
        return response


# Initialize JARVIS
print("\n" + "="*60)
print("🤖 INITIALIZING J.A.R.V.I.S.")
print("="*60 + "\n")

jarvis = JARVISWebAssistant()

print("✓ Flask framework loaded")
print("✓ CORS enabled")
print("✓ Ready to accept connections\n")

@app.route('/')
def index():
    """Serve the web interface"""
    return render_template('index.html')

@app.route('/api/listen', methods=['POST'])
def listen_command():
    """Listen for voice command"""
    try:
        command = jarvis.listen()
        return jsonify({'status': 'success', 'command': command})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/api/process', methods=['POST'])
def process_command():
    """Process a command"""
    try:
        data = request.json
        command = data.get('command', '')
        response = jarvis.process_command(command)
        
        # Speak the response in background
        threading.Thread(target=jarvis.speak, args=(response,), daemon=True).start()
        
        return jsonify({'status': 'success', 'response': response})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/api/speak', methods=['POST'])
def speak():
    """Make JARVIS speak"""
    try:
        data = request.json
        text = data.get('text', '')
        threading.Thread(target=jarvis.speak, args=(text,), daemon=True).start()
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/api/status', methods=['GET'])
def status():
    """Get JARVIS status"""
    return jsonify({
        'status': 'online',
        'name': 'JARVIS',
        'version': '1.0',
        'mode': 'web'
    })

if __name__ == '__main__':
    print("="*60)
    print("🚀 STARTING WEB SERVER")
    print("="*60)
    print("\n📍 Access JARVIS at: http://localhost:5000")
    print("🎤 Microphone: Ready")
    print("🔊 Speaker: Ready")
    print("✓ Web interface: http://localhost:5000\n")
    print("="*60)
    print("\n✨ JARVIS is online! Open your browser and navigate to:")
    print("   http://localhost:5000")
    print("\nPress Ctrl+C to stop the server\n")
    
    try:
        app.run(debug=False, host='localhost', port=5000, use_reloader=False)
    except KeyboardInterrupt:
        print("\n\n⏹️  JARVIS shutting down...")
        sys.exit(0)
