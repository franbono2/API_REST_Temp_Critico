FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /dockerDSC
WORKDIR /dockerDSC
COPY . /dockerDSC/
RUN pip install -r requirements.txt