FROM python:3.10
ENV PYTHONUNBUFFERED=1
ARG USER_ID=0

RUN apt-get update && apt-get install -y python3-dev default-libmysqlclient-dev build-essential
RUN mkdir -p /home/appuser
RUN chown -R ${USER_ID}:${USER_ID} /home/appuser
RUN groupadd -r appuser
RUN useradd -r -u ${USER_ID} -g appuser appuser
USER appuser

COPY requirements.txt /code/
WORKDIR /code
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /code/
