from microbit import *
import music
import radio

silent = True
dotTune = ["A4:1","R:1"]
dashTune = ["A4:4","R:1"]

codes = [".-",      #A
         "-...",    #B
         "-.-.",    #C
         "-..",     #D
         ".",       #E
         "..-.",    #F
         "--.",     #G
         "....",    #H
         "..",      #I
         ".---",    #J
         "-.-",     #K
         ".-..",    #L
         "--",      #M
         "-.",      #N
         "---",     #O
         ".--.",    #P
         "--.-",    #Q
         ".-.",     #R
         "...",     #S
         "-",       #T
         "..-",     #U
         "...-",    #V
         ".--",     #W
         "-..-",    #X
         "-.--",    #Y
         "--..",    #Z
         ".----",   #1
         "..---",   #2
         "...--",   #3
         "....-",   #4
         ".....",   #5
         "-....",   #6
         "--...",   #7
         "---..",   #8
         "----.",   #9
         "-----",   #0
         ".-.-.-",  #.
         "--..--",  #,
         "..--.."]  #?
decodes = [ "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "0",
            ".",
            ",",
            "?"]
            
dot  = Image("00000:"
             "00500:"
             "05950:"
             "00500:"
             "00000")
             
dash = Image("00000:"
             "00000:"
             "59995:"
             "00000:"
             "00000:")

wasBeep = False
loopCount = 0
loopLimit = 80
letterish = ""

listening = True

radio.on()

while True:
    if button_a.is_pressed():
        if not wasBeep:
            wasBeep = True
            listening = False
            sleep(200)
            if button_a.is_pressed():
                if not silent:
                    music.play(dashTune)
                letterish += "-"
                display.show(dash)
                
            else:
                if not silent:
                    music.play(dotTune)
                letterish += "."
                display.show(dot)
                wasBeep = False
                loopCount=0
                
    else:
        if wasBeep:
            loopCount=0
            wasBeep = False
        else:
            if loopCount < loopLimit:
                loopCount+=1
            elif loopCount == loopLimit:
                for idx, val in enumerate(codes):
                    if val == letterish:
                        radio.send(str(idx))
                        display.show(decodes[idx])
                        break
                letterish=""
                listening = True
        if listening:
            incoming = radio.receive()
            if incoming is not None:
                ind = int(incoming)
                display.show(decodes[ind])
                for x in codes[ind]:
                    if x == "-":
                        music.play(dashTune)
                    else:
                        music.play(dotTune)
    sleep(1)
