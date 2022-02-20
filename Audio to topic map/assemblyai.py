import requests
from refiner import *
import json

auth_key = 'de360e77e84f4cd88a553930eb979168'
headers = {"authorization": auth_key}#, "content-type": "application/json"}
def read_file(filename):
   with open(filename, 'rb') as _file:
       while True:
           data = _file.read(5242880)
           if not data:
               break
           yield data
 
upload_response = requests.post('https://api.assemblyai.com/v2/upload',
 headers=headers, data=read_file('testlec.mp4'))
audio_url = upload_response.json()["upload_url"]

transcript_request = {'audio_url': audio_url}
transcript_response = requests.post("https://api.assemblyai.com/v2/transcript", json=transcript_request, headers=headers)
_id = transcript_response.json()["id"]
#print(transcript_response.json())
polling_response = requests.get("https://api.assemblyai.com/v2/transcript/" + _id, headers=headers)
while polling_response.json()['status'] != 'completed':
    if polling_response.json()['status'] != 'completed':
        polling_response = requests.get("https://api.assemblyai.com/v2/transcript/" + _id, headers=headers)
    else:
        with open(_id + '.txt', 'w') as f:
            f.write(polling_response.json()['text'])
            print('Transcript saved to', _id, '.txt')
        break
print(polling_response.json()['text'])


initial = starter_format(polling_response.json()['text'])

misc(initial, "common.txt")

second = format_dataset("other.txt")


print("\nFormatted data and searching for keywords.... \n")


query_words = filter(initial, second)
print(query_words)

# save the query words to a json file
query_words_json = {"query_words": list(query_words)}
with open('query_words.json', 'w') as f:
    json.dump(query_words_json, f)
