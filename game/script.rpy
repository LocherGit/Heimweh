    #Verworfene Code-zipfel
    #$_preferences.set_volume('sfx', 0.2)       Force setzen von Musikstärke
    #$ renpy.pause()    Spieler klickt zum weitermachen
    #$ randomnum = renpy.random.randint(1,4)           Random zwischen 1-4
    #if randomnum == 1:                                 Was dann passieren soll
    #$ riddle = renpy.input("WHAT'S MIXED?")            Input Anfrage nach "String"
    #if riddle.strip().lower() == "nuts":               Ist das Eingetippte etwa "String"?
    #show expression Text(_("This is text."), size=50, yalign=0.5, xalign=0.5, drop_shadow=(2, 2)) as text       Zeige Text aufm Bildschirm
init python:
    
    def playmusic(music, channel, volume):
        renpy.music.set_volume(volume, delay=0, channel=channel)
        renpy.music.play(music, channel=channel, loop=False, fadeout=None, synchro_start=False, fadein=6, tight=None, if_changed=True)

init:
    $ import time
    $ year, month, day, hour, minute, second, dow, doy, dst = time.localtime()
    $ renpy.music.register_channel("sfx1", mixer="sfx", loop=False)
    $ renpy.music.register_channel("sfx2", "sound", True)
    $ renpy.music.register_channel("sfx3", "sound", True)
    
    $ flash = Fade(.25, 0, .75, color="#fff")

                                                                                        #Deklarationen und Initialisierungen *******************************
#Declare background
image bg train:
    "images/used bg/ch0_train.jpg"
    zoom 1.2
    
    parallel:
        yalign .5
        linear 3.0 yalign .6
        pause .3
        linear 6.0 yalign .4
        pause .3
        linear 3.0 yalign .5
        repeat

    parallel:
        xalign .5
        linear 3.0 xalign .45
        pause .2
        linear 6.0 xalign .55
        pause .2
        linear 3.0 xalign .5
        repeat


# Declare images
image conductor = "images/character/conductor_beta2.png"
image heiden beta = "images/character/heiden beta2.png"
image black = "images/used bg/black.jpg"

#Declare image animation/transformation
transform zoomin:
    parallel:
        linear 2.0 zoom 1.5
        pause 1.0
        
    parallel:
        linear 2.0 xalign 1.0 yalign 0.35
        pause 1.0
        
transform zoomout:        
    parallel:
        linear 2.0 zoom 1.0
        pause 1.0
        
    parallel:
        linear 2.0 xalign 0.5 yalign 0.5
        pause 1.0 
        
transform c_entrance:                   #kann gelöscht werden
    xpos 1.0 yoffset 20
    linear 2.0 xalign 0.75

transform c_flip:                       #kann gelöscht werden
    linear .5 xzoom -1.0
    linear 1.0 xalign 0.5
    
transform c_flip2:                      #kann gelöscht werden
    linear .5 xzoom 1.0
    linear 1.0 xalign 0.6

transform c_adjust:
    linear .2 yoffset 0
    linear .2 yoffset 20
    pause .5
    
    block:
        linear .01 xoffset 20
        linear .01 xoffset -40
        linear .01 xoffset 20
        repeat 2

transform shiver:
    linear .1 xoffset 3
    linear .1 xoffset -6
    linear .1 xoffset 3
    repeat
    
transform shivertwice:
    linear .1 xoffset 3
    linear .1 xoffset -6
    linear .1 xoffset 3
    repeat 2
        
transform twitchtwice:
    linear .1 yoffset 3
    linear .1 yoffset -6
    linear .1 yoffset 3
    repeat 2
    
#Declare sfx
define audio.game_start = "audio/sfx/game_start1.mp3"
define audio.subway_door = "audio/sfx/subway_door.mp3"
define audio.footsteps = "audio/sfx/footsteps2.mp3"
define audio.footsteps2 = "audio/sfx/footsteps.mp3"
define audio.wind = "audio/sfx/wind.mp3"
define audio.windowopen = "audio/sfx/window.mp3"
define audio.train_whistle = "audio/sfx/train_whistle.mp3"
define audio.fail = "audio/sfx/fail.mp3"
define audio.briefcase = "audio/sfx/briefcase.mp3"
define audio.paper = "audio/sfx/paper.mp3"
define audio.train_passby= "audio/sfx/train_passby.mp3"


#Declare bgm
define audio.subway_train = "audio/bgm/train_interior.mp3"
define audio.train_meet = "audio/bgm/03 - Happy Meeting.mp3"

# Declare characters
define nv = Character(None, kind=nvl)
define hv = Character(None, kind=nvl, what_prefix="\"", what_suffix="\"", what_color="#1d87da")
define cv = Character(None, kind=nvl, what_prefix="\"", what_suffix="\"", what_color="#8fbc8f")
define mv = Character(None, kind=nvl, what_prefix="\"", what_suffix="\"", what_color="#a69c8d")
define bhg = DynamicCharacter(_("heidenname"), color="#1d87da")
define x = Character('???', color="#1d87da")
define bh = Character('Young Boy', color="#1d87da")
define h = DynamicCharacter(_("heidenname"), color="#1d87da") #define h = Character('Heiden', color="#1d87da")
define c = Character('Conductor', color="#8fbc8f")
define m = Character('Man', color="#a69c8d")
define cg = Character('Schaffner', color="#8fbc8f")    
define mg = Character('Mann', color="#a69c8d")                                                                                  
# The game starts here.
label start:
    
    $ defaultSFX = _preferences.get_volume('sfx')
         
    $renpy.music.set_volume(0.0, 0.0, channel="sfx1")
    $ renpy.block_rollback()
    $_game_menu_screen = "save_screen"
    $ save_name = "Chapter 0 - Proloque" if _preferences.language == None else "Kapitel 0 - Prolog"
    stop music
    show black
    play sound game_start             #game_Start.mp3 soll die sfx sein, die ertönt, wenn das Spiel gestartet wird.
    $ renpy.pause(4.0, hard=True)
    play music subway_train loop
    
    nv "\nWhen the night has drawn its curtain over the buzzling cities {w}\nand human-shaped owls begin to swarm the streets..."
    nv "\nRestlessness has taken hold of those who challenge time itself; those who try to make every second count."
    nv "\nThe streets are filled with life and the colorful showcase lighting serves as a pleasant counterbalance to the meager and lifeless expressions that can be found on the faces of the passersby."
    nv "\nOne may think that at least the spectacular view on the glittering nightlife might change the grim faces for the better but for someone working day after day..."
    nv "\nThe view may be the last thing on his mind."

    nvl clear
    window hide
    scene bg train with fade
    
    mv "*Sigh*"
    nv "\nSitting in a rather unhealthy pose with his shoulders sagging, a man in his early thirties keeps himself awake while readjusting his suitcase that is in danger of slipping from his hands."
    nv "\nHis suit is wrinkled and visible eye bags mark his face - \nthe typical indication of sleeplessness."
    nv "\nThe wristwatch on his hand strikes 11PM, usually a time where the train wagons are at least a bit crowded with people eager to enjoy their weekend trips..."
    nv "\nBut nonetheless this particular train wagon remains as good as empty."
    nv "\nThat may be the reason why he occupies the four seater for himself and his battered suitcase."
    
    nvl clear
    window hide
    
    mv "*Sigh*"
    nv "\nThe monotonous sighs resound through the wagon of the train which give off the feeling that it is infact haunted."
    nv "\nLike a howling ghost of a lonesome individual who perished in his own loneliness?"
    nv "\nYeah, something like that."
    nv "\nThe train he currently boarded is headed to the outskirts of the city and not towards the city's center; \na train that is headed to nowhere, so to speak."
    nv "\nWhile he gazes outside the window to view the distant city and all its troubles become one with the night's sky, he slowly feels his own troubles crumbled and dissolved within the darkness."

    nvl clear
    window hide
    play sound subway_door
    $ renpy.pause(3.0, hard=True)
    
    nv "\nThe man is startled by the sound of the automated door randomly opening and closing."
    nv "\nSomeone definitely came in just now."
    
    window hide
    show bg train at zoomin
    show conductor:
        xpos 1.0 yoffset 20
        linear 2.0 xalign 0.75
    
    nv "\nThe man straightens his upper body and peeks between the seats toward the door to see a man in a uniform standing in the hallway with something in his hand."
    
    window hide
    show conductor:
        linear .5 xzoom -1.0
        linear 1.0 xalign 0.5
    
    nv "\nBigger than a smartphone and comparable to a calculator, that particular black device was connected to the uniform with some sort of cable.\n"
    
    show conductor:
        linear .5 xzoom 1.0
        linear 1.0 xalign 0.6
    
    mv "Ah, it's just the conductor."
    
    nvl clear
    window hide
    show conductor:
        linear .1 yoffset 0
        linear .1 yoffset 20
        pause .5
    
        block:
            linear .01 xoffset 5
            linear .01 xoffset -10
            linear .01 xoffset 5
            repeat 2
    
    nv "\nAfter inputting something into his device, the conductor crams it into his breast pocket and adjusts the cap on his head that has the train company's logo embedded on it."
    
    show conductor:
        linear .5 xzoom -1.0 yalign 0.5 xalign 0.7
    
    nv "\nWith a quick look at his watch the conductor readdresses his attention to the door behind the seated man."
    nv "\nIt seems like he just spotted the man at that moment and while slightly surprised,"
    
    play sound footsteps
    hide conductor with dissolve
    show bg train at zoomout
    $ renpy.pause(3.0, hard=True)
    
    nv "\n\nhe walks towards the source of his interest."
    
    nvl clear
    window hide
    scene bg train
    show conductor:
        xzoom -1.0 xalign .7
    
    c "What a pleasant surprise!"
    c "It does not often happen that I find passengers lodged in the very last wagon so I prematurely assumed that my shift was finally over."
    "Compared to the other wagons of the train, this peculiar wagon has a rather outdated look to it, making it stand out even more from the outside."
    "As if it is indeed alienating itself from the rest of the world - a natural outcast."
    "And outcasts tend to attract even more like-minded people."
     
    show conductor:
        linear .5 yoffset 50
        pause .3
        linear .2 yoffset 20
        
    "The conductor tips his cap while looking apologetically at the seated man. His smile is honest and bright, contrary to the weary appearance of the passenger."

    
    show conductor:
        linear 1.0 xzoom 1.0
        
    "They may both be around the same age but the conductor seems to be quite lax, unfitting for his professional appearance. That was the aura he is emitting."
    
    show conductor:
        linear 1.0 xzoom -1.0
        
    c "You may as well have the last ticket I have to check for this trip so let me get my thoughts out really quick or it's going to devour me."
    m "Then go ahead."
    "The man gives a spontaneous response to the sudden turn of events though it's more for the conductor to have his peace of mind than for the man to have a meaningful conversation."
    "The late hours may have taken its toll even on the conductor."
    c "Do you know how I want to blame my train company for using taxes to finance this nearly empty train trip every weekend?" 
    
    show conductor:
        linear 1.0 zoom 1.2 yalign 0.6
    
    c "Do they even spare a thought for the employees who are forced to give up their plans for the weekend?"
    
    show conductor:
        linear 1.0 zoom 1.4 yalign 0.4
        
    c "I mean the trip is fine and all and for the tourists there may be some pictures to take on their way to the city..."
    
    show conductor:
        linear 1.0 zoom 1.6 yalign 0.3
        
    c "but the numbers of tourists decreased to the point that I question the profitability of this trip - especially this trip here on the way back to the boonies."
    
    show conductor:
        linear 1.0 zoom 1.8 yalign 0.2
        
    c "How's your take on this, Sir?"
    
    "The man does not seem to respond."
    "He is neither awake enough for any reasonable input nor is he feeling like giving any kind of response at all."
    "Because at the moment he is also a passenger who rides this very train to reach his destination."
    m "I see your point but I guess we both can't do anything about it."
    m "Here's my ticket, Conductor."
    
    show conductor:
        linear 1.0 zoom 1.0 yalign 0.5
        
    "A dreary yawn escapes his lips as he reaches into his suit for the ticket and hands it over for inspection."
    "It's obvious that the man does not care the least about the circumstances of the conductor."
    "The man hopes to return to his state of silence and inner tranquility by cutting down the possibility of any conversation happening."
    
    show conductor:
        linear 0.2 xzoom 1.0
        
    c "Ah "
        
    show conductor:
        linear 0.2 xzoom -1.0
        
    extend "yes, that's what I will do then."
    
    show conductor:
        parallel:
            linear 1.0 zoom 1.5
            pause 1.0
            linear 1.0 zoom 1.0
        
        parallel:
            linear 2.0 yalign 0.8
            pause 1.0
            linear 1.0 yalign 0.5

    "The conductor bends himself to receive the ticket from the man's impassive hand."
    c "Ah, you got the special weekend ticket for two, Sir?"
    c "The lavatory ahead is currently in use so can I assume it's your dame?"
    "The question is well-placed as the man's ticket is a special offer for couples."
    "It's a current fashion to go on a trip with someone to somewhere quiet and relaxing as the lifestyle in the city can become quite hectic and also loud."
    m "Actually, no."
    m "Unfortunately I am travelling alone due to some special circumstances."
    "The man dismisses the assumption in an instant while the scenery behind the window glasses has completely darkened by now."
    "The glass now reflects his own tired facial expression, a genuine feeling he is currently experiencing."
    
    show conductor:
        linear .6 xzoom 1.0
    
    c "Special circumstances, I see."
    "While the conductor nods at the lanquid response of the man, he takes out a clipper-like device to evaluate the ticket."
    "The man's eyes stay fixated on the glas as if he is trying to stare into the eyes of his doppelganger behind the glas."
    c "Are you riding this train to the final destination?"
    m "Yup, that I do."
    
    show conductor:
        linear .6 xzoom -1.0
        
    c "Well, in any case, I will just evaluate half of the ticket."
    c "You may use that ticket again for the remainder of the weekend yourself."
    "The man reacts unimpressed."
    "Either way, he does not seem to care much about the ticket at all because it doesn't look like he is going to need it again any time soon."
    "The conductor also appears to have given that consideration as a mere routine measure."
    
    show conductor:
        parallel:
            linear 1.0 zoom 1.5
            pause 1.0
            linear 1.0 zoom 1.0
        
        parallel:
            linear 2.0 yalign 0.8
            pause 1.0
            linear 1.0 yalign 0.5

    
    "After handing the ticket back to the man, the conductor sags his shoulder further as if a burden has been lifted from them."
    c "I guess I can finally sit back for now."
    c "We will arrive at the final destination in approximately six hours."
    c "Well, only if there are no delays on the way, of course."
    c "Have an enjoyable trip, Sir."
    
    play sound footsteps
    show conductor:
        linear 2.0 xpos -0.5
        
    m "Yeah, I will."
    "Though the encounter took longer than expected, peace has finally returned to this particular train wagon."
    
    play sound paper
    "The man takes a moment to return the ticket to the inside pocket of the suit"
    "then lays his suitcase to the side"
    "and decides to seize the moment for a nap when his eyelids ever allow him to."
    "But things don't go well."
    
    show conductor:
        linear 0.3 xpos 0.0
        
    c "Oh, who do we have here?"
    "Seems like the conductor has found yet another passenger in the row of seats just behind the man."
    "And the man thought for the whole time that he occupied the entire wagon just for himself!"
    x "Hrm...Zzz..."
    c "Hey boy, wake up! I am here to check your ticket!"
    "The conductor tries to wake him up through verbal attempts."
    "..."
    
    show conductor at shiver
    "Seems like his efforts grew no fruits."
    "The conductor becomes desperate as his fruitless efforts cost him not only time but apparently also his patience."
    "The slumbering passenger appears to be his sole obstacle in reaching his end of the shift."
    "The noise that echoes through the wagon could even arouse the dead from their well-earned sleep."
    
    show conductor:
        linear 1.5 xalign 0.8
        
    show heiden beta:
        ypos 0.55 xpos -0.5
        linear 1.5 xalign 0.2
        
    $ renpy.pause(1.5, hard=True)
    
    "The man who was on the verge of sleeping in has become curious about the situation as he gears to the scene."
    "From the looks of it, the passenger in question appears to be a young boy with a blanket on him as he uses a huge trolly as his pillow."
    
    show heiden beta at shiver
    
    "He is either trying to dodge the fare by pretending to sleep"
    "or is a pretty deep sleeper."
    "Though that wouldn't make any sense because it may prove to be quite uncomfortable, sleeping in this disturbing position like that."
    "Either way, as wooly thoughts try to knit themselves into even more confusing theories..."
    
    show heiden beta:
        ypos 0.55 xalign 0.2
    
    m "If the problem lies on the fact that you must check his ticket then let me cover him with my ticket."
    m "Just let that boy sleep."
    "The man ultimately decides to rescue that boy from his adversity."
    "Though it mostly happened on a whim."
    "A whim, caused by the suspicion that the boy is infact awake right now."
    
    show conductor:
        linear 1.0 xalign 0.5
        
    show heiden beta:
        linear 1.0 xalign 0.1
        
    c "Well, that's one thing but I am bothered to see no adult around to supervise him."
    
    show heiden beta at shivertwice
    
    "A plausible reason."
    m "Well, they may be the ones using the lavatory right now as you have said earlier."
    m "Look.\nJust enjoy your off-hours for now."
    m "I am here, I will wake him up to ask him about that and inform you if he stays alone for a longer period of time."
    m "The next stop is not until an hour from now so we'll find a solution by then."
    
    show conductor:
        linear 1.0 xzoom 1.0 xalign 0.7
        
    "The conductor seems to ponder about the suggestion while the man tries to comprehend why he actually goes out of his way to vouch for the boy."
    "They are both complete strangers."
    
    show conductor:
        linear 1.0 xzoom -1.0 xalign 0.5
        
    c "Well, that's also a solution."
    c "To be honest, I don't actually want to babysit someone's child this late."

    show conductor:
        linear 1.0 xzoom 1.0 xalign 0.2
        
    c "Just go straight this corridor to find the conductor's cabin if you need me."
    c "And also, though I do not feel like playing caretaker and have no talents for such things, this is still part of my job."
    m "Yeah, will do."
    c "Okay, see ya."
    
    play sound subway_door
    show conductor:
        linear 1.0 xzoom -1.0 xpos -0.5
        
    show heiden beta:
        linear 1.0 xalign 0.2
        
    m "Since when did we become so informal?"
    m "Whatever."
    
    hide conductor
    show heiden beta:
        linear 1.0 xpos -0.5
     
    "Now that only the man and the boy remain as the sole inhabitants of the wagon, the former decides to just head back to his own seat while the latter stays unmoved in his sleeping position."
    m "What a night."
    "Regarding the \"seizing the moment\" and \"well-earned sleep\" from earlier, the man is now fully awake."
    "Maybe the exceeding amount of expended energy while talking has made his body think it's daytime by now."
    
    show heiden beta:
        ypos 0.0
        linear 1.0 xpos -0.15
    $ heidenname = "Junge"  
    $ save_name = "Chapter 0.1 - The Meeting" if _preferences.language == None else "Kapitel 0.1 - Die Begegnung"
    "But now he is awake enough to feel the gaze of yet another intruder of his time and tranquility."
    m "So what do you want from me now, boy?"
    bh "..."
    m "C'mon. I don't feel like holding a monologue all by myself now so if you have no further business with me..."
    bh "You knew I was awake just now, did you?"
    "The words formed a question but the boy's tone transformed it into a kind of accusation instead."
    m "Of course, nobody would just sleep soundly with the head in the knees like you did."
    m "It's bad for your back, you know.\nI sincerely hope you do not normally sleep like that."
    m "Do you want to look like the Hunchback of Notre Dame?"
    
    pause .5
    show heiden beta at shivertwice
    
    "The boy appears to be in thought for a moment but quickly grasps the reference."
    bh "Heh. That's a good one."
    bh "..."
    
    bh "Is that seat taken?"
    
    stop music fadeout 3.0
    show heiden beta:
        linear 1.0 xpos -0.5
        
    "But before the man can even utter some sort of protest or point out his right of privacy"
    
    show heiden beta:
        linear 1.0 xalign 0.5
        
    play music train_meet fadein 1.0
    
    "the boy immediately pflasters himself on the opposite seat with his trolly and blanket in tow."
    bh "Yo."
    m "And what did I do to deserve this?"
    bh "Mom always told me to thank people properly."
    m "Well, she is right about that one."
    bh "So here I am."
    bh "Thanks, Mister."
    m "I accept your gratitude."
    m "Can I perhaps have my peace back?"
    bh "Now now. You can be happy yourself."
    bh "In my eyes, you just graduated from spooky ghost person to lonely no fun mister person."
    m "Is that a fact?"
    m "I have a feeling that they're not entirely different from each other."
    m "And I especially don't feel like being praised right now."
    bh "Don't think too deeply about it, Mister."
    bh "This is more for me than for you."
    m "What's that supposed to mean?"
    bh "I stay here for the sake of your ticket."
    bh "So make yourself useful by pretending to be a relative or something, Mister."
    bh "It's the least you could do after giving me all those nightmares with your creepy moans."
    
    show heiden beta at shivertwice
    
    bh "I have goosebumbs all over me just thinking about it."
    m "You are quite full of yourself now, kid."
    m "And those \"creepy moans\" were adult signals that symbolize the harshness of life itself!"
    m "But anyways, weren't you being grateful and thanking me just a moment ago?"
    m "I want that boy back."
    bh "This is this and that is that."
    bh "But I can see you being a lame mister yourself, Mister."
    
    show heiden beta:
        linear 3.0 xalign 0.8
        
    "A feeling of irritation slowly creeps up on the man as he tries to communicate with the boy."
    
    show heiden beta:
        linear 2.0 ypos 150
        
    "Maybe he is just bad with kids in general."
    
    show heiden beta at shivertwice
    
    "But if every kid was like the one before him..."
    bh "What's with that suitcase of yours, Mister?"
    bh "It's so worn out that I could peek in its interior just by looking into the cracks."
    "Seems like {b}not{/b} babysitting the boy was the right decision for the conductor after all."
    
    show heiden beta:
        linear 0.5 xalign 0.5 yalign 0.5
        
    m "Hey kid, stop looking at my stuff!"
    bh "You really are no fun, Mister."
    m "Man, what did I get myself into?"
    "Did the goodwill of the man cause this situation?"
    "With no way to ascertain whether or not this was the case, the immediate social incompatibility of those two proves to be quite an obstacle."
    
    show heiden beta:
        linear 2.0 zoom 1.4
        
    "A silent and slightly awkward moment passes while the man tries to have a closer look at this free-spirited fellow."
    "From the looks of it, he might be around 12 years old."
    "His longish pale blond hair is a slight mess but doesn't really cover up his face at all."
    "His eyes as they stare at the window have an empty and melancholic vibe to them."
    "Like they were looking at something and at the same time not looking at all."
    "He also has his blanket wrapped around his shoulders while he rubs his fingertips together in an asynchronous pattern to produce heat."
    "Left. Left. Right. Left. Right. Rig- no, left again."
    "Other than that, his oversized trolly that is currently laying beside him on the seat like a passenger itself."
    "The man reluctantly decides to initiate a conversation in order to know more about the boy."
    "The motivation behind his decision however stems from the fact that he told the conductor earlier that he'll do it."
    
    $ ask_firsttime = True
    $ trainName = False
    $ trainParents = False
    $ trainReason = False
    
    jump trainMenu

label trainMenu:
    
    show heiden beta:
        linear 1.5 zoom 1.0 xalign 0.5 yalign 0.5
    
    if trainName == True and trainParents == True and trainReason == True:
        m "I guess it's time to go to sleep."
        jump trainEnd
        
    elif ask_firsttime:
        "But what to ask him about?"
        
    elif ask_firsttime == False and trainName == False:
        "What should he ask the boy next?"
        
    else:
        "What should he ask Heiden next?"
        
    $ ask_firsttime = False
        
    menu:
        "His name" if trainName == False:
            jump name  
        
        "The whereabouts of his parents" if trainParents == False:
            jump parents
        
        "His reason for boarding the train" if trainReason == False:
            jump reason
      
      
label name:
    if trainName:
        h "I'll call you old and senile if you ask me about my name again, Mister."
        m "I guess I won't then."
        jump trainMenu
        
    else:
        $ trainName = False
        "To be honest, the man never actually cared about asking the boy's name."
        "He guesses that he can't keep calling him kid or boy and may as well get it over with."
        m "Hey kid, what's your name anyways?"
        
        show heiden beta:
            linear 1.0 xzoom -1.0
            pause 3.0
            linear 1.0 xzoom 1.0
        
        "The boy ponders for quite some time about the question as if he wasn't prepared to be asked that."
        bh "Is my name that important to know?"
        bh "It worked so well with me calling you mister too, Mister."
        
        show heiden beta:
            linear 0.5 zoom 1.3
            
        m "Well, let's say it like that."
        
        show heiden beta:
            linear 0.5 zoom 1.7
            
        m "I did pay your fare for the train so at least I'd like to know the name of the one who is mooching off of my goodwill."
        bh "Sounds reasonable enough."
        bh "..."
        
        show heiden beta at shiver
        $ heidenname = "Heiden "
        "The boy twiddled with his thumbs as he is apparently trying to come up with a good excuse."
        h "It's Heiden."
        
        show heiden beta:
            linear 1.0 zoom 1.0
            
        m "Heiden? That's a rather unusual name."
        
        show heiden beta:
            linear 1.0 xzoom -1.0
            linear 1.5 xalign 0.2
            
        h "I didn't choose that name, Mom did."
        "Though the pause was long for him to give his name, his words felt genuine."
        m "Well, she might had a good reason for it. Not that I care."
        
        show heiden beta:
            linear 1.0 xzoom 1.0
            
        h "Yeah."
        m "..."
        h "..."
        "Another awkward silence passes."
        $ trainName = True
    
    jump trainMenu
    
    
label parents:
    if trainParents:
        if trainName:
            h "I'll call you old and senile if you ask me about that again, Mister."
        else:
            bh "I'll call you old and senile if you ask me about that again, Mister."
            
        m "I guess I won't then."
        jump trainMenu
        
    elif trainName:
        $ trainParents = False
        "The man begins to wonder about the whereabouts of Heiden's parents."
        "They have been talking for quite some time now but there are no signs of his parents returning anytime soon."
        "Also the fact that Heiden is carrying luggage for him alone is quite suspicious, given the fact that he is still just a kid."
        
        show heiden beta:
            linear 1.0 zoom 1.2
            linear 1.0 xzoom -1.0
            pause 3.0
            linear 1.0 xzoom 1.0    
            
        m "So can I guess that you boarded this train on your own?"
        m "Where are your parents?"
        h "You really nag about the strangest things, Mister."
        m "Just answer them."
        m "Or I'll get into trouble with that conductor the next time he pays us a visit."
        h "Mom always said to answer questions honestly."
        h "So I would have answered them anyways even if I didn't want to, Mister."
        m "I really need to give your mother credit sometimes."
        m "She really helped our conversations gain substance so far."
        
        show heiden beta:
            linear 1.0 xzoom -1.0
            linear 1.5 xalign 1.0
            
        h "Not gonna happen anytime soon."
        m "Why not?"
        
        show heiden beta:
            linear 1.0 xzoom 1.0
            
        h "She died."
        
        show heiden beta:
            linear 1.0 xzoom -1.0
            
        m "\(Ouch.\)"
        "Seems like the man scratched against a sensitive topic."
        "Heiden appears to be busy by snuggling into his blanket and looking into the faraway sky of the night outside the window like he was looking out for Santa Claus on the night before christmas"
        "but his uttering earlier didn't leave him unaffected."
        m "Sorry about that, seriously sorry."
        
        show heiden beta:
            linear 1.0 xzoom 1.0
        
        h "It's ok."
        h "You don't need to bow your head like that."
        h "Aren't you an adult?\nAren't adults embarassed to do that infront of a kid?"
        
        show heiden beta:
            linear 1.0 xzoom -1.0
            
        "Though his sermon hits the bull's eye, Heiden resumed his apparent search for Santa Claus with a more relaxed expression."
        "Sometimes kids act more mature than one may think."
        
        m "What about your Dad then?"
        
        pause 2.0
        show heiden beta:
            linear 1.0 xzoom 1.0
            
        h "Don't know about him."
        h "It's always been me and Mom."
        m "I see."
        
        show heiden beta:
            linear 1.5 xalign 0.5
            
        "It seems like his window staring contest is finally over as he slowly resumes his initial seated position."
        m "\(I guess I am dealing with a fatherless household here.\)"
        "The man can't help but feel sympathy and worry for the boy named Heiden as he tries to think about ways to brighten up the conversation."
        m "..."
        "But nothing comes to mind."
        
        $ trainParents = True
    
        jump trainMenu
    
    else:
        $ trainParents = False
        "The man begins to wonder about the whereabouts of the boy's parents."
        "They have been talking for quite some time now but there are no signs of his parents returning anytime soon."
        "Also the fact that the boy is carrying luggage for him alone is quite suspicious, given the fact that he is still just a kid."
        
        show heiden beta:
            linear 1.0 zoom 1.2
            linear 1.0 xzoom -1.0
            pause 3.0
            linear 1.0 xzoom 1.0    
            
        m "So can I guess that you boarded this train on your own?"
        m "Where are your parents?"
        bh "You really nag about the strangest things, Mister."
        m "Just answer them."
        m "Or I'll get into trouble with that conductor the next time he pays us a visit."
        bh "Mom always said to answer questions honestly."
        bh "So I would have answered them anyways even if I didn't want to, Mister."
        m "I really need to give your mother credit sometimes."
        m "She really helped our conversations gain substance so far."
        
        show heiden beta:
            linear 1.0 xzoom -1.0
            linear 1.5 xalign 1.0
            
        bh "Not gonna happen anytime soon."
        m "Why not?"
        
        show heiden beta:
            linear 1.0 xzoom 1.0
            
        bh "She died."
        
        show heiden beta:
            linear 1.0 xzoom -1.0
            
        m "\(Ouch.\)"
        "Seems like the man scratched against a sensitive topic."
        "The boy appears to be busy by snuggling into his blanket and looking into the faraway sky of the night outside the window like he was looking out for Santa Claus on the night before christmas"
        "but his uttering earlier didn't leave him unaffected."
        m "Sorry about that, seriously sorry."
        
        show heiden beta:
            linear 1.0 xzoom 1.0
        
        bh "It's ok."
        bh "You don't need to bow your head like that."
        bh "Aren't you an adult?\nAren't adults embarassed to do that infront of a kid?"
        
        show heiden beta:
            linear 1.0 xzoom -1.0
            
        "Though his sermon hits the bull's eye, the boy resumed his apparent search for Santa Claus with a more relaxed expression."
        "Sometimes kids act more mature than one may think."
        
        m "What about your Dad then?"
        
        pause 2.0
        show heiden beta:
            linear 1.0 xzoom 1.0
            
        bh "Don't know about him."
        bh "It's always been me and Mom."
        m "I see."
        
        show heiden beta:
            linear 1.5 xalign 0.5
            
            
        "It seems like his window staring contest is finally over as he slowly resumes his initial seated position."
        m "\(I guess I am dealing with a fatherless household here.\)"
        "The man can't help but feel sympathy and worry for the boy as he tries to think about ways to brighten up the conversation."
        m "..."
        "But nothing comes to mind."
        
        $ trainParents = True
    
        jump trainMenu
    
    
label reason:
    if trainReason:
        if trainName:
            h "I'll call you old and senile if you ask me about that again, Mister."
        else:
            bh "I'll call you old and senile if you ask me about that again, Mister."
            
        m "I guess I won't then."
        jump trainMenu
            
    elif trainName:
        $ trainReason = False
        "Though they both ride the same train, the man tries to think about reasons why Heiden would attempt such a long journey all on his own."
        m "Hm..."
        
        show heiden beta:
            linear 1.0 zoom 1.5
            
        h "You seem deep in thought, Mister."
        "Heiden draws nearer to examine the man like he was able to read out the man's thoughts with enough effort."
        m "Well, I guess it's worth a shot."
        
        show heiden beta:
            linear 1.0 zoom 1.2
            
        h "What is worth a shot?"
        m "Your reason for boarding this train, Heiden."
        h "Oh."
        
        show heiden beta:
            linear 1.0 zoom 1.0
        
        show heiden beta at shivertwice
        
        "Heiden repositions himself on his seat as he faces the man with a facial expression one may find on a kid that is about to witness a magic trick from a top magician."
        h "Let's hear it then."
        m "So a boy called Heiden boarded this train."
        
        show heiden beta:
            linear 0.5 yalign 0.4
        m "A train headed to nowhere with no ticket."
        
        show heiden beta:
            linear 0.5 yalign 0.25
        m "He also travels alone. This is important."
        
        show heiden beta:
            linear 0.5 yalign 0.1
        m "He is also carrying a large trolly with him, a trolly big enough for adult use."
        
        show heiden beta at shiver
        stop music fadeout 5.0
        m "I hope you're still with me here, Heiden."
        m "This will blow you mind."
        m "I can see it now. I got you!"
        h "Wait am moment, I-{nw}"
        m "You are a fugitive!" 
        m "On the run from the police!"
        m "You got a stash full of money in your trolly!"
        "..."
        h "..."
        m "...So?"
        
        show heiden beta:
            parallel:
                linear .1 yalign 0.2
                pause .5
                linear .1 yalign 0.5
                
            parallel:
                linear 0.5 zoom 1.5
                pause 0.3
                linear .5 zoom 1.0
        
        $ playmusic('audio/sfx/fail.mp3', "sfx1", 0.5)
        h "NO."
        
        show heiden beta:
            linear 1.0 xzoom -1.0
            pause 2
            linear 1.0 xzoom 1.0
            
        play music train_meet fadein 1.0 
        h "Though I give you a passing grade for your wanton imagination and efforts."
        m "So what else is there?"
        h "Isn't it obvious?"
        h "I am moving to my uncle's house. He lives quite far away from here, you know."
        
        show heiden beta:
            linear .5 xalign 0.2
            pause .5
            
        h "I have my luggage all stuffed in here."
        
        play sound briefcase
        show heiden beta at shivertwice
        
        show heiden beta:
            linear .5 xzoom -1.0
            
        "Heiden opens his trolly with swift motions to reveal many kinds of clothes and also a green soccer ball peeks out."
        "No stashes of money at all."
        "Just an ordinary trolly with ordinary things - minus the green soccer ball of course."
        h "I might as well say that I am currently carrying around my home."
        m "Like a snail?"
        h "Yup, exactly."
        m "Well, I am disappointed but I guess that is what you might call \"coming to terms with reality\"."
        
        show heiden beta:
            linear .5 xzoom 1.0
            pause .5
            
        show heiden beta at shivertwice
        play sound briefcase
        h "Disappointed?"
        "Heiden quickly packed his trolly together but not before removing something akin to a travel pillow."
        "He proceeds to lay it on top of his trolly "
        
        show heiden beta:
            linear 1.0 xalign .5
        
        extend "before returning to his own seated position."
        h "You don't need to feel disappointed."
        h "I actually had a bit of fun listening to your random rambles."
        
        show heiden beta at shivertwice
        
        "Heiden expresses something like a tiny weeny smile on his face as he tries to supress a giggle."
        "It genuinely feels like he is someone who never laughs."
        "Or forgot how to laugh."
        "Something that children should never do if they ever plan to become happy."
        
        if trainParents:
            m "So I guess your uncle will take care of you then?"
            h "Yeah. I have other relatives but they don't like me that much."
            "Is Heiden's uncle apparently the least troublesome person to deal with from a bunch of no-goods?" 
            m "I see."
            
            show heiden beta:
                linear .5 zoom 1.3 yalign 0.3
            
            h "It's fine! Really!"
            "Though Heiden retracts his smile, he replaces it with a beam full of confidence."
            m "Yeah, you're gonna be fine."
            
        else:
            m "But a stash of money would have make this situation all the more dubious."
            h "What do you mean by that?"
            m "I don't think you would think of dodging the fare if you had that much money in your disposal to begin with."
        
            show heiden beta:
                linear 1.0 xzoom -1.0
                pause.5
                linear 1.0 xzoom 1.0
                
            h "Oh, you right about that, Mister."
            m "But why did you dodge the fare in the first place?"
            h "I got lost in the central station and was about the miss the train, you see?"
            "To get lost in the central station might happen more often than one think."
            "It's especially the winding and complex underpasses that are poorly described."
            "Being a kid doesn't help the situation at all."
            m "Well, yeah. I can understand that."
        
        "..."
        $ trainReason = True
        
        jump trainMenu
        
    else:
        $ trainReason = False
        "Though they both ride the same train, the man tries to think about reasons why the boy would attempt such a long journey all on his own."
        m "Hm..."
        
        show heiden beta:
            linear 1.0 zoom 1.5
            
        bh "You seem deep in thought, Mister."
        "The boy draws nearer to examine the man like he was able to read out the man's thoughts with enough effort."
        m "Well, I guess it's worth a shot."
        
        show heiden beta:
            linear 1.0 zoom 1.2
            
        bh "What is worth a shot?"
        m "Your reason for boarding this train."
        bh "Oh."
        
        show heiden beta:
            linear 1.0 zoom 1.0
        
        show heiden beta at shivertwice
        
        "The boy repositions himself on his seat as he faces the man with a facial expression one may find on a kid that is about to witness a magic trick from a top magician."
        bh "Let's hear it then."
        m "So a boy boarded this train."
        
        show heiden beta:
            linear 0.5 yalign 0.4
        m "A train headed to nowhere with no ticket."
        
        show heiden beta:
            linear 0.5 yalign 0.25
        m "He also travels alone. This is important."
        
        show heiden beta:
            linear 0.5 yalign 0.1
        m "He is also carrying a large trolly with him, a trolly big enough for adult use."
        
        show heiden beta at shiver
        stop music fadeout 5.0
        m "I hope you're still with me here, little guy."
        m "This will blow your mind."
        m "I can see it now. I got you!"
        bh "Wait am moment, I-{nw}"
        m "You are a fugitive!" 
        m "On the run from the police!"
        m "You got a stash full of money in your trolly!"
        "..."
        bh "..."
        m "...So?"
        
        show heiden beta:
            parallel:
                linear .1 yalign 0.2
                pause .5
                linear .1 yalign 0.5
                
            parallel:
                linear 0.5 zoom 1.5
                pause 0.3
                linear .5 zoom 1.0
        
    
        $ playmusic('audio/sfx/fail.mp3', "sfx1", 0.5)
        bh "NO."
        
        show heiden beta:
            linear 1.0 xzoom -1.0
            pause 2
            linear 1.0 xzoom 1.0
            
        play music train_meet fadein 1.0
        bh "Though I give you a passing grade for your wanton imagination and efforts."
        m "So what else is there?"
        bh "Isn't it obvious?"
        bh "I am moving to my uncle's house. He lives quite far away from here, you know."
        
        show heiden beta:
            linear .5 xalign 0.2
            pause .5
            
        bh "I have my luggage all stuffed in here."
        
        play sound briefcase
        show heiden beta at shivertwice
        
        show heiden beta:
            linear .5 xzoom -1.0
            
        "He opens his trolly with swift motions to reveal many kinds of clothes and also a green soccer ball peeks out."
        "No stashes of money at all."
        "Just an ordinary trolly with ordinary things - minus the green soccer ball of course."
        bh "I might as well say that I am currently carrying around my home."
        m "Like a snail?"
        bh "Yup, exactly."
        m "Well, I am disappointed but I guess that is what you might call \"coming to terms with reality\"."
        
        show heiden beta:
            linear .5 xzoom 1.0
            pause .5
            
        show heiden beta at shivertwice
        play sound briefcase
        bh "Disappointed?"
        "The boy quickly packed his trolly together but not before removing something akin to a travel pillow."
        "He proceeds to lay it on top of his trolly "
        
        show heiden beta:
            linear 1.0 xalign .5
        
        extend "before returning to his own seated position."
        bh "You don't need to feel disappointed."
        bh "I actually had a bit of fun listening to your random rambles."
        
        show heiden beta at shivertwice
        
        "The boy expresses something like a tiny weeny smile on his face as he tries to supress a giggle."
        "It genuinely feels like he is someone who never laughs."
        "Or forgot how to laugh."
        "Something that children should never do if they ever plan to become happy."
        
        if trainParents:
            m "So I guess your uncle will take care of you then?"
            bh "Yeah. I have other relatives but they don't like me that much."
            "Is his uncle apparently the least troublesome person to deal with from a bunch of no-goods?" 
            m "I see."
            
            show heiden beta:
                linear .5 zoom 1.3 yalign 0.3
            
            bh "It's fine! Really!"
            "Though the boy retracts his smile, he replaces it with a beam full of confidence."
            m "Yeah, you're gonna be fine."
            
        else:
            m "But a stash of money would have make this situation all the more dubious."
            bh "What do you mean by that?"
            m "I don't think you would think of dodging the fare if you had that much money in your disposal to begin with."
        
            show heiden beta:
                linear 1.0 xzoom -1.0
                pause.5
                linear 1.0 xzoom 1.0
                
            bh "Oh, you right about that, Mister"
            m "But why did you dodge the fare in the first place?"
            bh "I got lost in the central station and was about the miss the train, you see?"
            "To get lost in the central station might happen more often than one think."
            "It's especially the winding and complex underpasses that are poorly described."
            "Being a kid doesn't help the situation at all."
            m "Well, yeah. I can understand that."
        
        "..."
        $ trainReason = True
        
        jump trainMenu
            
            
            
label trainEnd:
    h "Yeah, I can hardly keep my eyes open, Mister."
    
    show heiden beta:
        linear 1.0 xalign 0.2
        
    show heiden beta at shivertwice
        
    "Heiden quickly shakes his travel pillow around until it gave off the feeling that it was inflated with feathers."
    
    show heiden beta:
        linear 1.0 xzoom -1.0
        
    h "Good night, Mister. Off I go. Don't you go making those noises again!"
    hide heiden
    #$ renpy.music.play('audio/bgm/03 - Happy Meeting.mp3', channel=7, loop=True, fadeout=2, synchro_start=False, fadein=1, tight=True, if_changed=False)
    "As Heiden pronounces his own journey to the land of the dreams, he vanishes under his blanket completely."
    
    m "Yeah, whatever."
    
    "The man peeks at his wristwatch. It's 2AM after midnight."
    "Time sure flies when one is occupied with something."
    play sound briefcase
    "With the soundless sleeping of his sudden travelling companion, the man opens his suitcase to reveal a metallic item with a rubber handle."
    "A gun."
    "After staring at it for a short while that could have been a slow eternity..."
    
    play sound windowopen
    pause 0.7
    $ renpy.music.play('audio/sfx/wind.mp3', channel=6, loop=True, fadeout=0, synchro_start=False, fadein=0, tight=True, if_changed=False)
    pause 0.7
    
    "he opens the window... "
    extend "throws it out"
    
    play sound windowopen
    pause 0.2
    $ renpy.music.stop(channel=6)
    
    extend " before closing it again."
    m "I guess my story won't end like that."
    "The man sinks back into his seat as the accumulated heat passes over to his already chilled body."
    "Soon the night will become day again."
    "And day will eventually become night."
    "The cycle continues."
    stop music fadeout 2
    m "Heiden, I hope you'll be happy at your new place."
    m "As for me? I'll put my initial plans on hold."
    
    $ renpy.pause(2.0, hard=True)
   
    if _preferences.language == None:
        jump ch0_transition
    else:
        jump ch0_transitionDE