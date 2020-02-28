FROM python:3

ADD . .

CMD ["python", "./src/calculatorTests.py"]
