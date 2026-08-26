"""
JARVIS Configuration File
Customize your AI assistant's behavior and voice characteristics
"""

# VOICE SETTINGS
VOICE_SETTINGS = {
    'speech_rate': 150,           # 100-200 (lower = slower, clearer speech)
    'volume': 0.9,                # 0.0-1.0 (volume level)
    'language': 'en-US',          # Language for speech recognition
    'accent': 'british',          # Accent preference: 'british', 'american', 'neutral'
}

# MASTER SETTINGS
MASTER_SETTINGS = {
    'name': 'Sir',                # How JARVIS addresses you
    'greeting': True,             # Enable startup greeting
    'always_listen': True,        # Always listen for commands
}

# RESPONSE SETTINGS
RESPONSE_SETTINGS = {
    'response_delay': 0.5,        # Delay between responses (seconds)
    'timeout': 10,                # Microphone listening timeout (seconds)
    'ambient_noise_duration': 1,  # Ambient noise calibration (seconds)
}

# WEB BROWSER SETTINGS
BROWSER_SETTINGS = {
    'default_browser': 'auto',    # 'auto', 'chrome', 'firefox', 'edge'
    'search_engine': 'google',    # 'google', 'duckduckgo', 'bing'
    'new_tab': True,              # Open links in new tab
}

# APPLICATION SHORTCUTS
APP_SHORTCUTS = {
    'chrome': ['google-chrome', 'chrome.exe', 'open -a "Google Chrome"'],
    'firefox': ['firefox', 'firefox.exe'],
    'edge': ['microsoft-edge', 'msedge.exe'],
    'notepad': ['notepad', 'gedit', 'nano'],
    'calculator': ['gnome-calculator', 'calc.exe', 'open -a "Calculator"'],
    'spotify': ['spotify', 'snap run spotify'],
    'vlc': ['vlc'],
    'vscode': ['code', 'code.exe'],
}

# QUICK WEBSITE SHORTCUTS
WEBSITES = {
    'google': 'https://www.google.com',
    'youtube': 'https://www.youtube.com',
    'github': 'https://www.github.com',
    'reddit': 'https://www.reddit.com',
    'twitter': 'https://www.twitter.com',
    'facebook': 'https://www.facebook.com',
    'instagram': 'https://www.instagram.com',
    'linkedin': 'https://www.linkedin.com',
}

# SYSTEM SETTINGS
SYSTEM_SETTINGS = {
    'enable_shutdown': True,      # Allow shutdown commands
    'enable_sleep': True,         # Allow sleep mode
    'enable_screenshots': True,   # Allow screenshot capture
    'screenshots_folder': './screenshots/',  # Where to save screenshots
}

# COMMANDS CUSTOMIZATION
CUSTOM_COMMANDS = {
    # Format: 'command_keyword': {'response': 'what JARVIS says', 'action': 'action_type'}
    'iron man': {
        'response': "I am JARVIS, artificial intelligence assistant created by Tony Stark for the Iron Man suit.",
        'action': 'info'
    },
    'who are you': {
        'response': "I am JARVIS, your sophisticated AI assistant. Systems nominal, Sir.",
        'action': 'info'
    },
}

# LOGGING SETTINGS
LOGGING = {
    'enable_logging': True,
    'log_file': 'jarvis_activity.log',
    'log_level': 'INFO',  # 'DEBUG', 'INFO', 'WARNING', 'ERROR'
}

# ADVANCED FEATURES (Future)
ADVANCED_FEATURES = {
    'machine_learning': False,    # Learn from user preferences
    'smart_home_integration': False,  # Control smart devices
    'calendar_integration': False,     # Calendar management
    'email_integration': False,        # Email reading
    'news_briefing': False,            # Daily news update
}
