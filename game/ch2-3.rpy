#######################################################
#Chapter 2.5a : Home A

label homeA: #Get home during afternoon WITH a cake
    $ save_name = "Chapter 2.5a - The Disappearance of the Cake"
    $now_home = True
    h "Time to head back home for now."
    stop music fadeout 2.0
    stop sound
    scene bg livingroom with fade
    show tooltip_background
    show expression Text(_("Afternoon"), size=40, color="#FD8204", yalign=0.008, xalign=1.0, drop_shadow=(2, 2)) as text
    play music at_home fadein 2.0
    
    $ renpy.block_rollback()
    "The rustling of the plastic wrap announces my arrival."
    "Wherever [nickname_old] Old went, he's at least not occupying the living room."
    "Did he perhaps retreat to his own room?"
    "If that's the case then I'll have to come to a swift decision before facing him."
    with vpunch
    "I'll put the cake on the table, it's better to have both hands free in order to sort my thoughts."
    "I'll either destroy the cake all by myself or I'll let [nickname_old] get a slice of the cake, in the truest of sense."
    "I mean, it's to preserve the efforts of Lisette but getting the cake for [nickname_old] Old was like the whole idea about visiting the pub."
    show old funeral tired with dissolve
    "I feel torn apart by my choices."
    show old at twitchtwice
    "Maybe I've been taking things to far."
    "Maybe I should just come up straight and say that the cake is a present from me to him?"
    show old:
        linear 1.0 xalign .2 yalign .5
    "Oh wait, that's not what {i}come up straight{/i} means."
    o "Oh, a cake?"
    "But I feel like if I tell him the truth that the cake is from the pub, he'll have something to unnecessarily tease Lisette with."
    "And to be honest, [nickname_old] Old is surely someone who'd do something like that."
    show old at shivertwice
    "But on the other hand, why would I buy him a cake for no reason?"
    "Money is important, especially for me as a kid."
    "Kids like me don't work, I only get allowance or some christmas bonus."
    o "God, this is great."
    show old funeral normal at twitchtwice
    "I haven't really thought about it but if [nickname_old] Old doesn't know of the cake... {w}nothing will happen, right?"
    "It's quite plausible if you think about it."
    o "I don't know where you got that cake from but it's gone now, it just happened."
    "I went to the pub, right? {w}But there was no cake."
    "The cake would be a lie then, right? {w}I came back with nothing because there was no cake to begin with."
    show old funeral troubled
    o "Uhm this was your cake, right?"
    o "I just ate away your cake, right?"
    "Maybe this lie would become reality if I truly meant it."
    "Something like a white lie that would benefit both Lisette and [nickname_old] Old."
    "I mean, it's clear that both will lock horns with each other over some stupid cake."
    show old funeral tired
    o "Heiden, dear. {w}Please notice my existence."
    "But it might be revealed as a dirty lie if the cake's spotted somehow."
    "The cake shall disappear! {w}It must! {w}\nB-but I am too full to eat another helping."
    "How about... {w}throwing it out?"
    o "Heiden, I-"
    show old funeral normal
    o "I'll get a new cake for you!"
    show old:
        linear .3 xalign -0.5
    with hpunch
    "NO! {w}I refuse to throw the cake away! Even hiding it underground is a disrespectful act towards Lisette, infact even worse than outright giving it to [nickname_old] Old."
    "I think in this case hiding it in my room may be a valid choice."
    stop music fadeout 1.0
    "Wait. {w}The cake."
    play sound shock
    "It's gone."
    "But it was there."
    "Or not?"
    "Wait a moment, this predicament that I am currently in."
    "It's "
    play sound heaven
    extend "PERFECT."
    play music at_home fadein 1.0
    "I don't know where the cake is, therefore the cake was never mine to begin with."
    "If the cake is ever going to be found, I'll just vehemently refuse its connection to me."
    "Heck, what's with me?"
    "I was panicking over something as small as this, cowering like I was hiding a bad grade from school."
    "I should really grow up."
    "But hey, this plan."
    
    scene black with fade
    centered "Yup. {w}This sounds so plausible, it might just work out fine."
    $ renpy.pause(2.0, hard=True)
    centered "Some time later..." with dissolve
    
    scene bg livingroom with fade
    show tooltip_background
    show expression Text(_("Evening"), size=40, color="#ba0b0b", yalign=0.008, xalign=0.98, drop_shadow=(2, 2)) as text
    
    show old funeral tired:
        xalign -0.5
        linear .3 xalign .2
    o "I DID IT, Heiden!"
    h "What is it?"
    o "Aw, come on. {w} Lend me your eyes, avert them from the television."
    show old:
        linear .5 xalign .5
    h "Okay, I see you. I see you fine from here, [nickname_old]."
    o "Cake, here!"
    hide old with dissolve
    h "There's no cake. {w}I don't know of any cake."
    os_tired "Uhm, okay?"
    os_troubled "I'll just leave the cake in the refrigerator, okay?"
    hide screen gui_tooltip
    
    show black with fade
    os_tired "(I guess I'll leave that poor buddy alone for now.)"
    os_tired "(Probably has to come to terms with the current situation.)"
    os_tired "(But I couldn't help it. {w}The cake was so good.)"
    os_tired "(Sorry Heiden..)"
    $ renpy.pause(2.0, hard=True)
    centered "An uneventful afternoon passes..."
    
    scene bg livingroom
    $progression += 1
    
    jump freetime4
    
#######################################################
#Chapter 2.5b : Home B

label homeB: #Get home during afternoon WITHOUT a cake / Stay at home from noon til afternoon
    $ save_name = "Chapter 2.5b - Thunderato, the Bloody"
    $now_home = True
    h "Time to stay at home, I guess."
    stop music fadeout 2.0
    stop sound
    scene bg livingroom with fade
    show tooltip_background
    show expression Text(_("Afternoon"), size=40, color="#FD8204", yalign=0.008, xalign=1.0, drop_shadow=(2, 2)) as text
    play music at_home fadein 2.0
    
    $ renpy.block_rollback()
    "Well, yeah. {w}What now?"
    show bg livingroom:
        xalign 0.5
        linear 2.0 xalign 0.0
        linear 1.0 xalign 1.0
    "I glance around the living room to spot the television."
    "It is unoccupied, the sofa as well."
    "My uncle? {w}Nowhere to be seen."
    show tv off with fade
    "Let's check the schedule for the currently running TV shows."
    "{b}Black Hawt Clown - The sinister smiles\nJason Brown - Ultimate Rum\nSuplex Models - We'll squeeze your head and other head, too\nThunderato XIV\nLesley's Life - My secret love for salty popcorn{/b}"
    "Wait, could it be?"
    with hpunch
    "THUNDERATO IS SHOWING RIGHT NOW."
    play sound remote
    "I grab the TV remote to switch the television on, in a single and swift motion like the remote itself is just an extension of my body."
    show tv ch with fade
    play music thunderato fadeout 2.0 fadein 2.0
    "I stare at the television as the screen slowly flickers to a very familiar image of a green hero with red spiky hair."
    hs_active "Oh, yes! {w}It's him!"
    os_normal "Who's that?"
    with vpunch
    hs_standard "Woah! {w}Where'd you coming from, [nickname_old] Old?"
    os_wink "Just heard the TV so I came to check."
    os_normal "So what'ya watching?"
    hs_standard "You never heard of Thunderato XIV?"
    hs_active "He's like, super cool and beats baddies with his super powers."
    hs_standard "He also has a bush dog as his companion, I really hope they'll show him during this episode."
    hs_active "The bush dog is literally carrying the show right now, totally overpowered."
    os_normal "Well, to be honest. {w}This thunder guy looks like a baddie himself, you sure you want to root for him?"
    hs_tired "Geez, what's with you? {w}Look how determined he looks, there's no way that he's a baddie!"
    hs_standard "Oh, they're showing his enemy!"
    show tv enemy with fade
    os_tired "Okay, these fellas look like they're totally innocent."
    hs_tired "I always knew you were weird but that was totally whack."
    hs_tired "Totally embarrassing to even {i}think{/i} that this army of imminent black doom could possibly be good guys."
    os_normal "Don't think so, not in the least."
    show tv ch with fade
    hs_standard "Oh no, this is gonna be a hard fight for Thunderato..."
    os_troubled "Well, I gotta admit, he's keeping it up. {w}But now he is totally surrounded by those goons."
    os_normal "Oh, I see something in the distance. {w}Who could that be?"
    hs_active "Woah! It's him! {w}His partner arrived at the very last second!"
    show tv dog with fade
    hs_active "It's Van Ertal, the bush dog!"
    os_normal "It's getting sillier by the second."
    os_normal "This dog has a more human name than the hero himself."
    os_normal "And just look at it, it's totally sad. It's like he's going to cry at any moment."
    hs_tired "Oh gosh, just you be quiet!"
    hs_active "He always looks like that. {w}Crying? {w}\nThe only time he is allowed to cry is when he's bathed in the blood of his enemies!"
    hs_active "Get them, Van Ertal!"
    os_normal "Who's actually in charge for the unfortunate choice of names?"
    hs_active "Who cares? Look at the bush dog! {w}He's decimating his enemies left and right!"
    os_tired "Uhm, okay."
    show expression Text(_("Evening"), size=40, color="#ba0b0b", yalign=0.008, xalign=0.98, drop_shadow=(2, 2)) as text
    show tv enemy_defeated with fade
    os_normal "There's something incredibly wrong about this turn of events."
    os_normal "Is this show even appropriate for kids?"
    os_normal "I mean, is this even legal what they're showing on screen?"
    hs_active "VICTORY!"
    hs_active "THE GOOD GUYS EMERGE VICTORIOUS ONCE AGAIN."
    os_normal "I am clearly behind the times."
    hide screen gui_tooltip
    stop music fadeout 3.0
    scene black with fade
    centered "A rather eventful afternoon passes..."
    
    $progression += 1

    jump freetime4
    
    
#######################################################
#Chapter 2.5c : Park Again

label park2:
    $ save_name = "Chapter 2.5c - The Park Again"
    scene bg park with fade
    play sound playground loop
    stop music fadeout 2.0
    play music prittner fadein 2.0
    play music new_morning fadein 2.0
    show tooltip_background
    show expression Text(_("Afternoon"), size=40, color="#FD8204", yalign=0.008, xalign=1.0, drop_shadow=(2, 2)) as text
    
    $meeting_prittner = True
    "Maybe it's because I am doubtful after meeting Barty."
    "Doubtful that everything is apparently as fine as he claims it to be."
    "I've found myself wandering back to the park even though I have no intention of playing around."
    "Instead I feel myself strangely drawn to a certain spot of the park... {w}\ndrawn towards the swing set that was currently occupied by an grown person to be exact."
    h "Hey! {w}You!"
    show prittner stranger:
        yalign .5 xalign .8
    with dissolve
    "I gaze upon the man on the swing, his appearance as tired as I remember it."
    show prittner stranger:
        linear 3.0 xalign .5
    "He is turning his head ever so slowly towards my sound but as he do, I slowly piece together the situation."
    "He has exchanged his wrinkly suit with a wrinkly mantle and has no battered suitcase on him."
    "But everything else fits. {w}Those droopy eyes completed with his usual moody expression, it fits." 
    h "You're Mr. Spooky from the train!"
    show prittner:
        xalign .5 yalign .5
    with fade
    px "The hell? {w}It's the noisy brat from the train."
    h "That's not quite the rosy reunion that I always see on television."
    px "I won't treat you friendly with that choice of nickname."
    h "But it fits."
    px "No it doesn't."
    "Not even five minutes have passed and we're already at a stalemate."
    "Mr. Spooky isn't quite cooperative, I say."
    px "Whatever, this isn't the right time for little kids like you to play around."
    h "But at least it's the right location, right? {w}You're even occupying a swing."
    px "This swing is yours {w}when the daylight's out."
    px "Other than that, we adults get to play with it when it's slowly becoming dark like right now."
    h "And this just further cements your title as Mr. Spooky, the one who haunts good kids at night."
    px "You will never let it go for a second, right?"
    px "Fact is that you gotta do what adults tell you to. {w}You can consider yourself haunted if you don't."
    h "You're such a killjoy when you talk like this."
    h "You sound exactly like Barty."
    px "Oh, you already became aquainted with this town's bartender?"
    h "What? {w}Does that mean you got your stuffy attitude from him?"
    px "Enough with that babble. {w}But for you to know him is quite hilarious indeed!"
    "The worn man who never cracks a smile has finally revealed the bits of a cracked laughter albeit for unknown reasons."
    h "So what's funny about Barty?"
    px "No, it's okay! {w}Perhaps I have expressed my joy with the wrong words."
    with vpunch
    show prittner at twitchtwice
    px "It is just pure {i}irony{/i}. Call it {i}fate{/i} if you will."
    px "Or maybe a sign from the heavens? {w}Both a punishment and a gratification."
    with vpunch
    show prittner at twitchtwice
    px "I can't find the right words, ha ha ha!"
    stop sound fadeout 2.0
    "His hysterical laughter brings unwanted attention as the few kids who are on their way home bestow us with their nervous glances."
    h "Your laughter, your words, they don't make sense."
    h "Are you okay, Mister?"
    "My words may have reached his ears because his laughter has come to an abrupt stop and that is even more strange than him suddenly bursting out laughing."
    px "Okay? {w}Yeah, I really think that I am actually feeling okay for once."
    px "I am sorry to have startled you, this is quite unlike me."
    h "It's okay, Mister. {w}If I had the choice, I would rather take a maniacal laughing mister than a depressive spooky mister."
    px "Heh, you and your pesky words. {w}But I'll take them for once."
    hide prittner with moveoutright
    "With one dash, his body jumps away from the swing and lands himself right before me."
    "He deliberately lowers his body to reach my eye height."
    show prittner:
        xalign .5 zoom 2.0 yalign .2
    with dissolve
    px "I also know the bartender. {w}We are sometimes friends, sometimes not."
    px "It's a strange relationship but I do frequent his pub so you and me are bound to come across each other again."
    show prittner:
        linear 1.0 xalign .5 zoom 1.0 yalign .5
    px "I'll be going now so you better behave in the presence of your relatives."
    h "Yeah, but I think I behave better than my uncle though."
    px "It's not just your uncle."
    h "?"
    p "The name's Prittner, see you."
    hide prittner with fade
    h "Gone with the wind."
    "And I so badly wanted to get back at him for his selfishness yesterday."
    "But if he's speaking the truth, a reunion at the pub is a possibility."
    "It's strange how everything's connected to the pub."
    h "..."
    h "Well, whatever. {w}It's getting dark so I better head back home."
    hide screen gui_tooltip
    
    $progression += 1
    
    jump freetime4


#######################################################
#Chapter 2.6 : Evening

label freetime4:
    $ save_name = "Chapter 2.6 - Evening"
    $now_home = True
    stop music fadeout 2.0
    stop sound
    scene bg livingroom with fade
    show tooltip_background
    show expression Text(_("Evening"), size=40, color="#ba0b0b", yalign=0.008, xalign=0.98, drop_shadow=(2, 2)) as text
    play music at_home fadein 2.0
    
    $final_check = False
    
    show old funeral normal with dissolve
    o "Hey Heiden, you're here."
    h "We are going to the pub now, Uncle?"
    show old funeral wink with dissolve
    o "Yup, that's right."
    show old funeral normal
    h "Are you fine now? {w}You did look pretty awful this morning."
    show old funeral wink with dissolve
    o "No need to worry, Barty's medicine always kicks me right back into my working status."
    h "Always?"
    "I can only imagine what it's like with Uncle Old and his daily mishaps."
    show old funeral normal with dissolve
    o "I'll be waiting outside, Heiden."
    o "Just get ready and meet me outside."
    hide old with dissolve
    "I have only been here since yesterday but going to the pub every evening really feels like something I've been doing for several years now."
    "It's this strange kind of naturalness. {w}Maybe the ordinary life here agrees with me more than I have initially thought."
    "I can't seem to shake off the eagerness of seeing all those precious people that I've become friends with."
    "It's not even restricted to the rough but endearing regulars of the pub."
    
    if meeting_liz >= 1:
        "Like Lisette, who is also working at the café/pub/whatever it is."
    if meeting_prittner == True:
        "Like Mister Prittner, who might also come to the pub tonight."
        
    "But either way, let's get ready for another fun filled evening with everyone!"
    
label freetime41:
    if final_check == True:
        scene livingroom with fade
        show tooltip_background
        show expression Text(_("Evening"), size=40, color="#ba0b0b", yalign=0.008, xalign=0.98, drop_shadow=(2, 2)) as text
        "Anything else I need to do before we head out to the pub?"
        
    window hide
    show smartphone map2 at pullup
    $ renpy.pause(1.5, hard=True)
    call screen true_landkarte

    $ click = _return
        
    if click == "pw":
        jump pw_input
        
    if click == "pp":
        jump pingpong_play
    
    if click == "final":
        pass
        
    show smartphone map2 at pullout
    $ renpy.pause(1.5, hard=True)
    hide smartphone map2
    $ renpy.block_rollback()

    h "Let's get going to the {a=final_desc}pub{/a}! We don't want to keep everyone waiting, right?"
    menu:
        "Yes!":
            stop music fadeout 2.0
            jump finalpub
        "Wait a moment.":
            $final_check = True
            jump freetime41
    return
    
    
    
    
#######################################################
#Chapter 2.7 : Final March to the Pub (END)

label finalpub:
    scene bg wayhome2night with fade
    play music evening fadein 3.0
    hide screen gui_tooltip
    
    $ save_name = "Chapter 2.7 - Final March to the Pub"
    "The evenings are so peaceful here."
    "It's not comparable to where I lived, everyday life was kind of hectic and noisy in the city."
    "And sometimes even dangerous based on the suburbs."
    "Which makes me wonder how Mrs. Becky and her family are doing?"
    "I am feeling kind of nostalgic even though I've spoken to her just two days ago."
    "I mean, she sounded really nervous about sending me off all by myself."
    "The best thing I could do now is to write her letters. {w}\nYeah, letters are a great idea!"
    os_tired "Woah, I am kinda feeling wobbly."
    h "Hang in there, Uncle!"
    if nickname_old == "Mister":
        os_normal "Since when are you calling me \"Uncle\" instead of \"Mister\"?"
        h "You don't like it? {w}You can go back to being a mister, if you like."
        $ oldname = "Uncle Old"
        os_tired "No, by all means no."
        os_wink "Being called uncle is the family feel that I've missed."
        os_normal "And thanks for the encouragement, I'll keep myself together from now on."
    else:
        os_tired "Yeah, let's do this."
    
    
#######################################################
#Chapter 2.8 : Living the Publife (END)

    scene black with fade
    stop music fadeout 2.0
    play sound pubdoor
    $progression += 1
    $ save_name = "Chapter 2.8 - Living the Publife"
    centered "{color=#1d87da}Here. I'll even hold the door for you, Uncle.{/color}"
    centered "{color=#d72b2b}*sniff* What a fine boy I have.{/color}"
    centered "{color=#1d87da}Just don't go crying near my vicinity.{/color}"
    centered "{color=#d72b2b}I'll try, I'll try.{/color}"
    
    play music pub fadein 2.0
    $ renpy.music.play('audio/sfx/pub_crowd.mp3', channel=6, loop=True, fadeout=0, synchro_start=False, fadein=2, tight=True, if_changed=False)
    scene bg pubnight with pixellate
    
    "Yeah, this is the place."
    "The Big Jackal" "Oh, the boy's here!"
    "The Walking Triceps" "Heya Heiden! {w}Care to see me flex again?"
    h "'Sup guys! {w}Let me just say hi to Barty!"
    "One-eyed Goppy" "*grin*"
    h "Hey there, Goppy!"
    with hpunch
    "I slowly come over to Goppy to shake his hands."
    "He's an old guy with a pretty terrible eyesight but he is still able to tell the people apart."
    "His eyes are actually both intact but he is called \"One-eyed\" because he always squints with one eye in order to see something clearly."
    with hpunch
    "A nice old guy who never actually loses a word, sadly."
    "But seeing him smile when I'm coming over is much more worth than extending a warm welcome."
    with hpunch
    "At least it's the case with him."
    h "Uhm, you can stop shaking my hand now Goppy."
    "One-eyed Goppy" "*grin*"
    "Oh well."
    
    show barte normal lookaway:
        yalign .5 xalign .9
    show old funeral normal:
        yalign .5 xalign .1
    with fade
    o "He's made friends with the entire pub in just one day, how ridiculous is that?"
    show barte normal standard with dissolve
    b "Boy's got a talent, that's for sure."
    show barte normal lookaway with dissolve
    b "Earnesty, innocence"
    show barte normal smug with dissolve
    extend " and sometimes being pesky as well."
    show barte normal lookaway with dissolve
    b "I'd say, he's going to make friends at school pretty easy."
    b "Speaking of which, did you look through the documents that I've handed to you with the medicine?"
    show old funeral wink with dissolve
    o "It's fine, I did some calls in the afternoon."
    show barte normal lookaway with dissolve
    b "That's okay then."
    show lisette bstandard behind barte:
        xalign .9 yalign .5
    with dissolve
    if meeting_liz == 0:
        lx "Sorry Boss! {w}I'm coming through so step aside, please!"
    else:
        l "Sorry Boss! {w}I'm coming through so step aside, please!"
    show barte normal surprised with dissolve
    show barte:
        linear .5 xalign 1.0
    show lisette bserious:
        linear .5 xalign .5
    if meeting_liz == 0:    
        lx "Geez, what are you guys doing!"
        show barte normal lookaway
        show old funeral normal
        lx "You're blocking the entire traffic!"
        lx "Make way! Make way!"
    else:
        l "Geez, what are you guys doing!"
        show barte normal lookaway
        show old funeral normal
        l "You're blocking the entire traffic!"
        l "Make way! Make way!"
    show old:
        linear .5 xalign -0.2
    show lisette:
        linear .5 xalign -0.5
    pause 0.5
    show old:
        linear .5 xalign .1
    show barte:
        linear .5 xalign .9
    pause 0.5
    o "Quite hectic today, eh?"
    show barte normal standard with dissolve
    b "Yeah, you could say that."
    
    if meeting_liz == 0:
        h "Uhm who was that?"
        show barte normal lookaway with dissolve
        b "Oh right. Heiden, you didn't know her yet."
        show barte normal standard with dissolve
        b "That's Lisette, she's a part-timer here at the pub."
        b "There are days like tonight when I just need a helping hand."
        ls_annoyed "Would be nice to see you working for once, Boss."
        b "Well, someone has to take care of the guests by the counter."
        show barte normal lookaway with dissolve
        ls_standard "If you say so."
        ls_standard "Heiden's your name? {w}Can I get you something?"
        h "It's fine!"
        o "So what's your first impression of my little nephew?"
        ls_standard "Oh, so you're relatives."
        ls_serious "I'd say he's doing fine so far, considering that he might not go gobbling down all my cakes like a certain someone."
        show old funeral tired with dissolve
        o "Ouch."
        
    elif meeting_liz == 1:
        h "Oh, it's Lisette!"
        show barte normal lookaway with dissolve
        b "You met her at the café?"
        h "Yes, though the plan with the cake didn't work."
        show barte thinking lookaway with dissolve
        b "Then there's a mistake on your part."
        b "I guess the code phrase was a little bit too hard for a kid."
        show barte thinking standard with dissolve
        ls_standard "Oh hey it's you again, Heiden!"
        h "Yeah! Thanks again for earlier!"
        ls_standard "No biggie."
        o "So what's your impression of my little nephew?"
        ls_standard "Oh, so you're relatives."
        ls_serious "I'd say he's doing fine, considering that he's not gobbling down all my cakes like a certain someone."
        show old funeral tired with dissolve
        o "Ouch."
        
    else:
        h "Oh, it's Lisette!"
        ls_standard "Heya Heiden!"
        show barte normal lookaway with dissolve
        b "Oh, so you're already friends?"
        ls_embarrassed "Well yeah, considering the fact that we share some similarities.."
        h "(What did I do, Barty? Why is she acting like that?)"
        show barte normal smug with dissolve
        b "(Just play along, boy. {w}I find the circumstances pretty humorous.)"
        o "So what's your impression of my little nephew?"
        ls_standard "Oh, so you're relatives."
        ls_serious "I'd say he's doing fine, considering that he's not gobbling down all my cakes like a certain someone."
        show old funeral tired with dissolve
        o "Ouch."
    
    show barte thinking lookaway with dissolve
    ls_standard "Either way..."
    ls_standard "Just make yourself at home and let Boss serve you something to drink if you need any."
    h "Yeah I will, thanks Lisette."
    show barte thinking standard with dissolve
    ls_serious "At least someone who thanks me for my efforts."
    ls_annoyed "Would be nice to hear your praise sometimes, Boss."
    show barte normal smug with dissolve
    b "I would but your idea of a praise is a bit too much."
    ls_standard "I'd say many people would be delighted if they were asked out by a girl."
    show barte thinking lookaway with dissolve
    b "And I'd say that you're ten years too early for those strange ideas."
    show barte thinking standard with dissolve
    b "Get to work."
    ls_annoyed "Hmpf."
    h "She has it rough, I think."
    show barte normal lookaway with dissolve
    b "She'll get over it. {w}Let kids get their way for once and you'll lose control over them pretty quickly."
    show old funeral normal with dissolve
    o "Woah, the bartender's breaking a young maiden's heart with no mercy. \nLike it's no big deal."
    show barte normal lookaway with dissolve
    b "It's only a big deal if you make it one."
    o "Your principle?"
    show barte normal standard with dissolve
    b "My principle."
    
    play sound pubdoor
    ls_standard "Oh, hello! {w}Let me show you to a tab-"
    ls_serious "Uhm, you're a regular?"
    ls_serious "..."
    show barte thinking standard with dissolve
    b "Lisette, I'll handle him."
    ls_standard "Well, if you say so."
    
    if meeting_prittner == False:
        show prittner stranger:
            xalign -0.5 yalign .5
            linear 2.0 xalign 0.0
        show old:
            linear 1.0 xalign .5
        show barte:
            linear 1.0 xalign 1.0
            
        "Man" "Mr. Bartender, you claim you can take care of me?"
        h "Uhm."
        "That's strange."
        show barte thinking lookaway with dissolve
        "I've seen this guy before but somehow it's hard to put one and one together."
        "This attitude, the scary expression, hm."
        "Oh wait."
        show barte normal smug
        h "Wait a bit, you're Mr. Spooky from the train!"
        show prittner standard with fade
        show barte normal smile
        px "Indeed I am... {w}Wait. Stop it with that weird nickname first, ok?"
        show barte normal standard with dissolve
        b "You may not believe me, Heiden. But this man here is Mr. Prittner, an old friend of mine."
        p "'Came back to town in order to visit him, you see."
        show barte normal smug with dissolve
        b "What a heartfilled reunion, I didn't know you're already aquainted with each other."
        p "Well, one way led to another."
        h "That's for sure. {w}He was like really scary back in the train, like a spooky ghost."
        p "No need to go into detail, you pesky lass."
        
    else:
        show prittner standard:
            xalign -0.5 yalign .5
            linear 2.0 xalign 0.0
        show old:
            linear 1.0 xalign .5
        show barte:
            linear 1.0 xalign 1.0
    
        h "I can't believe it! {w}You actually came, Mr. Prittner!"
        p "I said that I come so I came, nothing too fancy about it."
        show barte thinking lookaway with dissolve
        b "It seems like my pub has become a kind of meeting spot of sorts."
        
        show barte gray
        show old gray
        with dissolve
        p "Don't make too much of a deal out of it."
        
        show prittner gray
        show old funeral normal
        with dissolve
        o "Yeah, Barty."
        
        show old gray
        with dissolve
        h "Right, Barty."
        show barte thinking standard with dissolve
        
        b "It's kind of annoying how you all seem to agree to that so easily."
        show old funeral normal
        show prittner standard
        with dissolve
    
    h "But this pub is really packed, tonight."
    p "Packed, indeed. {w}My last visit has been some years ago so I am glad that nothing major has changed."
    show barte thinking lookaway with dissolve
    b "Yeah, as long as I am here, there will be no major-"
    show lisette bannoyed behind barte:
        xalign -0.5 yalign .5
        linear 3.0 xalign 1.5
    l "Coming though, coming through.\nGeez, let's speak about a salary increase after this, Boss."
    b "Oh well."
    b "Ah yeah, as long as I am here. noth-"
    show lisette bstandard behind barte:
        linear 3.0 xalign -0.5
    l "Guests, guests.\nComing, coming!"
    show barte normal standard with dissolve
    b "No major changes to the business."
    p "Whatever."
    show old funeral tired with dissolve
    show old at twitchtwice
    o "Yeah, who cares."
    show old funeral normal with dissolve
    o "Oh right! {w}With all of us here, let's take a memorial photo!"
    show barte thinking lookaway with dissolve
    b "Meh, I am not sure about this."
    p "Me, too."
    h "If you ask me, I'd want that photo taken."
    show old funeral wink with dissolve
    o "That's my son!"
    show barte normal standard with dissolve
    b "He's not your son. {w}But well, let's take one."
    p "You don't sound so delighted."
    show barte normal lookaway with dissolve
    b "I don't but at least you're going to join us. "
    show barte normal smug with dissolve
    extend "Right, Pritty?"
    p "...Fine."
    h "Yes!"
    show barte thinking standard with dissolve
    b "Lisette, bring the camera."
    ls_annoyed "Get it yourself, hmpf!"
    show barte thinking lookaway with dissolve
    b "Oh well."
    show barte:
        linear 2.0 xalign 1.5
    h "Lisette, join us!"
    show old:
        linear 1.0 xalign 1.0
    show prittner:
        linear 1.0 xalign .5
    show lisette bserious:
        linear 1.0 xalign 0.0
    l "A photo? {w}I am not sure..."
    h "Barty's already getting the cam!"
    show old funeral wink with dissolve
    o "I'd say we should take it before the bartender changes his mind."
    show lisette bembarrassed with dissolve
    l "Boss is joining as well?"
    
    show lisette bstandard with dissolve
    show prittner:
        linear 1.0 xalign .33
    show old funeral normal:
        linear 1.0 xalign .66
    show barte normal standard:
        linear 1.0 xalign 1.0
    
    b "Found one. {w}Let's take a pic."
    b "Who's going to shoot it?"
    show lisette bserious:
        linear 1.5 xalign .66
    show prittner:
        linear 1.0 xalign 0.0
    show old funeral normal:
        linear 1.0 xalign .33
    l "Come. give it to me."
    show lisette:
        linear .5 xalign .8
    show barte:
        linear .5 xalign .8
    pause .5
    show lisette:
        linear .5 xalign .66
    show barte:
        linear .5 xalign 1.0
    pause .5
    l "You see, this camera has a feature called \"delayed-action shutter release\" which makes it possible to shoot it without having someone press the button."
    show barte thinking standard with dissolve
    b "Problem's solved, I guess."
    show prittner at twitchtwice
    show barte thinking lookaway with dissolve
    p "Let's get this over. {w}I am here for the beer, not for this chitchat."
    b "Without further ado, get into position."
    show barte normal standard with dissolve
    b "Come on, Heiden. {w}You're the lead character in here so snuggle yourself right in the middle of us."
    stop music fadeout 2.0
    $renpy.music.stop(channel=6, fadeout=2)
    hide barte
    hide lisette
    hide old
    hide prittner
    hide bg pub
    
    scene bg pubnight onlayer trans5
    show heiden final onlayer trans5:
        xalign .5 yalign .5
    show barte thinking standard onlayer trans5 behind heiden:
        xalign .75 ypos 100
    show lisette bstandard onlayer trans5:
        xalign 1.0
    show old funeral normal onlayer trans5 behind heiden:
        xalign .25 ypos 150
    show prittner onlayer trans5:
        xalign 0.0 ypos 100
    with fade
    
    play music at_home fadein 2.0
    h "It's pretty cramped here."
    show barte thinking standard onlayer trans5 with dissolve
    b "Deal with it. {w}We won't fit into one picture otherwise."
    show barte thinking closed onlayer trans5 with dissolve
    b "Also Lisette, your hair's constantly in my face."
    show lisette bembarrassed onlayer trans5 with dissolve
    show lisette onlayer trans5 :
        linear 1.5 ypos 100
    l "S-Sorry!"
    show barte normal lookaway onlayer trans5 with dissolve
    show lisette bstandard onlayer trans5 with dissolve
    h "And you're kinda bending too much, Uncle."
    show old funeral wink onlayer trans5 with dissolve
    show old onlayer trans5 :
        linear 1.5 ypos 100
    o "Hey hey, it's harder than it looks."
    show old funeral normal onlayer trans5 with dissolve
    p "So when does this \"release shutter trigger\" thingie go off?"
    show lisette bserious onlayer trans5 with dissolve
    l "..."
    l "I knew I forgot something."
    hide lisette onlayer trans5 with dissolve
    show barte thinking standard onlayer trans5 with dissolve
    b "Get a move on or we'll squeeze dear little Heiden here to death."
    show heiden onlayer trans5 at shivertwice
    h "I can manage. {w}It's kind of exciting."
    ls_serious "Yeah yeah."
    ls_serious "Uhm."
    ls_annoyed "Well, the trigger is kinda broken."
    ls_standard "But someone nice can press the trigger for us instead."
    p "Who will?"
    ls_annoyed "{i}Someone{/i} will."
    show lisette bstandard onlayer trans5:
        xalign 1.0 ypos 100
    with dissolve
    l "Back into position, guys!"
    
    show finalframe at pullup
    $ renpy.pause(1.5, hard=True)
    h "Hm?"
    show barte normal standard onlayer trans5 with dissolve
    b "Seems like we have to get even closer."
    
    show barte thinking standard onlayer trans5 behind heiden:
        linear 1.0 xalign .6 ypos 100
    show lisette bstandard onlayer trans5:
        linear 1.0 xalign 0.8 ypos 100
    show old funeral normal onlayer trans5 behind heiden:
        linear 1.0 xalign .4 ypos 100
    show prittner onlayer trans5:
        linear 1.0 xalign 0.2 ypos 100
    
    pause 1.0
    show heiden onlayer trans5 at shivertwice
    h "Urgh."
    b "Uhm, give that lad some room."
    
    show barte thinking standard onlayer trans5 behind heiden:
        linear 1.0 xalign .7 ypos 100
    show lisette bstandard onlayer trans5:
        linear 1.0 xalign 0.9 ypos 100
    show old funeral normal onlayer trans5 behind heiden:
        linear 1.0 xalign .3 ypos 100
    show prittner onlayer trans5:
        linear 1.0 xalign 0.1 ypos 100
        
    pause 1.0
    #$progression += 1
    o "Yeah, I think this works."
    o "And put your hands away, Barty."
    show barte normal standard onlayer trans5 behind heiden:
    b "There's no need to tell me."
    l "Okay! Let's shoot the photo!"
    h "Whose smartphone is it anyways?"
    show barte onlayer trans5 behind heiden at shivertwice
    b "Shhh, Heiden."
    h "Okay."
    l "Press the button, please!"
    
    window hide
    call screen true_landkarte
    $ click = _return
    
    if click == "picture":
        jump finalpic1
        
label finalpic1:
    
    play sound camera
    show barte normal lookaway onlayer trans5 behind heiden
    show old funeral wink onlayer trans5 behind heiden
    show prittner onlayer trans5:
        linear .5 ypos 300
    show lisette bembarrassed onlayer trans5
    pause .5
    with flash
    show prittner onlayer trans5:
        linear .2 ypos 100
    show barte normal standard onlayer trans5 behind heiden
    show old funeral normal onlayer trans5 behind heiden
    "Everyone in union" "Cheeese!"
    "Everyone" "..."
    show lisette bannoyed onlayer trans5
    l "Geez, cut me some slack!"
    p "I thought I saw a shiney nickle under my shoe."
    show lisette bstandard onlayer trans5
    l "Well, let's have a proper photo shoot now."
    show heiden onlayer trans5 at shivertwice
    h "It's kinda getting hot."
    b "Let's hurry with the next photo then."
    
    window hide
    call screen true_landkarte
    $ click = _return
    
    if click == "picture":
        jump finalpic2
        
label finalpic2:
    show barte thinking standard onlayer trans5 behind heiden
    play sound camera
    pause .5
    with flash
    "Everyone in union" "Cheers!"
    
    show finalframe at pullout
    $ renpy.pause(1.5, hard=True)
    hide heiden onlayer trans5 with dissolve
    show barte thinking lookaway onlayer trans5:
        linear 2.0 xalign .66 ypos 0
    show lisette bstandard onlayer trans5:
        linear 2.0 xalign 1.0 ypos 0
    show old funeral normal onlayer trans5:
        linear 2.0 xalign .33 ypos 0
    show prittner onlayer trans5:
        linear 2.0 xalign 0.0 ypos 0
    
    b "Looks like this photo is decent enough."
    show lisette bannoyed onlayer trans5 with dissolve
    l "Even though you had your hand up, again?"
    show lisette bembarrassed onlayer trans5 with dissolve
    l "But I still want a copy of that photo, okay Boss?"
    show lisette bstandard onlayer trans5 with dissolve
    l "Now that it's settled, let's get back to the guests."
    l "You'll come with me, Boss."
    show barte normal surprised onlayer trans5
    b "Hey-"
    show lisette bserious onlayer trans5:
        linear 2.0 xalign 1.75
    show barte normal lookaway onlayer trans5:
        linear 2.0 xalign 1.50
    show old funeral normal onlayer trans5:
        linear 2.0 xalign .8
    show prittner onlayer trans5:
        linear 2.0 xalign .2
    b "Can't really escape you this time, huh?"
    show prittner onlayer trans5 at twitchtwice
    p "Man, this took longer than expected."
    show old funeral wink onlayer trans5
    o "It was well worth it if you ask me."
    p "Whatever, I'll go check out the folks."
    show prittner onlayer trans5:
        linear 2.0 xalign -0.5
    pause 1.0
    
    hide bg onlayer trans5
    hide barte onlayer trans5
    hide old onlayer trans5
    hide prittner onlayer trans5
    hide lisette onlayer trans5
    
    scene bg pubnight 
    $ renpy.music.play('audio/sfx/pub_crowd.mp3', channel=6, loop=True, fadeout=0, synchro_start=False, fadein=2, tight=True, if_changed=False)
    show old funeral normal:
        xalign .5 yalign .5
    with fade
    o "Hey Heiden."
    h "What is it."
    show old funeral troubled with dissolve
    o "Uhm."
    show old funeral normal with dissolve
    extend " Thank you."
    h "That came out of nowhere, Uncle."
    o "You see, things will work out here."
    o "I mean, we got the bartender here, all the people here, you and me."
    o "We'll figure things out while you grow bigger and bigger."
    h "I think you are kinda treating me like a tree?"
    o "Yeah, well. {w}Maybe."
    o "But you're a good tree."
    show old funeral wink with dissolve
    extend " The best tree there is."
    show old funeral normal with dissolve
    o "But the thing is, the stuff we talked about at the funeral."
    o "Stuff about home and where you want to settle."
    o "They're right at the palm of your hands."
    o "So it's cool to just stay the way you are."
    o "That's like the bottom line of your story."
    h "Your words sound so artificially deep right now, Uncle."
    h "But it's pretty hilarious that someone I regard as \"hopeless\" is telling me all that."
    show old funeral wink with dissolve
    o "I guess that's just the way I am?"
    "Yeah, just the way you are."
    with vpunch
    "*laugh*"
    hide old with dissolve
    window hide
    show black with dissolve
    
    centered "Yeah, I think I understand now."
    centered "The stuff about the future, {w}what I do, {w}when I want to do it, {w}where I will be at..."
    centered "These questions are so out of reach for me but yet I can feel like grasping the answers if I tried."
    centered "Is it because I am still a kid?"
    centered "That I still don't understand."
    centered "And now I finally feel like I don't care about understanding it."
    centered "There's much more fun to be had when you leave the theory behind and just learn to feel it instead."
    centered "I think I am no longer scared to think about tomorrow."
    centered "Because Uncle's here who is even more hopeless than me."
    centered "And Barty who always has an answer to everything."
    centered "I am not feeling so alone anymore."
    centered "But I'll tell you more about it the next time I meet you, okay?"
    
    window show
    hide black with dissolve
    show old funeral normal with dissolve
    h "Uhm, Uncle?"
    o "What is it, Heiden?"
    h "Let's visit Mum sometimes, okay?"
    show old funeral wink with dissolve
    o "That's fine by me! {w}Let's rent a car for a little trip."
    bs_standard "Hey, I heard that."
    bs_lookaway "You guys better let me drive."
    bs_smug "Or Old's gonna wreck it."
    show old funeral tired with dissolve
    o "Well, you're probably right."
    
    scene black with fade
    stop music fadeout 2.0
    $renpy.music.stop(channel=6, fadeout=2)
    $ renpy.pause(2.0, hard=True)
    window hide
    
    centered "See, Mum? {w}I {i}know{/i} that I am going to feel right at home here." with dissolve
    $ renpy.pause(2.0, hard=True)
    
    hide ch1_umriss1 onlayer trans3
    hide ch1_umriss0 onlayer trans4
    hide ch1_umriss2 onlayer trans4
    hide ch1_chara0 onlayer trans4
    hide ch1_chara1 onlayer trans4
    hide ch1_chara2 onlayer trans4
    hide ch1title onlayer trans4
    hide black
    
    
    jump end1_transition