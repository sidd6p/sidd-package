# src/main.py
import os
import streamlit.web.cli as stcli
import sys

def run():
    app_path = os.path.join(os.path.dirname(__file__), 'Home.py')
    sys.argv = ["streamlit", "run", app_path]
    stcli.main()


run()