from django import forms
from .models import *


class quiz_form(forms.ModelForm):
    score = 0
    score = int(score)
    name = input("What is your name?")
    name = name.title()
    print("""Hello {}, welcome to Quiz night! 
    You will be presented with 5 questions.
    Enter the appropriate number to answer the question
    Good luck!""".format(name))
    print("""What is the term for ‘Maori’ language?
    1. Te Rex 
    2. Hangi 
    3. Hongu 
    4. Te Reo""")
    answer1 = "4"
    response1 = input("Your answer is:")
    if (response1 != answer1):
        print("Sorry, that is incorrect!")
    else:
        print("Well done! " + response1 + " is correct!")
        score = score + 1
        print("Your current score is " + str(score) + " out of 5")
        print("""What is the Maori term for ‘tribe’ or ‘mob’?
1. Mihi 
2. Iwi 
3. Awi 
4. Hapu""")

    answer2 = "2"
    response2 = input("Your answer is:")
    if (response2 != answer2):
        print("Sorry, that is incorrect!")
    else:
        print("Well done! " + response2 + " is correct!")
    score = score + 1
    print("Your current score is " + str(score) + " out of 5")
    print("Your total score is " + str(score) + " out of 5")
    print("Thank you for playing {}, goodbye!".format(name))

    class Meta():
        model = q_a
        fields = ['Question', 'Answer1', 'Answer2', 'Answer3', 'Answer4', 'CorAns']
