# 🤖 J.A.R.V.I.S. - Iron Man AI Assistant (Web Version)

A sophisticated web-based AI assistant inspired by JARVIS from Iron Man, featuring voice recognition, text-to-speech with a British accent, computer control, and web browsing capabilities.

## ✨ Features

🎤 **Voice Recognition & Response**
- Continuous listening through microphone
- Real-time voice commands
- JARVIS-like British accent responses
- Natural language processing

🌐 **Web Browsing & Search**
- Google search integration
- YouTube search and navigation
- Website opening
- Link navigation

💻 **Computer Control**
- Open applications (Chrome, Firefox, Notepad, Calculator)
- Web browser integration
- System information access
- Command execution

🌍 **Web-Based Interface**
- Access JARVIS from any browser
- Beautiful dark theme UI
- Real-time chat display
- Voice and text input

## 📦 Installation & Setup

### Option 1: Quick Start (Recommended)

```bash
python run_jarvis.py
```

This will:
- ✅ Automatically install all dependencies
- ✅ Initialize the voice engine
- ✅ Start the web server
- ✅ Open JARVIS in your browser

### Option 2: Manual Setup

**Step 1: Install dependencies**
```bash
pip install -r requirements.txt
```

**Step 2: Run the web server**
```bash
python jarvis_web_server.py
```

**Step 3: Open in browser**
```
http://localhost:5000
```

## 🎮 How to Use

### Web Interface

1. **Open your browser** and go to `http://localhost:5000`
2. **Click the 🎤 LISTEN button** to start voice recognition
3. **Speak your command** clearly into your microphone
4. **JARVIS responds** with voice and text
5. **Chat history** shows all interactions

### Voice Commands

**Greetings**
- "Hello JARVIS"
- "Hi JARVIS"
- "Wake up"

**Web Search**
- "Search for [query]"
- "Google [query]"

**YouTube**
- "Open YouTube"
- "Search YouTube for [video name]"

**Open Applications**
- "Open Chrome"
- "Open Firefox"
- "Open Notepad"
- "Open Calculator"

**Open Websites**
- "Open Google"
- "Open GitHub"
- "Open Facebook"

**System Information**
- "What time is it?"

**Text Input**
- Type commands in the text box and click "Send"

## 🔧 System Requirements

- **Python 3.7+**
- **Microphone** (for voice input)
- **Speaker** (for audio output)
- **Browser** (Chrome, Firefox, Safari, Edge)
- **Internet connection** (for speech recognition and web searches)
- **4GB RAM** minimum
- **Windows, macOS, or Linux**

## 🎯 Architecture

```
JARVIS Web System
├── Frontend (Browser)
│   ├── HTML/CSS/JavaScript UI
│   ├── Speech Recognition API
│   └── WebSocket/Fetch API
│
├── Backend (Flask Server)
│   ├── Voice Processing
│   ├── Command Handler
│   ├── Text-to-Speech
│   └── Web Integration
│
└── System Integration
    ├── Microphone Access
    ├── Browser Control
    ├── Application Launcher
    └── Web APIs
```

## 🎨 Features Breakdown

### Voice Engine
- **Rate**: 150 WPM (deliberate, clear speech)
- **Volume**: 0.9 (loud and clear)
- **Accent**: British English (JARVIS-like quality)
- **Processing**: Real-time audio synthesis

### Web Interface
- **Dark Theme**: Easy on the eyes
- **Gold Accents**: Iron Man color scheme
- **Responsive Design**: Works on any screen size
- **Real-time Updates**: Live chat and status

### Command Processing
- **Natural Language**: Understands varied phrasing
- **Context Aware**: Remembers conversation
- **Fast Response**: Immediate feedback
- **Error Handling**: Graceful error messages

## 🚀 Advanced Commands

### Computer Control
```
"take a screenshot" - Captures screen
"volume up" - Increases volume
"volume down" - Decreases volume
"mute" - Mutes audio
```

### Smart Features
```
"current time" - Tells time
"what's the date" - Tells date
"weather" - Weather information
```

## 🐛 Troubleshooting

### Microphone Not Working
1. Check microphone is connected and enabled
2. Allow browser permission for microphone access
3. Check Windows/Mac sound settings
4. Try refreshing the page

### Speech Not Recognized
1. Speak clearly and closer to microphone
2. Reduce background noise
3. Check internet connection
4. Try different browser

### JARVIS Not Speaking
1. Check speaker volume
2. Allow browser audio output
3. Refresh the page
4. Check system volume settings

### Server Won't Start
1. Make sure port 5000 is not in use
2. Check all dependencies are installed
3. Try running with admin privileges
4. Check Python version (3.7+)

## 📝 Configuration

Edit `jarvis_web_server.py` to customize:

### Change Response Voice
```python
self.engine.setProperty('voice', voice.id)
```

### Adjust Speech Rate
```python
self.engine.setProperty('rate', 150)  # Lower = slower
```

### Change Master Name
```python
self.master_name = "Sir"  # Change to "Tony", "Boss", etc.
```

### Add Custom Commands
Edit the `process_command()` method in `jarvis_web_server.py`:
```python
elif 'your command' in command:
    response = "Your response"
    return response
```

## 🔐 Security Notes

- JARVIS runs locally on `localhost:5000`
- No data is sent to external servers (except for speech recognition API)
- All commands are processed locally
- Browser has access to microphone when you click "LISTEN"

## 📦 Dependencies

- **Flask** - Web server framework
- **Flask-CORS** - Cross-origin support
- **SpeechRecognition** - Voice command recognition
- **pyttsx3** - Text-to-speech synthesis
- **Pillow** - Image processing (screenshots)
- **requests** - HTTP requests for web data

## 🎓 Learning & Customization

The codebase is well-documented and easy to modify:

1. **Add new commands** in `process_command()` method
2. **Change UI** by editing `templates/index.html`
3. **Add integrations** via `jarvis_web_server.py`
4. **Customize voice** in `setup_voice()` method

## 🌟 Future Enhancements

- 🤖 Machine learning for smarter responses
- 🏠 Smart home device integration
- 📅 Calendar and reminder management
- 📧 Email reading and sending
- 📰 News briefing capability
- 🎬 Movie recommendations
- 🌡️ Smart device control
- 🧠 Advanced NLP engine

## 📄 License

Open-source and available for educational purposes.

## 💬 Support

If you encounter issues:
1. Check the Troubleshooting section
2. Check browser console (F12) for errors
3. Check server terminal for backend errors
4. Ensure all dependencies are installed

## 🙏 Credits

Inspired by JARVIS from Iron Man (Marvel)

---

**🤖 JARVIS is online and ready to serve you, Sir!**

*"Good morning, Sir. Systems nominal. All indicators green. How may I be of service?"*

**Version**: 1.0 (Web Edition)  
**Created**: 2026  
**Author**: wt9dyr9jww-byte
