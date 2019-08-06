image sakura filmstrip = anim.Filmstrip("images/etc/leaf.png", (80, 60), (2, 1), .15)
image snowblossom = SnowBlossom("sakura filmstrip", xspeed=(200, 400), yspeed=(100, 150))
########################################################################################
#Chapter 1.5 : Afternoon

label afternoon:
    $ save_name = "Chapter 1.5 - Afternoon"
    play music watch
    $ renpy.pause(2.0, hard=True)
    centered "30 minutes later...?" with dissolve
    $ renpy.pause(2.0, hard=True)
    
    os_normal "Hey."
    play sound punch
    with hpunch
    centered "Urgh."
    $ renpy.pause(1.0, hard=True)
    os_normal "Hey, Heiden."
    play sound punch
    with hpunch
    centered "Stop pinching me..."
    $ renpy.pause(1.0, hard=True)
    os_normal "That ain't pinches, they're slaps of love."
    os_normal "C'mon, wake up."
    play sound punch
    with hpunch
    stop music fadeout 2.0
    centered "God, I am awake. I am awake already."
    
    play music at_home fadein 2.0
    scene bg bedroom with pixellate
    show old funeral normal:
        xalign 0.5 yalign 0.2 zoom 1.5
        pause 1.0
        linear 1.0 zoom 1.0 yalign 0.5
    o "There you are."
    h "Did I nod off?"
    o "Yeah you did but it's no problem."
    o "I am about to head downtown, visiting a good friend of mine."
    h "Okay?"
    h "Should I watch over the house while you're gone?"
    o "'Course not, you're coming with me."
    h "..."
    show old funeral wink:
        linear 0.5 xzoom -1.0
    o "*grin*"
    h "Give me ten minutes."
    show old funeral wink:
        linear 0.5 xzoom 1.0
    pause .5
    show old funeral normal
    o "That's my boy."
    show old:
        linear 1.0 xalign 0.8
    o "I'll see you downstairs in five."
    hide old with Dissolve (1.0)
    play music sleepyroom fadein 2.0 fadeout 2.0
    play sound stairs
    h "It seems like I had enough sleep."
    
    if location_table == 4:
        "There's a suspicious cake on the table."
        h "Seems like [nickname_old] left it here from before."
        h "I guess I should either eat it or leave it be."
        
        menu:
            extend ""
            "Eat the cake":
                $ old_points += 1
                h "I should be considerate of [nickname_old]'s efforts to keep me sated."
                h "Let's at least eat the cake to replenish energy that I've lost during my slumber."
                with hpunch
                "*munch*"
                h "It's actually good."
            
            "Leave the cake":
                "I am really not feeling the hunger, even after waking up from my sleep."
                "I hope [nickname_old] is not too angry at me for leaving out a meal."
                "I swear I'll make up for it, somehow."
    
    "I look around the room for a clock and found a black digital one sitting on a rack above my bed."
    play sound shock
    "I slept for {b}eight hours{/b}."
    "The sight outside my window verified an imminent sunset coming."
    h "Wait, what."
    h "How could I sleep in for that long?"
    "It seems like my internal clock is totally broken right now."
    "I should take better care of my sleep pattern."
    h "Well, let's not make [nickname_old] wait for too long."
    "I left my deal with the time behind as I rubbed my eyes."
    stop music fadeout 2.0
    show black with fade
    play sound stairs
    centered "Time to head out, I guess."
    
    play music evening fadein 3.0
    scene bg house_night with squares
    show snowblossom
    os_normal "Evening's just around the corner, Heiden."
    h "Yeah. Good evening to you, too."
    
    show old funeral normal:
        yalign .5 xalign .5
    with dissolve
    
    o "I guess we can get going then."
    h "Uhm."
    o "What's the matter?"
    
    play sound wind fadein 2.0
    pause 1
    show old funeral troubled at twitchtwice
    pause 1
    stop sound fadeout 1.0
    h "Aren't you cold right now?"
    h "You sure you don't need a jacket or something, [nickname_old]?"
    show old funeral normal with dissolve
    o "This much is nothing, though the coldness from this morning was kind of a bummer for me."
    
    show old funeral normal:
        linear 1.0 xzoom -1.0
        pause 1
        linear 1.5 xalign -0.5
        
    o "Let's depart."
    h "Well, if you say so."
    
    $ renpy.pause(2.0, hard=True)
    scene bg wayhome2night with wiperight
    show snowblossom
    
    $ renpy.music.play('<from 0 to 8>audio/sfx/footsteps3.mp3', channel=6, loop=True, fadeout=0, synchro_start=False, fadein=0, tight=True, if_changed=False)
    "Oh, it's this place again."
    "There are some leaves here and there that are dancing through the windy afternoon."
    "The street's lighting is on and illuminates our moving bodies."
    "Our shadows swiftly appearing and disappearing as we pass each street lamp one by one."
    "There's nothing to say while I follow his back."
    
    show old funeral normal:
        xalign -0.25 yalign .5
        linear 2.0 xalign 0.2
        
    o "Don't worry, it's not as far as going to the station."
    
    show old funeral normal:
        linear 2.0 xalign -0.5
        
    h "I am not really opposed to going outside but having activities this late is really suspicious."
    h "Or that's what Mum used to say."
    o "Hm."
    
    $renpy.music.stop(channel=6, fadeout=None)
    stop music fadeout (4.0)
    h "Why'd you stop?"
    os_normal "'Cause we're here."
    with vpunch
    h "Woah."
    hide snowblossom
    scene black with blinds
    play sound pubdoor
    centered "He grabs my hand with a single motion and enters something that looked awfully like..."
    pause 1.0
    centered "A café?" with fade
    
#Chapter 1.5 : Afternoon [END]
################################################################################
#Chapter 1.6 : The Pub

    $ save_name = "Chapter 1.6 - The Pub"
    play music pub fadein 2.0
    $ renpy.music.play('audio/sfx/pub_crowd.mp3', channel=6, loop=True, fadeout=0, synchro_start=False, fadein=2, tight=True, if_changed=False)
    scene bg pubnight with pixellate
    "Okay."
    "I am reassessing the situation here."
    "I wouldn't call it a café."
    "Calling it a café is quite an understatement to begin with."
    "This place is crawling with loud people, feasting away on their alcoholic liquor."
    "How this noise level couldn't be heard from the outside is just little short of a miracle."
    with vpunch
    "There's a huge guy in the back with some nasty tattoos!"
    with vpunch
    "Oh! Oh! A guy with a huge scar stretched across his cheek!"
    with vpunch
    "Or this guy with muscles as big as my head!"
    "I am nothing but flabbergasted by the fact that my Uncle is mixing with those kind of people!"
    
    show old funeral tired:
        xalign -0.25 yalign .5
        linear 3.0 xalign 0.5
        
    o "C'mon, Heiden. Don't just stand at the entrance."
    h "[nickname_old], I--"
    o "Let's go straight to the bar and get our seats."
    
    show old:
        linear 3.0 xalign 1.5
    with vpunch
    
    h "This place is {b}awesome{/b}!"
    os_tired "Yeah, yeah. I heard ya."
    "He sounds seemingly tired as he walks towards the bar."
    "With nothing else to do, I follow suit but without breaking eye-contact with a guy wearing an eyepatch."
    "One-eyed Man" "*Grin*"
    "I grin back as I make my way to the bar."
    
    show old funeral normal:
        xalign 0.1 yalign .5
    show barte normal lookaway:
        xalign 0.9 yalign .5
    with fade
    
    "I seat myself right next to my Uncle, facing a rather unresponsive barkeeper."
    show old at twitchtwice
    o "Heya, Bartender."
    h "It's like we're amidst pirates, [nickname_old] Old!"
    show barte normal standard with dissolve
    b "In a pirates' den, heh?"
    $ barte_points = 0
    
    if nickname_old == "Mister":
        show barte normal smug with dissolve
        b "And Old, that boy's calling you [nickname_old]."
        o "Well, I'll take my time to settle him down."
    else:
        $barte_points += 1
        show barte normal smug with dissolve
        b "And Old, that boy's calling you [nickname_old] already."
        o "What can I say? {w}That's the first step towards a happy family, right?"
    
    show barte normal lookaway with dissolve
    b "That aside."
    
    show barte normal standard with dissolve
    b "My pub does attract a lot of {i}unique{/i} clientele."
    
    h "How should I call you, Mister?"
    
    show barte normal lookaway with dissolve
    pause 1
    show barte normal standard
    b "Just call me Bartender, like everyone else."
    show barte normal lookaway with dissolve
    o "Well, that's the one thing he insists on."
    h "Okay, Mister Bartender."
    show barte normal standard
    b "{b}Bartender{/b}, just Bartender."
    show barte normal lookaway with dissolve
    
    if nickname_old == "Mister":
        b "Wouldn't want the same fate as Old over there."
        show old funeral wink with dissolve
        show old at shivertwice
        b "You heard me, Old."
        show old funeral normal with dissolve
    else:
        b "The name's not my last name but my profession."
        b "No need for the 'Mister'."
    
    h "B-Bartender then."
    show barte normal closed with dissolve
    b "That's more like it."
    show barte normal standard with dissolve
    h "And you can call me Heiden, Barty."
    show barte normal smug
    show old funeral wink 
    with dissolve
    b "{i}Barty{/i}? {w}The boy's learning, Old."
    o "Barty's a new one. {w}But it kinda fits."
    show old funeral normal
    show barte normal standard 
    with dissolve
    b "So. {w}Welcome to my pub, Heiden."
    show barte normal lookaway with dissolve
    b "Don't let my customers disturb your time here."
    b "Despite their appearances, they're pretty chill and don't mean trouble."
    o "You alone tonight?"
    show barte normal standard with dissolve
    b "Yes, I can handle that much activity tonight all by myself."
    b "No need for a part timer fizzling around me."
    b "But back to the topic at hand."
    show barte normal lookaway with dissolve
    b "You're both here for a drink?"
    o "Just give me the usual."
    o "And get Heiden something non-alcoholic."
    h "Bring me some juice, Barty!"
    show barte normal standard with dissolve
    b "Right away."
    hide barte with dissolve
    show old:
        linear 1.0 xalign 0.5
    pause 1
    o "So what's your first impression of this place?"
    h "It's really loud and there are lots of scary looking people!"
    o "Well, you don't really sound scared yourself."
    h "Of course not, I think that guy over there can lift me up with a single finger!"
    "My excitement knows no bound, this café/bar/whatever's like a convention of super bullies."
    "I feel like I am in a movie set full of pirates, thugs and other strong looking muscular men."
    "Though in all sincerity, I wouldn't have expected to find those kind of people in my rather quiet neighborhood."
    o "I guess I am happy that you're not displeased to be here."
    h "Not at all!"
    
    if location_table == 1:
        o "I come here every evening to get my mind off of work."
        bs_smug "Oh isn't that right, [nickname_old] Writer?"
    elif location_table == 2:
        o "I come here every evening and also whenever I feel troubled."
        bs_smug "Which is to say that dear milady is usually the reason behind the troubles."
    else:
        o "I come here every evening to chat with my good ol' friend here."
        bs_lookaway "I wonder how much truth lies in that statement."
    
    show old funeral tired with dissolve
    o "Oh you get off my back, my parched throat rather needs your attention right now."
    
    show old funeral normal with dissolve
    "The Bartender has his hands full with the orders of the customers and ours but still somehow manages a comeback."
    
    h "You're friends with him even though you call him Bartender too, [nickname_old]?"
    o "Since the day he became successor of this pub, he demands that his name's better be 'Bartender' or else there's no use becoming one."
    h "But if he is the successor of the pub, doesn't it make him a barkeeper?"
    show old funeral tired with dissolve
    o "Woah, my head."
    o "That's actually a good one."
    
    show old:
        linear 1.0 xalign .1
    show barte normal standard:
        xalign .9 yalign .5
    with dissolve
    
    play sound glass
    b "I am actually both a barkeeper and a bartender."
    b "But I started as an apprentice here, working as a bartender."
    show barte normal lookaway with dissolve
    b "So I ended up being more comfortable with being called a bartender."
    show barte normal standard with dissolve
    b "There's nothing else to it, really."
    b "Now without further ado, here are the drinks."
    
    with vpunch
    b "A glass of orange juice for the little guy."
    o "Thanks."
    
    with vpunch
    stop music fadeout 1.0
    $renpy.music.stop(channel=6, fadeout=1)
    b "And a selfmade non-alcoholic lemonade fizzy soda for you, Old."
    show old at twitchtwice
    h "Alright!"
    
    play sound silence loop
    "Somehow that came unexpected."
    "It feels like this drink drew the music of the entire room at once."
    "I mean, really? {w}A lemonade soda in this kind of place?"
    show old funeral normal with dissolve
    o "What's up, Heiden?"
    h "No, it's just..."
    show barte thinking standard with dissolve
    b "Look, Old. {w}Even the kid's doubting your sense of taste."
    h "Never said I had faith in his taste buds in the first place."
    show old funeral tired with dissolve
    show old at shivertwice
    o "You're just spouting those sad words because you have never drank it yourself, do you?"
    h "A challenge? Give me that booze, I'll drink that hellish beverage before your eyes in one single go and tell you what's on my mind!"
    show barte thinking lookaway with dissolve
    b "I want to compliment your eagerness to drink my creation but at the same time I am hurt to hear a kid saying \"{i}Give me that booze{/i}\" at such a young age."
    
    show old:
        linear .4 zoom 1.4
    show barte thinking standard:
        linear .4 zoom 1.4
    pause .4
    with vpunch
    play sound glass
    show old:
        linear 1 zoom 1.0
    show barte normal standard:
        linear 1 zoom 1.0
    pause 1.0
    
    "I grab the drink and proceed to take a closer look at it."
    stop sound
    play sound heartbeat
    "It's soda, so I expect it to taste unhumanly sourly to some extent as well as sugary."
    "I am not much of a sweet tooth myself but if it's to disagree with [nickname_old]'s taste buds, I am totally in."
    "But on a second note, what if it's really bad?"
    "As a consequence, I would get a tummy-ache and that would really suck."
    b "Don't think too much 'bout it."
    show barte normal lookaway with dissolve
    b "You don't need to force yourself to drink this."
    h "I am not a chicken!"
    b "That's got nothing to with--"
    stop sound
    play sound gulping
    "I am doing it."
    "I am a madman but I am doing it anyways."
    stop sound fadeout 2.0
    "The yellow liquid falls strongly on my tongue as it wanders straight down my throat with little resistance."
    "I feel a mellow sweetness as opposed to the strong dominant sugar rush that would have penetrated my taste buds."
    "Wait, I can taste more."
    "Overcoming the sweet fragrance that has inhered my mouth, a precious friskiness takes the reins."
    "As if complementing the purely sweety taste, a balance between two opposing tastes has been achieved."
    h "It's... "
    show barte normal smile with dissolve
    play sound heaven
    extend "It's actually good!"
    show old funeral normal with dissolve
    o "What did I told you, Barty's drinks are the best."
    show barte thinking lookaway with dissolve
    b "Oh, don't you start calling me that, too."
    play music pub fadein 2.0
    $ renpy.music.play('audio/sfx/pub_crowd.mp3', channel=6, loop=True, fadeout=0, synchro_start=False, fadein=2, tight=True, if_changed=False)
    
    b "But it's nice that people compliment my creations though it's not officially on the menu."
    b "Not many people try my soda because they don't think it even exists."
    show barte thinking smile with dissolve
    b "Well, as long as there are some freaks out there who happily down it, I won't complain."
    hide barte with dissolve
    show old:
        linear 1.0 xalign .5
    "With that comment the Bartender has resumed his business as he is called by one of the groups of thu-, I mean customers."
    
    o "You know, I am happy that the drink was to your liking."
    show old funeral tired with dissolve
    o "But you actually drank my drink away..."
    h "Sorry about that, [nickname_old]."
    h "You can have my juice instead!{w} I'll go check out those people!"
    
    show old:
        linear .4 zoom 1.4
    pause .4
    with vpunch
    play sound glass
    show old funeral normal:
        linear 1 zoom 1.0
    pause 1.0
    
    o "Oh well, there he went."
    show old at shivertwice
    o "*sip*"
    show old funeral tired with dissolve
    o "God, it's super sour."
    show old:
        linear 1.0 xalign .1
    pause 1
    show barte thinking smile:
        xalign .9 yalign .5
    with dissolve
    b "Because it's freshly squeezed orange juice."
    b "Hand-picked oranges, resulting in a drink with hundred percent fruit content."
    
    show old funeral normal with dissolve
    o "Now you're just messing with me."
    
    show barte normal lookaway with dissolve
    b "Well, it was originally Heiden's drink."
    b "You just spoiled my chance to see his contorted face due to the sourness."

    show barte normal standard with dissolve
    show old at twitchtwice
    o "Man, don't I look like a protective uncle right now, heh?"
    
    show barte normal lookaway with dissolve
    b "Speaking of the boy, he looks like he's having fun."
    o "You consider {i}this{/i} fun?"
    o "I only see a boy being spinned around by some bulky ex-marine."
    show barte thinking smile with dissolve
    b "Don't you see the smiling face of his? {w}It's radiating and devoid of fear. {w}That's what {i}having fun{/i} looks like."
    show barte thinking lookaway with dissolve
    b "This brings us back. {w}Old memories right, Old?"
    show old funeral troubled with dissolve
    o "..."
    show barte thinking standard with dissolve
    b "Apropos, you forgot your jacket here last time."
    show old funeral normal with dissolve
    o "Oh that's there it was."
    o "I should have expected it."
    show barte normal lookaway with dissolve
    b "You should try to get rid of your easygoing way of handling things, Old."
    b "It's not good, not responsible. {w}Especially with a kid like him."
    show old funeral troubled with dissolve
    o "Man, you sure know how to rub it in."
    show barte normal standard with dissolve
    b "I remember also being the one who told you that you aren't good with that kind of stuff."
    show old funeral wink with dissolve
    o "That I won't do."
    show barte normal lookaway with dissolve
    b "You're being too much of a pain yourself to be able to take care of things."
    show old funeral normal with dissolve
    o "Heiden's not a {i}thing{/i}, you know."
    o "I am his uncle. {w}Which in turn makes me his family."
    show barte normal standard with dissolve
    show old at shivertwice
    b "A {b}part{/b} of his family. {w}You're not the only family member he has, right?"
    o "You know about my family situation, do you?"
    show barte normal closed with dissolve
    b "It's just vexing."
    b "Because your problems automatically involve me as well."
    show barte normal lookaway with dissolve
    b "It's the silly and troublesome part of being friends."
    o "I can't say that I am not grateful for it."
    show barte normal standard with dissolve
    b "Because {b}you{/b} are usually on the receiving side of the contract called friendship, you know."
    show old funeral wink with dissolve
    o "My, aren't I lucky~"
    show barte normal closed with dissolve
    b "I feel like I am talking against a wall."
    show barte normal lookaway with dissolve
    b "Fine, I'll tag along your babysitting plans."
    b "..."
    b "Nothing else to say, dear friend of mine?"
    show old funeral normal with dissolve
    o "I am super happy for your deeds so far."
    o "Oh. And can I get more of your Irin-soda, please?"
    show barte normal standard with dissolve
    b "..."
    show barte normal smile with dissolve
    b "Certainly."
    show barte normal standard with dissolve
    b "But from now on you're forbidden to call it like that."
    b "Its name is \"selfmade non-alcoholic lemonade fizzy soda\" until I can find a more fitting name, am I clear?"
    show old funeral troubled with dissolve
    o "Oh well."
    show old funeral normal with dissolve
    hide barte with dissolve
    bs_lookaway "And while I am at it, have applied for a change of school for Heiden yet?"
    o "Oh, uhm."
    bs_closed "You haven't."
    o "I haven't, {b}yet{/b}."
    bs_lookaway "I am not even sure how serious you are about being a caretaker, or at the very least being an uncle."
    o "I am super serious."
    bs_standard "Would be nice to see some merit to those words."
    show old funeral tired with dissolve
    o "Easy on the mysterious mushrooms, please."
    o "I know that you'll put some in for my own demise. {w}I just had a bad premonition that you'll do what you're about to do."
    bs_lookaway "Don't worry, you'll survive the dose."
    show old funeral normal with dissolve
    bs_standard "It's currently past spring so children usually have vacation or some other sort of idiotic holiday."
    bs_standard "Look out for schools and enroll him to one, the sooner the better."
    bs_lookaway "Kids like him won't have an easy time finding friends in school if cliques were already established."
    o "Thanks."
    bs_standard "I don't even know why I have to hand it to you on a platter."
    bs_lookaway "You're his {i}family{/i}, keep your act together."
    
    show barte thinking standard:
        xalign .9 yalign .5
    with dissolve
    show barte at twitchtwice
    play sound glass
    
    b "Here."
    show old funeral tired with dissolve
    o "This is either paradise or hell, I don't know it for sure."
    show barte normal smug with dissolve
    b "There is only one way to find out, right?"
    o "I guess this is my punishment for my carelessness."
    show barte thinking closed with dissolve
    b "Oh believe me, if I had to hand out punishments for every single blooper of yours, you'd be long dead."
    b "Besides, the soda's the only thing that I pour you out for free."
    show barte thinking standard with dissolve
    show old funeral normal with dissolve
    o "I am relieved, and thankful."
    o "And a bit worried."
    show old funeral tired with dissolve
    o "I will now execute my punishment and down this pot of evil."
    show old at twitchtwice
    o "Hm..."
    show old gray at twitchtwice
    show barte thinking surprised
    o "Urgh, woah."
    show old green at twitchtwice
    show barte thinking standard
    o "Uff."
    show old hue at shivertwice
    show barte thinking surprised
    o "Oh my god."
    show old invert at twitchtwice
    o "This is kinda bad."
    show old funeral tired at shivertwice
    show barte thinking standard
    o "Did I somehow turn back normal?"
    o "Oh man, what a ride."
    show old funeral normal with fade
    o "The drink is good but yet so bad, I don't know what to make out of it."
    b "You don't need to."
    b "There were some interesting reactions."
    show old funeral tired with dissolve
    o "Well, I am actually not feeling so good right now."
    show barte thinking lookaway with dissolve
    b "You survived, that's the result."
    
    scene black with blinds
    pause 1
    $renpy.music.stop(channel=6, fadeout=3)
    play music at_home fadein 2.0 fadeout 2.0
    scene bg pubnight with blinds
    show old funeral tired:
        xalign .1 yalign .5 zoom 1
    show barte normal standard:
        xalign .9 yalign .5 zoom 1
    with dissolve
    
    h "I am back!"
    show barte normal lookaway with dissolve
    b "Well, you sure took your sweet time."
    b "How was the experience?"
    with vpunch
    h "There's that guy called Steven, he kind of claims to be able to speak solely by rolling his eyes back and forth in order to create sound!"
    h "But the pub was too loud to make out any kind of sounds..."
    with vpunch
    h "And- And there's this Robsen guy who always has some hardened newspaper under his shirt in case he got stabbed in the back!"
    h "But it was all greasy and smelly but he told me like it's the price to pay if you want to survive out there!"
    with vpunch
    h "And-!{nw}"
    show old at shivertwice
    o "Beuf."
    h "Uhm."
    show barte thinking closed with dissolve
    b "It's nice that you could accumulate some {i}interesting{/i} experiences."
    show barte thinking lookaway with dissolve
    b "But it's getting late for kids, {w}and dear Old here looks like he's had too much soda."
    h "You really don't look so well, [nickname_old]."
    show barte normal smug with dissolve
    b "He's just getting {i}old{/i}, that's all."
    show barte normal standard with dissolve
    b "You better get him home, I'll call a taxi."
    show old funeral normal with dissolve
    o "There's- there's no reason to. The house's right 'round the corner."
    show barte normal lookaway with dissolve
    b "Well, let thickheads be."
    show barte normal standard with dissolve
    b "You both get home safe."
    h "Can I come again, Barty?"
    
    show barte thinking lookaway with dissolve
    pause 1
    show barte thinking standard with dissolve
    b "Yes, but only with Old when it's this late."
    b "Kids these days need a guardian at all times."
    o "We'll be going then."
    show old funeral wink with dissolve
    o "You're such a worryward, Barty."
    show old funeral tired with dissolve
    show old at shivertwice
    o "Beufff."
    show barte normal lookaway with dissolve
    b "Just get going already before you're messing up my pub."
    show barte normal standard with dissolve
    h "Bye, Barty! {w}You too, Goppy!"
    "One-eyed Goppy" "*grin*"
    hide old with dissolve
    show barte:
        linear 1.0 zoom 0.5
    hide barte with dissolve
    pause 1
    
    scene black with pixellate
    stop music fadeout 2.0
    play sound pubdoor
    pause 2
    scene bg pubnight with blinds
    show barte thinking closed with dissolve
    pause 1
    b "..."
    show barte thinking surprised with dissolve
    b "Oh wait."
    show barte thinking standard with dissolve
    b "That bastard's forgotten his jacket again."
    show barte thinking lookaway with dissolve
    b "Oh well."
    "One-eyed Goppy" "*wink*"
    show barte normal standard with dissolve
    b "'Coming."
    hide barte with dissolve
    "One-eyed Goppy" "I-Is this young lad perhaps milady's--?"
    bs_lookaway "Yeah he is but please don't leap for joy because of it or you'll sprain your hips again."
    "One-eyed Goppy" "*grin* {w}It's like she finally came back after all those years.."
    bs_closed "..."
    scene black with slowBlack
    $ renpy.pause(2.0, hard=True)
    show screen disable_Lmouse()
    
    jump ch1_transition
    
#Chapter 1.6 : The Pub [END]
################################################################################