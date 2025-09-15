FROM python:3.11.11-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential pkg-config default-libmysqlclient-dev \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip 
RUN pip install -r requirements.txt
COPY . .

CMD ["python","manage.py","runserver","0.0.0.0:8000"]
