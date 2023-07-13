@echo off
python -m venv venv
call venv\Scripts\activate.bat
pip install -r requirements.txt
pre-commit install