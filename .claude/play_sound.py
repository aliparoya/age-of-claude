#!/usr/bin/env python3
"""
Cross-platform sound player for Age of Claude hooks.
Works on Windows, macOS, and Linux.
"""

import sys
import random
import os
import platform
import time
from pathlib import Path

DEBOUNCE_SECONDS = 10

def play_sound(sound_file):
    """Play a sound file using the appropriate method for the OS."""
    sound_path = Path(sound_file).resolve()
    
    if not sound_path.exists():
        print(f"Sound file not found: {sound_path}", file=sys.stderr)
        return False
    
    system = platform.system()
    
    try:
        if system == 'Darwin':  # macOS
            os.system(f'afplay "{sound_path}" 2>/dev/null &')
        elif system == 'Windows':
            os.system(f'powershell -WindowStyle Hidden -Command "(New-Object Media.SoundPlayer \'{sound_path}\').PlaySync()" 2>nul')
        elif system == 'Linux':
            if os.system('which aplay >/dev/null 2>&1') == 0:
                os.system(f'aplay -q "{sound_path}" 2>/dev/null &')
            elif os.system('which paplay >/dev/null 2>&1') == 0:
                os.system(f'paplay "{sound_path}" 2>/dev/null &')
            elif os.system('which ffplay >/dev/null 2>&1') == 0:
                os.system(f'ffplay -nodisp -autoexit "{sound_path}" 2>/dev/null &')
            else:
                print("No suitable audio player found. Install aplay, paplay, or ffplay.", file=sys.stderr)
                return False
        else:
            print(f"Unsupported operating system: {system}", file=sys.stderr)
            return False
        return True
    except Exception as e:
        print(f"Error playing sound: {e}", file=sys.stderr)
        return False

def check_debounce():
    """Check if enough time has passed since the last sound played."""
    script_dir = Path(__file__).parent
    marker_file = script_dir / "sounds" / ".last_sound_time"
    
    current_time = time.time()
    
    try:
        if marker_file.exists():
            last_play_time = marker_file.stat().st_mtime
            if current_time - last_play_time < DEBOUNCE_SECONDS:
                return False
        return True
    except (OSError, IOError):
        return True
    
def update_last_played():
    """Update the timestamp after initiating sound playback."""
    script_dir = Path(__file__).parent
    marker_file = script_dir / "sounds" / ".last_sound_time"
    
    try:
        marker_file.touch()
    except (OSError, IOError):
        pass

def main():
    if len(sys.argv) < 2:
        print("Usage: python play_sound.py <sound_file> [sound_file2 ...]")
        print("If multiple files provided, one will be chosen randomly.")
        sys.exit(1)
    
    if not check_debounce():
        sys.exit(0)
    
    sound_files = sys.argv[1:]
    chosen_sound = random.choice(sound_files) if len(sound_files) > 1 else sound_files[0]
    
    script_dir = Path(__file__).parent
    silence_file = script_dir / "sounds" / "silence.wav"
    if silence_file.exists():
        play_sound(str(silence_file))
    
    if not play_sound(chosen_sound):
        sys.exit(1)
    
    update_last_played()

if __name__ == "__main__":
    main()