FROM python:3.8

WORKDIR /code

COPY . .

RUN pip install -r requirements.txt

ENV FLASK_ENV=development

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8000"]
