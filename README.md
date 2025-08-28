# Age of Claude 🏰⚔️

*Wololo! An empire begins from humble beginnings!*

## Overview

Age of Claude brings the iconic sounds of Age of Empires to your Claude Code sessions. Every action triggers nostalgic AoE dialogue and sound effects, turning your coding sessions into an RTS experience. It's also actually useful and not just a gimmick. For example, I have it say "Hey, I'm in your town" when Claude starts to create or edit a file. There's a 10 second delay, so it doesn't become annoying when things are moving fast. The sounds folder has a ton of unused sounds, so feel free to play around in .claude/settings.json to put in other sounds for the different hook triggers. It's also a fun way to learn about the hook system in Claude Code.

You'll need to have python installed as that's what I used to have it work on all of the major operating systems. You can update the hook commands to run things natively in your OS if you prefer not to use python.

## Features

- 🎮 **Cross-platform support** - Works on Windows, macOS, and Linux
- 🔊 **Smart sound mapping** - Different sounds for different Claude Code hooks and notification types
- ⏱️ **Delay Between Sounds** - Configurable delay between sounds so it doesn't become annoying.

## Hook Sound Mappings

| Hook | Trigger Condition |
|------|------------------|
| **SessionStart** | Session begins (startup/resume) |
| **UserPromptSubmit** | User sends a message |
| **Stop** | Claude stops responding |
| **Notification** | |
| - Approval needed | Messages containing: approve, permission, confirm |
| - Error occurred | Messages containing: error, failed, problem |
| - Task completed | Messages containing: complete, success, done |
| **Tool Usage** | |
| - Read/Search | Using Read, Grep, Glob, LS tools |
| - Write/Edit | Using Write, Edit, MultiEdit tools |
| - Bash commands | Executing shell commands |
| - Web operations | WebFetch, WebSearch |
| - Task management | TodoWrite, Task agents |
| **Session Management** | |
| - SessionEnd | Exiting or clearing session |
| - PreCompact | Before context compaction |
| - SubagentStop | When subagents complete |

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

### Sound Selection
- Edit `.claude/settings.json` to customize sound mappings
- The `.claude/sounds/` folder contains many Age of Empires sound files to choose from
- You can assign different sounds to any hook by modifying the command paths in settings.json

### Debounce Control
- Adjust the minimum time between sounds by editing `DEBOUNCE_SECONDS` at the top of `.claude/play_sound.py`
- Default is 10 seconds
- Set to 0 to disable debounce entirely

## Credits

Sound effects from the original Age of Empires game by Ensemble Studios/Microsoft.