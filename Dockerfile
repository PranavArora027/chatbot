FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -y

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "login.py"]