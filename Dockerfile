FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

CMD exec gunicorn \
    --bind :$PORT \
    --workers 2 \
    resume_site.wsgi:application