#!/usr/bin/python3

import os
import eyed3

if __name__ == "__main__":
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for filename in files:
        try:
            album = eyed3.load(filename).tag.album
            if not os.path.exists(album):
                os.mkdir(album)
            os.rename(filename, album+'/'+filename)
        except AttributeError:
            print("Skipping {}".format(filename))
        except eyed3.Error as e:
            print(e)
