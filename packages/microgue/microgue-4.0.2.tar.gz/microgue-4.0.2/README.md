# AWS Microservice Bootstrap Code

This project contains bootstrap code to speed up the development of AWS based microservices

This includes:
- Redis Cache
- EventBridge
- DynamoDB Models, Tables, and Objects
- SQS Queues
- Secrets Manager
- S3 Storage

This project also includes base code for:
- Logger Definitions
- Service Connections
- Flask App Definitions
- Additional Utilities


### Working On Microgue

Repo: https://bitbucket.org/michaelhudelson/microgue/src/master

Clone: `git clone https://bitbucket.org/michaelhudelson/microgue/src/master`

### Requirements

- Python 3.7+

### Pre-Setup

- Make sure you have an IAM user created with correct permissions in your AWS account

    - Create an Access Key on that user

    - Install awscli `pip install awscli`

    - Add that Access Key with `aws configure`

    - Verify you are using the correct Access Key with `aws configure list`

    - You can also verify by looking at the file `~/.aws/credentials`

### Install Microgue

```
pip install microgue
```

### Flask Setup (Optional)

- Put the following code in the app.py file in the root of the project

```python
import logging
from microgue.abstract_app import AbstractApp

logging.basicConfig()


class App(AbstractApp):
    pass


app = App().app

```

- In the terminal run the following commands

```
export PYTHONUNBUFFERED=1
export FLASK_DEBUG=1
flask run
```

- GET http://127.0.0.1:5000

### Distribution
```
# update version in setup.py

# commit and push changes
git add .
git commit -m "v1.0.X"
git push origin master

# tag the commit and push
git tag -a v1.0.X -m "Release v1.0.X"
git push --tags

# package with:
python setup.py sdist bdist_wheel

# https://pypi.org/project/microgue/
# upload to pypi with:
python -m twine upload dist/*

# OPTIONAL
# https://test.pypi.org/project/microgue/
# upload to test pypi with:
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

### Backlog
- get_all accept sk_operation ["eq", "begins_with", "between", "lt", "lte", "gt", "gte"]
  - Operation.begins_with = lambda sk, sk_value: Key(sk).begins_with(sk_value)
