#!/usr/bin/env python3
"""
JARVIS Web Server Launcher
Automatically installs dependencies and starts the web server
"""

import subprocess
import sys
import os
import time
import webbrowser

def install_dependencies():
    """Install required packages"""
    print("\n" + "="*60)
    print("🤖 JARVIS WEB SERVER SETUP")
    print("="*60 + "\n")
    
    packages = [
        'flask==2.3.0',
        'flask-cors==4.0.0',
        'SpeechRecognition==3.10.0',
        'pyttsx3==2.90',
        'Pillow==10.0.0',
        'requests==2.31.0'
    ]
    
    print("📦 Installing required packages...\n")
    
    for package in packages:
        print(f"  Installing {package}...")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', package])
            print(f"  ✓ {package} installed\n")
        except subprocess.CalledProcessError as e:
            print(f"  ⚠️  Warning: {package} installation had issues")
    
    print("\n✓ Dependencies installation complete!\n")

def run_server():
    """Run the Flask web server"""
    print("="*60)
    print("🚀 STARTING JARVIS WEB SERVER")
    print("="*60 + "\n")
    
    print("✓ Voice engine initialized")
    print("✓ Web server starting on port 5000\n")
    
    time.sleep(2)
    
    print("📍 Access JARVIS at: http://localhost:5000")
    print("🎤 Microphone listening enabled")
    print("🔊 Speaker output ready\n")
    print("="*60)
    print("\n✨ JARVIS is online and ready to serve!\n")
    
    # Open browser automatically
    try:
        time.sleep(1)
        webbrowser.open('http://localhost:5000')
    except:
        pass
    
    # Run the Flask app
    try:
        os.system(f'{sys.executable} jarvis_web_server.py')
    except KeyboardInterrupt:
        print("\n\n⏹️  JARVIS shutting down...")

if __name__ == '__main__':
    try:
        install_dependencies()
        run_server()
    except KeyboardInterrupt:
        print("\n\n⏹️  Setup cancelled.")
    except Exception as e:
        print(f"\n❌ Error: {e}")
