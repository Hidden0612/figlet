import os
from pyfiglet import Figlet
#------------------------#
os.system("cls")
os.system("clear")
s = input("Enter Text : ")
#------------------------#
def font (text):
    col_text=Figlet(font='doh') # fons = http://www.figlet.org/examples.html
    return str(col_text.renderText(text))
#------------------------#
if __name__ == '__main__':
    print(font(s))