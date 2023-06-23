#Detecting the mention of one of the following programming languages in a text input
#python, java, pearl, visual basic

"""Detect any mention of a Progamming language in the input text."""

text = input("Enter a sentence >> ")
if "python" in text.lower():
    print("Python was mentioned.")
elif "java" in text.lower():
    print("Java was mentioned.")
elif "pearl" in text.lower():
    print("Pearl was mentioned.")
elif "visual basic" in text.lower():
    print("Visual Basic mentioned.")
else:
    print("No Programming language was mentioned.")