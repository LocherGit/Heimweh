################################################################################
init python:

    class StarLight(object):

        def __init__(self):

            self.sm = SpriteManager(update=self.update)

            # A list of (sprite, starting-x, speed).
            self.stars = [ ]

            # Note: We store the displayable in a variable here.
            # That's important - it means that all of the stars at
            # a given speed have the same displayable. We render that
            # displayable once, and cache the result.

            d = Transform("images/etc/star.png", zoom=.02)
            for i in range(0, 50):
                self.add(d, 20)

            d = Transform("images/etc/star.png", zoom=.025)
            for i in range(0, 25):
                self.add(d, 80)

            d = Transform("images/etc/star.png", zoom=.05)
            for i in range(0, 25):
                self.add(d, 160)

            d = Transform("images/etc/star.png", zoom=.075)
            for i in range(0, 25):
                self.add(d, 320)

            d = Transform("images/etc/star.png", zoom=.1)
            for i in range(0, 25):
                self.add(d, 640)

            d = Transform("images/etc/star.png", zoom=.125)
            for i in range(0, 25):
                self.add(d, 1280)

        def add(self, d, speed):
            s = self.sm.create(d)

            start = renpy.random.randint(0, 840)
            s.y = renpy.random.randint(0, 600)

            self.stars.append((s, start, speed))

        def update(self, st):
            for s, start, speed in self.stars:
                s.x = (start + speed * st) % 840 - 20

            return 0
            
################################################################################
init:

    image bg pong field = "images/minigame/pong_field.png"

    python:

        class PongDisplayable(renpy.Displayable):

            def __init__(self):

                renpy.Displayable.__init__(self)

                # Some displayables we use.
                self.paddle = Image("images/minigame/pong.png")
                self.ball = Image("images/minigame/pong_ball.png")
                self.player = Text(_("Heiden"), size=36)
                self.eileen = Text(_("CPU"), size=36)
                self.ctb = Text(_("Click to Begin"), size=36)

                # The sizes of some of the images.
                self.PADDLE_WIDTH = 8
                self.PADDLE_HEIGHT = 79
                self.BALL_WIDTH = 15
                self.BALL_HEIGHT = 15
                self.COURT_TOP = 108
                self.COURT_BOTTOM = 543

                # If the ball is stuck to the paddle.
                self.stuck = True

                # The positions of the two paddles.
                self.playery = (self.COURT_BOTTOM - self.COURT_TOP) / 2
                self.computery = self.playery

                # The speed of the computer.
                self.computerspeed = 350.0

                # The position, dental-position, and the speed of the
                # ball.
                self.bx = 88
                self.by = self.playery
                self.bdx = .5
                self.bdy = .5
                self.bspeed = 300.0

                # The time of the past render-frame.
                self.oldst = None

                # The winner.
                self.winner = None

            def visit(self):
                return [ self.paddle, self.ball, self.player, self.eileen, self.ctb ]

            # Recomputes the position of the ball, handles bounces, and
            # draws the screen.
            def render(self, width, height, st, at):

                # The Render object we'll be drawing into.
                r = renpy.Render(width, height)

                # Figure out the time elapsed since the previous frame.
                if self.oldst is None:
                    self.oldst = st

                dtime = st - self.oldst
                self.oldst = st

                # Figure out where we want to move the ball to.
                speed = dtime * self.bspeed
                oldbx = self.bx

                if self.stuck:
                    self.by = self.playery
                else:
                    self.bx += self.bdx * speed
                    self.by += self.bdy * speed

                # Move the computer's paddle. It wants to go to self.by, but
                # may be limited by it's speed limit.
                cspeed = self.computerspeed * dtime
                if abs(self.by - self.computery) <= cspeed:
                    self.computery = self.by
                else:
                    self.computery += cspeed * (self.by - self.computery) / abs(self.by - self.computery)

                # Handle bounces.

                # Bounce off of top.
                ball_top = self.COURT_TOP + self.BALL_HEIGHT / 2
                if self.by < ball_top:
                    self.by = ball_top + (ball_top - self.by)
                    self.bdy = -self.bdy
                    renpy.sound.play("audio/sfx/pong_beep.mp3", channel=0)

                # Bounce off bottom.
                ball_bot = self.COURT_BOTTOM - self.BALL_HEIGHT / 2
                if self.by > ball_bot:
                    self.by = ball_bot - (self.by - ball_bot)
                    self.bdy = -self.bdy
                    renpy.sound.play("audio/sfx/pong_beep.mp3", channel=0)

                # This draws a paddle, and checks for bounces.
                def paddle(px, py, hotside):

                    # Render the paddle image. We give it an 800x600 area
                    # to render into, knowing that images will render smaller.
                    # (This isn't the case with all displayables. Solid, Frame,
                    # and Fixed will expand to fill the space allotted.)
                    # We also pass in st and at.
                    pi = renpy.render(self.paddle, 800, 600, st, at)

                    # renpy.render returns a Render object, which we can
                    # blit to the Render we're making.
                    r.blit(pi, (int(px), int(py - self.PADDLE_HEIGHT / 2)))

                    if py - self.PADDLE_HEIGHT / 2 <= self.by <= py + self.PADDLE_HEIGHT / 2:

                        hit = False

                        if oldbx >= hotside >= self.bx:
                            self.bx = hotside + (hotside - self.bx)
                            self.bdx = -self.bdx
                            hit = True

                        elif oldbx <= hotside <= self.bx:
                            self.bx = hotside - (self.bx - hotside)
                            self.bdx = -self.bdx
                            hit = True

                        if hit:
                            renpy.sound.play("audio/sfx/pong_boop.mp3", channel=1)
                            self.bspeed *= 1.10

                # Draw the two paddles.
                paddle(68, self.playery, 68 + self.PADDLE_WIDTH)
                paddle(724, self.computery, 724)

                # Draw the ball.
                ball = renpy.render(self.ball, 800, 600, st, at)
                r.blit(ball, (int(self.bx - self.BALL_WIDTH / 2),
                              int(self.by - self.BALL_HEIGHT / 2)))

                # Show the player names.
                player = renpy.render(self.player, 800, 600, st, at)
                r.blit(player, (20, 57))

                # Show Eileen's name.
                eileen = renpy.render(self.eileen, 800, 600, st, at)
                ew, eh = eileen.get_size()
                r.blit(eileen, (790 - ew, 57))

                # Show the "Click to Begin" label.
                if self.stuck:
                    ctb = renpy.render(self.ctb, 800, 600, st, at)
                    cw, ch = ctb.get_size()
                    r.blit(ctb, (400 - cw / 2, 57))


                # Check for a winner.
                if self.bx < -200:
                    self.winner = "cpu"

                    # Needed to ensure that event is called, noticing
                    # the winner.
                    renpy.timeout(0)

                elif self.bx > 1000:
                    self.winner = "heiden"
                    renpy.timeout(0)

                # Ask that we be re-rendered ASAP, so we can show the next
                # frame.
                renpy.redraw(self, 0)

                # Return the Render object.
                return r

            # Handles events.
            def event(self, ev, x, y, st):

                import pygame

                # Mousebutton down == start the game by setting stuck to
                # false.
                if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                    self.stuck = False

                # Set the position of the player's paddle.
                y = max(y, self.COURT_TOP)
                y = min(y, self.COURT_BOTTOM)
                self.playery = y

                # If we have a winner, return him or her. Otherwise, ignore
                # the current event.
                if self.winner:
                    return self.winner
                else:
                    raise renpy.IgnoreEvent()
                    
################################################################################
# Declare characters again
define definition = Character(None, window_yfill=True, window_xmargin=20, window_ymargin=200)
define bv = Character(None, kind=nvl, what_prefix="\"", what_suffix="\"", what_color="#62ac5b")
define hv = Character(None, kind=nvl, what_prefix="\"", what_suffix="\"", what_color="#1d87da")
define ov = Character(None, kind=nvl, what_prefix="\"", what_suffix="\"", what_color="#d72b2b")

define pv = Character(None, kind=nvl, what_prefix="\"", what_suffix="\"", what_color="#b66a1c")


define bs_jstandard = Character('Bartender', color="#62ac5b", window_left_padding=160, show_side_image=Image("images/character/barte_jogside0.png", xalign=0.0, yalign=1.0))
define bs_jlookaway = Character('Bartender', color="#62ac5b", window_left_padding=160, show_side_image=Image("images/character/barte_jogside1.png", xalign=0.0, yalign=1.0))
define bs_jclosed = Character('Bartender', color="#62ac5b", window_left_padding=160, show_side_image=Image("images/character/barte_jogside2.png", xalign=0.0, yalign=1.0))
define bs_jsurprised = Character('Bartender', color="#62ac5b", window_left_padding=160, show_side_image=Image("images/character/barte_jogside3.png", xalign=0.0, yalign=1.0))
define bs_jsmile = Character('Bartender', color="#62ac5b", window_left_padding=160, show_side_image=Image("images/character/barte_jogside4.png", xalign=0.0, yalign=1.0))
define bs_jsmug = Character('Bartender', color="#62ac5b", window_left_padding=160, show_side_image=Image("images/character/barte_jogside5.png", xalign=0.0, yalign=1.0))

define hs_standard = Character('Heiden', color="#1d87da", window_left_padding=160, show_side_image=Image("images/character/heiden_side0.png", xalign=0.0, yalign=1.0))
define hs_tired = Character('Heiden', color="#1d87da", window_left_padding=160, show_side_image=Image("images/character/heiden_side1.png", xalign=0.0, yalign=1.0))
define hs_active = Character('Heiden', color="#1d87da", window_left_padding=160, show_side_image=Image("images/character/heiden_side2.png", xalign=0.0, yalign=1.0))

define ls_standard = Character('Lisette', color="#ef92ac", window_left_padding=160, show_side_image=Image("images/character/lisette_side0.png", xalign=0.0, yalign=1.0))
define ls_embarrassed = Character('Lisette', color="#ef92ac", window_left_padding=160, show_side_image=Image("images/character/lisette_side1.png", xalign=0.0, yalign=1.0))
define ls_serious = Character('Lisette', color="#ef92ac", window_left_padding=160, show_side_image=Image("images/character/lisette_side2.png", xalign=0.0, yalign=1.0))
define ls_annoyed = Character('Lisette', color="#ef92ac", window_left_padding=160, show_side_image=Image("images/character/lisette_side3.png", xalign=0.0, yalign=1.0))

define ps_standard = Character('Prittner', color="#b66a1c", window_left_padding=160, show_side_image=Image("images/character/prittner1.png", xalign=0.0, yalign=1.0))

define lx = Character('Waitress', color="#ef92ac")
define l = Character('Lisette', color="#ef92ac")
define px = Character('Mr. Spooky', color="#b66a1c")
define p = Character('Mr. Prittner', color="#b66a1c")

#Declare character images
image barte jog stranger = "images/character/barte_jog_stranger.png"
image barte jog standard = "images/character/barte_jog0.png"
image barte jog lookaway = "images/character/barte_jog1.png"
image barte jog closed = "images/character/barte_jog2.png"
image barte jog surprised = "images/character/barte_jog3.png"
image barte jog smile = "images/character/barte_jog4.png"
image barte jog smug = "images/character/barte_jog5.png"

image heiden kitchen standard = "images/character/heiden_kitchen_normal.png"
image heiden kitchen active = "images/character/heiden_kitchen_active.png"
image heiden kitchen tired = "images/character/heiden_kitchen_tired.png"
image heiden final = "images/character/heiden_final.png"

image lisette standard = "images/character/lisette_1.png"
image lisette embarrassed = "images/character/lisette_2.png"
image lisette serious = "images/character/lisette_3.png"
image lisette annoyed = "images/character/lisette_4.png"
image lisette bstandard = "images/character/lisette_11.png"
image lisette bembarrassed = "images/character/lisette_12.png"
image lisette bserious = "images/character/lisette_13.png"
image lisette bannoyed = "images/character/lisette_14.png"

image prittner standard = "images/character/prittner.png"
image prittner stranger = "images/character/prittner_shadow.png"

image barte gray = im.Grayscale("images/character/barte_thinking1.png")
image old gray = im.Grayscale("images/character/old_funeral.png")
image prittner gray = im.Grayscale("images/character/prittner.png")

image irina photo = im.FactorScale("images/character/irina_0.png", 0.9, 1.0)

#Declare background images
image bg starlight = "images/used bg/starlight.jpg"
image bg park = "images/used bg/ch2_park.jpg"
image bg bridge = "images/used bg/ch2_bridge.jpg"
image bg jog1 = "images/used bg/ch2_jog1.jpg"
image bg jog2:
    "images/used bg/ch2_jog1.jpg"
    xzoom -1.0
image bg sport = "images/used bg/ch2_sport.jpg"
image bg terrace = "images/used bg/ch2_balcony.jpg"
image bg bench = "images/used bg/ch2_bench.jpg"

#Declare other images
image test = "images/gui/quick_main_hover.png"
image earth = "images/etc/earth.png"
image smartphone receive = "images/etc/smartphone.png"
image smartphone map = "images/etc/smartphone_map.png"
image smartphone map2 = "images/etc/smartphone_map2.png"
image tooltip_background : 
    "images/GUI/tooltip_background.png" 
    xalign 0.0 yalign 0.0
image bench_emergency :
    "images/gui/tooltip_park1.png"
    xalign 0.0 yalign 0.0
    
image cafe_emergency :
    "images/gui/tooltip_cafe.png"
    xalign 0.0 yalign 0.0
    
image pub_emergency :
    "images/gui/tooltip_bridge1.png"
    xalign 0.0 yalign 0.0
    
image tv off = "images/etc/tv0.png"
image tv ch = "images/etc/tv1.png"
image tv dog = "images/etc/tv2.png"
image tv enemy = "images/etc/tv3.png"
image tv enemy_defeated = "images/etc/tv4.png"
    
image finalframe = "images/etc/finalframe.png"

#Declare transformation
transform pullup:
    xpos 1.5
    linear 1.5 xalign .5
    
transform pullout:
    linear 1.5 xpos 1.5
    
define flash = Fade(.25, 0, .75, color="#fff")
    
#Declare audio
define audio.asteroid = "<from 10 to 30>audio/bgm/asteroid.mp3"
define audio.morning = "<from 10 to 30>audio/bgm/morning.mp3"
define audio.lisette = "audio/bgm/12 - The Cafe.mp3"
define audio.prittner = "audio/bgm/17 - Emptiness (literally ver.).mp3"
define audio.minigame = "audio/bgm/15 - Minigame.mp3"
define audio.thunderato = "audio/bgm/16 - Thunderato Theme (Full ver.).mp3"

#Declare sounds
define audio.scifidoor = "<from 5 to 20>audio/sfx/scifi_door.mp3"
define audio.charge = "audio/sfx/charge.mp3"
define audio.fence = "audio/sfx/fence.mp3"
define audio.doorbell = "audio/sfx/doorbell.mp3"
define audio.river = "audio/sfx/river.mp3"
define audio.playground = "audio/sfx/playground.mp3"
define audio.jogging = "audio/sfx/jogging.mp3"
define audio.chatter = "audio/sfx/cafe.mp3"
define audio.shock = "audio/sfx/shock.mp3"
define audio.remote = "audio/sfx/remote.mp3"
define audio.camera = "<from 0 to 1.5>audio/sfx/camera.mp3"

#Define special transitions
define wipe_starlight = CropMove(3.0, mode="wiperight")

################################################################################
#Chapter 2.0 : Starlight

label ch2:
    $ renpy.block_rollback()
    $ save_name = "Chapter 2.0 - Starlight"
    hide screen disable_Lmouse
    centered "Heed my words." with dissolve
    centered "Heed the story that is about to unfold." with dissolve
    play sound scifidoor
    $ renpy.pause(11.0, hard=True)
    show expression (StarLight().sm) as starfield
    with wipe_starlight
    play music asteroid
    stop sound
    centered "In a distant place, multiple lightyears away from the predators of the universe." with dissolve
    centered "A blue planet shines its light to the stars."
    hide expression (StarLight().sm) as starfield
    scene bg starlight
    with fade
    show earth:
        xalign .5 ypos 1.0
        parallel:
            linear 10.0 ypos .4
        parallel:
            linear 60 rotate 360
            repeat
        
    centered "This beautiful planet is inhabited by various lifeforms, including humans." with dissolve
    centered "They're all struggling, busy trying to stay alive, catching food, doing whatever." with dissolve
    centered "I am not really much of an inspirational and imaginative person myself." with dissolve
    centered "Infact, I am already aimless when it comes to my plans for today." with dissolve
    centered "Mum told me to stay diligent and do whatever I am able to do." with dissolve
    centered "But when push comes to shove, I'd much rather like to stay at home and keep it clean." with dissolve
    centered "And then I get scolded...{w} for cleaning up our {b}appartment{/b}!?" with dissolve
    centered "She wasn't much of a rational type of person."
    centered "But I still liked her."
    centered "And I liked our apartment, too."
    centered "But the place at uncle's not bad, either."
    centered "Speaking of which... {w}who's in charge of preparing breakfast?"
    centered "I better check the kitchen."
    centered "..."
    centered "PS: I love you, Mum. {w}I guess I am doing fine for now."
    stop music fadeout 2.0
    pause 2.0
    
    show earth:
        parallel:
            linear 40 rotate 360
            repeat
        parallel:
            linear 4 zoom 2.0 yalign .5
            
    play sound charge
    pause 3.0
    
    stop sound fadeout 1.0
    
    jump morning
            
    return
    
#Chapter 2.0 : Starlight [END]
################################################################################
#Chapter 2.1 : Morning

label morning:
    $ save_name = "Chapter 2.1 - Morning"
    scene bg house with pixellate
    $ renpy.pause(3.0, hard=True)
    "???" "Yup, that's the house alright."
    show barte jog stranger:
        xalign 0.5 yalign 0.5
    with dissolve
    window hide
    
    play music morning fadein 2.0
    nv "\nA strange figure is standing by the fence of the house."
    nv "\nThe moning dew, thawed due to the rising sun, has now spread to the blades of the plants."
    nv "\nA natural green adorns the scenery, a typical landscape of most rural areas."
    nv "\nThe house stands sturdy and acts as a reminder that this peaceful place is accented by man."
    nvl clear
    nv "\nMorning has come."
    nv "\nLike the perception of a \"cock-a-doodle-doo\" from a rooster, the day has began to spread its wings."
    nv "\nMorning has indeed come.\n"
    
    nvl hide
    show barte:
        linear 1.0 xalign .2
    pause 1
    show barte at shivertwice
    play sound fence
    nvl show
    
    bv "The gate's not locked?"
    nv "\nThe gate has sprung wide open by a single touch as if to invite him to the manor."
    
    nvl hide
    show barte:
        linear 2.0 xalign 1.5
    nvl show
    
    nv "\nWith the wind urging him to proceed, he takes short steps to cover this distance to the frontdoor."
    
    nvl clear
    play sound doorbell
    
    nv "\n\n\n\n\n\n\nNow face to face with the frontdoor, the man rings the door-bell but to no avail.\n"
    bv "..."
    nvl clear
    nvl hide
    
    pause 2.0
    play sound doorbell
    pause .2
    play sound doorbell
    pause .2
    play sound doorbell
    pause 2.0
    
    nvl show
    bv "Did something happen yesterday, after all?"
    nv "\n\nWith the suspicions lying in the air, the man can't help but feel a slightish bit restless.\n"
    nv "But those suspicions ended up being needless worries as he can listen to a discussion that can be heard from the inside.\n"
    hv "Uhm, [nickname_old]? {w}Should I go answer that?"
    ov "Don't bother, it's surely just a door-to-door salesman."
    hv "But [nickname_old], they're right at the frontdoor."
    hv "I can see the shadow looming behind the door already."
    hv "Don't you think that a salesman would have stopped right at the gate?"
    
    nvl clear
    ov "Urgh. You're being pesky today, Heiden."
    ov "My headache's 'bout to split me in half and the door's not making it any better."
    ov "..."
    ov "Now that I think about it, I think I forgot to lock the gate yesterday evening."
    hv "Your problems aside, I think I will answer the door anyways."
    stop music fadeout 2.0
    play sound footsteps2
    pause 2.0
    nv "\n\nWalking motions can be felt as the footsteps draw closer, the door knob being twisted and turned."
    
    nvl clear
    nvl hide
    
#Chapter 2.1 : Morning [END]
################################################################################
#Chapter 2.2 : After Breakfast

    scene bg livingroom with fade
    play music at_home fadein 2.0
    $ save_name = "Chapter 2.2 - After Breakfast"
    
    show heiden kitchen standard:
        xalign .5 yalign .5
    show barte jog standard:
        xalign -0.5 yalign .5
    with dissolve
    pause .5
    show heiden:
        linear .5 xalign 1.0
    show barte:
        linear .5 xalign .2
    pause .5
    h "Oh. It's just you, Barty."
    os_tired "Heya Barty!"
    b "I can see you fine from here, Old."
    b "No need to stand up from the sofa."
    os_tired "Much appreciated."
    
    show heiden:
        linear .5 xalign .9
    show barte:
        linear .5 xalign .1
        
    h "You've got bad timing, the breakfast has been served already."
    show barte jog lookaway with dissolve
    b "Nah, I am not here for food."
    b "I came here to deliver some medicine."
    show barte jog standard with dissolve
    os_normal "My hero."
    show barte jog lookaway with dissolve
    b "And your jacket, too."
    h "You can give them all to me."
    
    show barte:
        linear .5 xalign .4
    show heiden:
        linear .5 xalign .6
    pause .5
    show barte at twitchtwice
    show heiden at twitchtwice
    pause 1.0
    h "Woah, that's a lot."
    b "Big medicine for a big guy, I'd say."
    show barte:
        linear .5 xalign .1
    show heiden:
        linear .5 xalign .9
    pause .5
    show barte jog standard with dissolve
    b "Oh right, Heiden."
    h "Anything else?"
    b "Here, take this."
    h "What?"
    hide barte
    hide heiden
    with fade
    
    show smartphone receive at pullup
    
    $ renpy.pause(1.5, hard=True)
    hs_standard "What's this?"
    bs_jlookaway "This is a smartphone."
    bs_jstandard "Kids these days should carry one for safety."
    hs_active "Smartphones have games on it, right?"
    bs_jsmug "Not with the parental lock enabled."
    hs_tired "Figured as much."
    hs_tired "What a spoilsport you are."
    bs_jstandard "Well, well. No reason to be disheartened."
    bs_jstandard "Let me show you something."
    
    show smartphone receive at pullout
    $ renpy.pause(1.5, hard=True)
    show smartphone map at pullup
    $ renpy.pause(1.5, hard=True)
    
    hs_active "Woah, a map!"
    bs_jlookaway "Yes, at least it never hurts to know the city you're in."
    os_tired "You consider this a city?"
    bs_jstandard "Don't butt in, Old. {w}Kid's getting a valuable lesson right now."
    bs_jlookaway "Where was I? {w}Ah, yes."
    $ show_tutorial_haus = True
    with fade
    bs_jstandard "I've marked your house for now."
    bs_jstandard "If you ever get lost, just check the map."
    bs_jlookaway "The GPS-system works wonders nowadays."
    hs_active "It's like magic."
    bs_jsmile "For a little kid like you, the whole world would seem like a magic show."
    bs_jstandard "But well, now I am not too worried about you, you're free to enjoy the city if you like."
    
    show tooltip_background
    show expression Text(_("Morning"), size=40, color="#f0ff00", yalign=0.005, xalign=.98, drop_shadow=(2, 2)) as text with dissolve
    
    bs_jlookaway "You can spend your time however you like but be sure to be at home when it's {color=#ba0b0b}{b}Evening{/b}{/color}."
    hs_standard "Thanks, Barty!"
    
    $ show_tutorial_haus = False
    show smartphone map at pullout
    $ renpy.pause(1.5, hard=True)
    show heiden kitchen standard:
        xalign .9 yalign .5
    show barte jog lookaway:
        xalign .1 yalign .1
    with fade
    b "No problem. {w}Just try not to break it, okay?"
    b "These modern phones are quite costly even though they break fairly easy."
    h "But if it's that costly, why give it to a kid like-"
    show barte jog standard with dissolve
    b "Like I said, it's worth the investment if it's for your safety so just take it."
    show barte jog lookaway with dissolve
    b "All relevant phone numbers are already added to the phone's internal memory."
    b "I hope you're never gonna need them, but you have them just in case."
    show heiden kitchen active with dissolve
    h "Woah."
    show heiden kitchen standard
    h "Hey wait, where's [nickname_old] Old's number?"
    show barte jog standard with dissolve
    b "He"
    show barte jog smug
    extend " already broke his."
    os_tired "I can't help it, it's literally turning into mush the moment I touch it."
    show barte jog lookaway with dissolve
    b "I guess he's got an enormous grip strength."
    show barte jog standard with dissolve
    b "And that wasn't a compliment."
    show barte jog lookaway with dissolve
    b "But alas, I'll get going now."
    b "I am in the middle of my morning jog, you see."
    show heiden active with dissolve
    h "Don't mind us then."
    os_normal "We're sure to visit you tonight as well."
    os_tired "At least I hope so, it will depend on the effect of the medicine."
    show barte jog standard with dissolve
    b "Just take it easy, ok?"
    b "I'll be on my way then."
    show barte:
        linear 1.0 xalign -0.5
    h "See ya!"
    hide barte
    
    show heiden:
        xalign .5
    show old funeral normal:
        xalign .9
    with fade
    h "My first smartphone. It's so cool!"
    show old:
        linear .5 xalign .5
    o "Lemme see it for a bit."
    
    show heiden kitchen standard:
        linear .5 xalign .1
    h "Woah, hold on!"
    h "Based on what Barty said, you are likely to break it."
    show old:
        linear 1.0 xalign .9
    o "What'ya saying, Heiden? {w}You think I'll break it like a feisty infant?"
    show heiden kitchen tired with dissolve
    h "..."
    o "Stop it with that look, I understand."
    show heiden kitchen standard with dissolve
    o "Then let me say this: The next time you're on the map, try pressing the upper right corner of the smartphone."
    h "Where's that \"upper right corner\" of a smartphone supposed to be?"
    o "You'll know it if you hover your finger around it."
    h "What's gonna happen?"
    o "Just a tiny advice, try inputting the name of your mother when you're asked for a {b}password{/b}."
    h "Wha?"
    o "If I guessed right, Barty's surely someone who would do something like that."
    o "He's plainly using people's names as passwords, ha ha!"
    show heiden kitchen active with dissolve
    h "Maybe this password will unlock a hundred games!"
    show old funeral tired with dissolve
    o "With that out of the way, I guess I'll take a nap on the sofa and let the medicine do its work."
    hide old with dissolve
    os_tired "Just get out there and breathe some fresh air."
    show heiden kitchen standard with dissolve
    h "Well, if you say so."
    
    $progression = 0
    $mum_pw = True
    $park_unlock = 1
    $park_check = False
    $bridge_unlock = 1
    $bridge_check = False
    
    $now_park0 = False
    $now_bridge = False
    $now_park1 = False
    $now_home = False
    $now_cafe = False
    
#Chapter 2.2 : After Breakfast [END]
################################################################################
#Chapter 2.3 : Freetime

label freetime:
    scene bg livingroom
    show tooltip_background
    show expression Text(_("Morning"), size=40, color="#f0ff00", yalign=0.005, xalign=.98, drop_shadow=(2, 2)) as text

    $now_home = True
    $ save_name = "Chapter 2.3 - Morning Freetime"
    show heiden kitchen standard:
        yalign .5 xalign .5
    with fade
    h "Well, what should I do now?"
    
    show smartphone map2 at pullup
    $ renpy.pause(1.5, hard=True)
    call screen true_landkarte

    $ click = _return
    
    if click == "house":
        show smartphone map2 at pullout
        $ renpy.pause(1.5, hard=True)
        hide smartphone map2
        show heiden kitchen standard:
            yalign .5 xalign .5
        $ renpy.block_rollback()
        h "I am already at [nickname_old] Old's house..."
        h "And he told me to get out for some fresh air."
        h "I can't possibly stay here with him snoring away."
        h "Maybe I'll try to spend time somewhere else."
        jump freetime
        
    if click == "pw":
        jump pw_input
        
    if click == "pp":
        hide heiden with dissolve
        jump pingpong_play
    
    if click == "park":
        $bridge_check = False
        $park_check = True
        
    if click == "bridge": 
        $park_check = False
        $bridge_check = True
        
    show smartphone map2 at pullout
    $ renpy.pause(1.5, hard=True)
    hide smartphone map2
    show heiden kitchen standard:
        yalign .5 xalign .5
    $ renpy.block_rollback()
    if park_check:
        h "Should I spend my time at the {a=park_desc}park{/a} until {color=#f9aa19}noon{/color}?"
    else:
        h "Should I head to the {a=bridge_desc}bridge{/a} and spend time until {color=#f9aa19}noon{/color}?"
    menu:
        "Yes!":
            if park_check:
                $park_check = False
                $now_home = False
                h "Time to check out the park!"
                show heiden kitchen tired with dissolve
                h "Well. {w}After I've washed the dishes of course."
                jump park0
            else:
                $bridge_check = False
                $now_home = False
                jump bridge
        "No.":
            jump freetime
    
    
#######################################################
# Special Labels
label pw_input:
    show smartphone map2 at pullout
    $ renpy.pause(1.5, hard=True)
    hide smartphone map2
    $ renpy.block_rollback()
    "WELCOME TO THE PASSWORD OPERATOR\nPLEASE INPUT A PASSWORD TO UNLOCK ADDITIONAL FEATURES."
    
#                                                                               ######################
#    "TEST MODE"
#    menu:
#        "Reset persistent data":
#            $persistent.musicroom_unlocked = False
#            $persistent.bonus_unlocked = False
#            $persistent.oldie_unlocked = False
#            $persistent.pritty_unlocked = False
#            $pingpong = False
#            $mum_pw = True
#            "Persistent data cleared."
#        "No":
#            pass
#                                                                               ######################            
          
    if pingpong and persistent.musicroom_unlocked and persistent.bonus_unlocked and persistent.oldie_unlocked and persistent.pritty_unlocked:
        "WAIT A MOMENT.\nYOU ALREADY UNLOCKED EVERYTHING."
        hs_standard "Uhm, that's it?"
        hs_tired "Where are my hundred games?"
        "TERMINATING PASSWORD OPERATOR PROCESS.\nBYE BYE."
            
        if progression == 0:
            jump freetime
        elif progression == 1:
            jump freetime2
        elif progression == 2:
            jump freetime3
        else:
            jump freetime41
    else:
        pass
                
    if mum_pw == True:
        hs_standard "Oh right, what did [nickname_old] told me? {w}The name of my Mum should be a password?"
        hs_standard "Her name was \"Irina\" so I guess that's a password?"
        $ riddle = renpy.input("Input Password")
        if riddle.strip().lower() == "Irina" or riddle.strip().lower() == "irina":
            if pingpong == False:
                $pingpong = True
                $mum_pw = False
                "PASSWORD ACCEPTED.\n{w}THE GAME \"PING PONG\" HAS BEEN UNLOCKED."
                hs_standard "Oh."
                hs_active "OH YES."
        else:
            "PASSWORD INCORRECT."
            hs_tired "Well, it can't be helped."
            
    else:
        $ riddle = renpy.input("Input Password")
        if riddle.strip().lower() == "Heiden" or riddle.strip().lower() == "heiden":
            if persistent.musicroom_unlocked == False:
                $persistent.musicroom_unlocked = True
                "PASSWORD ACCEPTED.\n{w}A \"MUSIC ROOM\" HAS BEEN ADDED TO THE \"EXTRAS\" ON THE MAIN MENU."
                "COMPLETE THE VISUAL NOVEL AT LEAST ONCE IN ORDER TO GAIN ACCESS."
                hs_standard "Oh."
                hs_tired "Wait, a music room? {w}This smartphone does odd things..."
            else:
                "PASSWORD ALREADY ACCEPTED.\n\"MUSIC ROOM\" HAS ALREADY BEEN ADDED ADDED TO EXTRAS."
                hs_standard "Uhm."
                hs_tired "Did I use this password before?"
                
        elif riddle.strip().lower() == "Trevor" or riddle.strip().lower() == "trevor":
            if persistent.bonus_unlocked == False:
                $persistent.bonus_unlocked = True
                "PASSWORD ACCEPTED.\n{w}THE BONUS CHAPTER \"TREVOR'S PAST\" HAS BEEN ADDED TO THE \"EXTRAS\" ON THE MAIN MENU."
                "COMPLETE THE VISUAL NOVEL AT LEAST ONCE IN ORDER TO GAIN ACCESS."
                hs_standard "Oh."
                hs_tired "Wait, who is this \"Trevor\"? {w}This smartphone does odd things..."
            else:
                "PASSWORD ALREADY ACCEPTED.\n\"BONUS CHAPTER\" HAS ALREADY BEEN ADDED IN EXTRAS."
                hs_standard "Uhm."
                hs_tired "Did I use this password before?"
                
        elif riddle.strip().lower() == "Oliver" or riddle.strip().lower() == "oliver":
            if persistent.oldie_unlocked == False:
                $persistent.oldie_unlocked = True
                "PASSWORD ACCEPTED.\n{w}...BUT NOTHING WAS UNLOCKED."
                hs_standard "Oh."
                hs_tired "Wait, is [nickname_old] Old really that useless?"
            else:
                "PASSWORD ALREADY ACCEPTED.\nTHERE IS STILL NOTHING UNLOCKED."
                hs_standard "Uhm."
                hs_tired "Did I use this password before?"
                
        elif riddle.strip().lower() == "Prittner" or riddle.strip().lower() == "prittner":
            if persistent.pritty_unlocked == False:
                $persistent.pritty_unlocked = True
                "PASSWORD ACCEPTED.\n{w}A \"GALLERY\" HAS BEEN ADDED TO THE \"EXTRAS\" ON THE MAIN MENU."
                "COMPLETE THE VISUAL NOVEL AT LEAST ONCE IN ORDER TO GAIN ACCESS."
                hs_standard "Oh."
                hs_tired "Wait, a \"gallery\" of all things? {w}This smartphone does odd things..."
            else:
                "PASSWORD ALREADY ACCEPTED.\n\"GALLERY\" HAS ALREADY BEEN ADDED IN EXTRAS."
                hs_standard "Uhm."
                hs_tired "Did I use this password before?"
                
        elif riddle.strip().lower() == "Irina" or riddle.strip().lower() == "irina":
            "PASSWORD ALREADY ACCEPTED.\n\"PING PONG\" HAS ALREADY BEEN ADDED ADDED TO THE SMARTPHONE."
            hs_standard "Uhm."
            hs_tired "Did I use this password before?"
        else:
            "PASSWORD INCORRECT."
            hs_tired "Well, it can't be helped."
    "TERMINATING PASSWORD OPERATOR PROCESS.\nBYE BYE."
    
    if progression == 0:
        jump freetime
    elif progression == 1:
        jump freetime2
    elif progression == 2:
        jump freetime3
    else:
        jump freetime41
        

label pingpong_play:
    show smartphone map2 at pullout
    $ renpy.pause(1.5, hard=True)
    hide smartphone map2
    $ renpy.block_rollback()
    "ACTIVATE PING PONG."

label pingpong_now:
    stop music fadeout 2.0
    "REFER TO THE {a=pingpong_rules}MANUAL{/a} FOR THE GAME RULES."
    play music minigame
    window hide None
    scene bg pong field

    python:
        ui.add(PongDisplayable())
        winner = ui.interact(suppress_overlay=True, suppress_underlay=True)
    
    if now_home:
        scene bg livingroom with fade
    elif now_park0:
        scene bg park with fade
    elif now_bridge:
        scene bg bridge with fade
    elif now_park1:
        scene bg park with fade
    elif now_cafe:
        scene bg pub with fade
    else:
        scene bg livingroom with fade
    
    show tooltip_background
    
    if progression == 0:
        show expression Text(_("Morning"), size=40, color="#f0ff00", yalign=0.005, xalign=.98, drop_shadow=(2, 2)) as text
    elif progression == 1:
        show expression Text(_("Noon"), size=40, color="#f9aa19", yalign=0.008, xalign=.95, drop_shadow=(2, 2)) as text
    elif progression == 2:
        show expression Text(_("Afternoon"), size=40, color="#FD8204", yalign=0.008, xalign=1.0, drop_shadow=(2, 2)) as text
    else:
        show expression Text(_("Evening"), size=40, color="#ba0b0b", yalign=0.008, xalign=0.98, drop_shadow=(2, 2)) as text
        
    window show None

    if winner == "cpu":
        "YOU LOSE.\nYOU LOSE.\nWHAT A LOSER."
        hs_tired "Oh, what a humiliation..."
        
    else:
        hs_active "Ha! Take that! I won!"
        "HA HA HA.\nTHAT WAS JUST PURE LUCK.\nCONSIDER YOURSELF LUCKY THIS TIME."


    menu:
        hs_standard "How about another round?"
        "Sure.":
            jump pingpong_now
        "No thanks.":
            pass
    play music new_morning
    if progression == 0:
        jump freetime
    elif progression == 1:
        jump freetime2
    elif progression == 2:
        jump freetime3
    else:
        jump freetime41
            
#######################################################
# Definition Labels 

label tutorial_house:
    $ show_tutorial_haus = False
    definition "{b}Old's House{/b}\nThis is the house of [nickname_old] Old. It's pretty old but really big and has like four levels with the fourth being used as a storage. I don't know how he could afford such a big house all by himself..."
    $ show_tutorial_haus = True
    return
    
label pingpong_rules:
    definition "{b}Ping Pong{/b}\nOne of the oldest games out there. You move the left paddle with your mouse, up and down. Hit the ball by touching it with your paddle. If the ball goes beyond the reach of your opponent's paddle, you win!"
    return
    
label park_desc:
    definition "{b}The Park{/b}\nIt seems like this is a place with a huge playground. This is where kids my age would spend their time, right?\n\nI think [nickname_old] Old would like me to check it out for once."
    return
    
label bridge_desc:
    definition "{b}The Bridge{/b}\nI think Barty's heading that way. Maybe I can catch up to him and let him tour me around the town? That'd be better than me aimlessly wandering around, I guess.\n\nTime to bug Barty for a little favor."
    return