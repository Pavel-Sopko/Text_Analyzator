# author = "Pavel Sopko"

TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

         '''
At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

         '''
The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
         ]
ODDELOVAC = "=" * 35
ODDELOVAC_mini = "-" * 15
data_uzivatel = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}
print(f"""{ODDELOVAC}
Welcome in application 'Text Analyzator'
{ODDELOVAC}
""")

username = input("Enter username: ")
heslo = input("Enter password: ")

if data_uzivatel.get(username.lower()) == heslo:
    print("Login OK, continue.")

else:
    print("Sorry, your login is incorrect. Exit application."), exit()

print(f"""{ODDELOVAC}
Welcome to the app, {username}
We have 3 texts to be analyzed.
{ODDELOVAC}
""")
for i, text in enumerate(TEXTS, 1):
    print(f"TEXT{i}\n{text}\n{ODDELOVAC}")

vyber_textu = TEXTS[int(input("Enter a number btw. 1 and 3 to select: ")) - 1]

list_slov_z_textu = vyber_textu.strip(",.:!").split()
pocet_slov_text = len(list_slov_z_textu)

pocet_tittlecase, pocet_uppercase, pocet_lowercase, pocet_numeric, suma_numeric = 0, 0, 0, 0, 0

for slovo in list_slov_z_textu:
    if slovo.istitle():
        pocet_tittlecase += 1
    elif slovo[:].isalpha() and slovo[:].isupper():
        pocet_uppercase += 1
    elif slovo[:].isalpha() and slovo[:].islower():
        pocet_lowercase += 1
    elif slovo.isdigit():
        pocet_numeric += 1
        suma_numeric += int(slovo)

print(f"""{ODDELOVAC}
There are {pocet_slov_text} words in the selected text.
There are {pocet_tittlecase} titlecase words.
There are {pocet_uppercase} uppercase words.
There are {pocet_lowercase} lowercase words.
There are {pocet_numeric} numeric strings.
The sum of all the numbers {suma_numeric}
{ODDELOVAC}
""")

graf = {}
for slovicka in list_slov_z_textu:
    graf[len(slovicka)] = graf.get(len(slovicka), 0) + 1

vsechny_hodnoty = sorted(list(graf.items()))

print("LEN | OCCURENCES | Nr.")
for neco in vsechny_hodnoty:
    print(neco[0], "|", "*" * int(neco[1]), "|", neco[1])
