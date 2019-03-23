#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, pickle, platform, string, sys
from colorama import init, Fore, Style

# songs
songs = [
    'Bolero',
    'Eponas',
    'Minuet',
    'Nocturne',
    'Prelude',
    'Requiem',
    'Sarias',
    'Serenade',
    'Storms',
    'Song of Time',
    'Suns Song',
    'Zeldas Lullaby']

# SONG checks
song_checks = [
    'Bolero Check',
    'Burning Kak',
    'Minuet Check',
    'OoT Check',
    'Prelude Check',
    'Requiem Check',
    'Serenade Check',
    'Suns Song Check']

# core items
items = [
    'Bomb Bag',
    'Boomerang',
    'Boss Key',
    'Bow',
    'Claim Check',
    'Dins Fire',
    'Divers',
    'Farores Wind',
    'Fire Arrows',
    'Hammer',
    'Hover Boots',
    'Iron Boots',
    'Lens of Truth',
    'Light Arrows',
    'Magic',
    'Mirror Shield',
    'Hookshot',
    'Slingshot',
    'STR Upgrade',
    'Wallet']

# list of checklists, full
check_list_full = [
    'Always',
    'Bean',
    'Boss',
    'Dungeon Names',
    'Dungeon Special',
    'Minigame',
    'Overworld',
    'Places']

# list of checklists, small
check_list_small = [
    'Dungeon Names',
    'Places']

# ALWAYS checks
always_checks = [
    '10 Big Poes',
    '30 Gold Skulltulas',
    '40 Gold Skulltulas',
    '50 Gold Skulltulas',
    'Biggoron',
    'DT Skull Mask',
    'Frogs 2']

# MINIGAME checks
minigame_checks = [
    'Adult Fishing',
    'Adult Shooting Gallery',
    'Bombchu Bowling Bomb Bag',
    'Bombchu Bowling Piece of Heart',
    'Child Fishing',
    'Child Shooting Gallery',
    'Horseback Archery 1500 Points',
    'Treasure Chest Game']

# OVERWORLD checks
overworld_checks = [
    '20 Gold Skulltulas',
    'Composer Grave Chest',
    'Darunias Joy',
    'Gerudo Valley Hammer Rocks Chest',
    'Goron City Left Maze Chest',
    'Goron City Pot',
    'Shoot the Sun',
    'Skull Kid',
    'Suns Song Check Chest',
    'Unfreeze King Zora',
    'Wasteland Chest',
    'Zoras Fountain Ice Lake']

# DUNGEON checks
dungeon_checks = [
    'BotW Dead Hand',
    'Colossus Left Side (Adult)',
    'Colossus Right Side (Kid)',
    'FireT Megaton Hammer Chest',
    'FireT Scarecrow Chest',
    'ForestT Floormaster Chest',
    'GTG Final Chest',
    'GTG Toilet Chest',
    'ShadowT Floormaster Chest',
    'WaterT Boss Key Chest',
    'WaterT River Chest']

# DUNGEONNAME checks
dungeon_name_checks = [
    'Bottom of the Well',
    'Deku Tree',
    'Dodongos Cavern',
    'Fire Temple',
    'Forest Temple',
    'Ganons Castle',
    'GTG',
    'Ice Cavern',
    'Jabu Jabu',
    'Shadow Temple',
    'Spirit Temple',
    'Water Temple']

# BOSS checks
boss_checks = [
    'Barinade',
    'Bongo Bongo',
    'Gohma',
    'King Dodongo',
    'Morpha',
    'Phantom Ganon',
    'Twinrova',
    'Volvagia']

# BEAN checks
bean_checks = [
    'Bean at Crater',
    'Bean at Desert',
    'Bean at Graveyard']

# PLACE checks
place_checks = [
    'Desert Colossus',
    'DM Crater',
    'DM Trail',
    'Gerudo Fortress',
    'Gerudo Valley',
    'Goron City',
    'Graveyard',
    'Haunted Wasteland',
    'Hyrule Castle',
    'Hyrule Field',
    'Kakariko',
    'Kokiri Forest',
    'Lake Hylia',
    'Lon Lon Ranch',
    'Lost Woods',
    'Market',
    'Sacred Forest Meadow',
    'Zora Domain',
    'Zora Fountain',
    'Zora River']

class _Getch:
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()

class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

def pc(text, color):
    op = {'b': Fore.BLACK,
          'r': Fore.RED,
          'g': Fore.GREEN,
          'y': Fore.YELLOW,
          'u': Fore.BLUE,
          'm': Fore.MAGENTA,
          'c': Fore.CYAN,
          'w': Fore.WHITE}
    return op.get(color) + text + Style.RESET_ALL

def pexit():
    sys.exit()

def itoa(i):
    return chr(i + 97)

def atoi(c):
    return ord(c) - 97

def askq(list, question):
    os.system('cls')

    for i, c in enumerate(list):
        print("{}. {}".format(itoa(i), c))

    print('\n' + question + ' ', end='')
    return atoi(getch().decode('ascii'))

def get_check(type):
    if type == 'small':
        cln = check_list_small
        cl = [dungeon_name_checks,
              place_checks]
    else:
        cln = check_list_full
        cl = [always_checks,
              bean_checks,
              boss_checks,
              dungeon_name_checks,
              dungeon_checks,
              minigame_checks,
              overworld_checks,
              place_checks]

    t = askq(cln, 'Category?')
    c = askq(cl[int(t)], 'Check?')

    return cl[int(t)][int(c)]

def ghint(ct, clt):
    global hints

    if ct == 'item':
        s = askq(items, 'Item?')
    c = get_check(clt)

    if ct == 'item':
        hints.append(['item', items[s], c])
    else:
        hints.append([ct, c])

    main_loop()

def song_hint():
    global hints

    s = askq(songs, 'Song?')
    c = askq(song_checks, 'Check?')

    hints.append(['song', songs[s], song_checks[c]])
    main_loop()

def item_hint():
    ghint('item', 'full')

def dead_hint():
    ghint('dead', 'full')

def woth_hint():
    ghint('woth', 'small')

def fool_hint():
    ghint('fool', 'small')

def phint(type, text, check):
    global hints

    r = [e for e in hints if e[0] == type]

    if len(r) > 0:
        print('\n' + text)

    for h in r:
        if check == True:
            print('\t' + h[1] + pc(' is at ','m') + h[2])
        else:
            print('\t' + h[1])

def undo_hint():
    global hints

    del hints[-1]
    main_loop()

def kill_hint():
    global hints

    hints.clear()
    main_loop()

def loadf():
    global fname, hints
    if os.path.isfile(fname) and os.stat(fname).st_size != 0:
        f = open(fname, 'rb')
        hints = pickle.load(f)
        f.close()

def writef():
    global fname, hints
    f = open(fname, 'wb')
    pickle.dump(hints, f)

def main_hints():
    phint('woth', pc('Way of the Hero:', 'y'), False)
    phint('fool', pc('Barren Locations:', 'r'), False)
    phint('song', pc('Songs:', 'g'), True)
    phint('item', pc('Items:', 'c'), True)
    phint('dead', pc('Dead Checks:', 'u'), False)

def main_prompt():
    op = {'s': song_hint,
          'i': item_hint,
          'd': dead_hint,
          'w': woth_hint,
          'f': fool_hint,
          'u': undo_hint,
          'k': kill_hint,
          'e': pexit}

    print('\n=====================================================================')
    print('\n' + pc('(W)','y') + 'oth | ' + pc('(F)','r') + 'ool | ' + pc('(S)','g') + 'ong | ' + pc('(I)','c') + 'tem | ' + pc('(D)','u') + 'ead | ' + pc('(U)','m') + 'ndo | ' + pc('(K)','m') + 'ill | ' + pc('(E)','w') + 'xit ', end='')
    c = getch().decode('ascii')
    try:
        op[c.lower()]()
    except SystemExit:
        print()
        writef()
        pass
    except:
        main_loop()

def main_loop():
    os.system('cls')
    main_hints()
    main_prompt()

hints = []
if platform.system() == 'Windows':
    fname = '.\\.hinthelper.p'

else:
    fname = './.hinthelper.p'

getch = _Getch()
init()
loadf()

main_loop()
