# Email Voice Assistant                                                 

:point_right: This is a basic automation voice assistant with using python.Writing emails to colleagues 
and clients is a very time-consuming job, so this simple automation program that helps to send emails to 
clients without typing a single word on your computer.
 You can use any message you want to say that will help you to send emails without using the keyboard.

# Library Explanation
A package definition is *yagmail module* which is a  Gmail/SMTP(Simple Mail Transfer Protocol) client that 
removes the issues of sending emails through Python, *PyAudio library* and *Speech Recognition library* from Google API.
* These 3 libraries must be installed in your machine before performing the script. Now I just give a simple explanation about these three libraries.
Many of them don't know about this library, First one is a speech-recognition library. This library is used to record the audio through a microphone. And
we're going to give the real-time audio input to this program. So only we're using this library.
The next one is the yagmail library. It is used to automate emails by using the SMTP protocol.
And another one is the supporting library for the speech-recognition library. This library's name is pyaudio, Why we're using this library means when we
are connecting the microphone with a laptop for recording real-time audio this library is a much-needed one for performing this task.
This is the explanation about the packages that we installed.

# How It Works
Firstly, create a variable called a receiver, and in this variable type the receiver's email ID.
And next, you need to create a variable for the message and here you've to pass the variable called text.
After that, you need to create a variable for the sender and in this variable, you need to type the sender's email.
And finally, you have to send the email to the receiver end for that just write this code.
