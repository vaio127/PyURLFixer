__author__ = 'Owner'
import mailto, pyperclip, time


def main():
    while True:
        if mailto.canaccept(pyperclip.paste()):
            a = pyperclip.paste()
            pyperclip.copy(mailto.fix(pyperclip.paste()))
            print 'Fixed ' + a + ' into ' + pyperclip.paste()
        time.sleep(1)

main()