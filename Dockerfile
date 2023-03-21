FROM python:3.9
FROM mysql/mysql-server:8.0.24


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
# install python dependencies
#RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

# running migrations
RUN python manage.py migrate

# gunicorn
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "core.wsgi"]
