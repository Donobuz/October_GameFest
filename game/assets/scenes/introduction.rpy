# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.






# The game starts here.

label start:

#Introduction
    scene blackscreen

    show text "Before we being, please choose your Pronouns" at truecenter
    with text_dissolve
    pause 2

    show text "{color=#ffffff}Choose your Pronouns{/color}" at pronoun_text
    with text_dissolve

    menu:
        "She/Her":
            $ main_char_pronoun = "SHE/HER"
            $main_char_pronoun_possessive = "her"
            $main_char_pronoun_singular = "She"
            hide text
            jump scene1
 
        "He/Him":
            $ main_char_pronoun = "HE/HIM"
            $main_char_pronoun_possessive = "him"
            $main_char_pronoun_singular = "He"
            hide text
            jump scene1

        "They/Them":
           $ main_char_pronoun = "THEY/THEM"
           $main_char_pronoun_possessive = "them"
           $main_char_pronoun_singular = "They"
           hide text
           jump scene1

#return ends the game
