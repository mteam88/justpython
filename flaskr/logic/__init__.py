import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from stockwidget import stockwidgets

def isuser(userloginform):
    print(f"Login: {userloginform}")
    return False