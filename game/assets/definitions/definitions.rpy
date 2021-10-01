# python definitions      
init python:
    freak_out = 0
    stay_calm = 0
    main_char = ""
    main_char_pronoun = ""
    main_char_pronoun_singular = ""
    main_char_pronoun_possessive = ""
    costume = ""
    beginning_choice = ""
    routeA_scene3_choice = ""
    style.input.size = 40

# positional definitions
init:

    # Positional definitions that affects more than one
    define gui.BubbleDialogue_width = 650
    define gui.MainCharacterDialogue_xpos = 330
    define gui.DialogueBoxText_xpos = 320
    define gui.DialogueBoxText_ypos = 100
    define gui.DialogueBoxText_size = 20
    define gui.DialogueBox_ypos = 650
    define gui.Namebox_xalign = 0.5
    define gui.Namebox_ypos = 47
    define gui.Namebox_xpos = 402


    #Narrator Dialogue Texbox and Namebox
    define gui.narratorBubble_ypos = 670
    define gui.narratorDialogue_xpos = 285
    define gui.narratorDialogue_ypos = 50

    # Protagonist before naming
    define gui.innerThoughtsName_xpos = 400

    # Protagonist after naming
    define gui.innerThoughtsNameAfter_xpos = 405

    # Only Right Character Talking
    define gui.rightCharacterDialogue_xpos = 355


    # image definitions
    image sun = "../game/assets/images/sun.jpg"

    image blackscreen = "../game/assets/images/blackscreen.png"

    image tempbkgrd = "../game/assets/images/tempbkgrd.png"

    image namecard = "../game/assets/images/Backgrounds/namecard.png"

    image calender = "../game/assets/images/backgrounds/calender.png"

    image map_image = "../game/assets/images/map.png"

    image inner_thought = "../game/assets/images/speech_bubbles/SpeechBubble_narrator.png"

    image bedroom = "../game/assets/images/backgrounds/bedroom.png"

    image mirror_background = "../game/assets/images/backgrounds/mirror_background.png"
    
    image bathroom = "../game/assets/images/backgrounds/bathroom.png"

    image cafe = "../game/assets/images/backgrounds/cafe.png"

    image cafe_table = "../game/assets/images/backgrounds/cafe_table.png"

    image car = "../game/assets/images/backgrounds/car.png"

    image forest_fog = "../game/assets/images/flashlight_minigame/forest fog.png"

    image party = "../game/assets/images/Backgrounds/party.png"

    image my_movie = Movie(channel="movie", play="../game/assets/movie/phonebooth.mpeg")

    image forest_dark = "../game/assets/images/Backgrounds/forest_dark.png"
    image forest_day = "../game/assets/images/Backgrounds/forest_day.png"

    image winner_panther = "../game/assets/images/Backgrounds/winner cat.jpg"

    image winner_cup = "../game/assets/images/Backgrounds/winner cup.jpg"

    image winner_truper = "../game/assets/images/Backgrounds/winner ranger.jpg"

    # MC Costumes
    image cup = "../game/assets/images/Costumes/cup.png"
    image panther = "../game/assets/images/Costumes/cat.png"
    image truper = "../game/assets/images/Costumes/super.png"

    # Camilla Sprites
    image c_happy = "../game/assets/images/Camilla/c_happy.png"
    image c_neutral = "../game/assets/images/Camilla/c_neutral.png"
    image c_annoyed = "../game/assets/images/Camilla/c_annoyed.png"
    image c_scared = "../game/assets/images/Camilla/c_scared.png"
    image c_terrified = "../game/assets/images/Camilla/c_terrified.png"

    # Tanner Sprites
    image t_happy = "../game/assets/images/Tanner/t_happy.png"
    image t_annoyed = "../game/assets/images/Tanner/t_annoyed.png"
    image t_neutral = "../game/assets/images/Tanner/t_neutral.png"
    image t_angry = "../game/assets/images/Tanner/t_angry.png"


    # Jesse Sprites
    image j_neutral = "../game/assets/images/Jesse/j_neutral.png"
    image j_happy = "../game/assets/images/Jesse/j_happy.png"
    image j_annoyed ="../game/assets/images/Jesse/j_annoyed.png"
    image j_angry ="../game/assets/images/Jesse/j_angry.png"
    image j_scared = "../game/assets/images/Jesse/j_scared.png"
    image j_terrified = "../game/assets/images/Jesse/j_terrified.png"


    # Sequinn Sprites
    image s_neutral = "../game/assets/images/Sequinn/s_neutral.png"
    image s_happy = "../game/assets/images/Sequinn/s_happy.png"
    image s_annoyed = "../game/assets/images/Sequinn/s_annoyed.png"
    image s_angry = "../game/assets/images/Sequinn/s_angry.png"
    

    # character definitions
    define c_right = Character('Camilla', 
    color="#ffffff", 
    who_font="../fonts/gooey.ttf", 
    size=40, 
    window_background="../game/assets/images/speech_bubbles/SpeechBubble_right.PNG", 
    window_ypos = gui.DialogueBox_ypos,
    what_xsize = gui.BubbleDialogue_width,
    what_xpos = 320,
    what_ypos = gui.DialogueBoxText_ypos,
    what_size = gui.DialogueBoxText_size,
    who_xpos = gui.Namebox_xpos,
    who_ypos = gui.Namebox_ypos,
    who_xalign = gui.Namebox_xalign
    ) # Camilla

    define c_left = Character('Camilla', 
    color="#ffffff", 
    who_font="../fonts/gooey.ttf", 
    size=40, 
    window_background="../game/assets/images/speech_bubbles/SpeechBubble_left.PNG", 
    window_ypos = gui.DialogueBox_ypos,
    what_xsize = gui.BubbleDialogue_width,
    what_xpos = gui.rightCharacterDialogue_xpos,
    what_ypos = gui.DialogueBoxText_ypos,
    what_size = gui.DialogueBoxText_size,
    who_xpos = gui.Namebox_xpos,
    who_ypos = gui.Namebox_ypos,
    who_xalign = gui.Namebox_xalign
    ) # Camilla

    define j_left = Character('Jesse', 
    color="#ffffff", 
    who_font="../fonts/gooey.ttf", 
    size=40, 
    window_background = "../game/assets/images/speech_bubbles/SpeechBubble_left.png",
    window_ypos=gui.DialogueBox_ypos,
    what_xsize = gui.BubbleDialogue_width,
    what_xpos = gui.DialogueBoxText_xpos,
    what_ypos = gui.DialogueBoxText_ypos,
    what_size = gui.DialogueBoxText_size,
    who_xpos = gui.Namebox_xpos,
    who_ypos = gui.Namebox_ypos,
    who_xalign = gui.Namebox_xalign
    )  # Jesee

    define j_right = Character('Jesse', 
    color="#ffffff", 
    who_font="../fonts/gooey.ttf", 
    size=40, 
    window_background = "../game/assets/images/speech_bubbles/SpeechBubble_right.png",
    window_ypos=gui.DialogueBox_ypos,
    what_xsize = gui.BubbleDialogue_width,
    what_xpos = gui.DialogueBoxText_xpos,
    what_ypos = gui.DialogueBoxText_ypos,
    what_size = gui.DialogueBoxText_size,
    who_xpos = gui.Namebox_xpos,
    who_ypos = gui.Namebox_ypos,
    who_xalign = gui.Namebox_xalign
    )  # Jesee

    define s_left = Character('Sequinn', 
    color="#ffffff", 
    who_font="../fonts/gooey.ttf", 
    size=40,
    window_background = "../game/assets/images/speech_bubbles/SpeechBubble_left.png",
    window_ypos=gui.DialogueBox_ypos,
    what_xsize = gui.BubbleDialogue_width,
    what_xpos = gui.DialogueBoxText_xpos,
    what_ypos = gui.DialogueBoxText_ypos,
    what_size = gui.DialogueBoxText_size,
    who_xpos = gui.Namebox_xpos,
    who_ypos = gui.Namebox_ypos,
    who_xalign = gui.Namebox_xalign
    ) # Sequinn

    define s_right = Character('Sequinn', 
    color="#ffffff", 
    who_font="../fonts/gooey.ttf", 
    size=40,
    window_background = "../game/assets/images/speech_bubbles/SpeechBubble_right.png",
    window_ypos=gui.DialogueBox_ypos,
    what_xsize = gui.BubbleDialogue_width,
    what_xpos = gui.DialogueBoxText_xpos,
    what_ypos = gui.DialogueBoxText_ypos,
    what_size = gui.DialogueBoxText_size,
    who_xpos = gui.Namebox_xpos,
    who_ypos = gui.Namebox_ypos,
    who_xalign = gui.Namebox_xalign
    ) # Sequinn

    define t_right = Character('Tanner', 
    color="#ffffff", 
    who_font="../fonts/gooey.ttf", 
    size=40,
    window_background="../game/assets/images/speech_bubbles/SpeechBubble_right.PNG", 
    window_ypos = gui.DialogueBox_ypos,
    what_xsize = gui.BubbleDialogue_width,
    what_xpos = gui.DialogueBoxText_xpos,
    what_ypos = gui.DialogueBoxText_ypos,
    what_size = gui.DialogueBoxText_size,
    who_xpos = gui.Namebox_xpos,
    who_ypos = gui.Namebox_ypos,
    who_xalign = gui.Namebox_xalign
    ) # Tanner

    define t_left = Character('Tanner', 
    color="#ffffff", 
    who_font="../fonts/gooey.ttf", 
    size=40,
    window_background="../game/assets/images/speech_bubbles/SpeechBubble_left.PNG", 
    window_ypos = gui.DialogueBox_ypos,
    what_xsize = gui.BubbleDialogue_width,
    what_xpos = gui.DialogueBoxText_xpos,
    what_ypos = gui.DialogueBoxText_ypos,
    what_size = gui.DialogueBoxText_size,
    who_xpos = gui.Namebox_xpos,
    who_ypos = gui.Namebox_ypos,
    who_xalign = gui.Namebox_xalign
    ) # Tanner

    define t_and_s = Character('Tanner and Sequinn', 
    color="#ffffff", 
    who_font="../fonts/gooey.ttf", 
    size=35,
    window_background="../game/assets/images/speech_bubbles/SpeechBubble_both.PNG", 
    window_ypos = gui.DialogueBox_ypos,
    what_xsize = gui.BubbleDialogue_width,
    what_xpos = gui.DialogueBoxText_xpos,
    what_ypos = gui.DialogueBoxText_ypos,
    what_size = gui.DialogueBoxText_size,
    who_xpos = gui.Namebox_xpos,
    who_ypos = gui.Namebox_ypos,
    who_xalign = gui.Namebox_xalign)

    define t_and_j = Character('Tanner and Jesse', 
    color="#ffffff", 
    who_font="../fonts/gooey.ttf", 
    size=35,
    window_background="../game/assets/images/speech_bubbles/SpeechBubble_both.PNG", 
    window_ypos = gui.DialogueBox_ypos,
    what_xsize = gui.BubbleDialogue_width,
    what_xpos = gui.DialogueBoxText_xpos,
    what_ypos = gui.DialogueBoxText_ypos,
    what_size = gui.DialogueBoxText_size,
    who_xpos = gui.Namebox_xpos,
    who_ypos = gui.Namebox_ypos,
    who_xalign = gui.Namebox_xalign)

    define mc = Character('[main_char]', 
    color="#ffffff", 
    who_font="../fonts/gooey.ttf", 
    size=35, 
    window_background="../game/assets/images/speech_bubbles/ThoughtBubble.png", 
    window_ypos=gui.DialogueBox_ypos, 
    who_xpos=gui.innerThoughtsNameAfter_xpos, 
    who_ypos=gui.Namebox_ypos,
    who_xalign = gui.Namebox_xalign, 
    what_xsize= gui.BubbleDialogue_width, 
    what_xpos= gui.MainCharacterDialogue_xpos, 
    what_ypos= gui.DialogueBoxText_ypos
   ) # Protagonist

    define no_name = Character("???", 
    color="#ffffff", 
    who_font="../fonts/gooey.ttf", 
    size=35, what_prefix="{i}", 
    what_suffix="{/i}", 
    window_background="../game/assets/images/speech_bubbles/ThoughtBubble.png", 
    window_ypos=gui.DialogueBox_ypos, 
    who_xpos=gui.innerThoughtsName_xpos, 
    who_ypos=gui.Namebox_ypos,
    who_xalign = gui.Namebox_xalign, 
    what_xsize= gui.BubbleDialogue_width, 
    what_xpos= gui.MainCharacterDialogue_xpos, 
    what_ypos= gui.DialogueBoxText_ypos
    ) # Protagonist prior to naming

    define narrator = Character("", 
    color="#ffffff", 
    window_background="../game/assets/images/speech_bubbles/SpeechBubble_narrator.png", 
    window_top_padding=45, 
    window_left_padding=40, 
    window_ypos=gui.narratorBubble_ypos, 
    what_xsize=gui.BubbleDialogue_width, 
    what_xpos=gui.narratorDialogue_xpos, 
    what_ypos=gui.narratorDialogue_ypos
    ) # narrator 







