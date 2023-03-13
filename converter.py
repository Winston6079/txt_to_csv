# -*- coding: utf-8 -*-
import csv, os, re

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
  print("do you want to add another language?\n y | n")
  user_ans = input('-> ')
  if user_ans == 'y':
    print("how many?")
    new_lang_qnt = input("-> ")
    new_lang_qnt = int(new_lang_qnt)
    create_folders(new_lang_qnt)
  else:
    list_langs(qnt_files)

def how_many_langs():
  print("how many languages are currently learning?")
  num_of_langs = input("-> ")
  num_of_langs = int(num_of_langs)
  create_folders(num_of_langs)

def create_folders(qnt_folders):
  print("name the language(s) you are learning:")
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
  print("\nwrite the name")
  sel_lang = input("-> ")
  path_idm = path_idm+"\\"+sel_lang
  select_file()

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
  else:
    print("")
    print("Which file(s) do you want to open?")
    print_cwd()
    sel_file = input("-> ")
    sel_file = path_idm+"\\"+sel_file
    print(sel_file)
    process_txt(sel_file)
    copy_to_csv(sel_file)

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
  else:
    ask_continue()

check_exists_folders()