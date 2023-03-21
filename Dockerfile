FROM python:3.9

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && \
    apt-get install -y default-libmysqlclient-dev

# copy application requirements and install
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy application files
COPY . .

# run migrations
RUN python manage.py migrate

# start the application with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi:application"]
