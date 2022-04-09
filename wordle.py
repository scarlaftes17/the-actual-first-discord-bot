import random
in_game = False
randword = ""
counter = 6
file = open('fiveletterwords.txt', 'r')
def play_wordle(message, author):
  global randword
  global arr
  global wordarr
  global printarr
  global in_game
  global counter
  _, action, *rest = message.split(" ")
  value = " ".join(rest) if len(rest) >= 0 else ""
  if (action == 'start'):
    counter = 6
    in_game = True
    rand_num = random.randint(0, 500)
    for i in range(rand_num):
      randword = file.readline()
    return "Hello! You are now playing wordle!\n How to play: \n You have six tries to guess a five letter word. Each time you guess a word it will tell you which letters are correct or not. Below is how to indicate which letters are wrong or right: \n Wrong: strike-through ~~t~~ \n Right: bold **t** \n Right letter, wrong place: *t*"
  elif (action == 'end' and in_game == True):
    in_game = False
    return "You are no longer playing wordle :("
  elif (action == 'help' and in_game == True):
    return "How to play: \n You have six tries to guess a five letter word. Each time you guess a word it will tell you which letters are correct or not. Below is how to indicate which letters are wrong or right: \n Wrong: strike-through ~~t~~ \n Right: bold **t** \n Right letter, wrong place: *t*"
  elif (action == 'guess' and in_game == True):
    counter -= 1
    word = rest[0]
    arr = []
    wordarr = []
    printarr = []
    if (len(word) != 5):
      counter += 1
      return "The word should be five letters"
    for j in range(len(word)):
      colorletter = f'~~{word[j]}~~'
      for i in range(len(randword)):
        if (randword[i] == word[j] and j == i):
          colorletter = f'**{word[j]}**'
          continue
        elif (randword[i] == word[j] and j != i):
          colorletter = f'*{word[j]}*'
      printarr.append(colorletter)
    prstr = " ".join(printarr)

    for i in range(len(word)):
      if (randword[i] == word[i]):
        i += 1
    
    if (i == 5):
      in_game = False
      return f'{prstr}\nYou win! The word was {randword}'
    
    if (counter == 0):
      in_game = False
      return f'{prstr}\nYou lose :frowning2: The word was {randword}'
    return f'Guess: {prstr}\nCounter: {counter}'
  else:
    return "this is not a valid action"
  
  
