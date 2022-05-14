file = open('starters.txt', 'r')
def play_pokemon(message, author):
  _, action, *rest = message.split(" ")
  value = " ".join(rest) if len(rest) >= 0 else ""
  if (action == 'start'):
    return "hello! Welcome to pokemon battle! Choose a starter to battle with! (selct a number) \n  1. Charmander <:charmander:> \n 2. Bulbasaur \n 3. Squirtle \n 4. Pikachu \n 5. Eevee \n 6. Chikorita \n 7. Cyndaquil \n 8. Totodile \n 9. Treecko \n 10. Torchic \n 11. Mudkip \n 12. Turtwig \n 13. Chimchar \n 14. Piplup \n 15. Snivy \n 16. Tepig \n 17. Oshawott \n 18. Chespin \n 19. Fennekin \n 20. Froakie \n 21. Rowlet \n 22. Litten \n 23. Popplio \n 24. Grookey \n 25. Scorbunny \n 26. Sobble"
  elif (action == 'select'):
    starter1 = []
    starter1.append(rest[0])
    starter1.append(rest[1])
    pokemon1 = ''
    pokemon2 = ''
    #number = 0
    #line = 1
    for number, line in enumerate(file, 1):
      if (starter1[0] in line):
        pokemon1 = file.readline()
      elif(starter1[1] in line):
        pokemon2 = file.readline()
    
    return pokemon1, pokemon2
