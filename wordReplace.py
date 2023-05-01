def replaceWord(str):
    wordToReplace = input("Enter word to replace: ")
    if wordToReplace not in str:
        print("No such word found!")
        exit()
    replaceWith = input("Enter word to replace with: ")
    print(str.replace(wordToReplace, replaceWith))


replaceWord("Hey, my name is Shreevaths.")
