#!/usr/bin/env python3
"""
JARVIS Setup Script
Automatically installs all dependencies and sets up JARVIS
"""

import subprocess
import sys
import os

def install_dependencies():
    """Install all required packages"""
    print("\n" + "="*60)
    print("🤖 JARVIS INSTALLATION SETUP")
    print("="*60 + "\n")
    
    packages = [
        'SpeechRecognition==3.10.0',
        'pyttsx3==2.90',
        'Pillow==10.0.0',
        'requests==2.31.0'
    ]
    
    print("📦 Installing required packages...\n")
    
    for package in packages:
        print(f"Installing {package}...")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
            print(f"✓ {package} installed successfully!\n")
        except subprocess.CalledProcessError:
            print(f"❌ Failed to install {package}")
            print("Please try installing manually: pip install " + package)
            return False
    
    print("\n" + "="*60)
    print("✓ ALL DEPENDENCIES INSTALLED SUCCESSFULLY!")
    print("="*60 + "\n")
    
    return True

def check_microphone():
    """Check if microphone is available"""
    print("🎤 Checking microphone availability...\n")
    try:
        import speech_recognition as sr
        mic = sr.Microphone()
        print("✓ Microphone detected and ready!")
        return True
    except Exception as e:
        print(f"⚠️  Microphone check: {e}")
        print("Make sure your microphone is connected and enabled in system settings.")
        return False

def main():
    """Main setup function"""
    print("\n🚀 Starting JARVIS setup...\n")
    
    # Install dependencies
    if not install_dependencies():
        print("\n❌ Installation failed. Please install packages manually:")
        print("pip install SpeechRecognition==3.10.0 pyttsx3==2.90 Pillow==10.0.0 requests==2.31.0")
        sys.exit(1)
    
    # Check microphone
    check_microphone()
    
    print("\n" + "="*60)
    print("🎉 SETUP COMPLETE!")
    print("="*60)
    print("\n📋 Next Steps:")
    print("1. Run: python jarvis_ai.py")
    print("2. Allow microphone access when prompted")
    print("3. Speak your commands clearly")
    print("\n✨ JARVIS is ready to serve you, Sir!")
    print("="*60 + "\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⏹️  Setup cancelled by user.")
    except Exception as e:
        print(f"\n❌ Setup error: {e}")
        sys.exit(1)
