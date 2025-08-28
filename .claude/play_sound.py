#!/usr/bin/env python3
"""
Cross-platform sound player for Age of Claude hooks.
Works on Windows, macOS, and Linux.
"""

import sys
import random
import os
import platform
from pathlib import Path

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
            # Use Windows Media Player
            os.system(f'powershell -WindowStyle Hidden -Command "(New-Object Media.SoundPlayer \'{sound_path}\').PlaySync()" 2>nul')
        elif system == 'Linux':
            # Try multiple Linux audio players in order of preference
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

def main():
    if len(sys.argv) < 2:
        print("Usage: python play_sound.py <sound_file> [sound_file2 ...]")
        print("If multiple files provided, one will be chosen randomly.")
        sys.exit(1)
    
    # Get all sound files from arguments
    sound_files = sys.argv[1:]
    
    # Choose random sound if multiple provided
    if len(sound_files) > 1:
        chosen_sound = random.choice(sound_files)
    else:
        chosen_sound = sound_files[0]
    
    # Pre-initialize audio system with silent file to prevent cutoff
    script_dir = Path(__file__).parent
    silence_file = script_dir / "sounds" / "silence.wav"
    if silence_file.exists():
        play_sound(str(silence_file))
    
    # Play the actual sound
    if not play_sound(chosen_sound):
        sys.exit(1)

if __name__ == "__main__":
    main()