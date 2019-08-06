################################################################################
#Chapter 2.3a : Freetime (Park)

label park0:
    
    $ save_name = "Chapter 2.3a - Playing in the Park"
    scene bg park with fade
    play music new_morning fadeout 2.0 fadein 2.0
    play sound playground loop
    show tooltip_background
    if progression == 0:
        show expression Text(_("Morning"), size=40, color="#f0ff00", yalign=0.005, xalign=.98, drop_shadow=(2, 2)) as text
    else:
        show expression Text(_("Noon"), size=40, color="#f9aa19", yalign=0.008, xalign=.95, drop_shadow=(2, 2)) as text
    
    $ renpy.block_rollback()
    "Children's chatter can be heard from afar."
    "But that's to be expected, the weather seems to be doing fine albeit it could be better."
    "That doesn't hinder the children from playing to their hearts content."
    h "Wow, what a feast for my eyes!"
    "I guess with this gathering of children, the queue for the bumpy slide will be long."
    h "First come, first serve!"
    
    show black with fade
    show tooltip_background
    if progression == 0:
        show expression Text(_("Noon"), size=40, color="#f9aa19", yalign=0.008, xalign=.95, drop_shadow=(2, 2)) as text
    else:
        show expression Text(_("Afternoon"), size=40, color="#FD8204", yalign=0.008, xalign=1.0, drop_shadow=(2, 2)) as text
        
    centered "Some hours later..." with dissolve
    hide black with fade
    h "Man, what a blast."
    "Time has been running so swiftly when I am occupied like this."
    "[nickname_old] should be plenty pleased with my exercise for today."
    "But maybe it's time to move on."
    
    $old_points += 1
    $park_unlock += 1
    $progression += 1
    $now_park0 = True
    
    if progression == 1:
        jump freetime2
    else:
        jump freetime3
    


################################################################################
#Chapter 2.3b : Freetime (Bridge)

label bridge:
    $ save_name = "Chapter 2.3b - Jogging at the Bridge"
    h "Time to check out the bridge!"
    show heiden kitchen tired with dissolve
    h "Well. {w}After I've washed the dishes of course."
    
    scene bg bridge with fade
    show tooltip_background
    play music new_morning fadeout 2.0 fadein 2.0
    play sound river loop
    show expression Text(_("Morning"), size=40, color="#f0ff00", yalign=0.005, xalign=.98, drop_shadow=(2, 2)) as text
    $ save_name = "Chapter 2.3b - Bridge"
    
    $ renpy.block_rollback()
    "I can hear the river flowing but it's a gentle and refreshing kind of sound."
    "Oh, I can see Barty in the distance jogging."
    "I better keep up with his pace."
    "..."
    "..."
    "God, is he running away from me or is his jogging pace just that fast!?"
    h "Hey! Wait!"
    
    show barte jog standard:
        yalign .5 xalign .5
    with dissolve
    b "What'ya doing here, Heiden?"
    with vpunch
    h "Puhhh."
    h "You can really pack a punch with your jogging."
    show barte jog smug with dissolve
    b "Well, the price's high if you want to stay fit when you're my age."
    show barte jog lookaway with dissolve
    b "So?"
    h "Can you show me around the town?"
    show barte jog standard with dissolve
    b "A sightseeing tour, heh?"
    show barte jog closed with dissolve
    b "Hm..."
    with vpunch
    h "C'mon, Barty."
    h "There's not much to think about!"
    show barte jog smug with dissolve
    b "I'll just consider my jogging route."
    b "We can combine our causes. {w}I'll jog around the places while you follow me around like a puppy."
    show barte jog lookaway
    h "At least give me a break here and then."
    show barte jog standard with dissolve
    b "Let's go."
    hide barte with dissolve
    h "Ehhhhh?"
    h "Wait!"
    
    scene bg jog1 with fade
    show tooltip_background
    show expression Text(_("Morning"), size=40, color="#f0ff00", yalign=0.005, xalign=.98, drop_shadow=(2, 2)) as text
    stop sound
    play sound jogging loop
    bs_jstandard "How're you holding up, kid?"
    h "How are you able to talk this camly while jogging?"
    show barte jog standard with dissolve
    bs_jlookaway "This much is nothing, let's move on."
    h "*Sigh*"
    
    scene bg sport with fade
    show tooltip_background
    show expression Text(_("Morning"), size=40, color="#f0ff00", yalign=0.005, xalign=.98, drop_shadow=(2, 2)) as text
    bs_jstandard "Now we're at the town's sports stadium."
    bs_jlookaway "You're usually free to use it when teams aren't using it themselves."
    h "Huff.. Huff.."
    h "Why did we enter the stadium again?"
    bs_jstandard "No reason."
    bs_jstandard "Let's get going."
    h "Right.. behind you."
    
    scene bg jog2 with fade
    show tooltip_background
    show expression Text(_("Morning"), size=40, color="#f0ff00", yalign=0.005, xalign=.98, drop_shadow=(2, 2)) as text
    bs_jlookaway "Hm, what else does this town have in store for us?"
    h "Huff.. Huff.."
    bs_jstandard "Yeah, hang in there."
    bs_jstandard "We are about halfway through the course."
    h "Still another half remaining!?"
    bs_jlookaway "I thought kids would be brimming with energy."
    bs_jlookaway "I was so sure that you'd outpace me in no time."
    "Is he mistakingly thinking that frail children like me can pull off Herculean deeds on the fly!?"
    "I am sure I look quite active when compared to someone like [nickname_old] Old but still, this isn't even worth mentioning."
    "..."
    "Sorry [nickname_old] Old."
    h "No, I.. I won't give.."
    bs_jsmug "Did I perhaps wake your competitiveness?"
    bs_jstandard "Don't waste you energy and let's go straight to the finish line then."
    bs_jlookaway "We'll cut the course short."
    h "Huff.."
    
    scene bg bridge with fade
    show tooltip_background
    show expression Text(_("Noon"), size=40, color="#f9aa19", yalign=0.008, xalign=.95, drop_shadow=(2, 2)) as text
    stop sound fadeout 2.0
    play sound river loop

    show barte jog standard with dissolve
    b "Phew, that was good."
    h "How long did we jog? {w}Huff.. Surely more than an hour."
    show barte jog smug with dissolve
    b "Quite the marathon, right?"
    show barte jog lookaway with dissolve
    b "But you did good, this deserves some kind of reward."
    h "Games on my smartphone! Pronto!"
    show barte jog smug with dissolve
    b "{i}Your{/i} smartphone?"
    show barte jog standard with dissolve
    b "But no. You'll get something better."
    h "What could possibly surpass the vast universe of mobile games?"
    b "It's currently {color=#f9aa19}noon{/color} right now."
    b "If you head to the pub right about now, you'll get the best cake in town for free."
    h "I am not really interested in cake and especially not after such a heavy exercise."
    b "Then take some with you, bring them to Old. {w}You should know his deep passion for cakes by now, right?"
    h "Hmm.."
    show barte jog closed with dissolve
    b "Ah, right. "
    show barte jog standard with dissolve
    extend "You won't get the cake just solely by going there, you'll need to say the following:"
    b "{b}What would pleasure be if it were not accompanied by vice?{/b}"
    h "What do you mean, I have to say that?"
    h "Aren't you going to be there?"
    show barte jog smug with dissolve
    b "No I won't."
    show barte jog lookaway with dissolve
    b "You'll find out on your own eventually."
    show barte jog standard with dissolve
    b "I gotta go now, I have another friend to meet."
    hide barte with dissolve
    h "Uhm."
    "Okay, that was quick."
    "He was gone in the blink of an eye."
    "But look at the clock, my time and my calories have been burnt to a crisp!"
    "Now to find a new place to hang out.."
    
    $barte_points += 1
    $bridge_unlock += 1
    $progression += 1
    $now_bridge = True
    
    jump freetime2
    
    
################################################################################
#Chapter 2.4 : Second Freetime

label freetime2:
    $ save_name = "Chapter 2.4 - Noon Freetime"
    with fade
    h "Well, what should I do now?"
    
    $park_check = False
    $bench_check = False
    $bridge_check = False
    $cafe_check = False
    $house_check = False
    
    $namechange_old = False
    $meeting_liz = 0
    
    show smartphone map2 at pullup
    $ renpy.pause(1.5, hard=True)
    call screen true_landkarte

    $ click = _return
        
    if click == "pw":
        jump pw_input
        
    if click == "pp":
        jump pingpong_play
    
    if click == "house1":
        $park_check = False
        $bench_check = False
        $bridge_check = False
        $cafe_check = False
        $house_check = True
        
    if click == "park":
        $park_check = True
        $bench_check = False
        $bridge_check = False
        $cafe_check = False
        $house_check = False
        
    if click == "park1":
        $bridge_check = False
        $bench_check = True
        $park_check = False
        $cafe_check = False
        $house_check = False
        
    if click == "bridge1": 
        $park_check = False
        $bridge_check = True
        $cafe_check = False
        $house_check = False
        $bench_check = False
        
    show smartphone map2 at pullout
    $ renpy.pause(1.5, hard=True)
    hide smartphone map2
    $ renpy.block_rollback()
    if bench_check:
        h "Should I spend my time at the {a=bencha_desc}lonely park bench{/a} until {color=#FD8204}afternoon{/color}?"
    elif bridge_check:
        h "Should I head to the {a=cafe_desc}pub{/a} and spend time until {color=#FD8204}afternoon{/color}?"
    elif house_check:
        h "Should I go {a=home_desc}home{/a} for now and keep [nickname_old] Old company until {color=#FD8204}afternoon{/color}?"
    elif park_check:
        h "Should I spend my time at the {a=park_desc}park{/a} until {color=#FD8204}afternoon{/color}?"
    menu:
        "Yes!":
            if bench_check:
                $park_check = False
                $bench_check = False
                $bridge_check = False
                $cafe_check = False
                $house_check = False
                
                $now_park0 = False
                $now_bridge = False
                $now_park1 = False
                $now_home = False
                $now_cafe = False
                jump park1
                
            elif bridge_check:
                $park_check = False
                $bridge_check = False
                $cafe_check = False
                $house_check = False
                $bench_check = False

                $now_park0 = False
                $now_bridge = False
                $now_park1 = False
                $now_home = False
                $now_cafe = False
                jump cafe
                
            elif house_check:
                $park_check = False
                $bench_check = False
                $bridge_check = False
                $cafe_check = False
                $house_check = False
                
                $now_park0 = False
                $now_bridge = False
                $now_park1 = False
                $now_home = False
                $now_cafe = False
                jump home
            else:
                $park_check = False
                $bench_check = False
                $bridge_check = False
                $cafe_check = False
                $house_check = False
                
                $now_park0 = False
                $now_bridge = False
                $now_park1 = False
                $now_home = False
                $now_cafe = False
                jump park0
        "No.":
            jump freetime2
            
            
            

#######################################################
#Chapter 2.4a : Second Freetime (Park)        BENCH A  
            
label park1:
    $save_name = "Chapter 2.4a - The encounter at the Bench"
    $now_park = True
    h "Let's approach those people by the bench."
    stop music fadeout 2.0
    stop sound
    
    scene bg bench with fade
    show prittner stranger:
        xalign .1 yalign .5
    show barte jog stranger:
        xalign .9 yalign .5
    with dissolve
    play music prittner fadein 2.0
    hide screen gui_tooltip
    $ renpy.block_rollback()
    
    window hide
    nv "The turbulent wind rouses the grass by the bench while two men stand around it.\n"
    nv "Their physique being overshadowed by the hissing of the dull atmosphere, words can barely be made out.\n"
    bv "Anything else you want to report on?"
    pv "The kid's doing fine, better than I have expected to be honest."
    bv "On the other hand, you seemed to be more under shocked than the people involved."
    pv "Incident's taken a little bit of a toll on me, life's been turn'd around, you know?"
    pv "But that kind of incident is just standard fare for somebody like me."
    nvl clear
    
    bv "It doesn't look like a \"standard fare\" to me, Prittner."
    bv "You're to relay my earnings once a month and I am truly grateful for your services so far."
    bv "But with her death, the termination of that arrangement is inevitable; the reason for its existence voided."
    bv "You should be happy. {w}You're now free from our contract."
    pv "Happy? {w}I beg to differ."
    nvl clear
    
    pv "Finding a new purpose in my godforsaken life has been a challenge for me like nothing else."
    pv "Don't think that you're getting out of this affair without a moment's guilt."
    bv "You have simply overestimated your role in this whole charade, that's all."
    bv "This has nothing to do with purpose, nothing to do with the road you want to walk on in life."
    bv "I'll stay unstained by any kind of feeble emotions."
    bv "Acting all agitated about it is just plain stupid and will only distance us from life."
    pv "\"Distance us from life?\" This wasteland out here is the farthermost reach of life itself."
    pv "You have long discarded your role in this farce, you have absolutely nothing to say to me."
    nvl clear
    
    bv "Hmpf, suit yourself then."
    pv "Don't you run away from your responsibilities."
    bv "My place is here and my responsibilities therein."
    pv "And therein lies the rub."
    pv "You're leading a double life now but I wonder in which life your heart is truly beating."
    bv "..."
    pv "You gave purpose to the life of this mere bum and life in the city has kind of roughed me up."
    bv "You will do fine here so just take it as a vacation for now, okay?"
    nvl clear
    
    pv "Whatever."
    pv "And let me also say this: {w}Her death has nothing to do with him."
    pv "But he's still the only one who's facing it head on."
    pv "That's when it dawned on me."
    pv "We're all just trashy pieces of a grand puzzle, you and me."
    pv "So don't you dare abandon him, too."
    pv "And don't you hide vital pieces of the puzzle either, or else it will never be completed."
    pv "I'll see you at the pub so give me some beer later to take this trashy mood off me."
    play sound steps
    show prittner stranger:
        linear 1.5 xalign -0.5
        
    nvl clear
    nv "\nWith heavy steps, a shadow is distancing itself from the bench."
    bv "I never abandoned anyone."
    bv "Because this arrangement was put into motion to make sure of it."
    nv "\nA lonesome sigh is emitted to the air that is unable to hear."
    nvl clear
    window show
    
    play music new_morning fadeout 2.0 fadein 2.0
    h "Barty?"
    show barte jog surprised with dissolve
    b "Heiden?"
    show barte jog lookaway:
        linear .5 xalign .5
    with dissolve
    
    show tooltip_background
    show bench_emergency with dissolve
    if progression == 1:
        show expression Text(_("Noon"), size=40, color="#f9aa19", yalign=0.008, xalign=.95, drop_shadow=(2, 2)) as text
    else:
        show expression Text(_("Afternoon"), size=40, color="#FD8204", yalign=0.008, xalign=1.0, drop_shadow=(2, 2)) as text
        
    b "Fancy meeting you here."
    h "I thought I heard you speaking to someone."
    show barte jog standard with dissolve
    b "Ah yeah, I was meeting up with a friend."
    show barte jog lookaway with dissolve
    b "But he was kind of moody due to the weather."
    h "Could be better, yeah."
    show barte jog standard with dissolve
    b "Don't you hang out here all by yourself, kid's these days oughta take care of themselves."
    h "I never intended to do so."
    show barte jog lookaway with dissolve
    b "That's good, then."
    hide barte with dissolve
    bs_jstandard "I'll see you around, Heiden."
    bs_jlookaway "Gotta do some shopping before the pub opens."
    h "Okay, I'll see you later!"
    "Hm, what's with him?"
    "Oh well, let's get back to the park then."
        
    $progression += 1
    $park_unlock += 1
    scene bg park
    show tooltip_background
    if progression == 2:
        show expression Text(_("Afternoon"), size=40, color="#FD8204", yalign=0.008, xalign=1.0, drop_shadow=(2, 2)) as text
        jump freetime3
    else:
        show expression Text(_("Evening"), size=40, color="#ba0b0b", yalign=0.008, xalign=0.98, drop_shadow=(2, 2)) as text
        jump freetime4
    return
    
    
    
#######################################################
#Chapter 2.4b : Second Freetime (Café) 

label cafe:
    $save_name = "Chapter 2.4b - Wondrous cakes at the Café"
    $now_cafe = True
    $meeting_liz = 1
    h "Let's go check out the pub."
    stop music fadeout 2.0
    stop sound
    
    $ renpy.block_rollback()
    hide screen gui_tooltip
    show black with fade
    play sound pubdoor
    centered "Hm, wait."
    centered "The pub is indeed operating right now but the ambient is quite different from yesterday..."
    
    scene bg pub with fade
    play music lisette
    show tooltip_background
    show pub_emergency with dissolve
    play sound chatter loop
    show expression Text(_("Noon"), size=40, color="#f9aa19", yalign=0.008, xalign=.95, drop_shadow=(2, 2)) as text
    
    h "Uhm."
    "Okay."
    "I am reassessing the situation here."
    "I wouldn't call it a pub."
    hide pub_emergency with dissolve
    "Calling it a pub is quite an overstatement to begin with."
    "This place is crawling with elderly madams, dining away on their pies and cakes."
    "How this entire customer base could be replaced like that is just little short of a miracle."
    
    show lisette standard with dissolve
    lx "Oh, a customer!"
    h "Uhm."
    lx "No need to be shy, I haven't seen you around here."
    show cafe_emergency with dissolve
    lx "Welcome to the café! {w}I'll lead you to an empty table."
    hide lisette with dissolve
    "I am lost for words."
    "I certainly didn't expect something like this."
    with hpunch
    "After being walked to a nearby table, she hands me something that looked awfully like a menu and takes off."
    "Which leaves me with the realization:"
    " There was no indication whether this place was supposed to be a café or a pub."
    "From what I can see, the funiture in here certainly works both ways."
    "Elderly ladies are dining on the same tables that were occupied by ruffians yesterday."
    "Though it would be wise not to mention that fact in the presence of the women."
    
    show lisette standard with dissolve
    lx "Have you decided on something yet?"
    h "Oh, uhm."
    "I haven't thought about bringing money with me so ordering something is out of the question."
    "What did Barty tell me before?"
    "I had to say something in order to get {b}a cake for free{/b}?"
    "Well, it's worth a shot I guess."
    show lisette serious with dissolve
    lx "Uhm, maybe you need more time?"
    lx "I am sorry, I guess it sounds like I am hurrying you."
    h "No, that's not it!"
    h "Miss Waitress, I have something to tell you!"
    show lisette standard with dissolve
    lx "Well, let's hear it."
    l "Oh and my name is Lisette."
    h "My name is Heiden!"
    l "Hello. {w}Heiden it is, then."
    h "Uhm."
    $sade = 0
    
    menu:
        "In order to know pleasure, we must first acquaint ourselves with vice.":
            pass
        "What would be pleasure if it's accompanied by virtue?":
            pass
        "What would pleasure be if it were not accompanied by vice?":
            jump sade_true


label sade_false:
    show lisette serious with dissolve
    l "Uhm, okay?"
    "Wasn't that correct, after all?"
    "It doesn't feel like she picked up on a secret code, which means I've probably messed something up."
    show lisette standard with dissolve
    l "In case this is your first visit to this kind of venue, let me treat you to a slice of cake."
    hide lisette with dissolve
    h "Please don't bo-"
    "Ah, she's already making haste to another table."
    "I've clearly lost the thread of the whole deal."
    "Aside from the fact that I probably won't get a cake for [nickname_old] Old, my chances of getting out of here unscathed is steadily declining too."
    "Elderly Lady" "'s no need fer such a worrisome face, young'sh!"
    "It seems that my worries could be read straight from my face like a book."
    "And elderly lady nearby winks at me with a rather cordial charisma, the kind of aura that elderly people tend to emit."
    "Elderly Lady" "Yer one odd fella fer sayin' that kinda babble, ho ho!"
    h "I am sorry, I guess I didn't think that one through. {w}That definitely confused her."
    "Elderly Lady" "S'fine, lad. {w}She done dealt with much bigger hassles in the past, ho ho!"
    "The elderly lady is laughing heartily as she says that but it honestly doesn't make me feel better."
    jump cakey
    
    
label sade_true:
    $meeting_liz = 2
    l "Oh."
    show lisette embarrassed with dissolve
    l "You're citing Marquis de Sade, right?"
    l "But you're so young and yet you read his works?"
    h "Uhm."
    l "Wait a bit."
    hide lisette with dissolve
    "Did I say something wrong?"
    "She obviously didn't sound all that happy after hearing what Barty told me."
    "I've noticed a certain holler from an elderly lady who was sitting at a nearby table."
    "Elderly Lady" "Ya done made her sheepish, young'sh. Ho ho!"
    "She is laughing heartily but I didn't understand."
    h "I am sorry, madam. {w}I don't quite follow you?"
    "Elderly Lady" "Yer one mighty lad to bring spring to her cheeks."
    "Elderly Lady" "Lookin' at her's like lookin' atta mirror!"
    h "Well, if you say so.."
    "She looks like she's reminiscing in her memories so I better leave her be."
    
    
label cakey: 
    show lisette standard with dissolve
    l "I am sorry to keep you waiting."
    show lisette standard at twitchtwice
    l "I'll give you a slice of my special cake that I've been baking this morning."
    if meeting_liz == 2:
        show lisette embarrassed with dissolve
        l "You know, I am also a firm believer of the Marquis' holy teachings."
        l "Can't really judge a book by its cover nowadays, who knew that Marquis de Sade reached the youth by now."
    show lisette standard with dissolve
    l "The cake's on the house. {w}Please enjoy it."
    hide lisette with dissolve
    "I am actually here to take the cake home with me but I can't possibly say it with the cake ready to eat."
    if meeting_liz == 2:
        "Not sure what spell I chanted to make her act this way but I think it's better to leave her in disbelief for now."
        "Though it's partially because I couldn't pay for the cake infront of me incase I accidentally spill the beans."
    h "Well, here I go."
    
    play sound fork
    "Oh, the cake dough is so delicate and yet so firm."
    "But the most intriguing thing about it is the color."
    "A bright and scorching red dough is presented, two layers of red being separated by a thin but heavy looking cream."
    "I am filled with an extremely addictive taste yet for a cake it's not too sweet for me to complain."
    "I am slowly turning into a cake fanatic as I grasp the passion that [nickname_old] Old is always overindulging himself with."
    "Truly a devilish masterpiece of a cake!"
    show lisette standard with dissolve
    l "I see that the cake was to your liking!"
    l "Though it's not yet on the menu, I'll make it an effort to turn this Red Velvet Cake into a stable of the café."
    h "It was really good!"
    "Elderly Lady" "Yer pampering him quite a bunch, Liz my dear."
    show lisette serious with dissolve
    l "What are you saying, madam?"
    
    if meeting_liz == 2:
        l "This kid and me, we're like comrades in arms! {w}\nAnd with the words of the Marquis' as our guide!"
        "Elderly Lady" "Sure sure, ah'm just messing with yer, ho ho!"
    else:
        l "This kid was probably really nervous earlier, seeing that this might have been his first visit to a café all by himself!"
        "That's not true though."
        "Elderly Lady" "Ah say he's doin' mighty fine, ho ho!"
        
    show lisette annoyed with dissolve
    l "Hmpf."
    show lisette standard with dissolve
    l "But either way, you're free to come back anytime you want."
    l "This café's open everyday from {color=#f0ff00}morning{/color} 'til {color=#FD8204}afternoon{/color} with the exception of tuesday!"
    h "Is this café closing when it's afternoon?"
    l "Actually no, the café is reopened as a different café"
    show lisette serious with dissolve
    extend " for other kinds of guests."
    show lisette standard with dissolve
    l "You see, some guests don't mingle well with others."
    "Yeah. From what I've seen yesterday, this sentiment definitely holds true."
    show lisette serious with dissolve
    l "We made our best effort to let both sorts of guests enjoy what they're here for."
    show lisette standard with dissolve
    l "Good service and good cake."
    h "Yeah, that I can understand."
    h "Uhm."
    l "What is it? {w}Do you want seconds, by the way?"
    
    if meeting_liz == 1:
        "I can't possibly ask for more nor can I find the courage to ask for take away."
        "The cake was good and I am honestly happy that I could somehow keep the situation stable."
        "Let's keep it like that instead of pushing my luck."
        h "Uhm, that's okay. {w}I think I had enough for now."
        with hpunch
        "With a pampered stomach, I make my way to the door."
        jump cakey_bye
        
    h "Actually, I know it sounds rude but I know that my uncle at home would be excited to eat this cake of yours."
    h "I was hoping to bring some with me, {w}as a sign of promoting the cake, you see!"
    l "Ah, there lies the nub of the matter."
    show lisette serious with dissolve
    l "Normally I would be opposed to the idea of giving freebies."
    "I knew it."
    show lisette standard with dissolve
    l "But for you I'll make an exception, but only this once!"
    h "Are you serious?"
    show lisette annoyed with dissolve
    l "Do you thing I'm lying?"
    h "No, that's not it!"
    show lisette standard with dissolve
    l "If that's the case, wait here while I get another slice ready."
    hide lisette with dissolve
    h "Maybe this really sounded selfish of me.."
    "Elderly Lady" "Not the case at all, young'sh."
    "Elderly Lady" "Ah done say the Old after sunset s'been more selfish for cake."
    h "You know my uncle, madam? {w}He also loves cakes, you know?"
    "Elderly Lady" "Ah think it is yer uncle, then."
    "Elderly Lady" "But no telling Liz or else yer cake's gone fer good, ho ho!"
    h "Yeah, there's no denying that."
    h "But what do you mean with {i}the old after sunset{/i}?"
    "Elderly Lady" "This café, my lad."
    "Elderly Lady" "The ambient changes and so're people."
    h "Is my uncle a baddie, madam?"
    "Elderly Lady" "Ho ho, my dear. {w}He's done eating all her cakes like a madman, been driving her crazy."
    "Elderly Lady" "Consequence being, she don' baking after sunset no more."
    "Elderly Lady" "Not'o mention that she's done moody whenever he's around, ho ho!"
    h "So my uncle loves cakes so much that he is basically forcing her out of the kitchen."
    "Man, now I feel kind of bad for ordering her for cake that's going straight into [nickname_old] Old's stomach."
    show lisette standard with dissolve
    l "Here I am"
    show lisette at twitchtwice
    extend " with the cake."
    h "Thank you, Lisette!"
    l "Well, no need to thank me."
    l "Be sure to ask your uncle for feedback!"
    h "I will, I'll be going now!"
    "With the cake in a plastic wrap, I make my way to the door."

label cakey_bye:
    h "Thank you for everything! {w}And you too, madam!"
    "Elderly Lady" "*wink*"
    l "Bye bye!"
    hide lisette with dissolve
    
    "Now with that out of the way, let's look at our plans for the afternoon..."
    hide cafe_emergency
    $progression += 1
    $bridge_unlock += 1
    $barte_points += 1
    show tooltip_background
    show expression Text(_("Afternoon"), size=40, color="#FD8204", yalign=0.008, xalign=1.0, drop_shadow=(2, 2)) as text
    jump freetime3

#######################################################
#Chapter 2.4c : Second Freetime (Home) 
            
label home:
    $ save_name = "Chapter 2.4c - The Weed Whisperer"
    $now_home = True
    h "Time to head back home for now."
    stop music fadeout 2.0
    stop sound
    scene bg livingroom with fade
    show tooltip_background
    show expression Text(_("Noon"), size=40, color="#f9aa19", yalign=0.008, xalign=.95, drop_shadow=(2, 2)) as text
    play music at_home fadein 2.0
    
    $ renpy.block_rollback()
    h "[nickname_old]! I am home!"
    "..."
    "Huh, he's not here?"
    "The sofa that was occupied this morning is now laying in bare state."
    "Hm... if he's not here, where-"
    "Oh, wait. {w}The door leading to the terrace is wide open."
    
    scene bg terrace with wipeleft
    show tooltip_background
    show expression Text(_("Noon"), size=40, color="#f9aa19", yalign=0.008, xalign=.95, drop_shadow=(2, 2)) as text
    
    show old funeral normal with dissolve
    o "Hum, hum hum hum."
    h "What are you doing out here, [nickname_old]?"
    o "Oh hey, Heiden. {w}You're back from your adventures?"
    
    if park_unlock == 2:
        h "Yeah, I played in the park."
    else:
        h "Yeah, I jogged around the town."
    o "I am sure you had a lot of fun."
    
    if nickname_old == "Mister":
        o "But now that we're on the topic, I really think that getting called \"Mister\" here and \"Mister\" there doesn't really make us more connected, you know?"
        h "?"
        o "Hm, what I am trying to say is that when you're dealing with more than one person at the time, it's easy to get out of hand with all the \"Misters\", right?"
        h "So should I call you Uncle, then?"
        show old funeral wink with dissolve
        $ oldname = "Uncle Old"
        o "That's what I was aiming at!"
        o "True family ties."
        o "It's good that we're tuned on the same wavelength now."
        
        $namechange_old = True
        $nickname_old = "Uncle"
        $old_points += 1
        
    h "So anyways, what are you doing here?"
    show old funeral tired with dissolve
    o "Just trying to take care of some plants."
    h "Oh, that's admirable."
    h "But [nickname_old]."
    show old funeral normal with dissolve
    o "What is it?"
    h "You're watering weeds."
    show old funeral tired with dissolve
    o "Yeah, they're pretty easy to cultivate."
    o "You should try it out yourself if you ever have the time."
    h "Well, yeah I better pass up on that offer."
    show old funeral normal with dissolve
    o "But you should at least know how to grow some good crops or something, right?"
    o "Let me show you."
    h "Uhm, well if you insist."
    
    scene black with fade
    show tooltip_background
    show expression Text(_("Noon"), size=40, color="#f9aa19", yalign=0.008, xalign=.95, drop_shadow=(2, 2)) as text
    os_normal "Woah! You're doing good so far, Heiden!"
    hs_tired "Hm, but all I am doing is pouring water over the weeds."
    os_normal "Don't think of them as weeds, think of them as..."
    os_tired "Uhm."
    os_wink "Friends! Yeah, you're watering your best friends right now."
    hs_tired "This is the most sad thing I've yet to hear today."
    
    scene bg livingroom with wiperight
    show tooltip_background
    show expression Text(_("Afternoon"), size=40, color="#FD8204", yalign=0.008, xalign=1.0, drop_shadow=(2, 2)) as text
    h "Thanks [nickname_old] Old, I've become a master in weed gardening."
    os_tired "C'mon, Heiden. {w}What's with that look on your face when you said that?"
    "It's alright. I am sure that someone out there will understand your true splendor, [nickname_old]."
    "With my worries out of the way, it's time to spend time somewhere else."
    
    $home_unlock += 1
    $progression += 1
    $old_points += 1
    jump freetime3
    return            
            

#######################################################
#Chapter 2.5 : Last Freetime

label freetime3:
    $ save_name = "Chapter 2.5 - Afternoon Freetime"
    with fade
    h "Well, what should I do this afternoon?"
    
    $park_check = False
    $bench_check = False
    $bridge_check = False
    $cafe_check = False
    $house_check = False
    
    $meeting_prittner = False
    
    show smartphone map2 at pullup
    $ renpy.pause(1.5, hard=True)
    call screen true_landkarte

    $ click = _return
        
    if click == "pw":
        jump pw_input
        
    if click == "pp":
        jump pingpong_play
    
    if click == "housea": #HomeA
        $cafe_check = True
        $park_check = False
        $bench_check = False
        $house_check = False
        
    if click == "houseb": #HomeB
        $house_check = True
        $park_check = False
        $bench_check = False
        $cafe_check = False
        
    if click == "park1": #BenchA
        $park_check = True
        $bench_check = False
        $cafe_check = False
        $house_check = False
        
    if click == "benchb": #BenchB
        $bench_check = True
        $park_check = False
        $cafe_check = False
        $house_check = False
        
        
    show smartphone map2 at pullout
    $ renpy.pause(1.5, hard=True)
    hide smartphone map2
    $ renpy.block_rollback()
    if cafe_check and meeting_liz == 2:
        h "Should I take the cake with me and go {a=homea1_desc}home{/a} for now to keep [nickname_old] Old company until {color=#ba0b0b}evening{/color}?"
    elif cafe_check and meeting_liz == 1:
        h "Should I go {a=homea2_desc}home{/a} for now and keep [nickname_old] Old company until {color=#ba0b0b}evening{/color}?"
    elif house_check and park_unlock == 3:
        h "Should I finally head back {a=homeb2_desc}home{/a} and keep [nickname_old] Old company until {color=#ba0b0b}evening{/color}?"
    elif house_check:
        h "Should I stay at {a=homeb_desc}home{/a} for now and keep [nickname_old] Old company until {color=#ba0b0b}evening{/color}?"
    elif park_check:
        h "Should I spend my time at the {a=bencha_desc}lonely park bench{/a} until {color=#ba0b0b}evening{/color}?"
    else: #bench_check
        h "Should I spend my time again at the {a=benchb_desc}park{/a} until {color=#ba0b0b}evening{/color}?"
    menu:
        "Yes!":
            if cafe_check:
                $park_check = False
                $bench_check = False
                $cafe_check = False
                $house_check = False
                
                $now_park0 = False
                $now_bridge = False
                $now_park1 = False
                $now_home = False
                $now_cafe = False
                if meeting_liz == 2:
                    jump homeA
                else:
                    jump homeB
                
            elif house_check:
                $park_check = False
                $bench_check = False
                $cafe_check = False
                $house_check = False

                $now_park0 = False
                $now_bridge = False
                $now_park1 = False
                $now_home = False
                $now_cafe = False
                jump homeB
                
            elif park_check:
                $park_check = False
                $bench_check = False
                $cafe_check = False
                $house_check = False
                
                $now_park0 = False
                $now_bridge = False
                $now_park1 = False
                $now_home = False
                $now_cafe = False
                jump park1
                
            else: #bench_check
                $park_check = False
                $bench_check = False
                $cafe_check = False
                $house_check = False
                
                $now_park0 = False
                $now_bridge = False
                $now_park1 = False
                $now_home = False
                $now_cafe = False
                jump park2
        "No.":
            jump freetime3
            
            
#######################################################
# Definition Labels 

label bencha_desc:
    definition "{b}Lonely Park Bench{/b}\nAfter playing at the park, I've come across a pretty secluded looking park bench. I can see familiar looking people but can't make them out from the distance.\n\nShould I approach them?"
    return
    
label cafe_desc:
    definition "{b}The Pub{/b}\nBarty told me to go to the pub around {color=#f9aa19}noon{/color} if I want to get free cake. But if Barty's out here, who's working at the pub right now?\n\nI am interested enough to find out."
    return
    
label home_desc:
    definition "{b}[nickname_old] Old's House{/b}\nI am kind of worried about [nickname_old] Old right now. He's alone at home, anything can happen if you leave him alone for even a split second.\n\nMaybe he's grateful for some company."
    return 
    
label benchb_desc:
    definition "{b}The Park{/b}\nAfter meeting Barty, I've made my way back to the park. But it seems like I've come across someone.\n\nMaybe I should speak to him after all..."
    return
    
label homea1_desc:
    definition "{b}[nickname_old] Old's House{/b}\nNow that I am in the possession of Lisette's cake, I can either make this one of [nickname_old] Old's happiest days... or I can just hide the cake away from his thieving eyes.\n\nEither way, it's gonna be really fun."
    return
    
label homea2_desc:
    definition "{b}[nickname_old] Old's House{/b}\nSeems like I couldn't get the cake after all. But spending time at home with [nickname_old] Old might prove to be interesting.\nIf else, there's a television that I could use to pass the time.\n\nThere's nothing wrong with watching cartoons on television, I guess."
    return
    
label homeb_desc:
    definition "{b}[nickname_old] Old's House{/b}\nNow that I am at home, I'm not too thrilled to go outside again.\nAnd [nickname_old] Old seems to be doing better than before.\n\nThere's nothing wrong with staying at home and watching cartoons on television, I guess."
    return
    
label homeb2_desc:
    definition "{b}[nickname_old] Old's House{/b}\nEnough playing at the park! I am tired from all the playing that I just want to occupy the sofa in the living room and watch some cartoons.\n\nThere's nothing wrong with staying at home and watching cartoons on television, I guess."
    return
    
label final_desc:
    definition "{b}The Pub{/b}\nAnother evening, another visit to the pub!\nI guess I slowly understand why Uncle Old cherishes the pub even though he doesn't touch alcohol. The pub is like a focal point of our town's social interaction.\n\nLet's not keep everyone waiting!"
    return