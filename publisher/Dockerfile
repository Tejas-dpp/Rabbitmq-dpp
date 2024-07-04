FROM python:3.9-slim

WORKDIR /app

COPY publisher.py .

RUN pip install nameko

CMD ["nameko", "run", "--broker", "amqp://rabbitmq", "publisher"]
