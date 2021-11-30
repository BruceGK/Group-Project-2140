FROM python:3.10

WORKDIR /app/data

WORKDIR /app/src
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
ENV FLASK_APP=main.py
ENV FLASK_ENV=production
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
