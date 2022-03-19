import random
in_game = False
word = ""
file = open('fiveletterwords.txt', 'r')

def play_wordle(message, author):
  global word
  _, action, *rest = message.split(" ")
  value = " ".join(rest) if len(rest) >= 0 else ""
  if (action == 'start'):
    in_game = True
    rand_num = random.randint(0, 500)
    for i in range(rand_num):
      word = file.readline()
    return "Hello! You are now playing wordle!\n How to play: \n You have six tries to guess a five letter word. Each time you guess a word it will tell you which letters are correct or not. Below is how to indicate which letters are wrong or right: \n Wrong: strike-through ~~t~~ \n Right: bold **t** \n Right letter, wrong place: *t*"
  elif (action == 'end'):
    in_game = False
    return "You are no longer playing wordle :("
  elif (action == 'help'):
    return "How to play: \n You have six tries to guess a five letter word. Each time you guess a word it will tell you which letters are correct or not. Below is how to indicate which letters are wrong or right: \n Wrong: strike-through ~~t~~ \n Right: bold **t** \n Right letter, wrong place: *t*"
  elif (action == 'guess'):
    return word
  else:
    return "this is not a valid action"
  
  
