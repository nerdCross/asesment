import nltk

para = '''Welcome to the second lesson of the Doing Presentations Like A Pro.
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
In doing a poster the presenter would usually take about 5 minutes to speak to the poster and then stand by
for questions.
The number of questions a poster presentation generates can be a deciding factor for its success.
That is to you will know how successful your poster presentation is if it generates a lot of questions afterwards.
This would be an indication that your poster is interesting to people and that people are interested in the thoughts you
are trying to share in that poster.
The choice of poster formats is usually left for the presenter.
Of there are some events where you would be given a standard poster but in most cases you are allowed to choose what you like.
All kinds of templates can be downloaded online and adapted for use as a property.
You can feel free to get and tweak any format of interest you can find on the internet.
you are just edit templates of format you you adjust them to your own taste.
the creation of a poster will usually include brief in-s and discussion and conclusion.
You have to ensure you do justice to each part.
Inorganizing the content of a graphics and blank spaces should all be appropriately deployed for maximum impact.
This can be a real game changer.
Since the poster is mostly words should only be used when necessary.
Having too many words or words in unnecessary places in your poster can be a disaster.
Wordy posters can be boring.
they should be avoided by all means.
In font style and size should be carefully chosen for the desired impact.
Color combination is another crucial factor in a poster.
This is particularly important because the kinds of colors used can determine whether the poster will be good enough to
attract attention after printing.
good quality printing is important.
If you think of how your poster will after right from the moment you set out to design the poster.
this is all about keeping the end in view.
You do not want to choose formats or design templates or color combinations that will not be good after you print as a recap.
The poster presentation has a lot to do with a poster and as can you be taking to make good decisions about key features that I stated like organization and the printing.
A masterful interplay of all these components will set your poster presentation apart.
you want to show yourself as the master.
You want to show yourself as a pro you are supposed to be.
Now that you have these great you have to implement them.
They must not remain in the realm of ideas in your head.
You have to capitalize on the lessons you have on the tips you have got from this lesson.
that you can be an expert poster presenter.
that you can be that poster presenter that people look up to.
that you can be that person that people get ideas from.
What you make presentations should be able to get ideas for making their own posters in the future.
And that is why this lesson has been put across to you right now.
And you want to definitely make the most of this opportunity you have to be a master poster to be a master poster
and to be an inspiring one while at it.
Until I see you in the next lesson.
Thank you very much for paying attention.
Make sure you turn people's head the next time you present your poster.
See you later.
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