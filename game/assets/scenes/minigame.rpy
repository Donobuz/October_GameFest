# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.

label flashlight_minigame:
    scene forest_fog with Fade(1.0, 0.0, 1.0)
    "Find the traps hidden in the forest."
    "When you find everything, the button in the corner will say done."
    "Don't want to be bothered or can't find everything? Press skip."
    "But beware... there are consequenses to your actions."

    jump minigame


label flashlight_minigame_calm:
    "You manage to spot some odd looking contraptions." with text_dissolve

    mc "Hey, do you guys see that?" with text_dissolve
    
    "You point out the traps strewn about outside the path." with text_dissolve

    show c_scared at right
    with moveinright

    c_right "What the heck is that stuff doing in the woods?" with text_dissolve

    "Camilla looks around worriedly, on the verge of panic." with text_dissolve

    c_right "We really should just head back... Hey, I bet I could run back faster than how long it took us to get here. $10... who's in?" with text_dissolve

    show j_neutral at left
    with moveinleft

    j_left "Hey Mommy Long Legs, no one doubts that. You could outrun a cheetah fueled solely on your fear." with text_dissolve

    mc "Cami, we’re already so close now. There’s no point in turning back." with text_dissolve

    c_right "The fear... you feed off of it." with text_dissolve

    mc "And it tastes so good! Walk it missy." with text_dissolve

    show c_scared at offscreenright
    show j_neutral at offscreenleft
    with dict_emotion_change

    "You lead your friends through the path, making sure to avoid any traps that you see." with text_dissolve

    "Good eye on those traps. That could have slowed you down. Waldo could never." with text_dissolve

    hide text

    jump scene5_routeA



label flashlight_minigame_freakout:
    mc "Hmmm... we should be fine to keep going." with text_dissolve
    "You make your way forward without bringing up the glint you saw." with text_dissolve
    "Jesse and Camilla are following closely behind you when all of a sudden..." with text_dissolve

    "THWIP!" with hpunch
    "SMACK!" with hpunch
    "CRUNCH" with hpunch
    
    show j_terrified at left
    with moveinleft

    j_left "ACKKK!"

    show j_terrified at offscreenleft
    with dict_emotion_change

    "You turn around, only to see Jesse stopped by a tree spring trap and Camilla winding up like Roadrunner ready to high tail it out of there." with text_dissolve

    show j_angry at left
    with moveinleft

    j_left "Are you HECKING KIDDING ME!" with text_dissolve

    "Jesse struggles to get out of the pit while Camilla takes off running in fear, accidentally setting off the other traps nearby." with text_dissolve

    mc "Camilla! Wait!" with text_dissolve
    
    show j_annoyed at left
    with dict_emotion_change
    hide j_angry

    j_left "A little help here please!" with text_dissolve

    show j_annoyed at offscreenleft
    with dict_emotion_change

    "You rush over to pull Jesse's leg out of the pit." with text_dissolve

    "Suddenly you hear a scream break through the trees." with text_dissolve

    mc "Oh boy... this can't be good..." with text_dissolve

    "After one more good yank, you manage to free Jesse's leg." with text_dissolve

    "Good on you. You been working out?" with text_dissolve

    "You scramble down the path looking for Camilla but you see no one. You notice her shoe on the ground and leaves falling from above you." with text_dissolve

    "You and Jesse look up to see a frantic Camilla stuck in a net dangling above you." with text_dissolve

    show c_terrified at right
    with moveinright

    c_right "The woodland people... They're gonna eat us! My meat is so tender..." with text_dissolve

    show c_terrified at offscreenright
    with dict_emotion_change

    "You sigh and help Jesse up to release the ropes. Camilla drops to the ground, landing gracefully on her feet." with text_dissolve

    "If only her athletic abilities would have kept her from getting into this mess in the first place." with text_dissolve

    show c_scared at right
    with dict_moveinright

    c_right "Estoy chungo..." with text_dissolve

    show c_scared at offscreenright
    with dict_emotion_change

    "Camilla runs behind a bush, nauseous from hanging upside down." with text_dissolve

    "Eventually you and your friends continue on, being careful to avoid any more traps." with text_dissolve

    hide text
    jump scene5_routeA