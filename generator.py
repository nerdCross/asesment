from pipelines import pipeline
import requests
import os
from preprocessing import processor
cmd = "python -m nltk.downloader punkt"
returned_value = os.system(cmd)
nlp = pipeline("question-generation", model="valhalla/t5-base-qg-hl")
def gen(resource_link):
    url = 'http://3.8.100.147/transpile/'
    myobj = {"resource_link": "https://relen.s3.us-east-2.amazonaws.com/audio/samples/sample3.wav"}
    myobj["resource_link"] = resource_link
    print("Dictionary = ",myobj)
    transcribed_text = requests.post(url, json = myobj)
    transcribed_text = transcribed_text.text
    print(transcribed_text)
    preprocessed = processor(transcribed_text)
    print (preprocessed)
    questions_and_ans = nlp(preprocessed)
    print (questions_and_ans)
    #return questions_and_ans
link = "https://relen.s3.us-east-2.amazonaws.com/audio/samples/sample5.wav"
gen(link)