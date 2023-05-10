def vacations():
    ph = "Here is a madlibs on vacations. Please respond to the \
following prompts"
    print(ph)

    adj1 = input("Enter an adjective: ")
    adj2 = input("Enter another adjective: ")
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter another noun: ")
    plurnoun1 = input("Enter a plural noun: ")
    game1 = input("Enter a game: ")
    plurnoun2 = input("Enter another plural noun: ")
    verbING1 = input("Enter a verb ending in \'ing\': ")
    verbING2 = input("Enter another verb ending in \'ing\': ")
    plurnoun3 = input("Enter another plural noun: ")
    verbING3 = input("Enter another verb ending in \'ing\': ")
    noun3 = input("Enter another noun: ")
    plant1 = input("Enter a plant name: ")
    bodyPart1 = input("Enter a part of the body: ")
    place1 = input("Enter a place: ")
    verbING4 = input("Enter another verb ending in \'ing\': ")
    adj3 = input("Enter another adjective: ")
    num1 = input("Enter a number: ")
    plurnoun4 = input("Enter another plural noun: ")

    print(f"\nA vacation is when you take a trip to some {adj1} place\
\nwith your {adj2} family. Usually you go to some place\
\nthat is near a/an {noun1} or up on a/an {noun2}.\
\nA good vacation place is one where you can ride {plurnoun1}\
\nor play {game1} or go hunting for {plurnoun2} . I like\
\nto spend my time {verbING1} or {verbING2}.\
\nWhen parents go on a vacation, they spend their time eating\
\nthree {plurnoun3} a day, and fathers play golf, and mothers\
\nsit around {verbING3}. Last summer, my little brother\
\nfell in a/an {noun3} and got poison {plant1} all\
\nover his {bodyPart1}. My family is going to go to (the)\
\n{place1}, and I will practice {verbING4}. Parents\
\nneed vacations more than kids because parents are always very\
\n{adj3} and because they have to work {num1}\
\nhours every day all year making enough {plurnoun4} to pay\
\nfor the vacation.")


response = input("Are you ready for a MadLibs Game? ")
if response.lower() in "yyes":
    print("Great!")
    vacations()
else:
    print("No Problem! See you next time.")
