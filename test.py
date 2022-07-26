from tfa_python_sdk import TFA

auth = TFA('access_token')

result = auth.authUser('user_token')

statCode = result.status
data = result.data

if (statCode == 200):
    print('Authenticated.')
    user = data['user']
else:
    print(data['message'])