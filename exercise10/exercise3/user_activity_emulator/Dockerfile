FROM python:buster

RUN mkdir /src
RUN mkdir /data
COPY ./user_activity_emulator/src /src
COPY ./user_activity_emulator/data /data
ADD ./user_activity_emulator/requirements.txt /

RUN pip install -r requirements.txt

WORKDIR /src
CMD ["python3", "-u", "useractivity_app.py"]