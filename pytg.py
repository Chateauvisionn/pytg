from time import sleep
import sys
import os
from shutil import rmtree, copyfile

# project management
if sys.argv[1] == "project":

  # create a project
  if sys.argv[2] == "create":

    try:
      # game folder
      print(f"Creating {sys.argv[3]} folder")
      os.mkdir(sys.argv[3])
      # main.py
      print(f"Creating {sys.argv[3]}/main.py")
      with open(f"{sys.argv[3]}/main.py", "w") as mpy:
        mpy.write("from pytg import *\nfrom config import Config\n\ndef game():\n  # game script\n pass\n\nif __name__ == '__main__':\n  game()")
      # config.py
      print(f"Creating {sys.argv[3]}/config.py")
      with open(f"{sys.argv[3]}/config.py", "w") as cpy:
        cpy.write("class Config():\n # config class that you can import in main.py\n pass")
      # chars.txt
      print(f"Creating {sys.argv[3]}/chars.txt")
      with open(f"{sys.argv[3]}/chars.txt", "w") as ct:
        ct.write("[]")
      # saves
      os.mkdir(f"{sys.argv[3]}/saves")
      # module
      os.mkdir(f"{sys.argv[3]}/pytg")
      os.mkdir(f"{sys.argv[3]}/pytg/src")
      os.mkdir(f"{sys.argv[3]}/pytg/src/pytg")
      copyfile("pytg.py", f"{sys.argv[3]}/pytg/src/pytg/pytg.py")
      copyfile("__init__.py", f"{sys.argv[3]}/pytg/src/pytg/__init__.py")
      print("Project created")

    except FileExistsError:
      print("Error: This project already exist.")
  
  # delete a project 
  if sys.argv[2] == "delete":

    try:
      rmtree(sys.argv[3])
      print("Project deleted")

    except FileNotFoundError:
      print("Error: This project doesn't exist.")
  
  # rename
  if sys.argv[2] == "rename":
    try:
      os.rename(sys.argv[3], sys.argv[4])
    except:
      print("This project doesn't exist.")


chars = []

# créer un personnage
def crChar(name):
  chars.append(name)
  strChars = str(chars)
  with open("chars.txt", "w") as f:
    f.write(strChars)

# supprimer tout les personnages
def delAllChars():
  chars.remove()

# faire un choix
def choice(o1,cons1, o2=None, cons2=None):
  if isinstance(cons1, str):
    print(cons1)
  else:
    cons1
  if isinstance(cons2, str):
    print(cons2)
  else:
    cons2
  print(o1)
  print(o2)
  ch = True
  while ch:
    c = input("Choose: ")
    if c == o1:
      cons1
      ch = False
    elif c == o2:
      cons2
      ch = False
    else:
      print('Invalid choice')

# dialogue
def dialog(char, text, time=2):
  print(char,":", text)
  try:
    time.sleep(time)
  except:
    print("Indicated time is not valid")