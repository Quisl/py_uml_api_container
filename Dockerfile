FROM alpine:3.7
EXPOSE 8000
COPY scripts/main.py /scripts/main.py


RUN apk add --update --no-cache build-base
RUN apk add --update --no-cache python3  && ln -sf python3 /usr/bin/python
RUN apk add --update --no-cache python3-dev
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

RUN apk add --update --no-cache graphviz ttf-ubuntu-font-family


RUN pip install pylint
RUN pip install fastapi
RUN pip install aiofiles
RUN pip install python-multipart
RUN pip install uvicorn

WORKDIR /scripts
CMD uvicorn main:app --reload --host 0.0.0.0 --port 8000