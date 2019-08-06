#Here will be all chapter transitions that occur ingame.
init python:
    config.layers = ['trans1', 'trans2', 'trans3', 'trans4', 'trans5', 'master', 'transient', 'screens', 'overlay', ]

#################################################################################
#Declare all items that will be used within transitions
#general images like borders
image transition_frame = "images/chapter transitions/transition_frame.png"
image textborder = "images/chapter transitions/transition_text_border.png"
image textborder2 = "images/chapter transitions/transition_text_border.png"
image black = "#000"
image white = "#FFF"

#define special transition operation only used here
define ch1_specialOP1 = Dissolve (2.2)
define ch1_specialOP2 = Dissolve (0.2)
define longBlack = Dissolve (2.0)

define cr1_longBlack = Dissolve (3.0)
transform alphaINV:
    xalign .5 yalign 1.0 alpha 0.0
transform alphaON:
    linear 1.0 alpha 1.0
transform alphaOFF:
    linear 1.0 alpha 0.0
    
#Chapter jingles to be used
define audio.ch0_jingle = "audio/bgm/02 - Chapter Interlude.mp3"
define audio.ch1_jingle = "audio/bgm/02 - Chapter Interlude.mp3"
define audio.credit1 = "audio/bgm/14 - Credits.mp3"
define audio.credit2 = "audio/bgm/14 - Credits.mp3"

#proloque-only items
image ch0train = "images/chapter transitions/ch0_train.png"
image ch0traintrack = "images/chapter transitions/ch0_traintrack.png"
image ch0text = "images/chapter transitions/ch0_text.png"
image ch0title = "images/chapter transitions/ch0_title.png"
image ch0titleG = "images/chapter transitions/ch0_titleG.png"

#ch1-only items
image ch1_umriss0 = "images/chapter transitions/ch1_umriss0.png"
image ch1_umriss1 ="images/chapter transitions/ch1_umriss1.png"
image ch1_umriss2 = "images/chapter transitions/ch1_umriss2.png"
image ch1_transition0 = "images/chapter transitions/ch1_transition0.png"
image ch1_transition1 = "images/chapter transitions/ch1_transition1.png"
image ch1_chara0 = "images/chapter transitions/ch1_chara0.png"
image ch1_chara1 = "images/chapter transitions/ch1_chara1.png"
image ch1_chara2 = "images/chapter transitions/ch1_chara2.png"
image ch1title = "images/chapter transitions/ch1_title.png"

#credit1-only items
image credit1_frame = "images/chapter transitions/credit1_frame1.png"
image credit1 0 = "images/chapter transitions/credit1_0.png"
image credit1 1 = "images/chapter transitions/credit1_1.png"
image credit1 2 = "images/chapter transitions/credit1_2.png"
image credit1 3 = "images/chapter transitions/credit1_3.png"
image credit1 4 = "images/chapter transitions/credit1_4.png"
image credit1 5 = "images/chapter transitions/credit1_5.png"
image credit1 6 = "images/chapter transitions/credit1_6.png"
image credit1 8 = "images/chapter transitions/credit1_8.png"
image credit1 9 = "images/chapter transitions/credit1_9.png"
image credit2_frame = "images/chapter transitions/credit2_frame.png"

#################################################################################


label ch0_transition:
    
    $ _game_menu_screen = None
    #delete the entire scene with white, hiding that white and then begin transition
    scene white 
    hide white
    
    #We create our scene with white background, frame on top and two semi-transparent borders on the sides
    show white at truecenter onlayer trans1 with fade
    show transition_frame at truecenter onlayer trans5
    show textborder onlayer trans3:
        xpos 0.05 alpha 0.5
    show textborder2 onlayer trans3:
        xpos 0.85 alpha 0.5
    $ renpy.pause(1.0, hard=True)
    play music ch0_jingle noloop
    $ renpy.pause(1.0, hard=True)
    #Here comes the magic
    show ch0traintrack onlayer trans4:
        xpos -0.85 ypos 0.35
        linear 2.0 xpos 0.06
    
    show ch0title onlayer trans4:
        pause 5.0
        ypos 0.25 xalign 0.5
        
    show ch0train onlayer trans4:
        xpos -2.7 ypos 0.196
        pause 2.0
        linear 6.0 xpos 1.0
    
#   show ch0text onlayer trans2:
#       xpos 1.0 ypos 0.75
#       pause 2.0
#       linear 8.5 xpos -2.0        
    
    $ renpy.pause(1.0, hard=True)
    $ playmusic('audio/sfx/train_passby.mp3', "sfx2", 0.3)
    $ renpy.pause(1.0, hard=True)
    $ playmusic('audio/sfx/train_whistle.mp3', "sfx1", 0.7)
    $ renpy.pause(5.0, hard=True)
    stop sfx2 fadeout 2.0
    $ renpy.pause(6.0, hard=True)
    stop music fadeout 2.0
    $ renpy.pause(2.0, hard=True)
    show black with dissolve
    $ renpy.pause(1.0, hard=True)
    
    stop music
    hide white onlayer trans1
#   hide ch0text onlayer trans2
    hide textborder onlayer trans3
    hide textborder2 onlayer trans3
    hide ch0traintrack onlayer trans4
    hide ch0title onlayer trans4
    hide ch0train onlayer trans4
    hide transition_frame onlayer trans5
    $_game_menu_screen = "save_screen"
    jump ch1
    
########################################

label ch0_transitionDE:
    
    $ _game_menu_screen = None
    #delete the entire scene with white, hiding that white and then begin transition
    scene white 
    hide white
    
    #We create our scene with white background, frame on top and two semi-transparent borders on the sides
    show white at truecenter onlayer trans1 with fade
    show transition_frame at truecenter onlayer trans5
    show textborder onlayer trans3:
        xpos 0.05 alpha 0.5
    show textborder2 onlayer trans3:
        xpos 0.85 alpha 0.5
    $ renpy.pause(1.0, hard=True)
    play music ch0_jingle noloop
    $ renpy.pause(1.0, hard=True)
    #Here comes the magic
    show ch0traintrack onlayer trans4:
        xpos -0.85 ypos 0.35
        linear 2.0 xpos 0.06
    
    show ch0titleG onlayer trans4:
        pause 5.0
        ypos 0.25 xalign 0.5
        
    show ch0train onlayer trans4:
        xpos -2.7 ypos 0.196
        pause 2.0
        linear 6.0 xpos 1.0
    
#   show ch0text onlayer trans2:
#       xpos 1.0 ypos 0.75
#       pause 2.0
#       linear 8.5 xpos -2.0        
    
    $ renpy.pause(1.0, hard=True)
    $ playmusic('audio/sfx/train_passby.mp3', "sfx2", 0.3)
    $ renpy.pause(1.0, hard=True)
    $ playmusic('audio/sfx/train_whistle.mp3', "sfx1", 0.7)
    $ renpy.pause(5.0, hard=True)
    stop sfx2 fadeout 2.0
    $ renpy.pause(6.0, hard=True)
    stop music fadeout 2.0
    $ renpy.pause(2.0, hard=True)
    show black with dissolve
    $ renpy.pause(1.0, hard=True)
    
    stop music
    hide white onlayer trans1
#   hide ch0text onlayer trans2
    hide textborder onlayer trans3
    hide textborder2 onlayer trans3
    hide ch0traintrack onlayer trans4
    hide ch0title onlayer trans4
    hide ch0train onlayer trans4
    hide ch0titleG onlayer trans4
    hide transition_frame onlayer trans5
    $_game_menu_screen = "save_screen"
    
    centered "Die Demonstration der deutschen Übersetzung endet hier." with fade
    
    menu:
        "Zurück ins Hauptmenü":
             return
             
        "Mit der englischen Fassung weiterspielen":
            centered "Die Sprache wird nun auf \"Englisch\" gewechselt."
            $ renpy.change_language(None)
            jump ch1
    
########################################

label ch1_transition:

    play music ch1_jingle noloop
    $ _game_menu_screen = None
    hide ch0text onlayer trans2
    hide textborder onlayer trans3
    hide textborder2 onlayer trans3
    hide ch0traintrack onlayer trans4
    hide ch0title onlayer trans4
    hide ch0train onlayer trans4
    hide black onlayer trans5
    hide transition_frame onlayer trans5
    scene white
    hide white
    #We create our scene with white background, frame on top and two semi-transparent borders on the sides
    scene white at truecenter onlayer trans1
    show transition_frame at truecenter onlayer trans5 
    with ch1_specialOP1
    $ renpy.pause(1.0, hard=True)
    show ch1_umriss0 onlayer trans2:
        xalign 1.0
    show ch1_transition0 onlayer trans2:
        xalign 1.0 yalign .5
        linear 2.0 ypos -1.5
    $ renpy.pause(2.0, hard=True)
    show ch1_umriss0 onlayer trans4:
        xalign 1.0
    hide ch1_umriss0 onlayer trans2
    hide ch1_transition0 onlayer trans2
    
    show ch1_umriss2 onlayer trans2:
        xalign 1.0
    show ch1_transition1 onlayer trans2:
        xalign 1.0 yalign .5
        linear 2.0 ypos 1.5
    $ renpy.pause(2.0, hard=True)
    show ch1_umriss2 onlayer trans4:
        xalign 1.0
    hide ch1_umriss2 onlayer trans2
    hide ch1_transition1 onlayer trans2
    
    show ch1_umriss1 onlayer trans2:
        xalign 1.0
    show ch1_transition0 onlayer trans2:
        xalign 1.0 yalign .5
        linear 2.0 ypos -1.5
    $ renpy.pause(2.0, hard=True)
    show ch1_umriss1 onlayer trans3:
        xalign 1.0
    hide ch1_umriss1 onlayer trans2
    hide ch1_transition0 onlayer trans2
    
    show ch1_chara0 onlayer trans4 with ch1_specialOP2
    $ renpy.pause(0.5, hard=True)
    show ch1_chara1 onlayer trans4 with ch1_specialOP2
    $ renpy.pause(0.5, hard=True)
    show ch1_chara2 onlayer trans4 with ch1_specialOP2
    $ renpy.pause(0.5, hard=True)
    show ch1title onlayer trans4 with ch1_specialOP1
    stop music fadeout 3.0
    $ renpy.pause(1.0, hard=True)
    
    scene black with longBlack
    $ renpy.pause(2.0, hard=True)
    $_game_menu_screen = "save_screen"
    jump ch2
    
########################################

label end1_transition:
    
    play music credit1 noloop
    $ _game_menu_screen = None
    scene black onlayer trans2 
    $ renpy.pause(5.0, hard=True)                               #8secs
    if persistent.trueend_unlocked == False:
        show credit1_frame onlayer trans3 with cr1_longBlack
    else:
        show credit2_frame onlayer trans3 with cr1_longBlack
    $ renpy.pause(6.0, hard=True)                               #14secs
    
    show credit1 0 at alphaINV
    show credit1 0 at alphaON
    $ renpy.pause(9.0, hard=True)                               #23secs
    show credit1 0 at alphaOFF
    $ renpy.pause(2.0, hard=True)                               #25secs
    
    show credit1 1 at alphaINV
    show credit1 1 at alphaON
    $ renpy.pause(8.0, hard=True)                               #33secs
    show credit1 1 at alphaOFF
    $ renpy.pause(4.0, hard=True)                               #35secs
    
    show credit1 2 at alphaINV
    show credit1 2 at alphaON
    $ renpy.pause(3.0, hard=True)                               #38secs
    show credit1 2 at alphaOFF
    $ renpy.pause(2.0, hard=True)                               #40secs
    
    show credit1 3 at alphaINV
    show credit1 3 at alphaON
    $ renpy.pause(3.0, hard=True)                               #43secs
    show credit1 3 at alphaOFF
    $ renpy.pause(2.0, hard=True)                               #45secs
    
    show credit1 4 at alphaINV
    show credit1 4 at alphaON
    $ renpy.pause(6.0, hard=True)                               #53secs
    show credit1 4 at alphaOFF
    $ renpy.pause(2.0, hard=True)                               #55secs
    
    show credit1 5 at alphaINV
    show credit1 5 at alphaON
    $ renpy.pause(3.0, hard=True)                               #58secs
    show credit1 5 at alphaOFF
    $ renpy.pause(2.0, hard=True)                               #60secs
    
    hide credit1 5
    
    show credit1 6 onlayer trans2:
        ypos 600 xalign .5
        linear 21 ypos -1000
    
    $ renpy.pause(23.0, hard=True)                               #42.9secs
    
    hide credit1 6 onlayer trans2
    show credit1 8 at alphaINV
    show credit1 8 at alphaON
    $ renpy.pause(5.0, hard=True)                               #59.9secs
    
    if persistent.trueend_unlocked == False:
        show credit1_frame onlayer trans3:
            linear 2.0 alpha 0.0
    else:
        show credit2_frame onlayer trans3:
            linear 2.0 alpha 0.0
        
    show credit1 8:
        linear 3.0 yalign 0.5
    $ renpy.pause(4.0, hard=True)                               #63.9secs
    show credit1 8 at alphaOFF
    $ renpy.pause(3.0, hard=True)                               #66.9secs
    
    show credit1 9:
        xalign .5 yalign 0.5 alpha 0.0
    show credit1 9 at alphaON
    $ renpy.pause(5.0, hard=True)                               #71.9secs
    show credit1 9 at alphaOFF
    $ renpy.pause(2.0, hard=True)                               #76secs
    $_game_menu_screen = "save_screen"
    jump epilog
   

   
   
########################################

label end2_transition:
    
    play music credit1 noloop
    $ _game_menu_screen = None
    scene black onlayer trans2 
    $ renpy.pause(5.0, hard=True)                               #8secs
    show credit2_frame onlayer trans3 with cr1_longBlack
    $ renpy.pause(6.0, hard=True)                               #14secs
    
    show credit1 0 at alphaINV
    show credit1 0 at alphaON
    $ renpy.pause(9.0, hard=True)                               #23secs
    show credit1 0 at alphaOFF
    $ renpy.pause(2.0, hard=True)                               #25secs
    
    show credit1 1 at alphaINV
    show credit1 1 at alphaON
    $ renpy.pause(8.0, hard=True)                               #33secs
    show credit1 1 at alphaOFF
    $ renpy.pause(4.0, hard=True)                               #35secs
    
    show credit1 2 at alphaINV
    show credit1 2 at alphaON
    $ renpy.pause(3.0, hard=True)                               #38secs
    show credit1 2 at alphaOFF
    $ renpy.pause(2.0, hard=True)                               #40secs
    
    show credit1 3 at alphaINV
    show credit1 3 at alphaON
    $ renpy.pause(3.0, hard=True)                               #43secs
    show credit1 3 at alphaOFF
    $ renpy.pause(2.0, hard=True)                               #45secs
    
    show credit1 4 at alphaINV
    show credit1 4 at alphaON
    $ renpy.pause(6.0, hard=True)                               #53secs
    show credit1 4 at alphaOFF
    $ renpy.pause(2.0, hard=True)                               #55secs
    
    show credit1 5 at alphaINV
    show credit1 5 at alphaON
    $ renpy.pause(3.0, hard=True)                               #58secs
    show credit1 5 at alphaOFF
    $ renpy.pause(2.0, hard=True)                               #60secs
    
    hide credit1 5
    
    show credit1 6 onlayer trans2:
        ypos 600 xalign .5
        linear 21 ypos -1000
    
    $ renpy.pause(23.0, hard=True)                               #42.9secs
    
    hide credit1 6 onlayer trans2
    show credit1 8 at alphaINV
    show credit1 8 at alphaON
    $ renpy.pause(5.0, hard=True)                               #59.9secs
    
    show credit2_frame onlayer trans3:
        linear 2.0 alpha 0.0
    show credit1 8:
        linear 3.0 yalign 0.5
    $ renpy.pause(4.0, hard=True)                               #63.9secs
    show credit1 8 at alphaOFF
    $ renpy.pause(3.0, hard=True)                               #66.9secs
    
    show credit1 9:
        xalign .5 yalign 0.5 alpha 0.0
    show credit1 9 at alphaON
    $ renpy.pause(5.0, hard=True)                               #71.9secs
    show credit1 9 at alphaOFF
    $ renpy.pause(2.0, hard=True)                               #76secs
    $_game_menu_screen = "save_screen"
    jump epilog