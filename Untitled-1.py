import requests
import json
url="https://westus.api.cognitive.microsoft.com/vision/v1.0/describe?maxCandidates=1"
headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '1e8134bdc68e401bb07f143de8e9c1e0',
}
parameters={
   'maxCandidates':'1'
}
bod={
    "url":"http://www.planwallpaper.com/static/images/desktop-year-of-the-tiger-images-wallpaper.jpg"
    }


response=requests.post(url,"{'url':'http://www.wallpapereast.com/static/images/spring-in-nature-wide-wallpaper-603794.jpg'}",headers=headers)
#response=requests.post(url,data=bod,headers=headers)

data=response.json()
result=data['description']['captions'][0]['text']



#print(data)
print(result)




from gtts import gTTS
import os

tts = gTTS(text=result, lang='en')
tts.save("good.mp3")
os.system(" good.mp3")