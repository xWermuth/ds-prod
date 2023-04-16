FROM python:buster

RUN mkdir /src
COPY ./feedback/src /src
ADD ./feedback/requirements.txt /

RUN pip install -r requirements.txt

WORKDIR /src
CMD ["python3", "-u", "feedback.py"]