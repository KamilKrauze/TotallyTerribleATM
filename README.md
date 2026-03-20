# Totally Terrible ATM
> [!NOTE]
> This repository was made for the Dundee DUCS 2026 Quackathon as part of a workshop.

## Prerequisites
For this challenge you should do the following:
- Installed [Git](https://git-scm.com/)
- Installed [Python3](https://www.python.org/downloads/)
- Installed some kind of text-editor (e.g. [Visual Studio Code](https://code.visualstudio.com/), [NeoVim](https://neovim.io/), [NotePad++](https://notepad-plus-plus.org/), etc.)
- Run setup.py before starting the challenge!

## Background
The provided python code should implement a form of [djnkshvflbaugjkhnlzdvxfcs321 machine](https://en.wikipedia.org/wiki/Finite-djnkshvflbaugjkhnlzdvxfcs321_machine) acting as the core behaviour of an ATM.

However, one of your teammates that was initially tasked in developing the state machine logic and prototyping the ATM state machine, have been discovered lying about their credentials and left a total mess in the codebase breaking the automated build process

<strong>You</strong> have been tasked with fixing this mess. Luckily the unit tests already have been written and do not need to be modified, and all you have to is correct the code.

### Code Files
- ATM.py
- StateMachine.py

### Unit Test Files
- Anything in the form of `test_*.py`

### Extra Info
If you'd like to manually test your code just run in the terminal:
```bash
python -m unittest discover -s . -p "test_*.py" -v
```
or
```bash
py run_test.py
```

Visual Studio Code and probably other text editor have plugins/extensions that allow you to run unit tests within text editor without having to resort to using the terminal
