# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.
FROM python:3.6

# SECURITY WARNING: keep the secret key used in production secret!
ENV SECRET_KEY = '4zssufhakip_%dl@5^iiay^tj)fk3a9rhs6w5bhwvzb_x&@35w'
ENV POSTGRES_PASSWORD=postgres_password
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt
RUN python -m nltk.downloader punkt

