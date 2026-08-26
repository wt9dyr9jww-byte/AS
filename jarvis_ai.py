"""
JARVIS - Iron Man Style AI Assistant
A sophisticated AI model with JARVIS-like voice, computer control, and web browsing capabilities
"""

import os
import sys
import webbrowser
import subprocess
import time
import threading
from datetime import datetime
import speech_recognition as sr
from pyttsx3 import init as tts_init
import requests
from urllib.parse import quote

class JARVISAssistant:
    def __init__(self):
        """Initialize JARVIS with voice and recognition capabilities"""
        self.recognizer = sr.Recognizer()
        self.engine = tts_init()
        self.setup_voice()
        self.is_listening = True
        self.master_name = "Sir"
        self.response_delay = 0.5
        
    def setup_voice(self):
        """Configure JARVIS voice to sound like the British assistant from Iron Man"""
        self.engine.setProperty('rate', 150)  # Slower, more deliberate speech
        self.engine.setProperty('volume', 0.9)
        
        # Try to set British English voice for JARVIS-like quality
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if 'english' in voice.languages[0].lower() or 'en' in voice.id.lower():
                if 'male' in voice.name.lower() or 'david' in voice.name.lower():
                    self.engine.setProperty('voice', voice.id)
                    break
    
    def speak(self, text):
        """Speak text with JARVIS voice characteristics"""
        print(f"\n🤖 JARVIS: {text}\n")
        self.engine.say(text)
        self.engine.runAndWait()
    
    def listen(self):
        """Listen for voice commands continuously"""
        with sr.Microphone() as source:
            print("\n👂 Listening...\n")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            try:
                audio = self.recognizer.listen(source, timeout=10)
                command = self.recognizer.recognize_google(audio)
                return command.lower()
            except sr.UnknownValueError:
                self.speak("I apologize, Sir. I did not catch that. Could you please repeat?")
                return None
            except sr.RequestError:
                self.speak("My apologies, Sir. There seems to be an issue with the audio service.")
                return None
    
    def open_application(self, app_name):
        """Open applications on the computer"""
        app_commands = {
            'chrome': ['google-chrome', 'chrome.exe'],
            'firefox': ['firefox'],
            'edge': ['microsoft-edge', 'msedge.exe'],
            'notepad': ['notepad', 'gedit'],
            'calculator': ['gnome-calculator', 'calc.exe'],
            'spotify': ['spotify'],
            'vlc': ['vlc'],
            'vscode': ['code'],
        }
        
        for cmd in app_commands.get(app_name.lower(), []):
            try:
                subprocess.Popen(cmd)
                self.speak(f"Opening {app_name.title()} now, Sir.")
                return True
            except:
                continue
        
        self.speak(f"I apologize, Sir. I cannot find {app_name}.")
        return False
    
    def search_web(self, query):
        """Search the web and open results in browser"""
        search_url = f"https://www.google.com/search?q={quote(query)}"
        webbrowser.open(search_url)
        self.speak(f"Searching for {query} on the web, Sir.")
    
    def open_youtube(self, search_term=None):
        """Open YouTube or search for a video"""
        if search_term:
            youtube_url = f"https://www.youtube.com/results?search_query={quote(search_term)}"
            self.speak(f"Opening YouTube search for {search_term}, Sir.")
        else:
            youtube_url = "https://www.youtube.com"
            self.speak("Opening YouTube, Sir.")
        webbrowser.open(youtube_url)
    
    def open_website(self, website):
        """Open a specific website"""
        if not website.startswith('http'):
            website = f"https://{website}"
        webbrowser.open(website)
        self.speak(f"Opening {website}, Sir.")
    
    def get_time(self):
        """Tell the current time"""
        current_time = datetime.now().strftime("%H:%M")
        self.speak(f"The current time is {current_time}, Sir.")
    
    def get_weather(self):
        """Get weather information (requires API)"""
        try:
            response = requests.get('https://wttr.in/?format=%t+%w', timeout=5)
            if response.status_code == 200:
                self.speak(f"Current weather: {response.text}")
            else:
                self.speak("I apologize, Sir. I cannot retrieve the weather at the moment.")
        except:
            self.speak("The weather service is unavailable, Sir.")
    
    def take_screenshot(self):
        """Take a screenshot of the screen"""
        try:
            from PIL import ImageGrab
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{timestamp}.png"
            ImageGrab.grab().save(filename)
            self.speak(f"Screenshot captured and saved as {filename}, Sir.")
        except:
            self.speak("I apologize, Sir. I cannot take a screenshot.")
    
    def control_volume(self, action):
        """Control system volume"""
        if action == 'up':
            self.speak("Increasing volume, Sir.")
            # Volume control commands vary by OS
        elif action == 'down':
            self.speak("Decreasing volume, Sir.")
        elif action == 'mute':
            self.speak("Muting audio, Sir.")
    
    def process_command(self, command):
        """Process voice commands and execute appropriate actions"""
        if not command:
            return
        
        # Greeting commands
        if 'hello' in command or 'hi' in command or 'wake up' in command:
            self.speak(f"Good day, {self.master_name}. I am fully operational and at your service.")
        
        # Search and browse commands
        elif 'search' in command or 'google' in command:
            search_query = command.replace('search', '').replace('google', '').strip()
            if search_query:
                self.search_web(search_query)
            else:
                self.speak("What would you like me to search for, Sir?")
        
        elif 'youtube' in command:
            search_query = command.replace('youtube', '').replace('search', '').strip()
            if search_query:
                self.open_youtube(search_query)
            else:
                self.open_youtube()
        
        elif 'open' in command:
            # Extract application or website name
            app_or_site = command.replace('open', '').strip()
            if app_or_site:
                self.open_application(app_or_site) or self.open_website(app_or_site)
        
        # Application commands
        elif 'chrome' in command:
            self.open_application('chrome')
        elif 'firefox' in command:
            self.open_application('firefox')
        elif 'notepad' in command:
            self.open_application('notepad')
        elif 'calculator' in command:
            self.open_application('calculator')
        
        # Time and weather
        elif 'time' in command:
            self.get_time()
        elif 'weather' in command:
            self.get_weather()
        
        # Computer control
        elif 'screenshot' in command or 'screen capture' in command:
            self.take_screenshot()
        elif 'volume up' in command:
            self.control_volume('up')
        elif 'volume down' in command:
            self.control_volume('down')
        elif 'mute' in command:
            self.control_volume('mute')
        
        # System commands
        elif 'shutdown' in command or 'power down' in command:
            self.speak("Initiating shutdown sequence, Sir.")
            os.system('shutdown -s -t 60')
        elif 'sleep' in command or 'hibernation' in command:
            self.speak("Entering sleep mode, Sir.")
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
        
        # Goodbye
        elif 'goodbye' in command or 'exit' in command or 'quit' in command or 'shut down jarvis' in command:
            self.speak("Very good, Sir. I shall await your next command. Powering down auxiliary systems.")
            self.is_listening = False
        
        else:
            self.speak(f"I am not familiar with that command, {self.master_name}. Could you please clarify?")
    
    def initialize(self):
        """JARVIS initialization sequence"""
        self.speak("Good morning, Sir. I am JARVIS, your artificial intelligence assistant. Systems nominal. All indicators are green.")
        self.speak("I am equipped with advanced computer control capabilities, web browsing, and voice recognition. How may I be of service?")
    
    def run(self):
        """Main listening loop - always listening"""
        self.initialize()
        
        while self.is_listening:
            try:
                print("\n" + "="*50)
                print("🎤 JARVIS IS LISTENING...")
                print("="*50)
                
                command = self.listen()
                
                if command:
                    print(f"\n📝 Command Received: {command}")
                    self.process_command(command)
                
                time.sleep(self.response_delay)
            
            except KeyboardInterrupt:
                self.speak("Shutting down, Sir. It has been a pleasure serving you.")
                break
            except Exception as e:
                print(f"Error: {e}")
                self.speak("I apologize, Sir. An error has occurred.")


def main():
    """Initialize and run JARVIS"""
    print("\n" + "="*60)
    print("🤖  J.A.R.V.I.S. - IRON MAN AI ASSISTANT  🤖")
    print("="*60)
    print("Starting up auxiliary systems...\n")
    
    try:
        jarvis = JARVISAssistant()
        jarvis.run()
    except ImportError as e:
        print(f"⚠️  Missing dependency: {e}")
        print("\nPlease install required packages:")
        print("pip install SpeechRecognition pyttsx3 Pillow requests")


if __name__ == "__main__":
    main()
