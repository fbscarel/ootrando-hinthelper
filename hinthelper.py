#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import io, os, pickle, platform, re, string, sys, json
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
    "Eyeball Frog",
    "Eyedrops",
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
    "Prescription",
    "Prog Hookshot",
    "Prog Scale",
    "Prog Strength",
    "Prog Wallet",
    "Ruto's Letter",
    "Slingshot",
    "Small Key",
    "Triforce Piece",
    "Zora Tunic"]

# KEY checks
kchecks = [
    "Bolero of Fire",
    "Epona's Song",
    "Minuet of Forest",
    "Nocturne of Shadow",
    "Requiem of Spirit",
    "Saria's Song",
    "Song of Storms",
    "Song of Time",
    "Sun's Song",
    "Zelda's Lullaby",
    "Bomb Bag",
    "Boomerang",
    "Bottle",
    "Bow",
    "Claim Check",
    "Din's Fire",
    "Eyeball Frog",
    "Eyedrops",
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
    "Prescription",
    "Prog Hookshot",
    "Prog Scale",
    "Prog Strength",
    "Prog Wallet",
    "Ruto's Letter",
    "Slingshot",
    "Zora Tunic"]
kchecks.sort()

# repeatable items
repeatables = [
    "Bomb Bag",
    "Bombchus",
    "Boss Key",
    "Bottle",
    "Bow",
    "Deku Nut Capacity",
    "Deku Stick Capacity",
    "Goron Tunic",
    "Magic Meter",
    "Prog Hookshot",
    "Prog Scale",
    "Prog Strength",
    "Prog Wallet",
    "Slingshot",
    "Small Key",
    "Triforce Piece",
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
    "Anjus Chickens",
    "Barinade",
    "Bean at Crater",
    "Bean at Desert",
    "Bean at Graveyard",
    "Biggoron",
    "Bombchu Bowling Bomb Bag",
    "Bombchu Bowling Piece of Heart",
    "Bongo Bongo",
    "Boomerang Chest",
    "Bottom of the Well",
    "BotW Dead Hand",
    "Child Fishing",
    "Child Shooting Gallery",
    "Colossus Left Side (Adult)",
    "Colossus Right Side (Kid)",
    "Composer Grave Chest",
    "Anjus Cuccos",
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
    "Outside Ganon's Castle",
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

# woth-valid places
woth_places = [
    "Bottom of the Well",
    "Deku Tree",
    "Desert Colossus",
    "Death Mountain Crater",
    "Death Mountain Trail",
    "Dodongo's Cavern",
    "Fire Temple",
    "Forest Temple",
    "Ganon's Castle",
    "Gerudo Fortress",
    "Gerudo Valley",
    "Goron City",
    "Graveyard",
    "GTG",
    "Haunted Wasteland",
    "Hyrule Castle",
    "Hyrule Field",
    "Ice Cavern",
    "Jabu Jabu",
    "Kakariko Village",
    "Kokiri Forest",
    "Lake Hylia",
    "Lon Lon Ranch",
    "Lost Woods",
    "Market",
    "Outside Ganon's Castle",
    "Sacred Forest Meadow",
    "Shadow Temple",
    "Spirit Temple",
    "Temple of Time",
    "Water Temple",
    "Zora's Domain",
    "Zora's Fountain",
    "Zora's River"]

# shops
shops = [
    "Goron City Shop",
    "Kakariko Left Shop",
    "Kakariko Right Shop",
    "Kokiri Shop",
    "Market Left Shop",
    "Market Night Shop",
    "Market Right Shop",
    "Zora's Domain Shop"]

# scrubs
scrubs = [
    "Crater, near fairy fountain                 (1) [Nothing, Child]",
    "Crater, red rock near Goron City entrance   (3) [Hammer, Adult]",
    "Desert Colossus, silver rock near warp pad  (2) [Silvers, Adult]",
    "Dodongo's Cavern, after Lizalfo fight       (1) [Dungeon]",
    "Dodongo's Cavern, left side near entrance   (1) [Dungeon]",
    "Dodongo's Cavern, near Bomb Bag chest       (2) [Dungeon]",
    "Ganon's Castle, invisible wall under bridge (4) [Dungeon]",
    "Gerudo Valley, near carpenter's tent        (2) [SoS, Both]",
    "Goron City, past the lava room              (3) [Hookshot + Goron Tunic OR SoT, Adult]",
    "Hyrule Field, southern grotto               (1) [Bombs, Both]",
    "Jabu Jabu, diving behind the elevator       (1) [Dungeon]",
    "Lake Hylia, under gravestone                (3) [Nothing, Both]",
    "Lon Lon Ranch, southeast open grotto        (3) [Nothing, Child]",
    "Lost Woods, grotto near SFM                 (2) [Bombs, Both]",
    "Lost Woods, near bridge                     (1) [Nothing, Child]",
    "Lost Woods, near mask theater               (2) [Nothing, Child]",
    "Sacred Forest Meadow, grotto near warp pad  (2) [SoS, Both]",
    "Zora's River, grotto near entrance rocks    (2) [SoS, Both]"]

# cows
cows = [
    "DM Trail, bombable grotto near climb start       (1) [Bombs, Both]",
    "Gerudo Valley, bottom platform near waterfall    (1) [Nothing, Child]",
    "Hyrule Field, bombable grotto near Gerudo Valley (1) [Bombs/Hammer + Fire source, Both]",
    "Kakariko, inside Impa's House                    (1) [Nothing, Both]",
    "Kokiri Forest, inside Link's House               (1) [Epona, Adult]",
    "Lon Lon Ranch, back silo                         (2) [Nothing, Both]",
    "Lon Lon Ranch, right side door from entrance     (2) [Nothing, Both]"]

# entrances
entrances = [
    "Deku Tree",
    "Dodongo's Cavern",
    "Jabu Jabu",
    "Forest Temple",
    "Fire Temple",
    "Water Temple",
    "Shadow Temple",
    "Spirit Temple",
    "Bottom of the Well",
    "Ice Cavern",
    "Gerudo Training Grounds"]

# dungeons
dungeons = [
    "Deku Tree",
    "Dodongo's Cavern",
    "Jabu Jabu",
    "Forest Temple",
    "Fire Temple",
    "Water Temple",
    "Shadow Temple",
    "Spirit Temple",
    "Bottom of the Well",
    "Ice Cavern",
    "Gerudo Training Grounds"]

def question(type):
    q = {"item": pc("Item?", "c"),
         "location": pc("Check Location?", "r"),
         "song": pc("Song?", "g"),
         "song_check": pc("Song Check?", "r"),
         "shop": pc("Shop?", "m"),
         "dungeon": pc("Dungeon?", "m"),
         "entrance": pc("Entrance?", "m"),
         "cow": pc("Remaining Cow checks:", "m"),
         "scrub": pc("Remaining Scrub checks:", "m"),
         "trick": pc("Select trick from list:", "y"),
         "whints": pc("Select WOTH location:", "y"),
         "kchecks": pc("Check found there?", "y")}
    return q.get(type)

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
    return Back.CYAN + text + Style.RESET_ALL

def pexit():
    sys.exit()

def askq(olist, qt, ct):
    global hints
    plist = olist[:]
    s = ""
    i = 0

    r = [e for e in hints if e[0] == ct]
    if len(r) > 0:
        for h in r:
            if qt == "song_check" or qt == "entrance":
                if h[2] in plist: plist.remove(h[2])
            elif qt == "kchecks":
                for item in h[2:]:
                    if item in plist and item not in repeatables:
                        plist.remove(item)
            else:
                if h[1] in plist and h[1] not in repeatables:
                    plist.remove(h[1])

    while True:
        os.system(clearstr)

        r = re.compile(".*" + s + ".*", re.IGNORECASE)
        nlist = list(filter(r.match, plist))

        print(question(qt) + "\n")

        if len(s) >= 0:
            for x, y in enumerate(nlist):
                if x == i:
                    print(bc(y, "y"))
                else:
                    print(y)

        print("\n====================================================================")

        if len(s) > 0:
            if olist == cow_checks or olist == scrub_checks:
                print(pc("\n[UP and DOWN to scroll through list, ENTER to mark check as done, ESC to cancel]", "c"), end="")
                #print(pc("\n['<' and '>' to scroll through list, ENTER to mark check as done, ESC to cancel]", "c"), end="")
                print(pc("\nFilter: ", "u") + s, end="")
            else:
                print(pc("\n[UP and DOWN to scroll through list, ENTER to select, ESC to cancel]", "c"), end="")
                #print(pc("\n['<' and '>' to scroll through list, ENTER to select, ESC to cancel]", "c"), end="")
                print(pc("\nFilter: ", "u") + s, end="")
        else:
            if olist == cow_checks or olist == scrub_checks:
                print(pc("\nFilter: ", "u") + "[Type at least one letter to search, ENTER to mark check as done, ESC to cancel]", end="")
            else:
                print(pc("\nFilter: ", "u") + "[Type at least one letter to search, ESC to cancel]", end="")

        c = getkey()
        if c == keys.BACKSPACE or c == keys.DELETE:
            s = s[:-1]
        elif (c == keys.UP or c == keys.LEFT) and i > 0:
        #elif (c == keys.ANGLE or c == keys.TAIL) and i > 0:
            i -= 1
        elif (c == keys.DOWN or c == keys.RIGHT) and i < len(nlist) - 1:
        #elif (c == keys.RIGHT_ANGLE or c == keys.SPOT) and i < len(nlist) - 1:
            i += 1
        elif c == keys.ENTER:
            return nlist[i]
        elif c == keys.ESC:
            raise Exception('Break out')
        elif c.isalnum():
            s = s + c
            i = 0
        else:
            pass

def ghint(ct):
    global hints
    global cow_checks
    global scrub_checks

    if ct == "item" or ct == "shop":
        s = askq(items, "item", ct)

    if ct == "shop":
        c = askq(shops, "shop", ct)
        os.system(clearstr)
        print(pc("\nPrice? ", "u"), end="")
        p = input()
    elif ct == "cows":
        c = askq(cow_checks, "cow", ct)
    elif ct == "scrubs":
        c = askq(scrub_checks, "scrub", ct)
    elif ct == "woth" or ct == "fool":
        c = askq(woth_places, "location", ct)
    else:
        c = askq(full_checks, "location", ct)

    if ct == "shop":
        hints.append([ct, s, c, p])
    elif ct == "item":
        hints.append([ct, s, c])
    elif ct == "cows":
        cow_checks.remove(c)
    elif ct == "scrubs":
        scrub_checks.remove(c)
    elif ct == "woth":
        set = False
        for index, hint in enumerate(hints):
            if hint[0] == c:
                hints[index].insert(0, "woth")
                set = True
        if not set:
            hints.append([ct, c])
    else:
        hints.append([ct, c])

    main_loop()

def song_hint():
    global hints
    s = askq(songs, "song", "song")
    c = askq(song_checks, "song_check", "song")

    hints.append(["song", s, c])
    main_loop()

def entrance_sanity():
    global hints
    s = askq(dungeons, "dungeon", "entrance")
    c = askq(entrances, "entrance", "entrance")

    hints.append(["entrance", s, c])
    main_loop()

def item_hint():
    ghint("item")

def dead_hint():
    ghint("dead")

def woth_edit():
    global hints

    s = askq(woth_places, "location", "woth_edit")
    k = askq(kchecks, "kchecks", "woth")

    set = False
    for index, hint in enumerate(hints):
        if hint[1] == s:
            hints[index].append(k)
            set = True

    if not set:
        hints.append([s, k])

    main_loop()

def woth_hint():
    ghint("woth")

def fool_hint():
    ghint("fool")

def shop_sanity():
    ghint("shop")

def cow_sanity():
    ghint("cows")

def scrub_sanity():
    ghint("scrubs")

def advanced_tricks():
    c = askq(trick_list, "trick", "trick")
    for trick in tricks:
        if trick['Name'] == c:
            os.system(clearstr)
            print(pc("\nTrick name: ", "y") + trick['Name'], end="")
            print(pc("\nRequirements: ", "u") + trick['Requirements'], end="")
            print("\n\n====================================================================\n")
            for line in io.StringIO(trick['Description']):
                print("- " + line)
            print("\n====================================================================")
            print(pc("\nPress ANY KEY to return to main menu", "c"), end="")
            print()
            while True:
                c = getkey()
                if c:
                    raise Exception('Break out')
                else:
                    pass
    main_loop()

def phint(type, text, check):
    global hints

    r = [e for e in hints if e[0] == type]

    if len(r) > 0:
        print("\n" + text)

        r = sorted(r, key=itemgetter(1))
        for h in r:
            if check == "shop":
                print("\t" + h[1] + pc(" is at ","m") + h[2] + pc(" for ","m") + h[3] + pc(" rupees","m"))
            elif check == "long":
                print("\t" + h[1] + pc(" is at ","m") + h[2])
            elif check == "woth":
                print("\t" + h[1] + " (" + ', '.join(h[2:]) + ")")
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
    phint("woth", pc("Way of the Hero:", "y"), "woth")
    phint("fool", pc("Barren Locations:", "r"), "short")
    phint("song", pc("Songs:", "g"), "long")
    phint("item", pc("Items:", "c"), "long")
    phint("dead", pc("Dead Checks:", "u"), "short")
    phint("shop", pc("Shop Items:", "m"), "shop")
    phint("entrance", pc("Entrances:", "m"), "long")

def main_prompt():
    #global hints
    op = {"s": song_hint,
          "i": item_hint,
          "d": dead_hint,
          "w": woth_hint,
          "f": fool_hint,
          "u": undo_hint,
          "k": kill_hint,
          "h": shop_sanity,
          "t": entrance_sanity,
          "c": cow_sanity,
          "r": scrub_sanity,
          "a": advanced_tricks,
          "n": woth_edit,
          "e": pexit}

    print("\n=====================================================================")
    print("\n" + pc("(W)","y") + "oth | " + pc("(N)","y") + "ew Check | " + pc("(F)","r") + "ool | " + pc("(S)","g") + "ong | " + pc("(I)","c") + "tem | " + pc("(D)","u") + "ead")
    print("\n" + "s" + pc("(H)","m") + "ops | " + pc("(C)","m") + "ows | " + "sc" + pc("(R)","m") + "ubs | " + "en" + pc("(T)","m") + "rances")
    print("\n" + pc("(A)","w") + "dvanced tricks | " + pc("(U)","w") + "ndo | " + pc("(K)","w") + "ill | " + pc("(E)","w") + "xit ", end="")
    #print("\n")
    #print(hints)
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

global cow_checks
cow_checks = cows[:]

global scrub_checks
scrub_checks = scrubs[:]

global trick_list
trick_list = []
with open('tricks.json', 'r') as f:
    tricks = json.load(f)

    for trick in tricks:
        trick_list.append(trick['Name'])

    trick_list.sort()

main_loop()
