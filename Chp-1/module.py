import pyjokes

print("Hello! Here's a joke for you:")
joke = pyjokes.get_joke()
print(joke) 

import pyttsx3
engine = pyttsx3.init()
engine.say("Hello! Here's a joke for you:")
engine.runAndWait() 


import os

# Specify the directory path
path = "."   # "." means the current working directory

# Print all files and folders in the directory
for item in os.listdir(path):
    print(item)


