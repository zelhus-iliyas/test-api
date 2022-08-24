FROM ubuntu:jammy-20220801
RUN apt-get update && apt-get install -y \
    python3 python3-pip
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN apt install build-essential python3-dev
RUN pip install pytz --upgrade
# upgarde tzdata up to tzdata-2022.2
RUN pip install tzdata --upgrade

RUN apt install -y  gcc libffi-dev libc-dev apache2 libapache2-mod-wsgi-py3 
RUN pip install -r requirements.txt

COPY . /code/

# ENTRYPOINT ["bash", "entrypoint.sh" ]

# CMD [ "start" ]