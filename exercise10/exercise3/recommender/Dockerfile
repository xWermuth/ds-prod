FROM python:buster

RUN mkdir /src
RUN mkdir /data
COPY ./recommender/src /src
COPY ./recommender/data /data
ADD ./recommender/requirements.txt /

RUN pip install -r requirements.txt

WORKDIR /src
CMD ["python3", "-u", "recommender.py"]