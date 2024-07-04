FROM python:3.9-slim

WORKDIR /app

COPY listener.py .

RUN pip install nameko

CMD ["nameko", "run", "--broker", "amqp://rabbitmq", "listener"]
