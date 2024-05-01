### 1. Requirements
1. Python and anaconda environment
2. You will need 4.7GB of memory to download Llama3 model, so if you don't have enough space on your device work in Google Colab

### 2. Installation

1. Go to project directory and run the following command:
```
pip install -r requirements.txt
```

2. Dowload and install Ollama into your system. You can download it using the following link: https://ollama.com/download
3. After you installed Ollama you can make sure if it is installed correctly by typing the following in your terminal:
```
ollama serve
```
4. After you make sure you installed Ollama correctly, go and run this command in your project directory:
```
ollama pull llama3
```

### 3. Running the app
```
streamlit run app.py
```