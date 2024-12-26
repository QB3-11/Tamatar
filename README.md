# Tamatar

A pomodoro timer written in Python

## Requirements (Linux)
> python3, pip

## Requirements (Windows)
> python

## Installation (Linux)
```
git clone git@github.com:QB3-11/Tamatar.git
cd Tamatar
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pyinstaller tamatar.spec
mkdir ~/.config/tamtar 
cp themes/config.qss ~/.config/tamatar/
```

## Installation (Windows)
```
git clone git@github.com:QB3-11/Tamatar.git
cd Tamatar
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pyinstaller tamatar.spec
copy themes\config.qss %userprofile%
```

After installation, the file will be in the dist/ directory

## Errors (Windows)
While compiling, Windows Defender can mark the executable as a trojan (false positive).
Make sure to add an exception whenever that happens

### Why the name Tamatar?

Tamatar means tomato in Hindi

This is my very first public project
