# IDVA S3 Interface Microservice
The S3 Interface microservice is a Python [Flask](https://flask.palletsprojects.com/en/2.1.x/)
application that exposes a REST API for the access, normalization, and deletion of images stored
in IDVA's S3 bucket.

The service that is required to communicate with the S3 bucket is not able to sign requests per [AWS Signature Version 4](https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html).
Instead, this Flask app will act as an S3 interface using [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html).

The service that requires the images can only handle images as base64 strings - all images fetched are converted to base64 format.

## CI/CD Workflows with GitHub Actions
The most up-to-date information about the CI/CD flows for this repo can be found in the
[GitHub workflows directory](https://github.com/18F/identity-idva-s3-interface/tree/main/.github/workflows)

## Building Locally

### Pre-requisites
Make sure you have the following installed if you intend to build the project locally.
- [Python 3.10](https://www.python.org/)
- [CloudFoundry CLI](https://docs.cloudfoundry.org/cf-cli/)

### Development Setup
To set up your environment, run the following commands (or the equivalent
commands if not using a bash-like terminal):
```shell
# Clone the project
git clone https://github.com/GSA-TTS/identity-idva-s3-interface
cd identity-idva-s3-interface

# Set up Python virtual environment
python3.9 -m venv .venv
source .venv/bin/activate
# .venv\Scripts\Activate.ps1 on Windows

# Install dependencies and pre-commit hooks
python -m pip install -r requirements-dev.txt
pre-commit install
```

### Running the application
After completing [development setup](#development-setup) application locally with:
```shell
python -m pytest # NOTE that without DEBUG=True, local unit tests will fail
gunicorn s3-interface.main:app
```

### Available endpoints

`GET` or `DELETE` `/<vendor_id>?file=<file_name>`


### Testing the application
After completing [development setup](#development-setup) application locally with:
```shell
pytest
```

### Viewing API Endpoints and documentation
Documentation can be viewed locally by running the application and visiting
http://127.0.0.1:8000/redoc

### Deploying to Cloud.gov during development
All deployments require having the correct Cloud.gov credentials in place. If
you haven't already, visit [Cloud.gov](https://cloud.gov) and set up your
account and CLI.

*manifest.yml* file contains the deployment configuration for cloud.gov, and expects
a vars.yaml file that includes runtime variables referenced. For info, see
[cloud foundry manifest files reference](https://docs.cloudfoundry.org/devguide/deploy-apps/manifest-attributes.html)

Running the following `cf` command will deploy the application to cloud.gov
```shell
cf push --vars-file vars.yaml \
  --var ENVIRONMENT=<env>
```

## Public domain

This project is in the worldwide [public domain](LICENSE.md). As stated in
[CONTRIBUTING](CONTRIBUTING.md):

> This project is in the public domain within the United States, and copyright
and related rights in the work worldwide are waived through the
[CC0 1.0 Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/).
>
> All contributions to this project will be released under the CC0 dedication.
By submitting a pull request, you are agreeing to comply with this waiver of
copyright interest.
