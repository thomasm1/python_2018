FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

#COPY agents.py prompts.py ./

RUN mkdir /app/data


EXPOSE 80
#set the environmen variable 
#ENV PYTHONUNBUFFERED=1 

CMD ["python", "agents.py"]
