import random
print("""
__        __   _                            _          _       _   _        
\ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___   | | ___ | |_| |_ ___  
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | |/ _ \| __| __/ _ \ 
  \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | | | (_) | |_| || (_) |
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  |_|\___/ \__|\__\___/ 
                                                                            
               _ 
   _ __  _   _| |
  | '_ \| | | | |
 _| |_) | |_| |_|
(_) .__/ \__, (_)
  |_|    |___/   

""")

players = []
def add() :
  new_player = input("\ninsert the name of the new player: ")
  tot_tikets = input("\ninsert the number of tickets of the new player: ")
  print("")
  for x in range(int(tot_tikets)) :
    players.append(new_player)
  rules()
def play() :
  winner = random.choice(players)
  print(f"\nwin {winner}!")
  print("")
def info() :
  print("\ncoming soon!")
  print("")
  rules()
def exit_game() :
  print("\nbye bye!")
  print("")
  exit()
def rules():
  print("""
1) add one player
2) play
3) info
4) exit
""")
  answer = input("> ")
  if answer == "1" :
    add()
  elif answer == "2" :
    play()
  elif answer == "3" :
    info()
  elif answer == "4" :
    exit_game()
  else:
    print("\ninvalid option, retry!")
    rules()
rules()
