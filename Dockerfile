# Official Image untuk menjalankan aplikasi
FROM python:3.9

# Default Direktori untuk aplikasi
RUN mkdir -p /simpledjangorestapi
WORKDIR /simpledjangorestapi


# pasang paket pendukung atau dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN apt-get update -y
RUN apt-get install binutils libproj-dev gdal-bin -y

# Salin aplikasi ke Docker
COPY . /simpledjangorestapi

# Buka Port 8000 yang adalah port default web python django
EXPOSE 8000

# jalankan aplikasi web python django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

