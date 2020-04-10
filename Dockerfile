FROM python:3.6-alpine

ENV VIEW_ID="" \
    KEY_FILE_LOCATION=""

ADD . /usr/src/app
WORKDIR /usr/src/app
RUN pip install -r requirements.txt

EXPOSE 9177

CMD ["python", "ga_exporter.py"]
