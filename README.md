# 🤖 J.A.R.V.I.S. - Iron Man AI Assistant

A sophisticated AI assistant inspired by JARVIS from Iron Man, featuring voice recognition, text-to-speech with a British accent, computer control, and web browsing capabilities.

## Features

✨ **Voice Recognition & Response**
- Continuous listening for voice commands
- Responds with JARVIS-like British accent
- Natural language processing

🌐 **Web Browsing & Search**
- Google search integration
- YouTube search and navigation
- Website opening
- Link navigation

💻 **Computer Control**
- Open applications (Chrome, Firefox, Notepad, Calculator, etc.)
- Take screenshots
- Volume control
- System shutdown and sleep commands

⏰ **Smart Features**
- Tell current time
- Weather information
- Real-time responsiveness
- Command processing

## Installation

### Prerequisites
- Python 3.8 or higher
- Microphone for voice input
- Speaker for audio output

### Setup Steps

1. **Clone or download the repository**
```bash
cd AS
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Additional Setup for Speech Recognition**
   - **On Windows**: Install `pyaudio` (optional but recommended)
   ```bash
   pip install pyaudio
   ```
   
   - **On macOS**: Install `pyaudio` with Homebrew
   ```bash
   brew install portaudio
   pip install pyaudio
   ```
   
   - **On Linux**: Install dependencies
   ```bash
   sudo apt-get install portaudio19-dev python3-pyaudio
   pip install pyaudio
   ```

4. **Configure Voice (Optional)**
   - The AI will automatically select an English male voice
   - You can manually change voice in `setup_voice()` method if desired

## Usage

### Running JARVIS

```bash
python jarvis_ai.py
```

JARVIS will initialize and begin listening for commands.

### Voice Commands

**Greeting**
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
- "Open Spotify"

**Open Websites**
- "Open Google"
- "Open GitHub"
- "Open YouTube.com"

**System Information**
- "What time is it?"
- "Tell me the weather"

**Computer Control**
- "Take a screenshot"
- "Volume up"
- "Volume down"
- "Mute"

**System Commands**
- "Shutdown"
- "Sleep mode"
- "Hibernate"

**Exit**
- "Goodbye"
- "Exit"
- "Quit"
- "Shut down JARVIS"

## Voice Characteristics

JARVIS features:
- **British English accent** - Mimics the original Iron Man AI
- **Deliberate speech rate** - Clear, measured responses (150 WPM)
- **Professional tone** - Formal address ("Sir") and courteous responses
- **Status updates** - Confirms actions and provides feedback

## Customization

You can customize JARVIS by editing `jarvis_ai.py`:

### Change Master Name
```python
self.master_name = "Sir"  # Change to "Tony", "Boss", etc.
```

### Adjust Speech Rate
```python
self.engine.setProperty('rate', 150)  # Lower = slower, Higher = faster
```

### Adjust Volume
```python
self.engine.setProperty('volume', 0.9)  # 0.0 to 1.0
```

### Add Custom Commands
Add new elif statements in the `process_command()` method:
```python
elif 'your command' in command:
    self.speak("Your response")
    # Your action here
```

## Troubleshooting

**"I did not catch that"**
- Speak clearly and closer to the microphone
- Reduce background noise
- Check microphone is working properly

**Speech recognition not working**
- Ensure internet connection (Google Speech API requires it)
- Check microphone permissions
- Reinstall `SpeechRecognition`: `pip install --upgrade SpeechRecognition`

**JARVIS not speaking**
- Check speaker volume
- Verify `pyttsx3` is installed correctly
- Try different voices in `setup_voice()`

**Commands not recognized**
- Speak more clearly
- Use exact command phrases
- Check microphone isn't muted

## System Requirements

- **Processor**: Multi-core recommended (for speech processing)
- **RAM**: 4GB minimum
- **Internet**: Required for Google Search and Speech APIs
- **Audio Hardware**: Microphone and speakers
- **OS**: Windows, macOS, or Linux

## Architecture

```
JARVIS Assistant
├── Voice Input (SpeechRecognition)
├── Command Processing
├── Action Execution
│   ├── Web Operations (webbrowser, requests)
│   ├── System Control (subprocess, os)
│   ├── Application Launch
│   └── File Operations
└── Voice Output (pyttsx3 Text-to-Speech)
```

## Future Enhancements

- Machine learning for personalized responses
- Integration with smart home devices
- Calendar and reminder management
- Email reading and sending
- News briefing capability
- Movie/show recommendations
- Smart device control (lights, temperature)
- Advanced NLP for context understanding

## Dependencies

- **SpeechRecognition** - Voice command recognition
- **pyttsx3** - Text-to-speech synthesis
- **Pillow** - Screenshot capabilities
- **requests** - HTTP requests for web data

## License

This project is open-source and available for educational purposes.

## Notes

- JARVIS requires an internet connection for speech recognition and web searches
- Microphone must be enabled and configured in system settings
- Keep the listening loop running for continuous command availability
- JARVIS will politely ask for clarification if commands are unclear

---

*"Good morning, Sir. I am fully operational and at your service."*

🤖 **Created by**: wt9dyr9jww-byte  
📅 **Version**: 1.0  
✨ **Inspired by**: JARVIS from Iron Man
