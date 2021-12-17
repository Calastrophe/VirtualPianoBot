import pyautogui
import time


if __name__ == "__main__":
    savedString=''
    currentlyInBracket = False
    fn = input("Please input the file name of the music sheet(include .txt):")
    print('System is arming... Five seconds to prepare...')
    time.sleep(5)
    print('Now playing...')
    with open(fn, 'r') as text:
        for line in text:
            for letter in line.rstrip():
                if letter.isspace() == False and currentlyInBracket==False and letter != '[' and letter != ']' and letter != "|":
                    pyautogui.press(letter)
                    time.sleep(.15) # Edit this for the pacing of the song
                elif letter.isspace() == False and currentlyInBracket==True and letter != '[' and letter != ']' and letter != "|":
                    savedString+=letter
                elif letter.isspace() == True and currentlyInBracket==False and letter != '[' and letter != ']' and letter != "|":
                    time.sleep(.25) # Edit this for the pacing of the song, this is for if there is a space between notes...
                elif letter == "|":
                    time.sleep(.35) # Edit this for the pacing of the song, this is for the long pauses between notes...
                elif letter == '[':
                    currentlyInBracket = True
                elif letter == ']':
                    pyautogui.write(savedString)
                    savedString=''
                    currentlyInBracket = False
                    time.sleep(.15) # Edit this for the pacing of the song
    print('Finished playing...')
