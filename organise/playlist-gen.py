#!/usr/bin/python3

import os

FILE_TYPES = ['mp3', 'flac', 'ogg']
PLAYLIST_FILE = 'bestof.m3u'

def is_audio(name):
    return any(name.endswith(file_type) for file_type in FILE_TYPES)

if __name__ == "__main__":
    for root, folders, files in os.walk('.', topdown=False):
        if not root.startswith('./.') and PLAYLIST_FILE not in files:
            print("\nIn {}".format(root))
            with open(root+'/'+PLAYLIST_FILE, 'w+') as playlist:
                print("No playlist file found, creating one")
                audio_files = filter(is_audio, files)
                for filename in audio_files:
                    playlist.write(filename+'\n')

                for folder in folders:
                    try:
                        sub_playlist = open(root+'/'+folder+'/'+PLAYLIST_FILE, 'r')
                        print("Sub playlist file found in {}, adding to current playlist".format(folder))
                        for song in sub_playlist:
                            playlist.write(folder+'/'+song)
                        sub_playlist.close()
                    except IOError:
                        pass
