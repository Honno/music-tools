#!/usr/bin/python3

import os
import eyed3

if __name__ == "__main__":
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for filename in files:
        try:
            audio = eyed3.load(filename)
            try:
                album = audio.tag.album
                if album:
                    if not os.path.exists(album):
                        os.mkdir(album)
                        os.rename(filename, album+'/'+filename)
            except AttributeError:
                pass
        except eyed3.Error:
            print("{} is not a valid audio file".format(filename))
