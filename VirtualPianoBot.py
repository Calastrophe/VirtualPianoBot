import pyautogui
import time


if __name__ == "__main__":
    savedString=''
    currentlyInBracket = False
    fn = input("Please input the file name of the music sheet(include .txt):")
    print('System is arming... Five seconds to prepare...')
    time.sleep(5)
    with open(fn, 'r') as text:
        for line in text:
            for letter in line.rstrip():
                if letter.isspace() == False and currentlyInBracket==False and letter != '[' and letter != ']':
                    print('I\'ve tried to hit the', letter, 'key')
                    pyautogui.press(letter)
                    time.sleep(.3) # Edit this for the pacing of the song
                elif letter.isspace() == False and currentlyInBracket==True and letter != '[' and letter != ']':
                    print('I need to save this...')
                    savedString+=letter
                elif letter == '[':
                    currentlyInBracket = True
                elif letter == ']':
                    pyautogui.write(savedString) # Execute letters that are together
                    savedString=''
                    currentlyInBracket = False
                    time.sleep(.3) # Edit this for the pacing of the song
