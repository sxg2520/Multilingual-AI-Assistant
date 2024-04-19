# Multilingual Assistant 


# How to run?
### STEPS:

Clone the repository

```bash
Project repo: https://github.com/sxg2520/Multilingual-AI-Assistant.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mai python=3.8 -y
```

```bash
conda activate mai
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

### Create a `.env` file in the root directory and add your GOOGLE_API_KEY credentials as follows:

```ini
GOOGLE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```


```bash
# Finally run the following command
streamlit run app.py
```

Now,
```bash
open up localhost:
```


### Techstack Used:

- Python
- Google API
- Streamlit
- PaLM2
- s2t
- t2s


# How to Deploy Streamlit app on EC2 instance

## 1. Login with your AWS console and launch an EC2 instance

## 2. Run the following commands

### Note: Do the port mapping to this port:- 8501

```bash
sudo apt update
```

```bash
sudo apt-get update
```

```bash
sudo apt upgrade -y
```

```bash
sudo apt install git curl unzip tar make sudo vim wget -y
```


```bash
git clone "Your-repository"
Change Directory using cd command
touch .env #to create .env file
sudo nano .env #to open the file
Add GOOGLE_API_KEY = "*****"
ctrl+s to save
ctrl+x to close the file
```

```bash
sudo apt install python3-pip
```
```bash
sudo apt install portaudio19-dev
python3 -m pip install PyAudio
```


```bash
pip3 install -r requirements.txt
```

```bash
#Temporary running
python3 -m streamlit run app.py
```

```bash
#Permanent running
nohup python3 -m streamlit run app.py
```

Note: Streamlit runs on this port: 8501



