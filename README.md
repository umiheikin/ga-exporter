# ga-exporter

This is a sample exporter for google analytics metrics wich allow to get current active user for the viewId

REQUIRIMENTS:

1) Create your google service account on GCP and download json key file.

2) Provide to this account permissions for your ViewId in Google Analytics.
   More details about steps available by link https://developers.google.com/analytics/devguides/reporting/core/v4/authorization

3) Install docker on your host.


STEPS TO RUN:

1) Define key file location in ga_exporter.py (variable named KEY_FILE_LOCATION)

2) Run docker build -t <docker_tag/here:v1.0> .

3) Run docker container from the image which just created
   docker run -d --restart=always -p 9177:9177 -e VIEW_ID="215444465" -e ACCOUNT_EMAIL="your_account_name" <docker_tag/here:v1.0>
