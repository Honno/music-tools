## Music in question https://www.flashygoodness.com/music/gallery/

import requests
import os
import xml.etree.ElementTree as ET
import urllib
import re

folder_name = r'flashygoodness'

files_root = 'https://www.flashygoodness.com/sys/xml/'
files = ['main.xml', 'misc.xml', 'remix.xml']

if __name__ == '__main__':
    directory = os.path.dirname(os.path.realpath(__file__)) + '\\' + folder_name

    if not os.path.exists(directory):
        os.makedirs(directory)

    for path in files:
        sub_directory = directory + '\\' + re.match(r'(.*)\..+', path).group(1)

        if not os.path.exists(sub_directory):
            os.makedirs(sub_directory)

        os.chdir(sub_directory)

        page = requests.get(files_root + path)
        tree = ET.fromstring(page.content)

        url = tree.find('.//url').text

        tracks_element = tree.find('.//tracks')

        for group_element in tracks_element:

            additional_path = group_element.attrib['dir']
            if not additional_path == '':
                additional_path = additional_path + '/'

            for track_element in group_element:
                title = track_element.attrib['title'] + r'.mp3'

                print("Downloading " + title + " from " + url + additional_path + title)
                file = requests.get(url + additional_path + title)

                with open(title, 'wb') as f:
                    f.write(file.content)

