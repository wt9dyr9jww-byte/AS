"""
JARVIS - Iron Man Style AI Assistant
A sophisticated AI model with JARVIS-like voice, computer control, and web browsing capabilities
Enhanced with continuous microphone listening and voice interaction
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
        self.mic = None
        
    def setup_voice(self):
        """Configure JARVIS voice to sound like the British assistant from Iron Man"""
        self.engine.setProperty('rate', 150)  # Slower, more deliberate speech
        self.engine.setProperty('volume', 0.9)
        
        # Try to set British English voice for JARVIS-like quality
        voices = self.engine.getProperty('voices')
        print("\n🎤 Available Voices:")
        for i, voice in enumerate(voices):
            print(f"  {i}: {voice.name}")
        
        for voice in voices:
            voice_name = voice.name.lower()
            # Prefer British or male voices
            if any(keyword in voice_name for keyword in ['british', 'uk', 'david', 'male', 'james']):
                self.engine.setProperty('voice', voice.id)
                print(f"\n✓ Selected voice: {voice.name}")
                break
    
    def speak(self, text):
        """Speak text with JARVIS voice characteristics"""
        print(f"\n🤖 JARVIS: {text}\n")
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            print(f"Error speaking: {e}")
    
    def listen_for_command(self):
        """Listen for voice commands with improved microphone access"""
        try:
            with sr.Microphone() as source:
                print("\n👂 Listening for your command...\n")
                
                # Adjust for ambient noise
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                
                # Set timeouts for better responsiveness
                self.recognizer.energy_threshold = 4000
                
                # Listen for audio (timeout after 15 seconds if no speech detected)
                audio = self.recognizer.listen(source, timeout=15, phrase_time_limit=10)
                
                print("🔄 Processing speech...\n")
                
                try:
                    # Use Google Speech Recognition
                    command = self.recognizer.recognize_google(audio)
                    print(f"📝 You said: {command}\n")
                    return command.lower()
                
                except sr.UnknownValueError:
                    self.speak("I apologize, Sir. I did not catch that. Could you please repeat?")
                    return None
                except sr.RequestError as e:
                    self.speak(f"I am unable to access the speech recognition service at the moment, Sir. {str(e)}")
                    return None
        
        except Exception as e:
            print(f"❌ Microphone error: {e}")
            self.speak("There seems to be an issue with the microphone, Sir.")
            return None
    
    def open_application(self, app_name):
        """Open applications on the computer"""
        app_commands = {
            'chrome': ['google-chrome', 'chrome.exe', 'open -a "Google Chrome"'],
            'firefox': ['firefox', 'firefox.exe'],
            'edge': ['microsoft-edge', 'msedge.exe'],
            'notepad': ['notepad', 'gedit', 'nano'],
            'calculator': ['gnome-calculator', 'calc.exe', 'open -a "Calculator"'],
            'spotify': ['spotify', 'snap run spotify'],
            'vlc': ['vlc'],
            'vscode': ['code', 'code.exe'],
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
        elif action == 'down':
            self.speak("Decreasing volume, Sir.")
        elif action == 'mute':
            self.speak("Muting audio, Sir.")
    
    def process_command(self, command):
        """Process voice commands and execute appropriate actions"""
        if not command:
            return
        
        # Greeting commands
        if any(word in command for word in ['hello', 'hi', 'wake up', 'hey jarvis']):
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
        elif 'time' in command or 'what time' in command:
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
            time.sleep(2)
            # Uncomment to actually shutdown:
            # os.system('shutdown -s -t 60')
        elif 'sleep' in command or 'hibernation' in command:
            self.speak("Entering sleep mode, Sir.")
            time.sleep(2)
            # Uncomment to actually sleep:
            # os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
        
        # Goodbye
        elif any(word in command for word in ['goodbye', 'exit', 'quit', 'shut down', 'stop listening']):
            self.speak("Very good, Sir. It has been a pleasure serving you. Powering down.")
            self.is_listening = False
        
        else:
            self.speak(f"I am not familiar with that command, {self.master_name}. Could you please clarify?")
    
    def initialize(self):
        """JARVIS initialization sequence"""
        print("\n" + "="*60)
        print("🤖  J.A.R.V.I.S. INITIALIZING...")
        print("="*60 + "\n")
        
        self.speak("Good morning, Sir. I am JARVIS, your artificial intelligence assistant. Systems nominal. All indicators are green.")
        self.speak("I am equipped with advanced computer control capabilities, web browsing, and voice recognition. I am always listening.")
        self.speak("How may I be of service?")
    
    def continuous_listening_loop(self):
        """Main continuous listening loop - always listening for commands"""
        self.initialize()
        
        while self.is_listening:
            try:
                print("\n" + "="*60)
                print("🎤 JARVIS IS ALWAYS LISTENING - SPEAK NOW")
                print("="*60)
                
                # Listen for command
                command = self.listen_for_command()
                
                if command:
                    print(f"✓ Command received: '{command}'")
                    self.process_command(command)
                else:
                    print("⚠️  No command detected")
                
                # Brief pause before listening again
                time.sleep(self.response_delay)
            
            except KeyboardInterrupt:
                print("\n\n⏹️  Shutdown signal received...")
                self.speak("Shutting down, Sir. It has been a pleasure serving you.")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")
                self.speak("An error has occurred, Sir. Resuming listening.")
                time.sleep(1)


def main():
    """Initialize and run JARVIS with continuous listening"""
    print("\n" + "="*60)
    print("🤖  J.A.R.V.I.S. - IRON MAN AI ASSISTANT  🤖")
    print("="*60)
    print("\n📋 Starting up auxiliary systems...")
    print("🔧 Initializing microphone access...")
    print("🎧 Configuring voice synthesis...")
    
    try:
        jarvis = JARVISAssistant()
        print("\n✓ All systems ready!\n")
        
        # Start continuous listening
        jarvis.continuous_listening_loop()
        
    except ImportError as e:
        print(f"\n❌ Missing dependency: {e}")
        print("\nPlease install required packages:")
        print("pip install SpeechRecognition pyttsx3 Pillow requests")
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        print("Please check your microphone and audio settings.")


if __name__ == "__main__":
    main()
