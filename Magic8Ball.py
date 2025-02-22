#Magic8Ball.py
#Name:
#Date:
#Assignment:

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.
  answers = ["As I see it, yes.", "Ask again later.", "Better not tell you now.",
             "Cannot predict now.", "Concentrate and ask again.",
             "Don't count on it.", "It is certain.", "It is decidedly so.",
             "Most likely.", "My reply is no.", "My sources say no.",
             "Outlook not so good.", "Outlook good.", "Reply hazy, try again.", 
             "Signs point to yes.", "Very doubtful.", "Without a doubt.", 
             "Yes.", "Yes - definitely.", "You may rely on it."] 
  
  # Each item must be in quotes, separated by a comma.
  #Answer question randomly with one of the options from your earlier list.

  num = random.random() #decimal 0 - 1 
  num = num * 1000 #number 0 - 999 with decimals
  num = int(num) # no more decimals
  
  things = len(answers)
  num = num % things

  question = input("Ask me a question: ")
  print(answers[num])

  
if __name__ == '__main__':
  main()
