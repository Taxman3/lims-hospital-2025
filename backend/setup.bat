@echo off
echo Setting up Python virtual environment and installing dependencies...
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
echo Backend setup complete. Run 'python app.py' to start the backend.
