# pull official base image
FROM python:3.10

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# set work directory
WORKDIR /usr/src/welcome_proj

# install psycopg2 dependencies
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements_docker.txt .
RUN pip install -r /usr/src/welcome_proj/requirements_docker.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/welcome_proj/entrypoint.sh

# copy project
COPY . .

RUN chmod +x /usr/src/welcome_proj/entrypoint.sh
RUN apt install -y netcat

# run entrypoint.sh
ENTRYPOINT ["/usr/src/welcome_proj/entrypoint.sh"]
