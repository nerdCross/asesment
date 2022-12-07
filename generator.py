from pipelines import pipeline
import requests
nlp = pipeline("question-generation", model="valhalla/t5-base-qg-hl")

def gen(resource_link):
    url = 'https://ec2-18-134-208-139.eu-west-2.compute.amazonaws.com/transpile'
    data = resource_link
    transcribed_text = requests.post(url, data=data)
    print (transcribed_text)
    questions_and_ans = nlp(transcribed_text)
    print (questions_and_ans)
    return questions_and_ans

resource_link = "https://relen.s3.us-east-2.amazonaws.com/audio/samples/sample3.wav"
gen(resource_link)

