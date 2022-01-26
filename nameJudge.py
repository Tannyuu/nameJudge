import requests
import json

url = 'https://api.genderize.io/'
firstName=input("あなたの名前を入力してください>>")
params = {'name':str(firstName)}
res = requests.get(url, params)
data = json.loads(res.text)
#print(data)
judge = data['gender']
#print(judge)

if judge == 'female':
   print("あなたは女性ですね？")
else:
   print("あなたは男性ですね？")
