FROM python:3.11-slim

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt && \
    groupadd -r demouser && useradd -r -g demouser demouser && \
    mkdir /src && \
    chown -R demouser:demouser /src

USER demouser
WORKDIR /src

COPY app.py .

ENV FLASK_APP=app.py REDIS_HOST=redis

# Expose Flask default port
EXPOSE 5000

CMD ["flask", "run", "-h", "0.0.0.0"]
