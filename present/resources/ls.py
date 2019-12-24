import argparse
import sys
import random
import time

def write(text, sleeptime=0):
    sys.stdout.write(text)
    sys.stdout.flush()
    time.sleep(sleeptime)

def stutter(text, sleeptime):
    individual_sleeptime = sleeptime / len(text)
    for char in text[:-1]:
        write(char, individual_sleeptime)
    write(text[-1], 0)

songs = { }
def song_list(songs_dict):
    return ", ".join([key for key in songs_dict.keys()])

def boop():
    stutter("booooooooooop", 1.5)
songs["boop"] = boop

def ILoveBooper():
    write("I", 0.4)
    stutter("...\n", 1.2)
    write("love", 0.4)
    stutter("...\n", 1.2)
    write("my booper", 0.15)
    write(" OH", 0.25)
    stutter("...\n", 1.2)
    write("I", 0.15)
    write(" do", 0.25)
    stutter("...\n", 1.2)
    stutter("BOOOOOOOOOOOOP\n", 1.6)
songs["ILB"] = ILoveBooper

def lala():
    for i in range(0, 400):
        write("la", 0.0025)
        if random.randint(0, 20) == 1:
            write("\n", 0)
        write("\n")
songs["lala"] = lala

def POOB():
    stutter("...\n", 3)
    write("POOB!!!!!\n", 0.05)
songs["POOB"] = POOB

def TheWeirdVegetableShuffle():
    def shuffle_line(a, b):
        stutter(a, .8)
        stutter(b, .8)

    for _ in range(2):
        itw = ["It's", " the", " weird"]
        veg = [" veg", "'tab", "le\n"]
        shuffle_line(itw, veg)
        shuffle_line(itw, veg)
        stutter(["shuf", "fle!"], .8)
        time.sleep(1)
        stutter([" doo" for _ in range(3)], 1)
        time.sleep(.2)
        print()

    shuffle_line(["don't", " got"], [" these", " where", " we"])
    print()
    shuffle_line(["come", " from"], veg)
    time.sleep(.2)
    stutter(["shuf", "fle"], 1)
    print()

    time.sleep(1.6)
    stutter(["VEG", "E", "TAB", "LE"], 2)
    time.sleep(.5)
    print()
    stutter(["shuf", "fle!!!"], .8)
    time.sleep(1.6)


songs["TWVS"] = TheWeirdVegetableShuffle

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            prog="ls",
            description='l.s. -> love song.')
    parser.add_argument('song', metavar='s',
        help='Which song to play. Available songs: {}'.format(song_list(songs)))
    args = parser.parse_args()
    try:
        song = songs[args.song]
        song()
    except KeyError:
        print("Song {} not available...".format(args.song))

