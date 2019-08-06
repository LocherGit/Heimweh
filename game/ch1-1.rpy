#######################################################################################################

# Declare characters again
define nv = Character(None, kind=nvl)
define hv = Character(None, kind=nvl, what_prefix="\"", what_suffix="\"", what_color="#1d87da")

define x = Character('???', color="#1d87da")
define h = Character('Heiden', color="#1d87da")
define mm = Character('Middle-aged Man', color="#d72b2b")

define o = DynamicCharacter(_("oldname"), color="#d72b2b")
define os_normal = DynamicCharacter(_("oldname"), color="#d72b2b", window_left_padding=160, show_side_image=Image("images/character/old_side_normal.png", xalign=0.0, yalign=1.0))
define os_troubled = DynamicCharacter(_("oldname"), color="#d72b2b", window_left_padding=160, show_side_image=Image("images/character/old_side_troubled.png", xalign=0.0, yalign=1.0))
define os_tired = DynamicCharacter(_("oldname"), color="#d72b2b", window_left_padding=160, show_side_image=Image("images/character/old_side_tired.png", xalign=0.0, yalign=1.0))
define os_wink = DynamicCharacter(_("oldname"), color="#d72b2b", window_left_padding=160, show_side_image=Image("images/character/old_side_wink.png", xalign=0.0, yalign=1.0))

define b = Character('Bartender', color="#62ac5b")
define bs_standard = Character('Bartender', color="#62ac5b", window_left_padding=160, show_side_image=Image("images/character/barte_side0.png", xalign=0.0, yalign=1.0))
define bs_lookaway = Character('Bartender', color="#62ac5b", window_left_padding=160, show_side_image=Image("images/character/barte_side1.png", xalign=0.0, yalign=1.0))
define bs_closed = Character('Bartender', color="#62ac5b", window_left_padding=160, show_side_image=Image("images/character/barte_side2.png", xalign=0.0, yalign=1.0))
define bs_surprised = Character('Bartender', color="#62ac5b", window_left_padding=160, show_side_image=Image("images/character/barte_side3.png", xalign=0.0, yalign=1.0))
define bs_smile = Character('Bartender', color="#62ac5b", window_left_padding=160, show_side_image=Image("images/character/barte_side4.png", xalign=0.0, yalign=1.0))
define bs_smug = Character('Bartender', color="#62ac5b", window_left_padding=160, show_side_image=Image("images/character/barte_side5.png", xalign=0.0, yalign=1.0))


#Declare background images
image bg cemetery = "images/used bg/ch1_cemetery.jpg"
image bg cemetery2 = "images/used bg/ch1_cemeterycolor.jpg"
image bg train_stop = "images/used bg/ch0_train.jpg"
image bg trainstation = "images/used bg/ch1_trainstation.jpg"
image bg bakery = "images/used bg/ch1_bakery.jpg"
image bg city = "images/used bg/ch1_city.jpg" 
image bg wayhome1:
    "images/used bg/ch1_homeway.jpg"
    ypos 1.96
    linear 7 ypos 1.0
    
image bg wayhome2 = "images/used bg/ch1_homeway2.jpg"
image bg wayhome2night = "images/used bg/ch1_homeway2_night.jpg"

image bg house:
    "images/used bg/ch1_house.jpg"
    ypos 1.5 xalign 0.5
    pause 3.0
    linear 4.0 ypos 1.0
    
image bg house_night:
    "images/used bg/ch1_house_night.jpg"
    ypos 1.7 xalign 0.5
    pause 1.0
    linear 4.0 ypos 1.0
    
image bg livingroom = "images/used bg/livingroom.jpg"
image bg bedroom = "images/used bg/bedroom_heiden.jpg"
image bg weather = "images/used bg/ch1_weather.jpg"
image bg pub = "images/used bg/ch1_pub.jpg"
image bg pubnight = "images/used bg/ch1_pub_night.jpg"

#Declare character images
image old funeral normal = "images/character/old_funeral.png"
image old funeral troubled = "images/character/old_funeral2.png"
image old funeral tired = "images/character/old_funeral3.png"
image old funeral wink = "images/character/old_funeral4.png"

image barte normal standard = "images/character/barte_standard0.png"
image barte normal lookaway = "images/character/barte_standard1.png"
image barte normal closed = "images/character/barte_standard2.png"
image barte normal surprised = "images/character/barte_standard3.png"
image barte normal smile = "images/character/barte_standard4.png"
image barte normal smug = "images/character/barte_standard5.png"
image barte thinking standard = "images/character/barte_thinking0.png"
image barte thinking lookaway = "images/character/barte_thinking1.png"
image barte thinking closed = "images/character/barte_thinking2.png"
image barte thinking surprised = "images/character/barte_thinking3.png"
image barte thinking smile = "images/character/barte_thinking4.png"

image crowd = "images/etc/funeral_crowd.png"

#Declare other images
image kuchen1 = "images/etc/baumkuchen.png"
image kuchen2 = "images/etc/bienenstich.png"
image old gray = im.Grayscale("images/character/old_funeral3.png")
image old green = im.Map("images/character/old_funeral3.png", rmap=im.ramp(0, 0))
image old hue = im.MatrixColor("images/character/old_funeral3.png", im.matrix.hue(90))
image old invert = im.MatrixColor("images/character/old_funeral3.png",[ -1,  0,  0, 0, 1, 0, -1,  0, 0, 1, 0,  0, -1, 0, 1, 0,  0,  0, 1, 0, ])

#declare transformation/animation in ch1
transform oob_left:
    xpos -0.5
    
transform oob_right:
    xpos 1.5
  
transform spin:
    linear 1.0 xzoom -1.0
    
transform spinback:
    linear 1.0 xzoom 1.0
    
transform pulse:
    block:
        linear .1 zoom 1.05
        linear .1 zoom 1.0
        pause 1.0
        repeat
        
transform NullTransform:
    pass
    
transform invi_visible:
    alpha 0.0
    linear 2.0 alpha 1.0
    
transform facingON:
    ypos 0.0 zoom 1.8 xalign 0.5
    
define slowBlack = Dissolve (5.0)
    
image bakery_look1:
    subpixel True
    size (800, 600)
    xalign .5
    yalign .5
    "images/used bg/ch1_bakery.jpg"
    crop (128, 378, 252, 189)
    pause 1.0
    easeout 2.0 crop (160, 400, 200, 150)
    
image bakery_look2:
    subpixel True
    size (800, 600)
    xalign .5
    yalign .5
    "images/used bg/ch1_bakery.jpg"
    crop (120, 300, 252, 189)
    easein 2.0 crop (150, 350, 337, 253)
    
image bakery_look3:
    subpixel True
    size (800, 600)
    xalign .5
    yalign .5
    "images/used bg/ch1_bakery.jpg"
    crop (100, 203, 383, 262)
    linear 4.0 crop (210, 350, 200, 200)
    
define fadehold = Fade(1.0, 1.0, 0.5)
    
screen disable_Lmouse():
    key "mouseup_1" action NullAction()
    
#Declare audio
define audio.sad2 = "audio/bgm/04 - At the Funeral.mp3"
define audio.home = "audio/bgm/05 - Brand New Day Pt.1.mp3"
define audio.new_morning = "audio/bgm/07 - Hello World!.mp3"
define audio.at_home = "audio/bgm/08 - Peaceful Days.mp3"
define audio.sleepyroom = "audio/bgm/09 - Sleep Tight.mp3"
define audio.evening = "audio/bgm/10 - Night Stroll.mp3"
define audio.pub = "audio/bgm/11 - The Pub.mp3"

#Declare sfx
define audio.electric_door = "audio/sfx/electric_door.mp3"
define audio.whisper = "audio/sfx/whisper.mp3"
define audio.trolly = "audio/sfx/trolley_bag.mp3"
define audio.fence = "audio/sfx/fence_open.mp3"
define audio.fork = "audio/sfx/fork.mp3"
define audio.water = "audio/sfx/water_pouring.mp3"
define audio.stairs = "<from 0 to 3>audio/sfx/wooden_stairs.mp3"
define audio.pillow = "<from 0 to 3>audio/sfx/pillow.mp3"
define audio.watch = "<from 0 to 2>audio/sfx/wristwatch.mp3"
define audio.plate = "audio/sfx/plate_table.mp3"
define audio.fallinbed = "audio/sfx/falling_in_bed.mp3"
define audio.shock = "audio/sfx/shock.mp3"
define audio.punch = "<from 1.05>audio/sfx/punch.mp3"
define audio.steps = "<from 0 to 8>audio/sfx/footsteps3.mp3"
define audio.crowd = "audio/sfx/pub_crowd.mp3"
define audio.pubdoor = "audio/sfx/pub_door.mp3"
define audio.glass = "<from 14 to 16>audio/sfx/glass.mp3"
define audio.silence = "audio/sfx/awkward_silence.mp3"
define audio.heartbeat = "audio/sfx/heartbeat.mp3"
define audio.gulping = "audio/sfx/gulping.mp3"
define audio.heaven = "audio/sfx/heaven.mp3"

#Special Screens

screen imagemap_cake:
    imagemap:
        auto "images/used bg/imagemap_%s.png"

        hotspot (0, 0, 250, 200) action Return("baumkuchen") alt "Baumkuchen"
        hotspot (550, 0, 250, 200) action Return("bienenstich") alt "Bienenstich"
        
screen imagemap_location:
    imagemap:
        auto "images/used bg/imagemap2_%s.jpg"

        hotspot (0, 0, 800, 100) action Return("upstairs") alt "Upstairs"
        hotspot (0, 300, 400, 300) action Return("table") alt "Table"
        hotspot (400, 300, 400, 300) action Return("coach") alt "Coach"

########################################################################################
#Chapter 1.0 : Flashback

label ch1:
    
#Declare variables
    $ renpy.block_rollback()
    $ languageON = False
    $ save_name = "Chapter 1.0 - Flashback"
    $ nickname_old = ""
    
    pause 2.0
    centered "When was the first time I felt like this?"
    pause 2.0
    
    play music sad2 fadein 5.0
    nv "A certain and indescribable kind of feeling takes hold of your heart when you begin to realize that noone is waiting for you at home."
    nv "It is exactly that moment when you feel your own home becoming something disconcerting. Something different. Something that is not home."
    nv "\nI heard it at first from Mrs. Becky from next door and as she gave her best to tell me something while trying to sound as comforting as possible, {w}some bad-looking officers joined and told me the same thing again."
    nv "\nThey repeatedly told me to stay calm but the way they said it wasn't really convincing to me. {w}From the way how they behaved infront of me, I could only guess that something really really bad happened."
    nv "\nBecause they were running up to me in a hurry like they had seen a superhero descending to earth and babbled noticeably nervous about stuff that went way over my head."
    
    nvl clear
    window hide
    
    nv "Of course I was speechless. And nervous. And scared."
    nv "There were three people sitting in the living room, Mrs. Becky and two misters, and Mom wasn't at home to offer some drinks and I was also not able to."
    nv "Because they told me that Mom was involved in a terrible car accident."
    nv "Apparently some traffic lights were acting up but my brain didn't even try to register anything after the first sentence."
    nv "She was transferred into the hospital immediately where she was being operated but things were looking grim."
    nv "\nI just sat there and stared at the blank faces of the officers and Mrs. Becky who was on the verge of crying herself."
    nv "Those weren't the faces of people who would joke around at a time like this."
    
    nvl clear
    window hide
    
    centered "Can I see Mom?"
    pause 2.0
    
    scene bg cemetery with dissolve
    
    nv "It's cold."
    nv "\nBut I guess there is nothing wrong with a cemetery being cold."
    nv "\nWith hot summery temperatures, people would unmistakenly end up looking forward to their turn instead."
    nv "\nThe weather really turned to the worst as if it was lamenting over the loss of Mom."
    nv "\nThough it doesn't make me feel any better as the weather dampens the mood even further than it already was."
    
    nvl clear
    window hide
    
    nv "After the news of my Mom's passing away reached relatives I never knew existed, they swiftly organized a burial service."
    nv "Apparently I had two uncles and one aunt living without a care in the world and without ever feeling the need to keep in touch with us."
    nv "Or they never had the intention in the first place, that was more the case I think."
    nv "The thing is, Mom might have been a pretty bad child herself when she was a kid."
    nv "That is the feeling I get when I met with the relatives."
    nv "Actually..."
    nv "Does holding eye contact for less than 5 seconds while saying empty greetings count as a reunion?"
    nv "I don't really know."
    nv "But I know that a reunion doesn't usually sound so pitiful and puny, especially if it's supposed to be a heartfilled get-together with a never before seen relative."
    
    nvl clear
    window hide
    
    nv "I guess I felt pretty lonely at that time for spouting such things."
    nv "Lonely and kind of unwanted."
    nv "Though loneliness itself didn't bother me that much because I became used to being alone due to my Mom's jobs."
    nv "Maybe there were several kinds of loneliness and I might not be resistant to all of them."
    nv "\nInfact, I tried my hardest not to express the loneliness that I was experiencing in order to not feel vulnerable myself."
    nv "\nI kept telling myself that, but the feeling of aching still remains."
    nv "\nThis kind of aching really was different, the thing that clung to my heart and lungs as if trying to rob me of my ability to stand at least unbothered."
    
    nvl clear
    window hide
    
    nv "With the passing of mere minutes, my posture slowly began to stiffen."
    nv "Maybe my body tried to enclose the beating of my heart so that the lively sound does not escape me as it did my mom."
    nv "I could hear the dulled noise of adults talking around me but there was a different kind of sensation mixed inbetween them."
    nv "I was being watched."
    nv "\nThough it was not a stinging kind of watched but more like being properly observed."
    nv "\nI felt kind of glad that my newfound relatives paid me no heed as they conversed with each other though sometimes I was the topic of the conversation myself, which partly troubled me."
    
    nvl clear
    window hide
    
    nv "Normally they would occasionally glance toward the person they talk about, right?"
    nv "\nBut they didn't."
    nv "And this troubled me."
    nv "\nFeeling nothing about being uncared for; there is no way other than feeling troubled, right?"
    nv "That is the reason why I found myself peeking to the discussion myself from the corner of my eye."
    nv "But I could not detect the one who was observing me."
    nv "He or she was not among the group of adults."
    nv "\nAt that exact moment I staggered with panic when all the sudden someone tapped my shoulder from behind."
    
    nvl clear
    window hide
    scene bg cemetery2
    show old funeral normal at oob_left
    show old normal:
        linear .5 xalign .5
    with vpunch 
    stop music
    play music home fadein 4.0
    
    h "WOAH."
    mm "You alright, kid?"
    mm "You're totally out of your wits, heh."
    "A dry laugh escaped his lips."
    h "Don't just randomly tip people from behind, Mister!"
    h "That's really creepy!"
    mm "Hey hey. No harm's done, right?"
    
    show old normal:
        linear 1.5 zoom 1.5 yalign 0.2
        
    mm "Hm."
    h "Ogling me like that is creepy, too."
    
    show old normal:
        linear .5 zoom 1.0 yalign 0.5
        
    mm "Nah. Just thinking that children really do take after their parents."
    mm "Even the ugly ones. Heh, {i}especially{/i} the ugly ones."
    "The man looked with distant eyes to the sky as if remincing the last moment he laid eyes on ugly children."
    "Like that wasn't rude toward me at all."
    mm "But fret not. You are not ugly, kid."
    h "Thanks but no thanks, Mister."
    "I was not really in the mood for jokes at that time so I attempted to excuse myself but his earlier remark tickled my attention."
    h "You knew Mom?"
    mm "Of course I knew her!"
    mm "I was her older brother. The best brother. Her {b}número uno{/b}!"
    "He said that with so much confidence, with so much gusto, that it sounded like him being sarcastic."
    "And the way he managed to make the last part sound so fake and exaggerated didn't help either."
    h "And that I should seriously believe, Mister?"
    "The truth is that I had never seen him before, not as a guest at home nor elsewhere."
    mm "Totally. Like the fact that she loves bush dogs to death."
    mm "Or hates anchovies like they're her nemesis."
    h "Hm."
    "...Correct. And the thing with the anchovy was known to only me."
    mm "Heh. I know by your dumbfolded face that I was right." #Why does the word 'dumbfolded' not exist? :/
    mm "But enough of her, more of me."
    "Is this the correct way of changing topics?"
    "His flamboyant entrance continued to leave me behind in the conversation and hence he babbled forth."
    mm "The name's Oliver but you can call me Old or Mister Old like everyone else does."
    
    show old normal at pulse
    
    mm "I was your mother's brother, so that makes me ... ?"
    "The way he winked and blinked at me with his eyes really irritated me."
    "He must be dying to know the answer to the really obvious question from me."
    
    show old normal :
        zoom 1.0
        
    h "My uncle."
    $ oldname = "Mister Uncle Old"
    o "Yeah, you guessed right! I am infact your Mister Uncle Old, nice to meet you."
    h "I am not dumb, you know."
    h "If you're infact my Mom's brother, then-"
    o "I know, I know. And I also know that you're Heiden. Your mother told me."
    h "When?"
    "The fact that this overly familiar behaving man here knew things without my knowledge was starting to get on my nerves."
    "Not to say that he was behaving rather odd himself."
    "For now I felt like just going along his shtick may do the trick."
    o "She wrote me tons of letters, I don't really miss a single fact about your daily life."
    o "Like when you stopped wetting your bed and stuff. {w}It's very amusing, I must say. {w}Top read."
    
    with hpunch 
    
    h "Wa-"
    "MOM. Don't write that kind of stuff in your letters!"
    "Is this what you were doing every morning when I was asleep? Writing letters including events that I'd rather forget?"
    h "I knew it. You're creepy. Dangerous."
    "One thing was clear: This man spelled trouble for me, one way or another."
    o "No need to glare at me like that. And no need for useless hostility, kid."
    o "I just want to get on your good side for now."
    "By the way, he is doing a {b}crappy{/b} job at it."
    "And with the way he grinned, he must know it himself."
    o "So let's restart our conversation, shall we?"
    o "Hey Heiden, my name is Oliver and I am your uncle."
    o "You may call me Uncle or Old, my nickname."
    
    show old normal :
        linear 2.0 zoom 1.7 yalign 0
        
    o "Nice to meet you, Heiden."
    "He buckled himself to my eye level while gesturing me to respond with his outstretched hand."
    "How should I greet him?"
    $ old_points = 0
    
    menu:
        extend ""
        "Nice to meet you, Mister Oliver.":
            $ nickname_old = "Mister"
            $ oldname = "Mister Oliver"
            $ old_points += 1
            o "Quite the polite boy, you are!"
            h "Being called a mister for being a mister is only natural, [nickname_old]."
            o "I guess you're right about that, boy. Just gotta come to terms with me being a mister."
        
        "Sup', Uncle Old.":
            $ nickname_old = "Uncle"
            $ oldname = "Uncle Old"
            $ old_points += 2
            o "Heh, getting chummy with me already?"
            o "But I don't dislike it when people are using my nickname on the get-go, heh."
            h "Even if your nickname is literally {i}Old{/i}, [nickname_old]?"
            o "{b}Especially{/b} when I am {i}Old{/i}."
            "How can he even laugh at something like that?"
            o "Though I'll tell you more about it at another time."
                
        "Likewise, Mister Uncle Old.":
            $ nickname_old = "Mister"
            $ oldname = "Mister Uncle Old"
            o "Now in retrospect, that name really sounds idiotic."
            o "Heh, I guess my earlier vigor really came biting my back."
            o "I don't actually want that name unnecessarily sticking out so call me 'Mister Oliver' for the time being, ok?"
            $ oldname = "Mister Oliver"
            h "Well, if you say so, [nickname_old]."
            o "I implore you to do so or a certain someone is going to tease me about it everytime you mention it, heh."
            "He winks at me while dismissing any kind of discomfort that the topic might have aroused."
            
    "His lingering hand didn't stay untouched for long as I grasped it with both my hands."
    "My affectless squeezing was met with a vigorous response."
    
    show old normal:
        linear 2.0 zoom 1.0 yalign 0.5
        
    h "Are you done with me yet, [nickname_old]?"
    "Though the conversation itself didn't bother me, my thoughts often drifted to the picture of Mom which was hanging around the flower arrangement infront of the family grave."
    "Mom, too, will be placed into this place when the process of cremation was finished."
    "The thought alone didn't fit well with me."
    "I guess my facial expression at that time spoke louder than I myself could ever do."

    show old troubled:
        linear 1.0 xzoom -1.0
        
    o "I am not really in for happy conversation either, given the situation at hand."
    "[nickname_old] looked like he tried to choose his words as he scratched his head with a slightly dubious expression."
    
    show old normal:
        linear 2.0 xalign 0.2
        
    o "You came here with that lovely lady, over there?"
    "He gestured with a pointed nod toward the crowd of talking adults, the same group of people whom I peeked at earlier."
    h "You mean Mrs. Becky, [nickname_old]?"
    
    show old troubled:
        linear 1.5 xalign 0.8 xzoom 1.0
    
    h "Yeah, I am living at her place right now but not for too long."
    h "Apparently they wouldn't let me stay at home alone."
    "With they I refer to as simply all adults involved."
    
    show old troubled:
        linear 1.5 xalign 0.3 xzoom -1.0
        
    "But I thought it wouldn't be much of a problem for me to mind the house but apparently I didn't have a say on that matter."
    "Mrs. Becky said to take care of me until a more suitable option arises."
    h "It's better than being sent to a full-day care center or a protectory, at least."
    h "And Mrs. Becky can cook really well."
    
    show old troubled:
        linear 1.5 xalign 0.5 xzoom 1.0
        
    h "Hello? [nickname_old]?"
    
    o "{b}Mrs.{/b} Becky, you say?"
    "He was pretty deep in thought as he said it, as if he was trying to dissect the words within his mind and reassemble it while hoping that something has changed."
    "But it didn't change the fact that being ignored was a no-go for me."
    "Like, how uncouth can one be!? Hmpf!"
    "Witness the disatisfaction that adorned my face, you ignoring person!"
    
    show old normal:
        xalign 0.5 xzoom 1.0
    
    o "Oh well, sorry. I was distracted a bit there."
    "He just laughed it off as if it was not a big deal for him."
    o "But either way, I held a talk with her before coming to greet you."
    o "A pleasant lady, really."
    "I couldn't say why but this man infront of me seemed kind of hopeless right now."
    "I guess you can't just mingle all adults into a pot and call them all self-assured or confident or mature or something else."
    "Stuff one may expect from an adult, or what at least I expected them to be."
    
    show old troubled at shivertwice
    show old troubled :  
        linear 0.2 zoom 0.7 yalign 0.2
        
    h "You like her, [nickname_old]?"
    "My sudden question might have come as a surprise as [nickname_old] jerked a bit to the back before regaining his posture."
    "He was visibly sweating right now."
    
    show old troubled:
        linear 0.5 zoom 1.4 yalign 0.0
        
    o "No."
    
    show old normal:
        linear 2.0 zoom 1.0 yalign 0.5
        
    o "Don't get any weird ideas, kid."
    h "I didn't imply anything though, [nickname_old]. Just wanting to say that she-"
    o "Don't wanna hear."
    o "It's okay, that's not important to me."
    "He was weird to dismiss it like that but I guess adults do that sometimes."
    h "I realized that adults don't have it easy either, [nickname_old]."
    o "What's with the sympathetic look on your face, Heiden?"
    o "Stop that look, okay?"
    o "It's not gonna earn you any points with me."
    "I slowly began to realize that I thought too highly of the persons who were mistakenly labelled as adults."
    "I mean, they're humans like me. Though sometimes really weird, or really boring."
    
    show old troubled
    
    o "What I was trying to say is that we came to talk about your future, Heiden."
    "I peaked up at him while he was essentially trying to hold eye-contact with me but he would frequently avert his eyes to the sides but then return his attention to me once again."
    "A really weird habit to have, if it was one."
    "The situation has suddenly become really serious as he switched his demeanor like conveniently putting on a persona that fitted the respective circumstance."
    "I guess adults could do that, too."
    o "So, hey. I thought that now with your delicate situation, why not live at my place?"
    
    stop music fadeout 4.0
    show old:
        linear 1.5 xpos 1.5
    show crowd:
        xpos -1.0 yalign 1.0 zoom 1.4
        linear 2.0 xalign 0.5
    $ renpy.pause(2.0, hard=True)
    play sound whisper
    "At his words I unconsciously turned toward the crowd but they wouldn't respond nor seem to take note of me at all."
    "They never did. Their random babbling continued, seemingly in perpetuity."
    "That's when it hit me."
    "Maybe they never had the intention of paying me any attention."
    "Maybe they were trying to find a scapegoat to push me to."
    "Picking a place for living rather than a home for life."
    "It would have make more sense to enroll me to a protectory at once."
    h "Did they send you to me?"
    "My eyes didn't break contact with the unmoving crowd."
    with vpunch
    "My apparent babble received a meaning as I found [nickname_old]'s hands grabbing my shoulders from behind."
    
    play music home fadein 4.0
    $renpy.music.set_volume(0.2, delay=4, channel="music")
    queue music ["audio/bgm/06 - Brand New Day Pt.2.mp3"] loop
    
    os_troubled "Nah, it was your mother."
    os_normal "Kind of like a favor from the {s}dead{/s}, I mean, heaven."
    h "Hm."
    h "Mom always did what she wanted."
    h "She was also pretty selfish at times."
    h "Picky about food."
    h "Always on her toes."
    h "Crappy at doing household chores."
    h "Also flailing around in her sleep."
    h "Not always easy to deal with, to be honest."
    os_troubled "Yeah."
    os_troubled "She was always the free-spirited person to begin with, heh."
    os_normal "But for her, you took priority over everything else in her life."
    os_normal "That didn't change and never will, it's plain obvious from the contents of her letters."
    os_wink "I am sure of it."
    os_wink "You're her {b}número uno{/b}, like me."
    h "Hm."
    "His joke was so lame that I could only muster a dry smile."
    "I didn't even move one bit from my static position."
    "But holding my posture didn't become as exhausting as it did before."
    "It's like something within me had been lifted and slowly plummeted to my feet, together with all the locks that I had carefully attached."
    "They all came falling down, becoming nothing and also: Revealing the me I that I tried so hard to hide."
    "My dry smile turned slightly wet as I tasted the strange bitterness from my watery cheeks."
    "Tears?"
    "Was it the tears of relief or that of grief?"
    "I did not understand."
    "Maybe I did understand and just didn't want to acknowledge it."
    "And pushed it to the corners of my mind, slowly forgetting its existance."
    "I was so occupied with holding the status quo on my feelings that I nearly forgot for sure."
    "Forgot? What did I forget? Ah, yeah."
    "I nearly forgot but at last I remembered it."
    "To bid farewell to Mom, to tell her in my mind that I am gonna be ok."
    
    $renpy.music.set_volume(0.8, delay=4, channel="music") #0.8 should be the default music preference, if not already altered by the user
    
    "Probably gonna be ok."
    "Shouldn't make overly optimistic promises to Mom now, can't I?"
    "Call it a prayer of some sort but saying it out of my mind made me believe that she'll surely get my message somehow."
    "And I guess that's the thing I should be doing right now, the only thing that truly mattered."
    "The only thing that would make sense if she really was my Mom and I was her son."
    "Her {b}número uno{/b}..."
    "I guess..."
    "...?"
    "Gosh, his lame jokes are slowly rubbing off on me!"
    h "So, me living at your place, [nickname_old]?"
    "While trying to wipe away the tears with my sleeves, I tried to talk as normally and composed as possible."
    "The tiny sobs emitting from the depths of the sleeves' fabric did nothing to disguise my sobbing self, however."
    os_normal "Yup, my place."
    os_normal "Though it's quite far from here, to be honest."
    os_normal "But I promise it's the best place for you."
    h "A home?"
    os_troubled "I don't really understand what you meant by that."
    os_normal "I mean, a home is a home, right?"
    os_normal "I live in one, after all."
    h "I see."
    os_wink "So, we got a deal?"
    "I felt his firm grip on my shoulders."
    h "Not like I got a choice here, do I?"
    
    show crowd:
        linear 2.0 alpha 0.0
        
    "My vision of the crowd in front of me becomes smaller and more insignificant as my eyes trail toward the ground."
    os_troubled "There's always a choice in life, Heiden."
    os_normal "You're just a kid so your only choice right now is to be dumb and frolic around a sandpit."
    os_wink "Preferably around {i}my{/i} house, heh."
    "I felt his vigorous laughter through the trembling of his hands on my shoulders."
    h "Is this your idea of what kids do, [nickname_old]?"
    os_normal "Does it not match the reality?"
    os_wink "Then I guess it's your job to show me how to have fun: the kids' way."
    "His grip lessened before ultimately letting go."
    "After ten seconds of total silence, I heard the question that would turn my life around."
    os_troubled "So Heiden."
    os_troubled "Do we have a deal?"
    "He did not move nor did I."
    "He would not speak another word, his attention solely focused on the words I am about to utter."
    "I guess this here was the edge of the life I once lived before moving on."
    "My past life and new life are edging on each other, waiting for me to say one single word."
    "A single word to resume the wheel of time."
    "I shouldn't make him wait."
    "So I turned around to tell him my answer."
    
    stop music
    show conductor:
        xpos -1.0 zoom 2.5 ypos -0.15
        linear 0.5 xpos 0.0 
        
    h "Yes, I- !"
    c "Get out of here, you rascal."
    h "The heck!?"

#Chapter 1.0 : Flashback [END]
################################################################################
#Chapter 1.1 : Reunion with Uncle 

    scene bg train_stop with flash
    $ save_name = "Chapter 1.1 - Reunion with [nickname_old] Old"
    show conductor:
        xpos 0.0 zoom 2.5 ypos -0.15
        linear 2.0 zoom 1.0 xalign 0.5 yalign 0.5
        
    c "Final Destination, kid."
    c "Kids really do sleep like a log."
    c "But you gotta go now so we can perform some basic upkeep of this shabby train."
    
    play music new_morning fadein 4.0
    
    h "Oh."
    
    show conductor:
        linear 3.0 xpos 1.5
        
    "I let go of the travel pillow that I hugged during my sleep and wipe away the drool that I am sure to have."
    "It seems that I dreamed about Mom's funeral even though it wasn't even a week ago."
    with hpunch
    "I shake my fatique away as I cram everything into my trolly before noticing the absence of a certain man."
    h "Hey! Wait, Mister!"
    
    show conductor:
        linear 2.0 xalign 0.5 xzoom -1.0
        
    c "What's the matter this time?"
    "\"That's the first time I asked you something, Mister.\""
    "...is the first response that I had in mind but it quickly subsided."
    h "What happened to that creepy man?"
    
    show conductor:
        linear 1.0 xzoom 1.0
        
    c "Oh, the one with the dark circles around his eyes?"
    c "He already left."
    c "But not before telling me that some relatives are gonna pick you up at the train station."
    
    show conductor:
        linear 1.0 xzoom -1.0 zoom 1.5 ypos 0.8
        
    c "So hurry up, ok?"
    
    show conductor:
        linear 2.0 xzoom 1.0 zoom 1.0 yalign 0.5 xpos 1.5
        
    "Entirely losing the interest in me, the conductor resumes his way through the wagons and his search for passengers or lost properties."
    h "I guess he isn't wrong about my waiting relative."
    "Can't really help it if Mr. Spooky has already left the train though he could at least wake me up before leaving."
    "Hmpf, stupid Mister."
    "I am not so far as being angry but I do feel a bit irritated by his display of selfishness."
    "He was spooky but he was kinda fun."
    "That's what I think about the spooky man, the man I met on the train."
    "After one long look back to the old and empty wagon, I walk my way out of the train with trolly in hand."
    
    scene bg trainstation with fade
    
    "I step out of the train to find the cold wind pushing against me."
    h "Brr. I guess summer is still a long way off."
    "While a small amount of regret is overcoming me and I ask myself why I didn't leave my blanket out of the trolly, I search the station for my uncle."
    "A glimpse at the big clock that hangs on the station wall reveiled the time: 8am."
    "The estimated time of arrival for this train was 6am if I am not mistaken."
    "I guess even [nickname_old] can't handle the unexpected wait?"
    
    show old funeral troubled:
        xalign 0.5 alpha 0.0
        linear 1.0 alpha 1.0
    
    "As I think that, a shadow towers over me."
    with vpunch
    h "Woah, not again from behind!"
    o "Gosh, it's so cold out here."
    
    show old at shivertwice
    o "So friggin' cold."
    
    show old at shivertwice
    o "So {cps=*0.5}un-be-lie-vab-ly{/cps} cold, I swear."
    
    h "Just look at you, [nickname_old]. You're only wearing a shirt!"
    "I can't believe I am fighting the cold in my condition when people like him are dressed like {i}that{/i}."
    "I open my trolly and throw my blanket at him."
    
    show old normal at shivertwice
    
    o "Oh."
    
    show old at twitchtwice
    
    "[nickname_old] catches the blanket with seemingly no difficulty and quickly wraps it around his neck like a scarf."
    o "Nice one, Heiden."
    "I am taking care of an adult right now, is this really happening?"
    "My utopistic vision of an upstanding, normal adult is slowly dwindling away."
    h "There's a limit on how hopeless people can be, you know."
    o "Nah, it all worked out just fine."
    o "Though you did keep me waiting."
    h "Going home wasn't an alternative?"
    "I honestly still don't know where he lived."
    
    show old at twitchtwice
    
    "Maybe he needs more than an hour to get here?"
    
    show old:
        linear 1.0 xzoom -1.0
        
    "Though I cannot believe that's the case, I mean look at him."
        
    show old:
        linear 1.0 xzoom 1.0
        
    "I don't think that he walked an hour to get here and not burst into sweat."
    "Or froze to death."
    "Stations are said to represent the scale of the town, or that's what Mom always used to say."
    
    show old:
        linear 1.0 xzoom -1.0
        linear 1.0 xzoom 1.0
        
    "So if I am to compare this station here to that huge superstation back in the city..."
    o "You thinking hard about something?"
    h "What is it?"
    h "I need to sort out some thoughts right now."
    o "And that's more important than our talk?"
    
    show old troubled
    
    o "C'mon. Heiden, you're not even listening to me."
    o "Even though I am your {b}númer{/b}-"
    h "OK ok, I get your message."
    "I hold both my hands in defeat."
    "I already forgot what we were talking about but I sincerely hope that it wasn't important enough to remember."
    
    show old normal
    
    o "Well, I'll forgive you. I am your uncle now, after all."
    "[nickname_old] seems joyful enough with his newly attained job as an uncle and drops the matter."
    o "Well, with that said."
    o "Here you are."
    h "Yeah, here I am."
    
    show old:
        pause 2.0
        linear 2.0 xalign 0.2
    $ renpy.pause(2.0, hard=True)
    
    "He gives me one long look before heading towards the exit of the station." 
    o "Let's go then, Heiden."
    o "You gotta be tired or at least starving for a proper meal?"
    h "It's okay, I am not hungry."
    
    show old at spin
    
    o "You're not? Not even a tiny bit?"
    h "Nope [nickname_old], I am fine."
    h "I am generally not eating a lot in the first place."
    
    show old at spinback
    
    o "Is that so?"
    o "Well then, that's the first thing we gotta change."
    o "Kids eat a lot, they're like walking trash cans."
    o "In my opinion you need to become a little bit more burly before you can even worry about anything else."
    "Burly? Like those people on television with all the sugary drinks and overgrown pizzas who do not know when to stop?"
    "..."
    "I don't think I want to become something like that."
    "The imaginings inside my head are enough to completely shut down my sensation of hunger."
    "Yeah, I truly watched the wrong shows on television."
    h "I think I'll have to pass on that, [nickname_old]."
    
    show old at spin
    
    o "C'mon, boy. Don't be like that."
    o "Let's hit a bakery and get some food."
    
    scene black with fade
    
    $ renpy.music.set_volume(0.5, 2.0, channel='music')

    play sound electric_door
    centered "[nickname_old] entered a nearby store as he says that."
    centered "But the name of the store does not really live up to that of a bakery."
    centered "Now it's either waiting outside and becoming a sacrifice to the unrelentless blowing wind or following him inside."
    centered "Sigh."

#Chapter 1.1 : Reunion with Uncle [END]
################################################################################
#Chapter 1.2 : The Bakery 

    scene bg bakery with dissolve
    $ save_name = "Chapter 1.2 - The Bakery"
    $ renpy.music.set_volume(0.75, 2.0, channel='music')
    show old funeral normal:
        xalign 0.5 yalign 1.0
        linear 1.0 yalign 0.5
        linear 1.5 xalign 0.2 xzoom -1.0
    with dissolve
    
    $ renpy.pause(2.5, hard=True)
    
    o "Look at that sortiment!"
    o "So what'ya need, Heiden?"
    "[nickname_old] gestures toward the storefront."
    "A wide display of sweet buns, sweets and ... cake."
    "Not the kind of stuff you'd find in a traditional bakery but rather in a patisserie."
    "Or a sweets store."
    "Or the store we currently are: a store called {i}Sweet Dreams{/i}."
    h "Sweets aren't my thing, [nickname_old]."
    h "And I am not really hungry to begin with."
    o "Though I am. So it doesn't hurt to take a look, right?"
    "His smile doesn't leave me much of a choice, do I?"
    
    scene bakery_look1
    with fade
    $ renpy.pause(2.0, hard=True)
    
    "Woah..."
    
    scene bakery_look2
    with fade
    $ renpy.pause(1.5, hard=True)
    
    "Hmmmm..."
    
    scene bakery_look3
    with fade
    $ renpy.pause(3.5, hard=True)
    
    "Could it be!?"
    
    scene bg bakery with Dissolve(.1)
    show old funeral normal:
        xalign 0.8 yalign 0.5 xzoom 1.0
    
    h "Nope."
    o "You really don't have a sweet tooth, I see."
    o "In that case..."
    
    show old at twitchtwice
    pause 1.0
    show old:
        linear 1.0 xalign 0.2
    pause 1.0
    show old at twitchtwice
    pause 1.0
    show old:
        linear 0.6 xalign 0.5
    pause 1.0    
    show old at twitchtwice
    pause 1.0
    show old:
        linear 0.6 xalign 0.8
    
    "[nickname_old] helped himself with the wide array of sweetcakes, picking not the things that piqued his interest but rather choosing at random."
    "The woman behind the counter who is taking his order tries her hardest to keep up with the movement of his finger."
    o "It doesn't matter if there are wrong orders."
    o "Infact, it's more fun to find some surprise cakes that I didn't order."
    "I can feel a tiny bit of uneasiness oozing out from the shop assistant as she put the cakes into two shopping bags."
    "[nickname_old] here is clearly out of touch with the customs of a customer."
    h "That's a lot. Can you really finish all this on your own, [nickname_old]?"
    
    show old:
        linear 1.0 xalign .5
    
    o "Then how about helping me out with that load?"
    o "You can at least eat the cheese cake that I {b}didn't{/b} order, ok?"
    "A tiny shriek could be heard behind the counter before [nickname_old] turns to the shop assistant and pulls out his purse."
    "As for me..."
    $ cakeflag = False
    
    menu:
        extend ""
        "No, thanks. Cakes are my mortal enemies.":
            $ cakeflag = False
            "I find it hard to express an appetite for those cakes if they're in such large numbers."
            "I am sad that [nickname_old] went ahead and picked them out just like that but I guess it's his problem now."
            h "Sorry. I am not up to that task."
            
            show old funeral troubled
            o "Oh well, that can't be helped, right?"
            show old funeral normal
            o "I can deal with that much, I guess."
            o "You're welcome to try them all if you happen to change your mind."
            "Well, that's also possible."
            
        "Eating a single cake won't kill me...":
            $ cakeflag = True
            "Seeing [nickname_old] force himself to stuff all those sugary things down his throat seems kind of unfair."
            "Though I don't really care much about cakes, I guess I can do him a favor and just keep him company by eating one."
            h "Well, a single cake won't hurt."
            
            show old:
                linear 0.5 xzoom -1.0
            show old:
                linear 0.5 xzoom 1.0
       
            o "That's my boy."
            o "I'll even let you try a bite from my prized baumkuchen."
            "Baumkuchen? What's that? Its name doesn't give off much of an edible impression to me."
            "May as well find out."
            
    show old:
        linear 1.0 xalign 0.2
        
    o "Well, I am ready here."
    o "We better eat those cakes at home so you'll be slightly more hungry by then."
        
    show old at shivertwice

    "[nickname_old] holds both bags with his hands while I got my trolly."
    o "Let's start our trip home."
    
    scene black with fade
    $ renpy.music.set_volume(0.5, 2.0, channel='music')
    play sound electric_door
    centered "The automatic door opens just to have a cold gust of wind coming straight at my uncle."
    centered "But his steady pace remains unbroken by the thermal differences between the store and the street."
    centered "He seems to be really looking forward to his lunch cakes."
    
#Chapter 1.2 : The Bakery   [END]
################################################################################
#Chapter 1.3 : The Trip Home  
    
    $ save_name = "Chapter 1.3 - The Trip towards Home"
    $ renpy.music.set_volume(1.0, 2.0, channel='music')
    scene bg city with pixellate
    "We end up walking through parts of the village center..."
    "Some people can be seen window-shopping and parents walking with their children and dog."
    play sound trolly
    "The clattering of my trolly attracts attention though it doesn't bother me that much."
    "I can't help it with this brick paving that I am walking on."
    stop sound
    scene bg wayhome1 with pixellate
    "We enter a residential area after walking through the center of the village."
    "Contrary to the somewhat lively village center, this part of the village is more quiet and peaceful."
    "The people around here have taken shelter from the cold as shown by the barren alley."
    "With the cold post-spring weather coming down on us, it invokes a faint feeling of winter within my chest."
    "It's like I've travelled to the far north of earth, a place that knows no summer heat."
    "I don't want to admit it but I am slowly feeling the cold."
    "Maybe I am beginning to long for the slight warmth of the patisserie back at the station?"
    
    show old funeral normal at facingON with fade
    o "Hang in there, we're nearly there."
    show old normal:
        linear 1.0 alpha 0.0
    h "Ok."
    "He turns around for only a brief second to tell me that."
    "So I respond quickly in turn."
    h "(Is he able to read my mind?)"
    
    scene black with fade
    show black onlayer trans5
    scene bg wayhome2 at invi_visible
    "We must have walked ten minutes already... "
    
    scene bg house with pixellate
    $ renpy.pause(3.0, hard=True)
    extend "to finally reach this place."
    "Though slightly ominous looking due to its metal fence, this big house does seem quite like a small castle."
    h "Is this the place?"
    
    show old funeral normal at facingON
    o "Yup."
    o "The house's getting old but it's big and I got it all by myself."
    o "Well. It's ours now, Heiden."
    o "..."
    o "Let me get the keys."
    
    show old funeral normal:
        linear 1.0 yalign 0.5 zoom 1.0
        linear .5 xalign 0.7 yalign 0.5 zoom 1.0
    $ renpy.pause(1.5, hard=True)
    show old funeral normal at twitchtwice
        
    o "Yeah okay. Got me worried for a second but I got the keys with me."
    h "Wouldn't it be quite bad if you didn't find them?"
    show old:
        linear 1.0 xalign 0.5 yalign 0.5 xzoom -1.0
    o "Yeah maybe."
    o "But luckily, breaking into your own house isn't punishable by law."
    show old at spinback
    o "After many years of living here, I found some easy ways to do that."
    h "Isn't this a pretty bad thing to admit?"
    hide old funeral normal
    show old funeral normal at facingON
    o "Don't sweat it!"
    show old:
        linear .5 yalign 0.5 xzoom 1.0 zoom 1.0
        linear .5 xalign 0.2
    pause 1.0
    show old at shivertwice
    pause 1.0
    play sound fence
    o "Hell yeah, I got it."
    o "It's really open. {w}The keys really work."
    "It's your own house..."
    show old:
        linear .5 xalign .5
    o "Come in, come in."
    scene black with fadehold
    stop music fadeout 4.0
    $ renpy.pause(1.0, hard=True)
    
#Chapter 1.3 : The Trip Home  [END]
################################################################################
#Chapter 1.4 : Home 

    $ save_name = "Chapter 1.4 - Homecoming"
    $eat_clear = False
    $location_table = 4
    o "Careful, Heiden."
    h "Careful of what?"
    
    scene bg livingroom with dissolve
    play music at_home fadein 2.0
    show old funeral normal at facingON
    o "Careful not take the wrong choice!"
    show old funeral normal:
        linear 0.5 zoom 1.0 xalign 0.5 yalign 0.5
    show kuchen1 at oob_left
    show kuchen1:
        ypos 0.0
        linear 1.0 xpos 0.0
    show kuchen2 at oob_right
    show kuchen2:
        ypos 0.0
        linear 1.0 xpos 0.0 xalign 1.0
    "[nickname_old] didn't even bother to take off his shoes as he proclaims that."
    
    if cakeflag == False:
        h "I am obviously not hungry though, like I told you."
        o "That's why I waited."
        o "C'mon, keep me company."
        "[nickname_old] really seems eager for me to join him for a cake."
        "I am not really hungry but spending time with him should go fine, right?"
        
        menu:
            "I should accept the invitation.":
                "I can't really keep declining his requests over and over again."
                "I mean, he is my uncle after all."
                h "Yeah, well. I'll take one."
                h "Cake, I mean."
                o "That makes me happy."
                o "And hungry. Really hungry."
                $cakeflag = True
                
            "I should vehemently stand my point to decline his invitation.":
                "The drowsiness slowly overcomes me as the warmth of the room slowly creeps up my body."
                "Eating a sugary cake in my current condition may seriously upset my stomach."
                "At least I think it will."
                "I am not too eager to take my chances with the cake."
                show old funeral troubled
                o "You okay there, buddy?"
                o "You don't look fine to me, boy."
                h "I guess I am more tired than I thought."
                o "You may have unknowingly overexerted yourself during your stressful journey."
                show old funeral normal
                o "Kids don't have an inexhaustible supply of energy in them, after all."
                o "Don't worry about the cake, just take it easy and go upstairs for now."
                o "I'll have a bed ready for ya. And a cake, too."
                "Is he--? I guess I really made him worry somehow."
                h "Thanks a lot, [nickname_old]."
                o "Don't sweat it."
                
                stop music fadeout 2.0
                show black with fade
                play sound stairs
                o "You'll get the guest room for now, tell me if you need something."
                h "I'll manage somehow."
                $eat_clear = True
                jump upstairs
    
    "He really can't wait any longer to dig into his cake."
    o "So Heiden, which one do you choose?"
    with vpunch
    h "At least let me take off my shoes, [nickname_old]."
    h "As for the cake..."
    "Hm, the left one looks kinda bland and dry."
    "But the right one looks really creamy and sugary somehow, to the extent that it causes me goosebumbs the moment I bite into it."
    "I guess I'll take..."
    $ baumkuchen = False
    
#Cake Choosing
    window hide None
    $ old_points += 1
    call screen imagemap_cake
    window show None
    
    if _return == "baumkuchen":
        
        $ baumkuchen = True
        show kuchen1:
            linear 1.0 xpos -0.5
        show kuchen2:
            linear 1.0 xpos 1.5

        h "The choice was kind of difficult."
        h "But in the end, I'll choose the left cake."
        show old funeral troubled
        o "Ah. Yeah. The Baumkuchen cake shall be yours then, Heiden."
        "What's with that mournful gaze on my cake?"
        h "Want to change?"
        show old funeral normal:
            linear 0.5 zoom 1.0 xalign 0.5 yalign 0.5
        o "I ain't gonna take a cake from a kid."
        "Well, can't be helped then."

    elif _return == "bienenstich":
        
        $ baumkuchen = False
        show kuchen1:
            linear 1.0 xpos -0.5
        show kuchen2:
            linear 1.0 xpos 1.5

        h "The choice was kind of difficult."
        h "But in the end, I'll choose the right cake."
        o "Ah, I think this cake is called Bee Sting Cake or something."
        show old:
            linear 0.5 zoom 1.0 xalign 0.5 yalign 0.5 
        o "But sadly, it is inferior to my Baumkuchen cake."
        h "Well, no deal to me."
        "So that brown cake is what a Baumkuchen looks like?"
        "He seems happy that I've picked the other cake."
        "Which makes me want to ask why he asked me to choose one in the first place if he ogled one to begin with."
        "Oh well."
        
    "As to where I am going to eat my cake..."
    hide old

#Eating Location Choosing
    window hide None
    call screen imagemap_location
    window show None
    
    if _return == "upstairs":
        jump upstairs

    elif _return == "table":
        jump table
        
    elif _return == "coach":
        jump couch
    
###########################################    
    
label table:
    $ location_table = 1
    scene bg livingroom:
        xalign 0.5
        linear 2.0 xalign 0.0
    "I put my cake on the table while taking a seat on one of the chairs."
    show old funeral normal:
        xalign 0.5
        linear 0.5 xalign 0.8
    with dissolve
    
    o "Just take your time eating the cake, I'll show you to your room afterwards."
    hide old with dissolve
    os_normal "Yeah, this is good."
    if baumkuchen:
        os_normal "Though it does not rival the taste of a Baumkuchen, the cream of this Bee Sting Cake really does wonders."
    else:
        os_normal "Nothing beats a Baumkuchen, after all!"
    play sound fork
    "He sits himself near me while we pick on our cakes."
    os_normal "Yours good, so far?"
    
    if baumkuchen:
        h "Kind of dry."
        h "Are Baumkuchen cakes supposed to be like that?"
        os_troubled "I ain't letting you talk down my cake like that, you know?"
        os_normal "Eat it all up, you hear?"
    else:
        h "It's creamy."
        h "A bit too much actually, I can hardly eat it in one go."
        os_normal "Just take it easy for now, you hear?"
        
    h "Aye."
    play sound fork
    "Carelessly eating away at my cake, I couldn't help myself but look around the living room."
    
    scene bg livingroom:
        linear 3.0 xalign 1.0
        linear 3.0 xalign 0.0
    
    h "It's quite neat."
    os_normal "What is?"
    h "The living room, I mean."
    h "To be honest, I expected it to be more messy."
    "I guess you really can't judge a person based on their personality..."
    os_normal "I have plenty of time so tidying up my place has become kind of a habit."
    h "You don't work?"
    os_troubled "Work? Well, I do work..."
    os_normal "but from the comfort of my home."
    os_normal "I work from home, you see?"
    h "Okay."
    play sound fork
    "The musical ensemble of the forks seems to have resumed while I try to cram the cake into my mouth."
    "The foreign smell of this particular cake fills my nostrils and the pieces in my mouth immediately begin to crumble apart."
    "Yeah, well..."
    "That was dumb."
    h "W-Water."
    os_normal "Don't you want to know what I do for a living?"
    os_normal "You're honored to speak with a well-known writer of children's books!"
    h "Can't breathe. Water. Hurry."
    play sound water
    os_normal "Water?"
    os_troubled "Uhm."
    os_normal "Here you go."
    with hpunch
    "I gulp it down all at once."
    h "Pfuah.. I thought I was a goner for a second."
    
    if baumkuchen:
        os_troubled "Trying to pin the blame on my Baumkuchen again?"
        h "As if!"
        os_normal "Just joking around, this time."
        h "\"This time\"?"
    else:
        os_normal "And here I thought that the cream might make it harder to choke on."
        h "I am not doing that on purpose, you know."
        os_normal "Kids, you know."
        h "Grrrr."
        
    window hide
    show black with fade
    centered "Time passes as we indulge ourselves in idle conversation."
    
    scene bg livingroom with dissolve
    show old funeral normal:
        xalign 0.2
        linear 0.5 xalign 0.5
        
    o "Time to show you to your room."
    o "You should be plenty tired right now."
    h "I am not tired but I am interested enough to see the room."
    
    window hide
    stop music fadeout 2.0
    show black with fade
    play sound stairs
    o "You'll get the guest room for now, tell me if you need something."
    h "I'll manage somehow."
    $eat_clear = True
    jump upstairs
    
##############################################

label couch:
    $ location_table = 2
    scene bg livingroom:
        linear 2.0 xalign 1.0
    "I put my cake on the coffee table while taking a seat on the couch."
    show old funeral normal:
        xalign 0.5
        linear 0.5 xalign 0.2
    with dissolve
    
    o "Just take your time eating the cake, I'll walk you to your room afterwards."
    hide old with dissolve
    os_normal "Yeah, this is good."
    if baumkuchen:
        os_normal "Though it does not rival the taste of a Baumkuchen, the cream of this Bee Sting Cake really does wonders."
    else:
        os_normal "Nothing beats a Baumkuchen, after all!"
    "He sits himself near me."
    os_normal "Yours good, so far?"
    
    if baumkuchen:
        h "Kind of dry."
        h "Are Baumkuchen cakes supposed to be like that?"
        os_troubled "I ain't letting you talk down my cake like that, you know?"
        os_normal "Eat it all up, you hear?"
    else:
        h "It's creamy."
        h "A bit too much actually, I can hardly it in one go."
        os_normal "Just take it easy for now, you hear?"
        
    h "Aye."
    play sound fork
    "With the unusual silence in the room, I guess a conversation is in order."
    h "So how come Mother never told me about you?"
    os_troubled "..."
    os_normal "That question came out of left field."
    play sound fork
    "He's taking awfully long for that piece of cake."
    os_normal "Thing is, I don't always get along with her."
    os_normal "She is very.."
    h "Special?"
    os_normal "Yeah, that's it. Special."
    h "Even though you were her {b}número uno{/b}?"
    os_normal "What can I say, she was the type of person that'll turn you from number one to number last in just under ten minutes."
    os_normal "But that didn't hinder her to send me tons of letters."
    os_normal "Really a handful, that girl."
    h "Oh, you need to show them!"
    os_normal "There's no rush."
    os_normal "We got plenty of time."  
    h "Geez, party pooper."
    os_normal "Cake's gonna get cold if you keep it waiting like that."
    
    show old funeral normal:
        xalign 0.5 yalign 0.5
        block:
            linear 1.0 xzoom -1.0
            linear 1.0 xzoom 1.0
            repeat
            
    h "Wait, what?"
    "His grin is warming up the room."
    
    window hide
    show black with fade
    centered "Time passes as we indulge ourselves in idle conversation."
    
    scene bg livingroom with dissolve
    show old funeral normal:
        xalign 0.2
        linear 0.5 xalign 0.5
        
    o "Time to show you to your room."
    o "You should be plenty tired right now."
    h "I am not tired but I am interested enough to see the room."
    
    window hide
    stop music fadeout 2.0
    show black with fade
    play sound stairs
    o "You'll get the guest room for now, tell me if you need something."
    h "I'll manage somehow."
    $eat_clear = True
    jump upstairs
    
    
##############################################

label upstairs:
    if eat_clear:
        play music sleepyroom fadein 2.0
        scene bg bedroom with blinds
        show old funeral normal:
            xalign 0.0 yalign 0.5
            linear 0.5 xalign 0.5
            
        o "I hope you'll like it here."
        "The first thing that catches my eye is the huge bed as it is nearly taking up the entire room."
        "Other than that there's also a desk, a regular wardrobe and a bedside lamp."
        "That is oddly placed {i}on{/i} the bed."
        h "I won't complain, the room works."
        h "I didn't place that much importance on my room anyways."
        show old funeral troubled
        o "Low aspirations, I guess."
        h "But there is one thing that kind of bugs me."
        show old funeral normal
        o "Just spit it out, then."
        h "Can I, if it's okay, can I get other bedsheets than these bloomy sheets?"
        o "That's not a problem."
        o "Though it was originally from your Mother."
        "Mum hers, heh?"
        h "In that case, disregard what I said."
        h "I'll take them."
        show old funeral troubled
        o "Oh."
        show old funeral normal
        o "You sure about that?"
        show old funeral normal:
            linear 1.0 xalign 0.8
        o "When I look at it more closely, I guess the cheesy color {i}really{/i} does seem unfitting for a young growing boy."
        h "Hands off the bedsheets. I said it's fine."
        o "Well, suit yourself."
        
        if cakeflag == False:
            show old:
                linear 1.0 xalign 0.5
            o "Oh right, the cake."
            show old:
                linear 0.5 xalign 0.2
                linear 0.5 xzoom -1.0
            pause 1.0
            show old at twitchtwice
            pause 0.5
            show old:
                linear 1.0 xalign 0.8
                linear 0.5 xzoom 1.0
            o "I'll leave it on the desk, ok?"
            h "Much appreciated."
            o "C'mon, don't be so polite."
            o "Too stiff for a boy. I'll make it my mission to wean it out of you."
            "His carefree grin really makes it seem like he has nothing but his mission in mind."
            "Which kind of makes me happy, I guess?"
            
        o "I'll be downstairs if you need me."
        hide old with Dissolve (1.0)
        play sound stairs
        h "I guess this is where I'll be staying for the time being."
        
        if location_table == 0:
            h "Now for the cake."
            play sound plate
            "I place the plate on the table, along with a cake fork and a handful of kitchen paper."
            "It seems like [nickname_old] doesn't trust me on staying clean while eating cakes."
            h "Heh, I'll show you my refined cake eating skills."
            h "Just you wait, [nickname_old] you dummy!"
            with vpunch
            "I cramp the cake in my mouth as the sides of my mouth get sullied little by little."
            window hide
            show bg weather with wiperight
            "While doing so, I am met with a particular view behind the big window."
            h "The weather's not looking good today."
            "I hoped to be greeted with a more bright sky."
            "A more fitting sky to be remembered when I funnelled my courage in order to come here."
            h "There's no use complaining, I guess."
            show bg bedroom 
            with wipeleft
            h "The cake on my plate is no more."
            h "It wasn't half bad, that cake."
            play sound fallinbed
            "I plump down on my bed with the mass of a kid and a cake that is now a dweller of his stomach."
            
        play sound pillow
        h "Bed seems comfortable enough."
        
        if location_table == 4:
            "Though early, I guess a little bit of sleep may do me well."
            play sound fallinbed
            "I lose strength as my head falls softly on the pillow; my mind at peace."
            "My hands grab the edges of the bed, momentarily hugging the bed in its entireness."
            "I am not even bothered to tuck myself in."
            
        "And the bedsheets may as well be the only thing that's connecting me to this place."

        window hide
        stop music fadeout (4.0) 
        scene black with Dissolve (2.0)
        centered "With that train of thought, I slowly drifted into sleep." with dissolve
        
    else:
        $location_table = 0
        "I took the cake plate in my hands."
        "I don't know why but eating upstairs sounds like a plausible thing for me to do."
        h "I want to eat the cake in my room, is that okay?"
        show old funeral normal:
            xalign 0.5 yalign 0.5
        with Dissolve (0.5)
        o "Oh-ho. Eager to see the room already?"
        o "Though I'd hoped for us to spend some time together."
        h "I can't?"
        o "How can I ever say {i}no{/i} to you, Heiden?"
        "He adds a wide grin while at least a third of his cake had already vanished from his plate."
        o "I'll do you a service and show you to your room."
             
        window hide
        stop music fadeout 2.0
        show black with fade
        play sound stairs
        o "You'll get the guest room for now, tell me if you need something."
        h "I'll manage somehow."
        $eat_clear = True
        jump upstairs
        
    jump afternoon
return

#Chapter 1.4 : Home  [END]
################################################################################