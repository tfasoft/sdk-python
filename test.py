from tfa_python_sdk import tfa_python_sdk

auth = tfa_python_sdk.TFA('test')

result = auth.authUser('again')

print(result)