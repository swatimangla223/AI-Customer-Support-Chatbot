# Proxy launcher so `streamlit run app.py` works while the real app is in AI-Chabot/
import runpy

runpy.run_path("AI-Chabot/app.py", run_name="__main__")
