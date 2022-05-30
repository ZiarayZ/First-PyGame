from cryptography.fernet import Fernet
import os

test = levelName = ""
def looped():
    global levelName, test
    print("Default levels 1-11, name your levels 12+")
    levelName = input("\nSpecify name of map.\nFor example: \'level_12\'\n\n>: ").lower().strip() + ".bin"
    levelName = levelName.replace(".txt", "").replace(".bin.bin", ".bin")
    if "level_" in levelName:
        test = levelName.replace("level_","").replace(".bin","")
        test = int(test)

file = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "key.key"), "rb")
load_key = file.read()
levelKey = Fernet(load_key)
file.close()
print("Loaded key.")
print("")

running = True
while running:
    levelName = input("\nSpecify name of map (txt) file.\nFor example: \'example level.txt\'\n\n>: ").strip()
    level = ""
    if not levelName.endswith(".txt") and not levelName.endswith(".bin"):
        levelName += ".txt"
    elif levelName.endswith(".bin"):
        levelName.replace(".bin",".txt")

    file = open(os.path.join("build", levelName), "r")
    for line in file:
        level += line
    file.close()
    level = level.rstrip()
    print("\nTranslated level.")
    looped()

    while test >= 1 and test <= 11:
        print("You cannot replace the original 11 levels!!")
        looped()

    file = open(os.path.join("maps", levelName), "wb")
    #translate decrypted to encrypted
    file.write(levelKey.encrypt(level.encode()))
    file.close()
    print("Level creation finished successfully.")

    again = input("Would you like to load another level?\n\n>: ").lower().strip()
    if again == "no" or again == "n":
        running = False
