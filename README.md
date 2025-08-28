# Age of Claude 🏰⚔️

*Wololo! An empire begins from humble beginnings!*

## Overview

Age of Claude brings the iconic sounds of Age of Empires to your Claude Code sessions. Every action triggers nostalgic AoE dialogue and sound effects, turning your coding sessions into an RTS experience. It's also actually useful and not just a gimmick. For example, I have it say "Hey, I'm in your town" when Claude starts to create or edit a file. 

The sounds folder has a ton of unused sounds, so feel free to play around in .claude/settings.json to put in other sounds for the different hook triggers. It's also a fun way to learn about the hook system in Claude Code.

You'll need to have python installed as that's what I used to have it work on all of the major operating systems. You can update the hook commands to run things natively in your OS if you prefer not to use python.

There's a silence.wav file in the sounds folder that you can use as a placeholder for some of the hooks, so if you want to keep the hook in the file without it making a sound.

## Features

- 🎮 **Cross-platform support** - Works on Windows, macOS, and Linux
- 🔊 **Smart sound mapping** - Different sounds for different Claude Code hooks and notification types

## Hook Sound Mappings

```
📁 Session Lifecycle
├── UserPromptSubmit ────── Random villager selection sounds
├── Stop ────────────────── villager_train1.wav
├── SessionEnd 
│   ├── exit ────────────── Random farewell sounds
│   └── clear ───────────── soldier_select_papadakis5.wav
└── SubagentStop ────────── soldier_select_rudkin1.wav

📁 Tool Operations - PreToolUse (before tool runs)
├── Read ────────────────── Random villager selection sounds
├── Write ───────────────── dialogue_hey_im_in_your_town.wav
├── Edit/MultiEdit ──────── dialogue_hey_im_in_your_town.wav
├── NotebookEdit ────────── dialogue_hey_im_in_your_town.wav
├── Bash ────────────────── dialogue_attack_them_now.wav
├── Grep/Glob ───────────── dialogue_i_need_food.wav
├── LS ──────────────────── villager_select4.WAV
├── WebFetch/WebSearch ──── working_sound.wav
├── Task ────────────────── Random priest conversion sounds
├── TodoWrite ───────────── Random villager training sounds
└── ExitPlanMode ────────── dialogue_whos_the_man.wav

📁 Tool Operations - PostToolUse (after tool completes)
├── Write/Edit/MultiEdit ── Random success sounds
├── Bash ────────────────── dialogue_aww_yeah.wav
├── Grep/Glob/LS ────────── villager_select18.WAV
├── WebFetch/WebSearch ──── villager_select19.wav
├── Task ────────────────── working_sound.wav
└── TodoWrite ───────────── working_sound.wav

📁 Context Management
└── PreCompact
    ├── auto ────────────── dialogue_i_need_food.wav
    └── manual ──────────── dialogue_your_attempts_are_futile.wav
```

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
  - **Windows**: Python winsound library
  - **macOS**: Built-in `afplay`
  - **Linux**: `aplay`, `paplay`, or `ffplay`

## Customization

### Sound Selection
- Edit `.claude/settings.json` to customize sound mappings
- The `.claude/sounds/` folder contains many Age of Empires sound files to choose from
- You can assign different sounds to any hook by modifying the command paths in settings.json


## Credits

Sound effects from the original Age of Empires game by Ensemble Studios/Microsoft.
