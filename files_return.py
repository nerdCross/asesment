# take in a dir and index and return the list of file path.
# import OS module
import os
import files_return
# dirs=directories
# for (root, dirs, file) in os.walk(path):
#    for f in file:
#        if 'file_' in f:
#             #print(type(f))
#             ad = path+"/"+f
#             list.append(ad)
#             #print(path+"/"+f)
#             #print (list)
#             #print(type(list))
# print (list)

def returnthefiles(path):
    # This is my path
    #path = "assessment_index" #i will have to comment this out and get the real path in which will contain the index concatenated with the path.
    # to store files in a list
    list = []
    for (root, dirs, file) in os.walk(path):
        for f in file:
            if 'file_' in f:
                    #print(type(f))
                    ad = path+"/"+f
                    list.append(ad)
                    #print(path+"/"+f)
    #print(list)
    return list
                    #print(type(list))
    #########
#path = "assessment_index" #i will have to comment this out and get the real path in which will contain the index concatenated with the path.

#table = returnthefiles(path)
#print (table)