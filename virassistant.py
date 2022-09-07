from email import message
import speech_recognition as sr
import yagmail


#source means your microphone that you connected to your computer
recognizer=sr.Recognizer() 
with sr.Microphone() as source:
    print('Clearing background noise..')
    recognizer.adjust_for_ambient_noise(source,duration=1)
    print("waiting for your massage..")
    recordedaudio=recognizer.listen(source)
    print('Done recording!')

    try:
        print('Printing the massage')
        text=recognizer.recognize_google(recordedaudio,language='en-US')
        print('Your massage:{}'.format(text))


    except Exception as ex:
        print(ex)

    #Automate mails:

    reciever='sample1@gmail.com'
    massage=text
    sender=yagmail.SMTP('sample2@gmail.com')
    sender.send(to=receiver,subject='This is an automated mail',contents=message)