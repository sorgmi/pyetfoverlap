python -m pip install --upgrade pip
pip install -r requirements.txt

python -m build

pip install pyinstaller
pyinstaller --onefile main.py