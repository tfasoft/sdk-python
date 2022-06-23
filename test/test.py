from tfa_python_sdk import tfa_python_sdk as tfa

auth = tfa.TFA('test')

result = auth.authUser('again')

print(result)