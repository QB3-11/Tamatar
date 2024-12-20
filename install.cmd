python -m venv venv
./venv/bin/activate

pip install -r requirements.txt

pyinstaller --onefile --windowed src/main.py
