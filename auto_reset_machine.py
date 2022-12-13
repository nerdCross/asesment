import os
if (os.getcwd() == "/home/ubuntu/smart_transcribe"):
        cmd = "cd smart_transcribe/"
        returned_value = os.system(cmd)
        cmd2 = "source trans/bin/activate"
        returned_value2 = os.system(cmd2)
        cmd3 = "uvicorn main:app --reload"
        returned_value3 = os.system(cmd3)
else:
    pass
#elif(os.getcwd() != "/home/ubuntu/smart_transcribe"):    
 #   pass    