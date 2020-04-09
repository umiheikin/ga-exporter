FROM python:3.6-alpine

RUN apk update
RUN apk --no-cache add openssl-dev gcc libffi-dev linux-headers musl-dev
RUN pip install setuptools prometheus_client google-api-python-client cryptography cffi pyOpenSSL
RUN pip install --upgrade oauth2client

ENV BIND_PORT 9173
ENV START_DATE "2020-04-04"
ENV ACCOUNT_EMAIL "myserviceaccount-657@oval-bricolage-259713.iam.gserviceaccount.com"
ENV VIEW_ID "215444465"

ADD . /usr/src/app
WORKDIR /usr/src/app

CMD ["python", "ga_exporter.py"]
