# Telegram Factor Authentication - Python SDK

[Python SDK document is in docs.tfasoft.com](https://docs.amirhossein.info/sdks/python)

If you are using **TFA** as your authentication service in your python applications, you can use our library.

## How to use the library

So, let's have a quick review of our steps.

- Installation
- Configuration
- Checking result

### Installation

The easiest step is installation. You can install it with `pip` or `pipenv`. Just go ahead and enter the command below:

```shell
$ pip3 install tfa-python-sdk
```

Congratulations! First step is done!

### Configuration

After installation, go to your file and import the library:

```python
from tfa_python_sdk import TFA
```

Second, you need to epecify the **accecc_token**. You can get it in your dashboard panel. So, call the class:

```python
auth = TFA('access_token')
```

Ok, now library know your access token. Now it's time to enter the **user_token**. User token is the code you get it from your form field or a post method. Importent is to get user token. So, we use `authUser` function to pass user token and get the result.

```python
result = auth.authUser('user_token')
```

You are done it this step. Let's move forward and check status codes and check user result.

### Checking result

When you get the result, you can check codes and see what are them. Here is a quick review:

```python
statCode = result.status
data = result.data

if (statCode == 200):
    print('Authenticated.')
    user = data['user']
else:
    print(data['message'])
```

Now if your code is 200, it means that you know have user. If it is else, it means your code is 401. For object that returns to you, chesk object below.

## Returned Objects

Here let's know about them in deep.

- ### 200

```json
{
    "user": {
        "_id": "document id",
        "uid": "telegram user id",
        "token": "one time token. Every time become null",
        "createdAt": "when created",
        "updatedAt": "last update",
        "__v": 0
    }
}
```

- ### 401

One is access token is wrong.

```json
{
    "message": "User authentication token is not valid"
}
```

Another is when user token is wrong.

```json
{
    "message": "Admin access token is not valid"
}
```

## Development

If you want to develop the library, it is so simple. Edit library codes and run `test.py` like this:

```shell
$ python3 test.py
```

> Before you start: **Remember the base or codes are stored in `tfa_python_sdk/tfa_python_sdk.py`. You need to edit there.