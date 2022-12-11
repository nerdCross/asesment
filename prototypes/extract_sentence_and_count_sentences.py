import nltk

para = '''
Welcome to the second lesson of the Doing Presentations Like A Pro.
This course is designed to help you elevate your presentation game.
In the first we learnt about the rudiments of academic presentations.
We saw that these presentations are important to promote as they facilitate cross-fortalization of ideas.
We also identified poster and oral presentations as the two main types of presentation.
In the second we shall focus on poster presentations.
We will consider the and printing required for a good poster.
To start a poster is a visual representation of an idea or research finding to be disseminated to an audience.
One of the most common standard sizes of poster is the A zero paper size with dimension 841 by 1189 mm.
33.1
by 46.8
inches.
'''
sentensenumber = 0
tokens = nltk.sent_tokenize(para)
for t in tokens:
    #print(t)
    #sentensenumber =+1
#print(sentensenumber)
    print (t)
    sentensenumber +=1
print(sentensenumber)