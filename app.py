from gtts import gTTS 
from playsound import playsound
audio="speech.mp3"
text=''' Good morning sir,my name is sharan teja reddy.I am from Dharmavaram.
I have completed my btech in vardhaman engineering college,Inter in narayana college and schooling in narayana.
coming to my family,My father is a government teacher,My mother is a house wife,2 sisters are working as a software engineers in banglore.
My hobbies are playing cricket,badminton,watching Movies.
coming to my techincal skills i have knowledge on python,Webdevelopment,fundamentals of java and devops'''
sp=gTTS(text=text,lang='en')
sp.save(audio)
playsound(audio)


