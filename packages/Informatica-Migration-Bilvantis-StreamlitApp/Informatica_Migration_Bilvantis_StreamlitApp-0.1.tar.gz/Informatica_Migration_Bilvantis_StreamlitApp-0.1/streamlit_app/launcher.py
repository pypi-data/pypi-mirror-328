# my_streamlit_app/launcher.py
import subprocess

def run_streamlit():
    subprocess.run(["streamlit", "run", "streamplit_app/app.py"])
    