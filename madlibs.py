def mad_libs() -> None:
    adj1 = input("Adjective1 : ")
    v1 = input("Verb1 : ")
    v2 = input("Verb2 : ")
    n1 = input("Noun1 : ")
    v3 = input("Verb3 : ")
    v4 = input("Verb4 : ")
    print(f"Jimmie is {adj1}")
    print(f"He tends to {v1} and {v2} in his free time")
    print(f"{n1} is his bf and they {v3} together all the time!!!")
    print(f"{v4} Hitler!!!!")
Start_game = input("Play a game ? (Y/N) : ").upper()
if Start_game == "Y":
    mad_libs()
else:
    print("Bye")