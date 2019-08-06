image bg graypub = im.Grayscale("images/used bg/ch1_pub_night.jpg")
image credit1 10 = "images/chapter transitions/credit1_10.png"

define audio.fate = "audio/bgm/04 - At the Funeral.mp3"
define audio.bonus = "audio/bgm/01 - Main Menu.mp3"
define audio.togetherness = "audio/bgm/13 - Togetherness.mp3"

define audio.wipe = "<from 0 to 3>audio/sfx/wipe.mp3"
define audio.beerpour = "audio/sfx/beerpour.mp3"
define audio.beerclank = "<from 0 to 2>audio/sfx/beerclank.mp3"

image irina gstandard = im.Grayscale("images/character/irina_0.png")
image irina gmischief = im.Grayscale("images/character/irina_1.png")
image irina gactive = im.Grayscale("images/character/irina_2.png")

image irina standard = "images/character/irina_0.png"
image irina mischief = "images/character/irina_1.png"
image irina active = "images/character/irina_2.png"
image irina serious = "images/character/irina_3.png"
image irina blush = "images/character/irina_4.png"
image irina drunk = "images/character/irina_5.png"
image irina saddrunk = "images/character/irina_6.png"

define is_standard = Character('Irina', color="#f0a8ed", window_left_padding=160, show_side_image=Image("images/character/irina_side0.png", xalign=0.0, yalign=1.0))
define is_mischief = Character('Irina', color="#f0a8ed", window_left_padding=160, show_side_image=Image("images/character/irina_side1.png", xalign=0.0, yalign=1.0))
define is_active = Character('Irina', color="#f0a8ed", window_left_padding=160, show_side_image=Image("images/character/irina_side2.png", xalign=0.0, yalign=1.0))
define is_serious = Character('Irina', color="#f0a8ed", window_left_padding=160, show_side_image=Image("images/character/irina_side3.png", xalign=0.0, yalign=1.0))
define is_blush = Character('Irina', color="#f0a8ed", window_left_padding=160, show_side_image=Image("images/character/irina_side4.png", xalign=0.0, yalign=1.0))

define is_rstandard = Character('Irina', color="#f0a8ed", window_right_padding=160, show_side_image=Image("images/character/irina_side0.png", xalign=1.0, yalign=1.0))
define is_rmischief = Character('Irina', color="#f0a8ed", window_right_padding=160, show_side_image=Image("images/character/irina_side7.png", xalign=1.0, yalign=1.0))
define is_ractive = Character('Irina', color="#f0a8ed", window_right_padding=160, show_side_image=Image("images/character/irina_side2.png", xalign=1.0, yalign=1.0))
define is_rserious = Character('Irina', color="#f0a8ed", window_right_padding=160, show_side_image=Image("images/character/irina_side6.png", xalign=1.0, yalign=1.0))
define is_rblush = Character('Irina', color="#f0a8ed", window_right_padding=160, show_side_image=Image("images/character/irina_side5.png", xalign=1.0, yalign=1.0))

define ix = Character('Girl', color="#f0a8ed")
define i = Character('Irina', color="#f0a8ed")
define bt = Character('Trevor', color="#62ac5b")
define oo = Character('Oliver', color="#d72b2b")
#######################################################
#Chapter 3.x : Epilog

label epilog:
    scene bg graypub with fade
    $ renpy.block_rollback()
    $ save_name = "Chapter 3.x - Epilog"
    play music fate fadein 2.0
    $ renpy.music.set_volume(0.3, delay=0, channel=6)
    $ renpy.music.play('audio/sfx/pub_crowd.mp3', channel=6, loop=True, fadeout=0, synchro_start=False, fadein=2, tight=True, if_changed=False)
    
    "..."
    play sound pubdoor
    pause .5
    ix "Woah! What's this place?"
    oo "Magical, right?"
    oo "Trevie's doing his apprenticeship here."
    ix "Where is he? {w}Where is Trevie?"
    oo "Let's go to the bar and get our seats."
    "Sigh."
    ix "This place is awesome, brother!"
    oo "I always knew that this is your kind of place."
    
    show irina gstandard with dissolve
    ix "Oh! Oh! {w}There you are, Trevie!"
    b "I am the bartender here. {w}At least call me that when I am at the job."
    show irina gmischief with dissolve
    ix "Oh ho? Since when did my little Trevie learn how to backtalk?"
    show irina gstandard with dissolve
    ix "But anyways."
    show irina gactive with dissolve
    ix "How much did you pay those bullies to come to this place?"
    ix "It's like some sort of thieves' den, I'll tell ya!"
    show irina gstandard with dissolve
    b "Yeah yeah. {w}Calm down already, Irina."
    b "These are just regular guests, they kind of settled down when Master opened the pub."
    i "Who is this {i}Master{/i}?"
    b "He is the barkeeper of this place, an old war veteran."
    b "Might be the reason why we get those odd guests."
    b "Now, you both should head home for tonight. {w}You're hindering my work here."
    show irina gactive with dissolve
    with vpunch
    i "I won't."
    with vpunch
    i "I cannot!"
    show irina gstandard with dissolve
    i "Hey brother! {w}Tell Trevie he shall pour me some beer!"
    oo "Ask him yourself."
    show irina gmischief with dissolve
    i "Treeeeviiiie?"
    b "I can't, we're all minors here."
    show irina gstandard with dissolve
    i "Geez. {w}What a party pooper."
    b "And if you really insist on calling me anything other than bartender, at least call me {i}Trevor{/i}."
    show irina gactive with dissolve
    i "No."
    show irina gstandard with dissolve
    i "I will call you Trevie for the rest of my life. {w}It just fits."
    show irina gmischief with dissolve
    i "You want to be called bartender? {w}Then you've got to go through me first, little Trevie."
    
    scene black with fade
    centered "This girl...is so unreasonable." with dissolve
    
    scene bg graypub with fade
    play sound pubdoor
    pause .5
    show irina gstandard with dissolve
    i "Trevie~"
    
    scene black with fade
    centered "This girl..." with dissolve
    
    scene bg graypub with fade
    play sound pubdoor
    pause .5
    show irina gmischief with dissolve
    i "Oh, just look who I've found~"
    
    scene black with fade
    centered "This girl..." with dissolve
    
    scene bg graypub with fade
    play sound pubdoor
    pause .5
    show irina gactive with dissolve
    i "Trevie, Trevie, Trevie!!! \nI think I got the ultimate soda recipe!\nI swear it's gonna sell like hotcakes!"
    
    scene black with fade
    centered "This girl..." with dissolve
    
    scene bg graypub with fade
    $ renpy.pause(3.0, hard=True)
    scene black with fade
    $ renpy.pause(2.0, hard=True)
    $renpy.music.stop(channel=6, fadeout=5)
    scene bg graypub with fade
    $ renpy.pause(3.0, hard=True)
    scene black with fade
    $ renpy.pause(2.0, hard=True)
    scene bg graypub with fade
    $ renpy.pause(3.0, hard=True)
    scene black with fade
    $ renpy.pause(2.0, hard=True)
    scene bg graypub with fade
    $ renpy.pause(2.0, hard=True)
    
    play sound pubdoor
    scene bg pubnight
    stop music
    pause .5
    os_tired "C'mon, Heiden. Don't just stand at the entrance."
    hs_active "Uncle Old, I--"
    with vpunch
    hs_active "This place is {b}awesome{/b}!"
    os_tired "Yeah, yeah. I heard ya."
    
    show old funeral tired:
        xalign -0.5 yalign .5
        linear 2.0 xalign .5
    o "Heya, Bartender!"
    with vpunch
    hs_active "It's like we're amidst pirates, Uncle Old!"
    
    scene black with fade
    centered "{b}One-eyed Goppy{/b}\nI-Is this young lad perhaps milady's--?" with dissolve
    centered "{b}One-eyed Goppy{/b}\n*grin* {w}It's like she finally came back after all those years.." with dissolve
    centered "..."
    centered "{b}{color=#1d87da}Trevor{/color}{/b}\nThank you, Heiden." with dissolve
    centered "{b}{color=#1d87da}Trevor{/color}{/b}\nIt's really like a part of her that was dwelling inside you has finally found the way back to my pub." with dissolve
    
    $ renpy.pause(3.0, hard=True)
    show credit1 10:
        yalign .5 xalign .5
    with dissolve
    $ renpy.pause(2.0, hard=True)
    bt "In a pirates' den, heh?"
    $ renpy.pause(2.0, hard=True)
    hide credit1 10 with dissolve
    $ renpy.pause(3.0, hard=True)
    
    $persistent.extra_unlocked = True
    
    return
    
    
    
    
#######################################################
#Chapter x.x : Extras

label extras:
    $ save_name = "Chapter X - Extras"
    $ _game_menu_screen = None
    stop music
    show black
    play sound game_start
    $ renpy.pause(4.0, hard=True)
    play music bonus fadein 1.0
    $ renpy.block_rollback()
    centered "{b}Dweller of the Bonus Room{/b}\nWelcome to the Bonus Room."
    centered "{b}Dweller of the Bonus Room{/b}\nYou can unlock extras via the smartphone's {i}Password Operator{/i}."
    centered "{b}Dweller of the Bonus Room{/b}\nI will call those extras {i}bonuses{/i} from now on,\nhence why this is called the \"Bonus Room\"."
    
label extraroom:
    with fade
    call screen bonusroom

    $ click = _return
    
    if click == "no":
        centered "{b}Dweller of the Bonus Room{/b}\nThis bonus has yet to be unlocked."
        jump extraroom
    
    if click == "trevyes":
        centered "{b}Dweller of the Bonus Room{/b}\nAh, yes.\nThe \"Bonus Chapter\" it is."
        menu:
            "Start the Bonus Chapter":
                hide screen bonusroom
                jump trevpast
            "Return to the Bonus Room":
                jump extraroom
                
    if click == "credits":
        if persistent.trueend_unlocked == False:
            centered "{b}Dweller of the Bonus Room{/b}\n{b}Credit Version 1{/b} is currently being used."
        else:
            centered "{b}Dweller of the Bonus Room{/b}\n{b}Credit Version 2{/b} is currently being used."
        menu:
            "Use Credit Version 1":
                $persistent.trueend_unlocked = False
                centered "{b}Dweller of the Bonus Room{/b}\nWe shall use {b}Credit Version 1{/b} from now on."
                jump extraroom
            "Use Credit Version 2":
                $persistent.trueend_unlocked = True
                centered "{b}Dweller of the Bonus Room{/b}\nWe shall use {b}Credit Version 2{/b} from now on."
                jump extraroom
                
    if click == "delete":
        centered "{b}Dweller of the Bonus Room{/b}\nYou may not know what this does, but this option will essentially\n{b}Remove access to all bonus contents{/b} which is the Music Room, Bonus Chapter, Gallery and changing Credits."
        centered "{b}Dweller of the Bonus Room{/b}\nAre you sure you want to do that?"
        menu:
            "Yes, revoke my access to all bonus contents.":
                centered "{b}Dweller of the Bonus Room{/b}\nI'll ask you again. {w}Are you super super serious about this?"
                menu:
                    "Yeah, revoke my access already!":
                        centered "{b}Dweller of the Bonus Room{/b}\n*Sigh*{w} Okay, it's done.\n{w}You may regain access by inputting the corresponding passwords again via the smartphone's {i}Password Operator{/i}."
                        $persistent.musicroom_unlocked = False
                        $persistent.bonus_unlocked = False
                        $persistent.oldie_unlocked = False
                        $persistent.pritty_unlocked = False
                        $persistent.credit2_unlocked = False
                        jump extraroom
                        
                    "On second thought, let's not do that.":
                        centered "{b}Dweller of the Bonus Room{/b}\nPhew. {w}I am glad you reconsidered your choice."
                        jump extraroom
            "Actually no. I just misclicked.":
                centered "{b}Dweller of the Bonus Room{/b}\nOkay. {w}I did scare me for a little bit."
                jump extraroom
                    
                
                
#######################################################
#Chapter 4.x : Bonus Chapter

label trevpast:
    $_game_menu_screen = "save_screen"
    $ renpy.block_rollback()
    stop music fadeout 3.0
    $ renpy.pause(3.0, hard=True)
    
    scene bg pubnight with cr1_longBlack
    play music pub fadein 2.0
    $ renpy.pause(2.0, hard=True)
    bt "Urgh, Master sucks at cleaning the beer mugs."
    play sound wipe
    with hpunch
    bt "These stains will forever taint the glass if you leave them out to dry!"
    play sound wipe
    with hpunch
    bt "This master of mine, always too carefree to care."
    bt "And here I am, doing all his chores just because he's too busy being {b}not{/b} here."
    bt "A true slacker."
    play sound pubdoor
    pause .5
    i "Treeeeeviiiie~"
    bt "Goddamnit, another troublesome person has appeared."
    show irina serious with dissolve
    i "Trevie, Trevie, Trevie! {w}Lend me your bed for tonight, okay?"
    bt "I have so many questions right now.\n{w}Firstly, when did you come back? Did you run away from home again?\nThe pub's already closed. Can't you stay at your brother's place?"
    show irina standard with dissolve
    i "I'll answer only one question at the time, little Trevie. \n{w}surely I'll get a place to stay afterwards, right?"
    bt "I don't think I can-"
    show irina mischief with dissolve
    i "No. {w}Backtalk. "
    show irina standard
    extend "Okay?"
    bt "You're being as charmant as always, milady."
    i "Why, thank you!"
    show irina at twitchtwice
    i "One beer, pronto."
    bt "It's past working hours for this pub, dear guest."
    show irina serious with dissolve
    i "Oh my."
    show irina standard with dissolve
    i "But I don't care. {w}I want the beer anyways, Trevie."
    bt "*Sigh*"
    bt "But only because today's your birthday."
    show irina active with dissolve
    i "Oh my. {w}You remembered?"
    bt "You've been lying about your birthday everytime you visit this pub in order to get beer."
    bt "But now you're actually allowed to drink some."
    bt "...You could say this is the moment I've been waiting for."
    show irina standard with dissolve
    i "It feels like a private birthday party with only us two here."
    play sound beerpour
    bt "So what's the deal this time? {w}Did Old get on your nerves again?"
    show irina serious with dissolve
    i "That's only just the tip of the iceberg!"
    i "But the truth is, our parents back in the city are dragging me along to various marriage meetings as of late."
    bt "Sounds tough."
    with vpunch
    play sound glass
    extend " Here's the beer."
    show irina at twitchtwice
    i "Thanks, Trevie."
    show irina active with dissolve
    i "Wow, I am quite the adult now.{w} Don't you think so too, Trevie?"
    bt "I'd say you're still a child in mind."
    show irina mischief with dissolve
    i "Anyways."
    show irina serious with dissolve
    i "Just because I am the daughter of a highly respected family, the men are flaunting their interest in me."
    i "Yet they're so bad at hiding their ulterior motives. {w}Trying to buy themselves into the family, you know?"
    bt "Aren't you glad that there's such an interest in you? {w}Maybe you'll find your Prince Charming amongst them?"
    show irina mischief:
        linear 1.0 zoom 1.5 yalign .7
    pause 1.0
    play sound punch
    with hpunch
    pause 1.0
    show irina standard:
        linear 1.0 zoom 1.0 xalign .5 yalign .5
    pause 1.0
    i "I am sorry, I think I misheard that."
    bt "Ouch, no you didn't!"
    bt "But back to the topic, so why is your brother ignored in the family relations when he's the older one?"
    show irina standard with dissolve
    i "But you know my bro, he's pretty hopeless."
    i "Our grandfather out here took him in but that's mainly because he would have tarnished the family reputation if he stayed in the household for any longer."
    bt "Wow, that sounds pretty harsh on him. {w}So your brother has been basically pushed off to this remote town?"
    show irina at shivertwice
    i "Not at all. {w}He loves grandpa and is happy that he's free from all those shackles. {w}I'd say he's living his life free from worry."
    show irina serious with dissolve
    i "But now the burden's on me, you know?"
    show irina mischief with dissolve
    show irina at shivertwice
    i "Woah. Beer tastes so good. {w}Why didn't I know of such a simple pleasure before?"
    bt "Please don't become an alcoholic, okay? {w}\nIt would weight heavily on my conscience if it was me who pulled the trigger on your alcohol career."
    show irina standard with dissolve
    i "Join me for a drink, Trevie. {w}It's on me."
    bt "I can't, I am still a minor."
    bt "Besides, a bartender is not allowed to drink with his guests. \nIt's disrespectful to the art of bartending. \n{w}That's what Master always says."
    show irina mischief with dissolve
    i "Then let us break this logic one by one, shall we?" 
    i "You're a minor but right now you're in the presence of an adult. {w}\nWhich is me, of course."
    i "And your other point being that stuff about bartending? No no no! {w}\nI don't see a bartender infront of me, just my little Trevie."
    show irina standard with dissolve
    bt "Now you're being unreasonable again-"
    show irina serious with dissolve
    i "You let a poor maiden drink all by herself?{w} On her own birthday?"
    bt "*Sigh*"
    play sound beerpour
    bt "That's gonna stay a secret between us, okay?"
    show irina standard with dissolve
    i "That's the Trevie, I know."
    show irina mischief with dissolve
    i "Got some new stuff to blackmail my little Trevie with."
    bt "Please say these things after I drank my beer, okay?"
    bt "But seriously. {w}I'll just turn my back on this whole evening, it's beginning to give me headaches."
    with hpunch
    play sound glass
    bt "Cheers!"
    show irina standard with dissolve
    show irina at shivertwice
    i "Cheers!"
    show irina at twitchtwice
    play sound beerclank
    
    show irina mischief with dissolve
    i "Hiiyah, that hit's the spot."
    bt "Beuf... {w}It's definitely more bitter and stronger than I have thought."
    bt "Yeah, it definitely tastes the way it smells."
    bt "..."
    show irina standard with dissolve
    i "What are you thinking about, Trevie?"
    bt "I've been thinking about how my guests are able to gulp this garbage down their throats like it's nothing."
    bt "And some even dare to tip me for this?"
    bt "Heck, this isn't drinkable. {w}I prefer your soda over this."
    show irina mischief with dissolve
    i "Don't you worry, it might taste better after your fourth mug."
    bt "I hope you're not serious."
    show irina at twitchtwice
    i "You bet I am! {w}My party's just getting started!"
    stop music fadeout 2.0
    scene black with fade
    centered "Some time later..." with dissolve
    scene bg pubnight with fade
    play music togetherness fadein 1.0
    bt "Urgh."
    show irina drunk with dissolve
    i "And like that I've taken the next train back here to safety!"
    show irina saddrunk with dissolve
    i "But bro was like \"No way in hell do I get involved in your mess\" even though he's been using me as a scapegoat all this time!"
    show irina drunk with dissolve
    i "I'll tell ya! {w}I won't get shackled to some strange man! \n{w}My marriage is not a business decision! {w}True love prevails!"
    bt "Urgh. You're so noisy, Irina."
    show irina saddrunk with dissolve
    i "Oh dear. My little Trevie is totally gone now."
    bt "Urgh. Just.. {w}let me sleep, Irina."
    i "..."
    show irina blush with dissolve
    i "Say that again, Trevie."
    bt "Wha? {w}You're... {w} being noisy."
    show irina saddrunk with dissolve
    i "No, Trevie."
    show irina blush with dissolve
    i "Could you say my name again without the unimportant tidbits that you don't actually mean?"
    bt "Uhm, Irina?"
    show irina saddrunk with dissolve
    i "Again."
    bt "Irina."
    show irina drunk with dissolve
    i "Again."
    
    stop music fadeout 2.0
    scene black with cr1_longBlack
    bt "Irinah?"
    i "Don't stop."
    bt "Urgh, Irina."
    $ renpy.pause(1.0, hard=True)
    bt "Irina."
    $ renpy.pause(1.0, hard=True)
    bt "Iri.. na?"
    $ renpy.pause(2.0, hard=True)
    bt "Irina!"
    $ renpy.pause(1.0, hard=True)
    bt "..."
    $ renpy.pause(1.0, hard=True)
    bt "Uhm, Irina?"
    pause 1.0
    
    is_blush "What's the matter, Trevie?"
    bt "Why are you ... ?"
    is_serious "I felt cold so I had to wear something."
    bt "But you're in your underwear."
    is_blush "Psh."
    bt "...yeah.{w} Everything's slowly falling into place. {w}I think we really did it."
    bt "..."
    bt "I won't ask you for anything else but can I at least have my left arm back? {w}\nIt's totally numb."
    is_serious "Aww."
    is_mischief "Wait, let's do it like this."
    play sound fallinbed
    $ renpy.pause(1.0, hard=True)
    bt "Uhm, Irina?"
    is_rblush "What's the matter this time, Trevie?"
    bt "*Sigh*"
    bt "I feel like my left arm's still going to be usable tomorrow so there's that."
    is_rblush "I always wanted to try out the arm pillow, you know."
    is_rblush "I am not going to let this chance slip away."
    bt "There, you have my arms.\n{w}So how does it feel for you?"
    is_rserious "Uhm."
    is_rblush "Refreshing? {w}Reassuring? \n{w}Something about your warmth is making me feel content or so."
    is_rserious "It's hard to put into words."
    bt "..."
    is_rblush "Trevie, you're blushing."
    bt "No I am not."
    is_rblush "Sure you do. {w}Because I know I am."
    bt "How can you be so honest at a time like this?"
    stop music fadeout 2.0
    play music togetherness fadein 2.0
    is_rstandard "Trevie, do you know when a girl is at her happiest?"
    bt "Uhm, the day of her marriage? {w}You know, girls always watch those movie scenes on repeat."
    is_rserious "Hm, yeah. That's a moment in a girl's life that she'll never be able to forget."
    is_rstandard "But I didn't mean that."
    is_rstandard "If you think about marriage, I'd think about the whole organisation mess and the huge ordeal of keeping it in order."
    is_rserious "It's an important day indeed but quite the hassle for the poor girl, I think."
    bt "Then how about being confessed to by her biggest crush? {w}A feeling that makes your heart explode?"
    is_rserious "I think it's more of a momentarily kind of feeling."
    bt "Then what's your take on this?"
    is_rserious "Truth be told, I don't really know it either."
    bt "Then why did you ask?"
    is_rstandard "Psh, Trevie. {w}I don't know it for sure but I always had that one hunch."
    bt "..."
    bt "Consider me interested. {w}Tell me about that hunch."
    is_rmischief "Is this an interrogation, Trevie?"
    bt "...Sorry."
    bt "Please tell me more about that hunch of yours, Irina."
    is_rstandard "Much better."
    is_rblush "I think the girl is at her happiest after coupling with her beloved person."
    bt "Woah."
    is_rserious "Hear me out, will'ya?"
    bt "..."
    is_rblush "I think about the feeling of freedom, {w}while being naked, \n{w}with no secrets to hide from another..."
    is_rblush "Just knowing that your existence is a blessing to him \n{w}and his existence in turn is a blessing to you as well."
    is_rblush "Without the fakeness of the outside world."
    is_rblush "This is poetry, it's this kind of romance that girls like me are looking for in life."
    bt "..."
    is_rserious "Trevie?"
    bt "I am speechless."
    is_rblush "It's fine, though. {w}It's plain to see that your actual response is beating in union with your heartbeat."
    bt "Yeah, your speech really caught me off guard."
    is_rmischief "Never underestimate girls, my dear little Trevie."
    bt "I got it, I got it."
    is_rblush "You've got a lot to learn, Trevie."
    bt "..."
    bt "So who brought me upstairs? {w}I'd say I am on the heavier side."
    is_rstandard "You called him \"Master\"? He brought you up here."
    is_rstandard "He's a cool old man, he even let me stay here."
    is_rmischief "You cried out my name multiple times while we dragged you to your bed."
    is_rmischief "So he even told me to have some fun while I'm at it."
    bt "You being serious?"
    is_rblush "You dummy, that was a joke."
    bt "Just look at me, it didn't sound like a mere joke to me."
    is_rmischief "Let's just say you don't need to give me any presents for my birthday."
    bt "And the booze party?"
    is_rserious "Only the interlude to this of course, what else?"
    bt "...Irina."
    is_rserious "Hey! It turned out fine, right?"
    bt "What about the condom?"
    is_rblush "What are you spouting so suddenly?"
    bt "Do you remember seeing me take one out?"
    is_rserious "Why are you so nonchalant about this deal?"
    bt "Well. It's pretty important in this case, right?"
    is_rblush "I'd say I am pretty impressed if you were actually able to pull that on while being half conscious."
    bt "..."
    is_rmischief "You're so uptight, Trevie! {w}This is still my birthday party!"
    bt "Yeah, well. {w}Uhm, and {w}did our \"thing\" go well?"
    is_rserious "Hm."
    is_rblush "People say that complications and completions are two sides of the same coin! {w}I guess?"
    bt "I am not sure what to make out of this."
    is_rblush "Well, you did start hugging me in your sleep all of a sudden."
    is_rblush "We were left with no other choice than to improvise a little bit."
    bt "Wait, so it's my fault? {w}And in my defense: I hug things in my sleep so sorry for doing things that are out of my control."
    is_rserious "If only you were half as honest when you're awake."
    
    stop music fadeout 5.0
    bt "Hm. {w}Let's go to sleep."
    is_rserious "..."
    bt "Uhm, Irina."
    is_rstandard "Just say it."
    bt "Actually, you can use my left arm. {w}I am right-handed, after all. {w}\nI'd rather have my right arm free for tonight than my left."
    with vpunch
    is_rmischief "Geez."
    play sound fallinbed
    bt "Well I am sorry! {w}It's the first time I have someone using my arms as a pillow."
    is_mischief "Hopefully I am the first {b}and{/b} last person to do this."
    bt "Well, for the time being anyways."
    is_standard "You're dull, dense and boring."
    is_mischief "I bet I am the only one who sees anything in such a dull, dense and boring guy like you."
    bt "Hey now, I try my best not to let it show {w}but even someone like me has feelings."
    is_blush "Well, I hope now you know how I feel about you, right?"
    bt "Yeah, I got your feelings alright."
    is_mischief "Oh my, what an unromantic Trevie we have here."
    with hpunch
    bt "You can stop pinching my arm, my dear."
    
    is_serious "..."
    bt "..."
    play music fate fadein 4.0
    is_serious "Hey Trevie. {w}Can you look after my bro for me?"
    bt "What do you mean? {w}Isn't that what I am doing this whole time?"
    is_serious "Yes, you're right. But I mean it. {w}Taking care of him."
    is_serious "You see, the marriage meetings I've told you about."
    bt "Have you made up your mind?"
    is_standard "Yeah, I guess I have."
    is_standard "I'll be going away for awhile. {w}Away from home. {w}Also away from you guys here."
    bt "Can't you {w}like {w}just stay here with us? {w}I bet your brother and grandfather don't mind it either."
    is_standard "Thank you, I know they'll accept me with open arms."
    is_serious "But grandfather's old and burdening him for a longer period of time is just plain bad for his health."
    is_serious "He doesn't like troubles so much and wants to live his last years in peace."
    bt "Yeah, I'd want my days to be peaceful too."
    is_standard "Yeah."
    is_serious "That's why I can't stay here."
    bt "That's not what I meant, Irina."
    is_standard "I know."
    is_serious "But dragging you guys into this is not my intention, too."
    is_serious "I don't want quarrels between my parents and my grandfather."
    is_mischief "But I don't want to get engaged, too."
    bt "So what's the plan?"
    is_standard "Out of the town and out of the city. {w}A good friend of mine is providing me some place to live."
    bt "A guy?"
    is_blush "You getting jealous?"
    is_standard "But no. She's my best friend so I know I can trust her on this."
    is_active "It's like something straight out of runaway movies."
    bt "What about money? {w}What did you plan out so far? {w}If you ask me, you're not the type of person who has everything going according to plan."
    is_blush "Oh my, you may be right about that."
    is_mischief "But I am the type who can see things though."
    is_standard "Don't worry, it's going to be fine. {w}I give it some years. \n{w}When the coast is clear, I am swinging back to the pub like nothing's changed."
    bt "That's quite the plan you got there."
    bt "But if it's about money, I can help. {w}At least I think I can."
    bt "Or rather, I'll tell my pen pal to act as a go-between guy for that."
    is_standard "You will?"
    is_standard "That might make things easier for me."
    bt "Won't you be lonely? {w}Maybe I should come too."
    is_mischief "I'd say you're not ready to live in the city, you bumpkin."
    bt "So you treat my town as a village, too? {w}I hear your brother saying that a lot."
    is_standard "Psh, Trevie."
    is_serious "I need you to take care of my brother and grandfather while I am gone."
    is_serious "Especially if you guys are the first place to go for my parents when they realize that I am gone."
    is_standard "Keep this place safe for me so I can return to it."
    bt "This town won't change, I'll make sure of it."
    is_standard "Yeah, my little Trevie can do it. {w}I know you can."
    bt "Please keep me updated, will you?"
    is_standard "I will, and I will become happy."
    is_blush "And even happier once I am back."
    bt "Just don't keep us waiting for too long. {w}Or we'll come and drag you back ourselves."
    is_mischief "Oh my. Has my little Trevie become a slight bit manlier?"
    is_blush "..."
    is_standard "Thank you, Trevie. {w}I am really happy right now."
    bt "..."
    
    stop music fadeout 2.0
    $ renpy.pause(2.0, hard=True)
    play music watch
    centered "I've had this strange premonition somehow." with dissolve
    centered "I felt like I was going to lose my grasp on her when morning came." with dissolve
    centered "I felt sad knowing that and began to tighten my embrace." with dissolve
    centered "Tighten my embrace as if I was trying to prevent the hand of the clock from turning." with dissolve
    centered "She must felt it, too. {w}My embrace might hurt her but despite that she didn't sound a single word of complaint." with dissolve
    centered "We laid on my bed while the clock ticked away continuously." with dissolve
    centered "It ticked,{w} ticked,{w} ticked {w}and ticked. {w}It ticked me off." with dissolve
    centered "I wanted it to stop, or slow down, or die." with dissolve
    centered "I wanted the power to stop time, or stop fate itself." with dissolve
    centered "But here I laid, resolving myself to do the only thing I was capable of." with dissolve
    centered "..." with dissolve
    
    $ renpy.pause(2.0, hard=True)
    $ heidenname = "Heiden "
    stop music
    hs_standard "How do you want your eggs?"
    "..."
    play music at_home
    scene bg livingroom with pixellate
    show heiden kitchen standard with dissolve
    h "Barty?"
    "..."
    show heiden tired with dissolve
    h "Heheyyy."
    b "W-what?"
    h "Your eggs. {w}Sunny-side up or what?"
    b "What's your deal, boy?"
    h "My deal?"
    show heiden standard with dissolve
    h "Lately you've been spacing out occasionally, Barty."
    h "Is the pub keeping you up late?"
    b "Nah, that's not it."
    b "I want three eggs sunny-side up."
    show heiden:
        linear 2.0 xalign -0.5
    b "And bring me a coffee while you're at it. {w}Make it black, please."
    hs_tired "Then make it yourself with Uncle's coffee brewer."
    hs_tired "I have no idea how that thing works."
    b "*Sigh* {w}Watch and learn, Heiden. {w}I'll show you how to brew the best coffee with even the worst coffee brewer."
    hs_tired "I am not too thrilled about learning how that machine works. Coffee tastes bad anyways."
    b "Geez, just give it a try already."
    
    show old funeral tired with dissolve
    hs_standard "Man, what's with you today?"
    b "You'll never be even half of a real man if you miss out on this valuable coffee brewing technique."
    show old at shivertwice
    hs_active "What's that? {w}You think you can bail out on this one after spouting that bull?"
    b "Heh. {w}This kid really thinks he's hot shit even though he can't even brew me a simple coffee."
    hs_active "You dum dum! {w}Coffee in its simplicity is just dirt and water, mixed with a grain of salt and sugar."
    $oldname = "Uncle Old"
    o "Urgh, it's so early in the morning."
    show old funeral troubled with dissolve
    show old:
        linear 2.0 xalign .1
    o "Also no swearing in my house, am I clear?"
    with hpunch
    "Heiden & Barty" "What are you? {w}My mom?"
    show old funeral tired with dissolve
    show old at twitchtwice
    o "I don't know if I can deal with both of you at the same time, sometimes."
    b "Hey Heiden."
    hs_tired "What's the matter? {w}I am busy making {i}your{/i} eggs."
    show old funeral normal with dissolve
    show irina standard:
        xalign .9 yalign .5 alpha .2
    with dissolve
    b "You may call me Trevie now, if you like. {w}I think I'd rather not be called bartender when I am not working."
    hs_standard "..."
    show irina mischief:
        alpha .2 xalign .9
    with dissolve
    hs_tired "Nah, Barty fits you to a tee."
    b "Wha? {w}You little."
    show irina standard:
        xalign .9 yalign .5 alpha .2
    with dissolve
    with hpunch
    hs_tired "Ahaha! {w}D-don't tickle me while I am at the stove!"    
    o "Heh. Sister, I guess you really don't have to worry about your boy here."
    show irina blush:
        linear 1.0 xalign .7 alpha .2 
    with dissolve
    o "I mean, just look at them."
    show irina standard:
        xalign .7 alpha .2
    with dissolve
    hs_tired "Uncle. {w}Help!"
    show old funeral tired with dissolve
    show old:
        linear 2.0 xalign -0.5
    o "Oh well, time to fix my breakfast in the middle of this mess."
    show irina standard:
        linear 2.0 xalign 0.1 alpha .2
    with dissolve
    b "Hey Old. {w}Hands off my eggs, will you?"
    os_tired "Urgh."
    show irina mischief with dissolve
    hs_standard "You can have the burnt ones over there."
    hs_tired "You can thank Barty for that."
    os_tired "Thank you, Barty."
    show irina:
        linear 2.0 xalign -0.5 alpha 0.0
    with dissolve
    b "Ack! {w}Get off my back."
    "Everyone minus Bartender" "Ha ha ha!"
    
    $set_credits = True
    
    stop music fadeout 4.0
    scene black with cr1_longBlack
    $ renpy.pause(3.0, hard=True)
    show credit1 10:
        yalign .5 xalign .5
    with dissolve
    $ renpy.pause(2.0, hard=True)
    $ renpy.pause(2.0, hard=True)
    hide credit1 10 with dissolve
    $ renpy.pause(3.0, hard=True)
    
    if persistent.trueend_unlocked == False:
        $persistent.trueend_unlocked = True
        centered "{b}Dweller of the Bonus Room{/b}\nOh my, you just altered the credits a little bit. {w}\nWhat, you didn't know that? {w}I'd say you're welcome to watch it again."
    $ renpy.pause(1.0, hard=True)
    return