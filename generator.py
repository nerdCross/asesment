from pipelines import pipeline
import requests
from pre_parse import parseWords
# import OS module
import os
from files_return import returnthefiles
 
# This is my path
#path = " "
# to store files in a list
#list = []
#########
#cmd = "python -m nltk.downloader punkt"
#returned_value = os.system(cmd)
nlp = pipeline("question-generation", model="valhalla/t5-base-qg-hl")
def gen(resource_link,unique_id):
    url = 'http://35.179.12.250/transpile/'
    myobj = {"resource_link": "https://relen.s3.us-east-2.amazonaws.com/audio/samples/sample3.wav"}
    myobj["resource_link"] = resource_link
    print("Dictionary = ",myobj)
    transcribed_text = requests.post(url, json = myobj)
    transcribed_text = transcribed_text.text
    print(transcribed_text)
    path_to_directory = parseWords(transcribed_text,unique_id)
    path_to_directory = path_to_directory + unique_id
    #print(path_to_directory)
    #after the preprocessing is done now get all the text files and store the questions and ans in a list.
    path_to_text_files = returnthefiles(path_to_directory)

    print (path_to_directory)
    the_textfiles = returnthefiles(path_to_directory)
    print(the_textfiles)
    #questions_and_ans = nlp(preprocessed)
    #print (questions_and_ans)
    #return questions_and_ans
link = "https://relen.s3.us-east-2.amazonaws.com/audio/samples/sample5.wav"
unique_id = "asdfjhagerfiwenqrg"
gen(link,unique_id)