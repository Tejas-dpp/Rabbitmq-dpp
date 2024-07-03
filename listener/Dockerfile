FROM python
RUN pip install nameko
COPY listener.py /listener.py
CMD ["nameko", "run", "--broker", "pyamqp://guest:guest@rabbitmq", "listener"]
