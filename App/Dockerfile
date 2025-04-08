FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y nginx curl && \
    pip install --no-cache-dir flask

WORKDIR /app

COPY app.py requirements.txt ./

COPY default.conf /etc/nginx/sites-available/default

RUN pip install -r requirements.txt

RUN ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log

CMD ["sh", "-c", "service nginx start && exec python app.py"]

