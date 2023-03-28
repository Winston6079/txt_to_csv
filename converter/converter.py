# -*- coding: utf-8 -*-
import csv, os, re, sys

path_root = os.getcwd()
path_idm = os.getcwd()
questions = []
answers = []
call_again = True

def check_exists_folders():
  qnt_files = 0
  cur_dir = os.scandir(path_idm)
  for entry in cur_dir:
    qnt_files += 1
  if qnt_files == 1:
    how_many_langs()
  else:
    ask_create((qnt_files-1))

def ask_create(qnt_files):
  print("Do you want to add a language?\n y | n")
  user_ans = input('-> ')
  if user_ans == 'y':
    print("How many?")
    new_lang_qnt = input("-> ")
    new_lang_qnt = int(new_lang_qnt)
    create_folders(new_lang_qnt)
  else:
    list_langs(qnt_files)

def how_many_langs():
  print("How many languages are currently learning?")
  num_of_langs = input("-> ")
  num_of_langs = int(num_of_langs)
  create_folders(num_of_langs)

def create_folders(qnt_folders):
  print("Name the language(s) you are learning:")
  x = 1
  while x <= qnt_folders: 
    name_lang = input('-> ')
    if not os.path.exists(name_lang):
        os.mkdir(name_lang)
        print(f"Folder '{name_lang}' created successfully.")
        x += 1
    else:
        print(f"Folder '{name_lang}' already exists.")
  print("The folders were created. Now you have to create the txt files inside of each folder, and you will be able to select them.")

def list_langs(qnt_folders):
  print(f"There are {qnt_folders} language(s) to choose from: ") 
  print_cwd()
  select_language()

def select_language():
  global path_idm
  print("\nWrite the name")
  sel_lang = input("-> ")
  if not os.path.exists(path_root+"\\"+sel_lang):
    print("Enter a valid name.")
    select_language()
  else:
    path_idm = path_root+"\\"+sel_lang
    sub_menu()

def print_cwd():
  cur_dir = os.scandir(path_idm)
  for entry in cur_dir:
    if entry.name == 'converter.py':
      pass
    else:
      print(entry.name)

def select_file():
  cur_dir = os.scandir(path_idm)
  files=0
  for entry in cur_dir:
    files += 1
    print(files)
  if files == 0:
    print("There are no files yet. Create them and you will be able to convert them.")
    sub_menu()
  else:
    print("")
    print("Which file(s) do you want to open?")
    print_cwd()
    print("\n\nTo go back write 'b'")
    sel_file = input("-> ")
    if sel_file == 'b':
      sub_menu()
    sel_file = path_idm+"\\"+sel_file
    print(sel_file)
    process_txt(sel_file)
    copy_to_csv(sel_file)
    sub_menu()

def process_txt(sel_file):
  with open(sel_file, 'r', encoding='utf-8') as bloc:
    lines = bloc.readlines()
    for line in lines:
      before_hyphen = re.search(r"^[^-]*", line)
      after_hyphen = re.search(r"\-(.*)", line)
      if bool(re.search(r"^~$", line)) == True:
        break
      elif bool(re.search(r"https://", line)) == True:
        pass
      elif (bool((re.search(r"^\n$", line))) == False) and (bool((re.search(r"^[^-]+-[^-]+$", line))) == True): # ^[\s]*\n$
        questions.append(before_hyphen.group(0))
        answers.append(after_hyphen.group(1))
      else:
        pass
  bloc.close()

def copy_to_csv(sel_file):
  sel_file = sel_file.replace('.txt', '.csv')
  with open(sel_file, 'w', encoding='utf-8', newline='') as csv_file:
    writer = csv.writer(csv_file)
    
    zipped = zip(questions, answers)
    for entry in zipped:
      writer.writerow(entry)
  
  csv_file.close()
  print("Success\nDone\n")
  print("Do you want to process another file?")
  print("y\nn")
  
  while call_again:
    ask_continue()
  

def ask_continue():
  global call_again, path_idm, questions, answers
  answer = input("-> ")
  if answer == "y":
    answer = True
    call_again = answer
    questions = []
    answers = []
    select_file()  
  elif answer == "n":
    answer = False
    call_again = answer
    path_idm = path_root
  else:
    ask_continue()

def create_file():
  print("Do you want to create a file?\n y | n")
  ans = input("-> ")
  if ans == "y":
    print("How do you want to call it?")
    name_file = input("-> ")
    if os.path.exists(path_idm+'\\'+name_file+'.txt'):
      print("The file already exists.")
      create_file()
    else:
      new_file = open(path_idm+'\\'+name_file+".txt", "w")
      new_file.close()
      print("The file was succesfully created\n")
      create_file()
  elif ans == "n":
      sub_menu()
  else:
    print("Enter a valid answer.")
    create_file()

# not finished
def main_menu():
  print("""
  1) Create language folder
  2) Select language folder
  3) Exit
  
  Select a number:
  """)
  answer = input("-> ")

  if answer == "1":
    create_folders(1)
    main_menu()
  elif answer == "2":
    print("For which language?")
    select_language()
  elif answer == "3":
    print("Bye!")
    sys.exit(0)
  else:
    print("Write a valid answer.")  
    main_menu()


def sub_menu():
  print("""
  1) Create file
  2) Process file
  3) Go back to the main menu
  4) Exit
  """)

  answer = input("-> ")

  if answer == "1":
    create_file()
  elif answer == "2":
    select_file()
  elif answer == "3":
    path_idm = path_root
    main_menu()
  elif answer == "4":
    print("Bye!")
    sys.exit(0)
  else:
    print("Write a valid answer.")  
    sub_menu()



main_menu()