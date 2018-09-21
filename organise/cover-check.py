#!/usr/bin/python3

import os

if __name__ == "__main__":
    for root, folders, files in os.walk('.'):
        if not root.startswith('./.') and not folders:
             if not any(filename.startswith('cover') for filename in files):
                 print(root)
