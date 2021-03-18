FROM python:3.8
COPY . /app
WORKDIR /app
RUN pip install -r pip.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["main.py","wordlib.cllrqf9adx3k.us-east-1.rds.amazonaws.com","28R35M5qyw7nBDsQ"]