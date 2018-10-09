from src.search import main


def test():

    if len(main("", "PineaPple")) > 0 and main("", "PineaPple")[
            0][2] == 'slice of pineapple upside-down cake.':
        print("1. Case insensitive query working :)")
    else:
        print("1. Case insensitive query not working")

    if main("", "miles at") == [
            ['bulolli2.txt', 1, '   "Land Ho!  Four MILES AT starboard!  Land-Ho!"']]:
        print("2. Zero index bug fixed :D")
    else:
        print("2. Zero index bug present")
