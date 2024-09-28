import uvicorn
import subprocess

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)



def run_streamlit():
    # اجرای دستور Streamlit با استفاده از subprocess
    command = ["streamlit", "run", "app.py"]
    process = subprocess.Popen(command)



run_streamlit()
