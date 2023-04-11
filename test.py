from tfa_python_sdk import TFA

auth = TFA('rglscfrrdqdjvalsyvwzelrab')

result = auth.authUser("pjdbdzynbcqalcdnmoinsutdb")

statCode = result['status']
data = result['data']

if (statCode == 200):
    print({"user": data})
else:
    print({"message": data['message']})
