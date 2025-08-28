# Age of Claude 🏰⚔️

*Wololo! Your Claude Code experience just went back to classical antiquity!*

## Overview

Age of Claude brings the iconic sounds of Age of Empires to your Claude Code sessions. Every action triggers nostalgic AoE dialogue and sound effects, turning your coding sessions into an epic RTS experience.

## Features

- 🎮 **Cross-platform support** - Works on Windows, macOS, and Linux
- 🔊 **Smart sound mapping** - Different sounds for different Claude Code hooks
- 🎲 **Random variety** - Multiple sounds per hook keep things fresh
- 💬 **Heavy dialogue usage** - Classic AoE taunts and unit responses

## Hook Sound Mappings

| Hook | Sounds | Example Dialogue |
|------|--------|------------------|
| **SessionStart** | Startup music | "Start the game already!" "Hey, nice town!" |
| **UserPromptSubmit** | Acknowledgments | "Yes!" *villager select sounds* |
| **PreToolUse** | Resource gathering | "Working" |
| **PostToolUse (success)** | Victory sounds | "Aww yeah!" "Who's the man?" |
| **PostToolUse (error)** | Death/failure | "I'm weak, please don't kill me!" "Dad gum!" |
| **Stop** | Working sound | *construction sound* |
| **SubagentStop** | Soldier/priest | *soldier select* "Ayeohoho!" |
| **SessionEnd** | Ending taunts | "Get out!" "I'm weak, please don't kill me!" |
| **PreCompact** | Rejection | "Your attempts are futile!" |

## Installation

1. Clone this repository:
```bash
git clone https://github.com/aliparoya/age-of-claude.git
cd age-of-claude
```

2. Either:
   - Copy the `.claude` folder to your project root, or
   - Just `cd` into the repo and start using Claude Code directly
3. The hooks will automatically trigger during Claude Code sessions

## Requirements

- Python 3.x (for cross-platform sound playback)
- Audio playback support:
  - **Windows**: Built-in PowerShell
  - **macOS**: Built-in `afplay`
  - **Linux**: `aplay`, `paplay`, or `ffplay`

## Customization

Edit `.claude/settings.json` to customize sound mappings. The Python script `.claude/play_sound.py` handles cross-platform playback automatically.

## Credits

Sound effects from the original Age of Empires game by Ensemble Studios/Microsoft.

*An empire begins from humble beginnings.*