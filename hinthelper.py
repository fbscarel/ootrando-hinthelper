#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, pickle, platform, re, string, sys
from colorama import init, Fore, Back, Style
from getkey import getkey, keys
from operator import itemgetter

# songs
songs = [
    "Bolero of Fire",
    "Epona's Song",
    "Minuet of Forest",
    "Nocturne of Shadow",
    "Prelude of Light",
    "Requiem of Spirit",
    "Saria's Song",
    "Serenade of Water",
    "Song of Storms",
    "Song of Time",
    "Sun's Song",
    "Zelda's Lullaby"]

# SONG checks
song_checks = [
    "Bolero Check",
    "Burning Kak",
    "Minuet Check",
    "OoT Check",
    "Prelude Check",
    "Requiem Check",
    "Serenade Check",
    "Sun's Song Check"]

# core items
items = [
    "Biggoron's Sword",
    "Bomb Bag",
    "Bombchus",
    "Boomerang",
    "Boss Key",
    "Bottle",
    "Bottle with Big Poe",
    "Bow",
    "Claim Check",
    "Deku Nut Capacity",
    "Deku Stick Capacity",
    "Din's Fire",
    "Double Defense",
    "Farore's Wind",
    "Fire Arrows",
    "Goron Tunic",
    "Hover Boots",
    "Iron Boots",
    "Kokiri Sword",
    "Lens of Truth",
    "Light Arrows",
    "Magic Meter",
    "Megaton Hammer",
    "Mirror Shield",
    "Progressive Hookshot",
    "Progressive Scale",
    "Progressive Strength Upgrade",
    "Progressive Wallet",
    "Ruto's Letter",
    "Slingshot",
    "Small Key",
    "Zora Tunic"]

# list of checks, full
full_checks = [
    "10 Big Poes",
    "20 Gold Skulltulas",
    "30 Gold Skulltulas",
    "40 Gold Skulltulas",
    "50 Gold Skulltulas",
    "Adult Fishing",
    "Adult Shooting Gallery",
    "Barinade",
    "Bean at Crater",
    "Bean at Desert",
    "Bean at Graveyard",
    "Biggoron",
    "Bombchu Bowling Bomb Bag",
    "Bombchu Bowling Piece of Heart",
    "Bongo Bongo",
    "Bottom of the Well",
    "BotW Dead Hand",
    "Child Fishing",
    "Child Shooting Gallery",
    "Colossus Left Side (Adult)",
    "Colossus Right Side (Kid)",
    "Composer Grave Chest",
    "Darunia's Joy",
    "Deku Tree",
    "Desert Colossus",
    "Death Mountain Crater",
    "Death Mountain Trail",
    "Dodongo's Cavern",
    "Deku Theater Skull Mask",
    "Fire Temple",
    "Fire Temple Megaton Hammer Chest",
    "Fire Temple Pierre Chest",
    "Forest Temple",
    "Forest Temple Floormaster Chest",
    "Frogs 2",
    "Ganon's Castle",
    "Gerudo Fortress",
    "Gerudo Valley",
    "Gerudo Valley Hammer Rocks Chest",
    "Gohma",
    "Goron City",
    "Goron City Left Maze Chest",
    "Goron City Pot",
    "Graveyard",
    "GTG",
    "GTG Final Chest",
    "GTG Toilet Chest",
    "GTG Sunken Silver Rupees Chest",
    "Haunted Wasteland",
    "Horseback Archery 1500 Points",
    "Hyrule Castle",
    "Hyrule Field",
    "Ice Cavern",
    "Icy Waters",
    "Jabu Jabu",
    "Kakariko Village",
    "King Dodongo",
    "Kokiri Forest",
    "Lake Hylia",
    "Lon Lon Ranch",
    "Lost Woods",
    "Market",
    "Morpha",
    "Phantom Ganon",
    "Sacred Forest Meadow",
    "Shadow Temple",
    "Shadow Temple Floormaster Chest",
    "Shoot the Sun",
    "Skull Kid",
    "Spirit Temple",
    "Sun's Song Check Chest",
    "Temple of Time",
    "Treasure Chest Game",
    "Twinrova",
    "Unfreeze King Zora",
    "Volvagia",
    "Wasteland Chest",
    "Water Temple",
    "Water Temple Gilded Chest",
    "Water Temple River Chest",
    "Zora's Domain",
    "Zora's Fountain",
    "Zora's River",
    "Zora's Fountain Ice Lake"]

def pc(text, color):
    op = {"b": Fore.BLACK,
          "r": Fore.RED,
          "g": Fore.GREEN,
          "y": Fore.YELLOW,
          "u": Fore.BLUE,
          "m": Fore.MAGENTA,
          "c": Fore.CYAN,
          "w": Fore.WHITE}
    return op.get(color) + text + Style.RESET_ALL

def bc(text, color):
    return Back.YELLOW + text + Style.RESET_ALL

def pexit():
    sys.exit()

def askq(plist, question):
    s = ""
    i = 0    

    while True:
        os.system(clearstr)

        r = re.compile(".*" + s + ".*", re.IGNORECASE)
        nlist = list(filter(r.match, plist))

        print(question + "\n")

        if len(s) > 0:
            for x, y in enumerate(nlist):
                if x == i:
                    print(bc(y, "y"))
                else:
                    print(y)

        print("\n=====================================================")

        if len(s) > 0:
            print(pc("\n[UP and DOWN to scroll through list, ENTER to select]", "b"), end="")
            print(pc("\nFilter: ", "u") + s, end="")
        else:
            print(pc("\nFilter: ", "u") + "[Type at least one letter to search]", end="")

        c = getkey()
        if c == keys.BACKSPACE or c == keys.DELETE:
            s = s[:-1]
        elif c == keys.UP and i > 0:
            i -= 1
        elif c == keys.DOWN and i < len(nlist) - 1:
            i += 1
        elif c.isalnum():
            s = s + c
            i = 0
        elif c == keys.ENTER:
            return nlist[i]
        else:
            pass

def ghint(ct, clt):
    global hints

    if ct == "item":
        s = askq(items, pc("Item?", "c"))
    c = askq(full_checks, pc("Check Location?", "r"))

    if ct == "item":
        hints.append(["item", s, c])
    else:
        hints.append([ct, c])

    main_loop()

def song_hint():
    global hints
    print("songhint")
    s = askq(songs, pc("Song?", "g"))
    c = askq(song_checks, pc("Song Check?", "r"))

    hints.append(["song", s, c])
    main_loop()

def item_hint():
    ghint("item", "full")

def dead_hint():
    ghint("dead", "full")

def woth_hint():
    ghint("woth", "small")

def fool_hint():
    ghint("fool", "small")

def phint(type, text, check):
    global hints

    r = [e for e in hints if e[0] == type]

    if len(r) > 0:
        print("\n" + text)

        r = sorted(r, key=itemgetter(1))
        for h in r:
            if check == True:
                print("\t" + h[1] + pc(" is at ","m") + h[2])
            else:
                print("\t" + h[1])

def undo_hint():
    global hints

    print(hints[-1])
    del hints[-1]
    main_loop()

def kill_hint():
    global hints

    hints.clear()
    main_loop()

def loadf():
    global fname, hints
    if os.path.isfile(fname) and os.stat(fname).st_size != 0:
        f = open(fname, "rb")
        hints = pickle.load(f)
        f.close()

def writef():
    global fname, hints
    f = open(fname, "wb")
    pickle.dump(hints, f)

def main_hints():
    phint("woth", pc("Way of the Hero:", "y"), False)
    phint("fool", pc("Barren Locations:", "r"), False)
    phint("song", pc("Songs:", "g"), True)
    phint("item", pc("Items:", "c"), True)
    phint("dead", pc("Dead Checks:", "u"), False)

def main_prompt():
    op = {"s": song_hint,
          "i": item_hint,
          "d": dead_hint,
          "w": woth_hint,
          "f": fool_hint,
          "u": undo_hint,
          "k": kill_hint,
          "e": pexit}

    print("\n=====================================================================")
    print("\n" + pc("(W)","y") + "oth | " + pc("(F)","r") + "ool | " + pc("(S)","g") + "ong | " + pc("(I)","c") + "tem | " + pc("(D)","u") + "ead | " + pc("(U)","m") + "ndo | " + pc("(K)","m") + "ill | " + pc("(E)","w") + "xit ", end="")
    c = getkey()
    try:
        op[c.lower()]()
    except SystemExit:
        print()
        writef()
        pass
    except:
        main_loop()

def main_loop():
    os.system(clearstr)
    main_hints()
    main_prompt()

hints = []
if platform.system() == "Windows":
    fname = ".\\.hinthelper.p"
    clearstr = "cls"

else:
    fname = "./.hinthelper.p"
    clearstr = "clear"

init()
loadf()

main_loop()
