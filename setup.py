from setuptools import find_packages, setup

setup(
    name="Multilingual AI Assistant",
    version="0.0.1",
    author="Sid",
    author_email="siddardha.gurram@gmail.com",
    packages=find_packages(),
    install_requires=["SpeechRecognition","pipwin","pyaudio","gTTS","google-generativeai","python-dotenv","streamlit"]
)