init:
    
    transform pronoun_text:
        linear 0.75 ypos 100

    transform map_transform:
        linear 0.75 ypos 0

    transform top_text:
        ypos 100


    # Shakes the screen prefusley 
    # transform my_shake:
    #     linear 0.1 xoffset -2 yoffset 2 
    #     linear 0.1 xoffset 3 yoffset -3 
    #     linear 0.1 xoffset 2 yoffset -2
    #     linear 0.1 xoffset -3 yoffset 3
    #     linear 0.1 xoffset 0 yoffset 0
    #     repeat
    
    transform pronoun_namecard:
        xpos 405
        ypos 550

    transform basicfade:
        on show:
            alpha 0.0
            linear 1.0 alpha 1.0
        on hide:
            linear 1.0 alpha 0.0

define dict_dissolve_1seconds = { "master" : Dissolve(1.0) }
define dict_emotion_change = { "master" : Dissolve(0.5) }
define dict_ease = {"master" : ease}
define dict_hpunch = {"master": hpunch}
define dict_moveinright = {"master": moveinright}
define dict_moveinleft = {"master": moveinleft}
define dict_move = {"master" : move}
define dict_fade_4seconds = { "master" : Fade(0.0, 0.0, 4.0)}
define dict_fade_1seconds = { "master" : Fade(0.0, 0.0, 2.0)}

define scene_transition = Dissolve(1.0)
define dark_forest_transition = { "master" : Dissolve(4.0) }
define text_dissolve = Dissolve(0.25)
