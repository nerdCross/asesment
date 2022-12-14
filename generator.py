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
    #print("Dictionary = ",myobj)
    transcribed_text = requests.post(url, json = myobj)
    transcribed_text = transcribed_text.text
    #print(transcribed_text)
    path_to_directory = parseWords(transcribed_text,unique_id)
    #print(path_to_directory)
    #after the preprocessing is done now get all the text files and store the questions and ans in a list.
    #path_to_text_files = returnthefiles(path_to_directory)

    #print("here:", path_to_text_files )
    #the_textfiles = returnthefiles(path_to_directory)
    #print(the_textfiles)
    #questions_and_ans = nlp(preprocessed)
    #f = open(file_path+"/"+"demo.txt", "w")
    #var = f.read()
    #print (questions_and_ans)
    #return  print(the_textfiles)
    return path_to_directory

    #return questions_and_ans
#link = "https://relen.s3.us-east-2.amazonaws.com/audio/samples/sample5.wav"
#unique_id = "asdfjhagerfiwenqrg"
#path = gen(link,unique_id)

#thepath = path
# print(type(path))
#tab = returnthefiles(thepath)
#print(tab)

def assesment():
    link = "https://relen.s3.us-east-2.amazonaws.com/audio/samples/sample5.wav"
    unique_id = "asdfjhagerfiwenqrg"
    path = gen(link,unique_id)
    tab = returnthefiles(path)
    # getting length of list
    #length = len(tab)
    print(tab)

    # Iterating the index
    # same as 'for i in range(len(list))'#
    for i in tab:
        #print (i)
        f = open(i, "r")
        var = f.read()
        print(var)
        questions_and_ans = nlp(var)
        print ("?????????"+i)
        print (questions_and_ans)
        
assesment()




