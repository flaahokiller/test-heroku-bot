FROM alpine
RUN apk update
RUN apk upgrade
RUN apk add python3-dev gcc musl-dev
RUN python3 -m ensurepip
RUN pip3 install --no-cache -U pip wheel
COPY . /opt/botname
WORKDIR /opt/botname
RUN pip3 install -r requirements.txt
CMD [ "python3", "-m", "botname" ]
