from Levenshtein import *
import os
import time
import sys
import random


str1 ="ouiahedgoasefg"
str2 = "test"

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def match(s1, s2):
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return i

def replace_str_index(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])

def editString(str1, str2, delay=0, speed=.1):
    e = editops(str1, str2)
    time.sleep(delay)
    oldString = str1
    for i in range(len(e)):
        newString = apply_edit(e[:i], str1, str2)
        location = match(newString, oldString)

        if location != None:
            printString = replace_str_index(newString, location, bytes((219,)).decode('cp437'))
            print("\r" + '\x1b[2K' + printString, end="\r")
        oldString = newString
        time.sleep(speed)
    print(str2, end="\r")

def slow_type(t, typing_speed=50):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print('', end="\r")

def clearLine():
    print("\r" + '\x1b[2K', end="\r")

def main():
    defaultSleep = 1.1
    cls()
    str1 = "Hello there this is a very long string that could take some time to process"
    str2 = "this is another really long string and it might take some time to process"
    str3 = "This is a line that could use some editing"
    str4 = "This is a line that NEEDS editing"
    slow_type("this is the first line written slowly\n", 25)
    time.sleep(2)
    slow_type("this is the second line written quickly\n", 100)
    time.sleep(defaultSleep)
    slow_type(str3, 100)
    editString(str3, str4, 1, .1)
    print("")
    slow_type("\nthere may be more lines")
    time.sleep(defaultSleep)
    editString("there may be more lines", "there will be more lines", 1, .1)
    time.sleep(defaultSleep)
    slow_type("\nthere is more to say")
    time.sleep(1.5)
    editString("there is more to say", "there is more to read", 1, .1)
    time.sleep(defaultSleep)
    slow_type("\nthis is the sixth line")
    time.sleep(defaultSleep * .6)
    slow_type("\nthis is the eighth line")
    time.sleep(defaultSleep * 1.2)
    editString("this is the eighth line", "this is NOT the eighth line", 1, .1)
    time.sleep(defaultSleep)
    slow_type("\nthe seventh line is the eighth line")
    time.sleep(defaultSleep * 2)
    editString("the seventh line is the eighth line", "the seventh line is the eighth line?", 1, .1)
    time.sleep(defaultSleep)
    slow_type("\nthe eighth line is a paradox")
    time.sleep(defaultSleep)
    slow_type("\nthis is the tenth line written innocuously", 20)
    time.sleep(defaultSleep)
    slow_type("\nthis is the eleventh line written vigorously", 100)
    time.sleep(defaultSleep * .5)
    slow_type("\nthere are twelve lines")
    time.sleep(defaultSleep)
    editString("there are twelve lines", "there are now a dozen lines", 1, .1)
    time.sleep(defaultSleep)
    slow_type("\nthe twelfth line is wrong")
    time.sleep(defaultSleep)
    editString("there are twelve lines", "the twelfth line is unlucky", 1, .1)
    time.sleep(defaultSleep)
    slow_type("\nthefourteenthlineisimpatien", 200)
    time.sleep(defaultSleep * .4)
    editString("thefourteenthlineisimpatien", "the fourteenth line is impatient", 1, .05)
    time.sleep(defaultSleep)
    print("")
    time.sleep(defaultSleep)
    slow_type("\nthe sixteenth line is hiding")
    time.sleep(defaultSleep * .5)
    slow_type("\nthe eighteenth line thinks the seventeenth is lying", 100)
    time.sleep(defaultSleep)
    slow_type("\nthe nineteenth line is worried just about the sixteenth line")
    time.sleep(defaultSleep)
    slow_type("\nthe twentieth line is tired of the norms")
    time.sleep(defaultSleep)
    slow_type("\nthe twentyfirst line sets a precedent")
    time.sleep(defaultSleep)
    editString("the twentyfirst line sets a precedent", "the 21st line sets a precedent", 1, .1)
    time.sleep(defaultSleep)
    print("\n")
    time.sleep(3.5)
    slow_type("\n...", 5)
    time.sleep(3.5)
    print("\n")
    time.sleep(3.5)
    print("\n")
    time.sleep(3.5)
    slow_type("\nthis is the final line")
    dummy = input()


main()