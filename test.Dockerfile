FROM python
RUN python -m pip install --upgrade pip
WORKDIR /app
COPY ./testserver.py /app/
RUN pip install requests
CMD ["python", "testserver.py"]