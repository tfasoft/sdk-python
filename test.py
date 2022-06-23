from tfa_python_sdk import TFA

auth = TFA('access_token')

result = auth.authUser('user_token')

statCode = result.error

if (statCode == 800):
    print('Authenticated.')
elif (statCode == 820):
    print('User token is wrong.')
elif (statCode == 290):
    print('Admin token is wrong.')