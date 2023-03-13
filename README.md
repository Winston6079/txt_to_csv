# txt_to_csv
This program is meant to copy txt files to a csv file that can be imported to anki.

the txt file must be done in the following format: the word in the foreign language to the left - translation to the right, for example:

hola - hello
uno - one

The script then will create a csv file where on the A column you will have all the foreign words, and to the right on the B column all the translations. 
This is because when you import a file to anki, it needs to be (one possible format) csv, the left column will be imported as the "question" card and the right as the "answer" card
You can't add more than one hyphen per line.

For the moment you need to create the txt file by yourself, maybe in the future i'll add more features.
Also: I know that this script is probably full of bad practices and maybe mistakes. I'm learning this language, and found myself in the need of this script. 
I've used it, done some tests and hasn't failed me yet. Meaning it does what it's meant to do.

Why would I write on a txt file the words that I want to remember and then import to anki, if instead I can directly write it on a csv file?
- It's more comfortable and faster, at least in my experience. A txt file is lighter to open, there's no need to pay for it (like Microsoft Excel), you don't need to
cick on each column when writing both words (meaning writing is more fluid in the txt file).

After the conversion a csv file will be created, that's the one you import.
keep the folder that contains the script only with said script, and any other folder that's the language that you are learning.

For example in the txt_to_csv folder -> converter.py, french (folder), spanish(folder)
Only inside of these folders you add the txt.
