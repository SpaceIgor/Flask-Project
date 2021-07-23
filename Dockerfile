FROM python:3.8

WORKDIR /code

COPY . .

RUN pip install -r requirements.txt

ENV FLASK_ENV=development

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "80"]