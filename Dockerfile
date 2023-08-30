FROM python:3.9

RUN apt-get update && apt-get install -y \
    wget \
    xvfb \
    libfontconfig \
    libfreetype6 \
    libxrender1 \
    xfonts-75dpi \
    xfonts-base \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]