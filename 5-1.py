voted = {}
value = voted.get("tom")
def check_voter(name):
    if voted.get(name):
        print("is out!")
    else:
        voted[name] = True
        print('let vote')
check_voter("tom")
check_voter("tom")