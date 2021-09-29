# Costume Choices Here
label costume_change:
    show text "{color=#000000}{b}| {/color}{color=#E9810B}Choose your Costume{/color}{color=#000000} |{/b}{/color}" at top_text
    with text_dissolve
    menu:
        "Sexy Panther":
            jump confirm_panther
            hide text
            
        "90's Paper Cup":
            jump confirm_papercup
            hide text

        "Super TruperZ":
           jump confirm_truper
           hide text


label confirm_panther:
    scene panther with dissolve
    menu:
        "Sexy AF":
            hide text
            $costume = "Sexy Panther"
            jump namecard

        "Not It":
            scene mirror_background
            jump costume_change
            hide text

    #confirmation screen for panther

label confirm_papercup:
    scene cup with dissolve
    menu:
        "Sexy AF":
            hide text
            $costume = "90's Paper Cup"
            jump namecard

        "Not It":
            scene mirror_background
            jump costume_change
            hide text
    #confirmation screen for cup

label confirm_truper:
    scene truper with dissolve
    menu:
        "Sexy AF":
            hide text
            $costume = "Super Truperz"
            jump namecard

        "Not It":
            scene mirror_background
            jump costume_change
            hide text
    #confirmation screen for truper