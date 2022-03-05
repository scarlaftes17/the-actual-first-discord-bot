checklists = {}
def handle_checklist(message, author):
  _, action, *rest = message.split(" ")
  value = " ".join(rest) if len(rest) >= 0 else ""
  if (author not in checklists):
    checklists[author] = []
  if (action == 'add'):
    newlist = checklists[author]
    newlist.append(value)
    checklists.update({author: newlist})
    return 'Your message was successfully added'
  elif (action == 'view'):
    viewlist = checklists[author]
    response = ""
    for i in range(len(viewlist)):
      response = f'{response}{i+1}. {viewlist[i]}\n'
    return response
  elif (action == 'delete'):
    newlist = checklists[author]
    if (value.isnumeric() == False):
      return 'Item does not exist'
    if(len(newlist) < int(value)):
      return 'This item is not a number'
      
    index = int(value) - 1
    newlist.pop(index)
    checklists.update({author: newlist})
    return 'Item successfully deleted'
      
  elif (action == 'complete'):
    newlist = checklists[author]
    index = int(value) - 1
    newlist[index] = f'~~{newlist[index]}~~'
    checklists.update({author: newlist})
    return f'{value} was completed'
  elif (action == 'clear'):
    checklists.update({author: []})
    return 'Your checklist was cleared'
  else:
    return 'The command action was not valid'