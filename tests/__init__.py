'''
    Initializer file to add project level directory to PYTHONPATH
'''


import os
import sys

non_package_dir = ('tests', 'venv')

sys.path.append('..')
for entry in os.listdir():
    if (os.path.isdir(entry) and
            not entry.startswith('.') and
            entry not in non_package_dir):
        sys.path.append(entry)
