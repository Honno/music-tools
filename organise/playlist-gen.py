#!/usr/bin/python3

import os

FILE_TYPES = ['mp3', 'flac', 'ogg']
EXTENSION = '.m3u'
TOP_PLAYLIST_NAME = 'All'

def is_audio(name):
    return any(name.endswith(file_type) for file_type in FILE_TYPES)

def current_folder(path):
    dirs = path.split('/')
    if len(dirs) > 0:
        return dirs[-1]
    else:
        return TOP_PLAYLIST_NAME

if __name__ == "__main__":

    for root, folders, files in os.walk('.', topdown=False):
        folder = current_folder(root)
        playlist_name = folder + EXTENSION
        print("In {}".format(root))

        if not root.startswith('./.') and playlist_name not in files:
            with open(root+'/'+playlist_name, 'w+') as playlist:
                print("No playlist file found, creating one")
                audio_files = filter(is_audio, files)
                for filename in audio_files:
                    playlist.write(filename+'\n')

                for folder in folders:
                    try:
                        sub_playlist = open(root+'/'+folder+'/'+folder+EXTENSION, 'r')
                        print("Sub playlist file found in {}, adding to current playlist".format(folder))
                        for song in sub_playlist:
                            playlist.write(folder+'/'+song)
                        sub_playlist.close()
                    except IOError as e:
                        print(e)
