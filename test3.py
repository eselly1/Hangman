import random
word_list=['Maximum','Network',"Plan","Aardvark","Hydration","Morning","work",'hurricane','dream','sunshine','ring','book','fire','girl','chocolate','curly', 'bored','rambunctious','healthy', 'twitch', 'cool','minecraft','play','game','seltzer']
word=word_list[random.randint(0,len(word_list)-1)].lower()
print(' _                                             ')
print('| |                                            ')
print('| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  ')
print("| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ")
print("| | | | (_| | | | | (_| | | | | | | (_| | | | |")
print("|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|")
print("                    __/ |                      ")
print("                   |___/                       ")

print('Let\'s play Hangman!')

lives = 6

num_letters=[]
for i in word:
  i="_"
  num_letters.append(i)
def gallows6():
  print("   +---------------+   ")
  print("   |               |   ")
  print("   |               |   ")
  print("   |                   ")
  print("   |                   ")
  print("   |                   ")
  print("   |                   ")
  print(" __+__                 ")
def gallows5():
  print("   +---------------+   ")
  print("   |               |   ")
  print("   |               |   ")
  print("   |               O   ")
  print("   |                   ")
  print("   |                   ")
  print("   |                   ")
  print(" __+__                 ")
def gallows4():
  print("   +---------------+   ")
  print("   |               |   ")
  print("   |               |   ")
  print("   |               O   ")
  print("   |               |   ")
  print("   |                   ")
  print("   |                   ")
  print(" __+__                 ")
def gallows3():
  print("   +---------------+   ")
  print("   |               |   ")
  print("   |               |   ")
  print("   |               O   ")
  print("   |               |   ")
  print("   |              /    ")
  print("   |                   ")
  print(" __+__                 ")
def gallows2():
  print("   +---------------+   ")
  print("   |               |   ")
  print("   |               |   ")
  print("   |               O   ")
  print("   |               |   ")
  print("   |              / \  ")
  print("   |                   ")
  print(" __+__                 ")
def gallows1():
  print("   +---------------+   ")
  print("   |               |   ")
  print("   |               |   ")
  print("   |              \O   ")
  print("   |               |   ")
  print("   |              / \  ")
  print("   |                   ")
  print(" __+__                 ")
def gallows0():
  print("   +---------------+   ")
  print("   |               |   ")
  print("   |               |   ")
  print("   |              \O/  ")
  print("   |               |   ")
  print("   |              / \  ")
  print("   |                   ")
  print(" __+__                 ")
num_lettersfinal = ''
guess=input('Guess a letter: ').lower()
while num_lettersfinal!= word and lives>0 and guess!=word:
  if lives>0:
    
    x=word.count(guess)
    if x>0:
      if lives == 6:
        gallows6()
      elif lives == 5:
        gallows5()
      elif lives == 4:
        gallows4()
      elif lives == 3:    
        gallows3()
      elif lives==2:
        gallows2()
      elif lives == 1:
        gallows1()
      for i in range(0,len(word)):
        if word[i]==guess:
          num_letters[i]=guess
          num_lettersfinal=''
          for i in num_letters:
            num_lettersfinal += i
      print(f'You guessed the letter {guess}. {guess} is in the word, good job!')
      print(num_lettersfinal)
    else:
        lives -= 1
        if lives == 6:
          gallows6()
        elif lives == 5:
          gallows5()
        elif lives == 4:
          gallows4()
        elif lives == 3:    
          gallows3()
        elif lives==2:
          gallows2()
        elif lives == 1:
          gallows1()
        print(f'You guessed the letter {guess}, but it is not in the word! Try again!')
        print(num_lettersfinal)  
    print(f'Lives: {lives}')
    guess=input("Guess a letter or a word: ").lower()
if num_lettersfinal == word and lives>0:
  print('You guessed the right word. You win!')
elif num_lettersfinal != word and lives == 0:
  gallows0()
  print(f'You couldn\'t guess the word! The word was {word}. You lose!')
elif guess == word and lives > 0:
  print('You guessed the right word. You win!')

playagain=input('Would you like to play again? Y/N: ').lower
while playagain == "y" or "yes":
  print(' _                                             ')
  print('| |                                            ')
  print('| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  ')
  print("| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ")
  print("| | | | (_| | | | | (_| | | | | | | (_| | | | |")
  print("|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|")
  print("                    __/ |                      ")
  print("                   |___/                       ")
  word_list=['Maximum','Network',"Plan","Aardvark","Hydration","Morning","work",'hurricane','dream','sunshine','ring','book','fire','girl','chocolate','curly', 'bored','rambunctious','healthy', 'twitch', 'cool','minecraft','play','game','seltzer']
  word=word_list[random.randint(0,len(word_list)-1)].lower()
  print('Let\'s play Hangman!')

  lives = 6

  num_letters=[]
  for i in word:
    i="_"
    num_letters.append(i)

  num_lettersfinal = ''

  while num_lettersfinal!= word and lives>0 and guess != word:
    if lives>0:
      guess=input('Guess a letter: ').lower()
      x=word.count(guess)
      if x>0:
        if lives == 6:
          gallows6()
        elif lives == 5:
          gallows5()
        elif lives == 4:
          gallows4()
        elif lives == 3:    
          gallows3()
        elif lives==2:
          gallows2()
        elif lives == 1:
          gallows1()
        for i in range(0,len(word)):
          if word[i]==guess:
            num_letters[i]=guess
            num_lettersfinal=''
            for i in num_letters:
              num_lettersfinal += i
        print(f'You guessed the letter {guess}. {guess.upper()} is in the word, good job!')
        print(num_lettersfinal)
      else:
          lives -= 1
          if lives == 6:
            gallows6()
          elif lives == 5:
            gallows5()
          elif lives == 4:
            gallows4()
          elif lives == 3:    
            gallows3()
          elif lives==2:
            gallows2()
          elif lives == 1:
            gallows1()
          print(f'You guessed the letter {guess}, but it is not in the word! Try again!')
          print(num_lettersfinal)  
      print(f'Lives: {lives}')   
            
  if num_lettersfinal == word and lives>0:
    print('You guessed the right word. You win!')
  elif num_lettersfinal != word and lives == 0:
    gallows0()
    print(f'You couldn\'t guess the word! The word was {word}. You lose!')
  elif guess == word and lives >0:
    print('You guessed the right word. You win!')
  playagain=input('Would you like to play again? Y/N: ').lower
print("Thanks for playing!")
