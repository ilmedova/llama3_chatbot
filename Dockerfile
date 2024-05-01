FROM python:3.11-slim-buster
WORKDIR /llama3_chatbot
COPY . /llama3_chatbot
RUN curl -fsSL https://ollama.com/install.sh | sh
RUN ollama pull llama3
RUN pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]