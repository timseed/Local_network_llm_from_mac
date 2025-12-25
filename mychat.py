import streamlit as st
import requests
import json
import os

OLLAMA = os.getenv("OLLAMA_HOST", "http://localhost:11434")
MODEL="deepseek-coder"
st.title(f"Ollama Chat {MODEL}")

prompt = st.text_area("HAL:")

if st.button("Send"):
    with requests.post(
        f"{OLLAMA}/api/generate",
        json={"model": MODEL, "prompt": prompt, "stream": True},
        stream=True
    ) as r:
        output = ""
        box = st.empty()
        for line in r.iter_lines():
            if line:
                data = json.loads(line)
                output += data.get("response", "")
                box.markdown(output)
