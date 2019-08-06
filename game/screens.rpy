# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
default window_transform = NullTransform
transform NullTransform:
  pass
screen say(who, what, side_image=None, two_window=False):
    default side_image = None
    default two_window = False
    default window_transform = NullTransform

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window at window_transform:
        #window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:
                window at window_transform:
                #window:
                    style "say_who_window"

                    text who:
                        id "who"

            window at window_transform:
            #window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu
    
    # Which landkarten-version to use?
    if show_tutorial_haus:
        use tutorial_haus 
    if show_landkarte:
        use true_landkarte
    if show_interface_active:
        use interface_active
        
init -2 python:   
    show_tutorial_haus=False
    show_landkarte = False
    show_interface_active = False
    pingpong = False
    bridge_unlock = 0
    park_unlock = 0
    home_unlock = 0
    progression = 0

##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"

    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .5
        yalign .98

        has hbox

        textbutton _("Start Game") action Start() 
        textbutton _("Load Game") action ShowMenu("load")
        if persistent.extra_unlocked:
            textbutton _("Extras") action Start('extras')
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Quit") action Quit(confirm=False)

init -2:

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"

    #style.mm_button["Start Game"].activate_sound = "audio/sfx/game_start.mp3"

##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .5
        yalign .98

        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
#       textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"
        
##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker():

    frame:
        style "file_picker_frame"

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav"

            textbutton _("Previous"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("Next"):
                action FilePageNext()

        $ columns = 2
        $ rows = 5

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)


screen save():

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

screen load():

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text


##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():

    tag menu

    # Include the navigation.
    use navigation

    # Put the navigation columns in a three-wide grid.
    grid 3 1:
        style_group "prefs"
        xfill True

        # The left column.
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Display")
                textbutton _("Window") action Preference("display", "window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")

            frame:
                style_group "pref"
                has vbox

                label _("Transitions")
                textbutton _("All") action Preference("transitions", "all")
                textbutton _("None") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Text Speed")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time")

                if config.has_voice:
                    textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")


        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Skip")
                textbutton _("Seen Messages") action Preference("skip", "seen")
                textbutton _("All Messages") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Begin Skipping") action Skip()

            frame:
                style_group "pref"
                has vbox

                label _("After Choices")
                textbutton _("Stop Skipping") action Preference("after choices", "stop")
                textbutton _("Keep Skipping") action Preference("after choices", "skip")



        vbox:
            if languageON == True:
                frame:
                    style_group "pref"
                    has vbox
                    label _("Language")
                    textbutton "English" action Language(None)
                    textbutton "Deutsch" action Language("deutsch")
                
            frame:
                style_group "pref"
                has vbox

                label _("Music Volume")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Sound Volume")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Test"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

            if config.has_voice:
                frame:
                    style_group "pref"
                    has vbox

                    label _("Voice Volume")
                    bar value Preference("voice volume")

                    textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                    if config.sample_voice:
                        textbutton _("Test"):
                            action Play("voice", config.sample_voice)
                            style "soundtest_button"

init -2:
    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xmaximum 192
        xalign 1.0

    style soundtest_button:
        xalign 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action

    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Skip") action Skip()
        textbutton _("F.Skip") action Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu('preferences')

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"


############################################################
# Landkarten hier

screen interface_active:
    add "images/GUI/tooltip_background.png" xalign 0.0 yalign 0.0
    if progression == 0:
        add Text(_("Morning"), size=40, color="#f0ff00", yalign=0.0, xalign=.95, drop_shadow=(2, 2))
    elif progression == 1:
        add Text(_("Noon"), size=40, color="#f9aa19", yalign=0.0, xalign=.95, drop_shadow=(2, 2))
    elif progression == 2:
        add Text(_("Afternoon"), size=40, color="#FD8204", yalign=0.0, xalign=.95, drop_shadow=(2, 2))
        
screen gui_tooltip:
    add my_picture xpos my_tt_xpos ypos my_tt_ypos
    
screen tutorial_haus:
    imagebutton auto "gui/quick_main_%s.png" xpos 440 ypos 145 focus_mask True action Function(renpy.call, label="tutorial_house")

screen true_landkarte:
    
    if progression <= 3 and persistent.musicroom_unlocked:
        imagebutton auto "gui/quick_unlockmr_%s.png" xpos 633 ypos 285 focus_mask True 
    if progression <= 3 and persistent.bonus_unlocked:
        imagebutton auto "gui/quick_unlockbc_%s.png" xpos 633 ypos 345 focus_mask True
    if progression <= 3 and persistent.pritty_unlocked:
        imagebutton auto "gui/quick_unlockg_%s.png" xpos 633 ypos 405 focus_mask True
    
    if progression <= 3:
        imagebutton auto "gui/quick_pw_%s.png" xpos 633 ypos 165 focus_mask True action Return("pw") hovered Show("gui_tooltip", my_picture="images/gui/tooltip_pw.png", my_tt_xpos=0, my_tt_ypos=0) unhovered [Hide("gui_tooltip")]
    if pingpong == True and progression <= 3:
        imagebutton auto "gui/quick_pp_%s.png" xpos 633 ypos 225 focus_mask True action Return("pp") hovered Show("gui_tooltip", my_picture="images/gui/tooltip_pp.png", my_tt_xpos=0, my_tt_ypos=0) unhovered [Hide("gui_tooltip")]

# Freetime 1
    if progression == 0: #Home no trigger
        imagebutton auto "gui/quick_main_%s.png" xpos 440 ypos 230 focus_mask True action Return("house") hovered Show("gui_tooltip", my_picture="images/gui/tooltip_oldhouse.png", my_tt_xpos=0, my_tt_ypos=0) unhovered [Hide("gui_tooltip")]
    if bridge_unlock == 1 and progression == 0: # Bridge
        imagebutton auto "gui/quick_event_%s.png" xpos 395 ypos 321 focus_mask True action Return("bridge") hovered Show("gui_tooltip", my_picture="images/gui/tooltip_bridge.png", my_tt_xpos=0, my_tt_ypos=0) unhovered [Hide("gui_tooltip")]
    if park_unlock == 1 and progression <= 1: #Park
        imagebutton auto "gui/quick_event_%s.png" xpos 516 ypos 345 focus_mask True action Return("park") hovered Show("gui_tooltip", my_picture="images/gui/tooltip_park.png", my_tt_xpos=0, my_tt_ypos=0) unhovered [Hide("gui_tooltip")]
        
# Freetime 2
    if progression == 1: #Home
        imagebutton auto "gui/quick_main_%s.png" xpos 440 ypos 230 focus_mask True action Return("house1") hovered Show("gui_tooltip", my_picture="images/gui/tooltip_oldhouse.png", my_tt_xpos=0, my_tt_ypos=0) unhovered [Hide("gui_tooltip")]
    if bridge_unlock == 2 and progression == 1: #Cafepub
        imagebutton auto "gui/quick_event_%s.png" xpos 270 ypos 245 focus_mask True action Return("bridge1") hovered Show("gui_tooltip", my_picture="images/gui/tooltip_bridge1.png", my_tt_xpos=0, my_tt_ypos=0) unhovered [Hide("gui_tooltip")]
    if park_unlock == 2 and 1 <= progression <= 2: #BenchA
        imagebutton auto "gui/quick_event_%s.png" xpos 544 ypos 320 focus_mask True action Return("park1") hovered Show("gui_tooltip", my_picture="images/gui/tooltip_park1.png", my_tt_xpos=0, my_tt_ypos=0) unhovered [Hide("gui_tooltip")]

# Freetime 3
    if progression == 2 and park_unlock == 3: #BenchB
        imagebutton auto "gui/quick_event_%s.png" xpos 516 ypos 345 focus_mask True action Return("benchb") hovered Show("gui_tooltip", my_picture="images/gui/tooltip_park.png", my_tt_xpos=0, my_tt_ypos=0) unhovered [Hide("gui_tooltip")]
    if progression == 2 and bridge_unlock == 3: #HomeA
        imagebutton auto "gui/quick_main_%s.png" xpos 440 ypos 230 focus_mask True action Return("housea") hovered Show("gui_tooltip", my_picture="images/gui/tooltip_oldhouse.png", my_tt_xpos=0, my_tt_ypos=0) unhovered [Hide("gui_tooltip")]
    if progression == 2 and bridge_unlock <3: #HomeB
        imagebutton auto "gui/quick_main_%s.png" xpos 440 ypos 230 focus_mask True action Return("houseb") hovered Show("gui_tooltip", my_picture="images/gui/tooltip_oldhouse.png", my_tt_xpos=0, my_tt_ypos=0) unhovered [Hide("gui_tooltip")]

# Freetime 4
    if progression == 3: #Final Pub
        imagebutton auto "gui/quick_event_%s.png" xpos 270 ypos 245 focus_mask True action Return("final") hovered Show("gui_tooltip", my_picture="images/gui/tooltip_bridge1.png", my_tt_xpos=0, my_tt_ypos=0) unhovered [Hide("gui_tooltip")]

# Final Picture
    if progression == 4: #Final Picture
        imagebutton auto "gui/quick_final_%s.png" xpos 700 ypos 295 focus_mask True action Return("picture")
      
      
      
screen bonusroom:
    imagebutton auto "gui/bonus_back_%s.png" xpos 650 ypos 525 focus_mask True action MainMenu()
    
    if persistent.musicroom_unlocked == False:
        imagebutton auto "gui/bonus_mrno_%s.png" xpos 100 ypos 37 focus_mask True action Return("no")
    else:
        imagebutton auto "gui/bonus_mr_%s.png" xpos 100 ypos 37 focus_mask True action ShowMenu("music_room")
        
    if persistent.bonus_unlocked == False:
        imagebutton auto "gui/bonus_trevno_%s.png" xpos 100 ypos 225 focus_mask True action Return("no")
    else:
        imagebutton auto "gui/bonus_trev_%s.png" xpos 100 ypos 225 focus_mask True action Return("trevyes")   
        
    if persistent.pritty_unlocked == False:
        imagebutton auto "gui/bonus_gno_%s.png" xpos 100 ypos 412 focus_mask True action Return("no")
    else:
        imagebutton auto "gui/bonus_g_%s.png" xpos 100 ypos 412 focus_mask True action ShowMenu("gallery")
        
#    if persistent.credit2_unlocked == True:
 #       imagebutton auto "gui/bonus_credit2_%s.png" xpos 650 ypos 0 focus_mask True action Return ("credits")
    imagebutton auto "gui/bonus_delete_%s.png" xpos 650 ypos 275 focus_mask True action Return ("delete")

################################################################
init python:

    # Create a MusicRoom instance.
    mr = MusicRoom(fadeout=1.0)

    # Adding music files.
#   Normal BGMs
    mr.add("audio/bgm/03 - Happy Meeting.mp3",always_unlocked=True)
    mr.add("audio/bgm/04 - At the Funeral.mp3",always_unlocked=True)
    mr.add("audio/bgm/05 - Brand New Day Pt.1.mp3",always_unlocked=True)
    mr.add("audio/bgm/06 - Brand New Day Pt.2.mp3",always_unlocked=True)
    mr.add("audio/bgm/07 - Hello World!.mp3",always_unlocked=True)
    mr.add("audio/bgm/08 - Peaceful Days.mp3",always_unlocked=True)
    mr.add("audio/bgm/09 - Sleep Tight.mp3",always_unlocked=True)
    mr.add("audio/bgm/10 - Night Stroll.mp3",always_unlocked=True)
    
    mr.add("audio/bgm/11 - The Pub.mp3",always_unlocked=True)
    mr.add("audio/bgm/12 - The Cafe.mp3",always_unlocked=True)
    mr.add("audio/bgm/13 - Togetherness.mp3",always_unlocked=True)

#   Menu
    mr.add("audio/bgm/01 - Main Menu.mp3",always_unlocked=True)
    
#   Chapter Interludes
    mr.add("audio/bgm/02 - Chapter Interlude.mp3",always_unlocked=True)
    mr.add("audio/bgm/14 - Credits.mp3",always_unlocked=True)
    
#   Others
    mr.add("audio/bgm/15 - Minigame.mp3",always_unlocked=True)
    mr.add("audio/bgm/16 - Thunderato Theme (Full ver.).mp3",always_unlocked=True)
    mr.add("audio/bgm/17 - Emptiness (literally ver.).mp3",always_unlocked=True)
    
#   Discarded
    mr.add("audio/bgm/18 - Main Menu (discarded ver.).mp3",always_unlocked=True)
    mr.add("audio/bgm/19 - Happy Meeting (discarded ver.).mp3",always_unlocked=True)
    mr.add("audio/bgm/20 - The Pub (alternative ver.).mp3",always_unlocked=True)
    
screen music_room:

    tag menu

    frame:
        xpos 245 ypos 60
        has vbox spacing 5

        # The buttons that play each track.
        text "Menu BGMs"
        textbutton "Main Menu" action mr.Play("audio/bgm/01 - Main Menu.mp3")
        
        null height 20
        
        text "Interludes"
        textbutton "Chapter" action mr.Play("audio/bgm/02 - Chapter Interlude.mp3")
        textbutton "Credits" action mr.Play("audio/bgm/14 - Credits.mp3")
        
        null height 20
        
        text "Other BGMs"
        textbutton "Minigame" action mr.Play("audio/bgm/15 - Minigame.mp3")
        textbutton "Thunderato" action mr.Play("audio/bgm/16 - Thunderato Theme (Full ver.).mp3")
        textbutton "Emptiness" action mr.Play("audio/bgm/17 - Emptiness (literally ver.).mp3")
        
        
    frame:
        ypos 60 xpos 5
        has vbox spacing 5
        
        text "Normal BGMs"
        textbutton "Happy Meeting" action mr.Play("audio/bgm/03 - Happy Meeting.mp3")
        textbutton "At the Funeral" action mr.Play("audio/bgm/04 - At the Funeral.mp3")
        textbutton "Brand New Day Pt.1" action mr.Play("audio/bgm/05 - Brand New Day Pt.1.mp3")
        textbutton "Brand New Day Pt.2" action mr.Play("audio/bgm/06 - Brand New Day Pt.2.mp3")
        textbutton "Hello World!" action mr.Play("audio/bgm/07 - Hello World!.mp3")
        textbutton "Peaceful Days" action mr.Play("audio/bgm/08 - Peaceful Days.mp3")
        textbutton "Sleep Tight" action mr.Play("audio/bgm/09 - Sleep Tight.mp3")
        textbutton "Night Stroll" action mr.Play("audio/bgm/10 - Night Stroll.mp3")
        textbutton "The Pub" action mr.Play("audio/bgm/11 - The Pub.mp3")
        textbutton "The Café" action mr.Play("audio/bgm/12 - The Cafe.mp3")
        textbutton "Togetherness" action mr.Play("audio/bgm/13 - Togetherness.mp3")
        
    frame:
        ypos 60 xpos 402
        has vbox spacing 5
        
        text "Discarded BGMs"
        textbutton "Main Menu" action mr.Play("audio/bgm/18 - Main Menu (discarded ver.).mp3")
        textbutton "Happy Meeting" action mr.Play("audio/bgm/19 - Happy Meeting (discarded ver.).mp3")
        textbutton "The Pub" action mr.Play("audio/bgm/20 - The Pub (alternative ver.).mp3")        
        
    frame:
        ypos 10 xpos 5
        has hbox
        
        text "Music Volume"
        bar value Preference("music volume")
                
    frame:
        style_group "mm"
        xalign .5
        yalign .98

        has hbox

        # Buttons that let us advance tracks.
        textbutton "Previous Track" action mr.Previous()
        textbutton "Stop Playback" action mr.Stop()
        textbutton "Next Track" action mr.Next()
        
        null width 50
        # The button that lets the user exit the music room.
        textbutton "Main Menu" action ShowMenu("main_menu")

    # Restore the main menu music upon leaving.
    on "replaced" action Play("music", "audio/bgm/01 - Main Menu.mp3")
    
    
screen gallery:
    
    tag menu

    frame:
        style_group "mm"
        xalign .5
        yalign .86

        has hbox 
        
        textbutton "Heiden" action Show("gui_tooltip", my_picture="images/character/frame_heiden.png", my_tt_xpos=0, my_tt_ypos=0)
        textbutton "Uncle Old" action Show("gui_tooltip", my_picture="images/character/frame_oliver.png", my_tt_xpos=0, my_tt_ypos=0)
        textbutton "Bartender" action Show("gui_tooltip", my_picture="images/character/frame_trevor.png", my_tt_xpos=0, my_tt_ypos=0)

    frame:
        style_group "mm"
        xalign .5
        yalign .93

        has hbox 
        
        textbutton "Conductor" action Show("gui_tooltip", my_picture="images/character/frame_conductor.png", my_tt_xpos=0, my_tt_ypos=0)
        textbutton "Prittner" action Show("gui_tooltip", my_picture="images/character/frame_prittner.png", my_tt_xpos=0, my_tt_ypos=0)
        textbutton "Lisette" action Show("gui_tooltip", my_picture="images/character/frame_lisette.png", my_tt_xpos=0, my_tt_ypos=0)
        textbutton "Irina" action Show("gui_tooltip", my_picture="images/character/frame_irina.png", my_tt_xpos=0, my_tt_ypos=0)      
      
    frame:   
        xalign .5
        yalign 1.0

        has hbox
        textbutton "Main Menu" action [ ShowMenu("main_menu"), Hide("gui_tooltip")]
    on "replaced" action Play("music", "audio/bgm/01 - Main Menu.mp3")