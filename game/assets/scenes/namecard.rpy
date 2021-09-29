label namecard:

    no_name "Oh yeahhhh, that's hottttt..." with text_dissolve
    no_name "Now where did I put my ID?"
    "You find it lying on the nightstand..." with text_dissolve

    $ pronoun_uppercase = str.upper(main_char_pronoun)
    show namecard with dict_dissolve_1seconds 

    # show text "{color=#000000}{font=../fonts/gooey.ttf}She/her{/font}{/color}" at pronoun_namecard
    show text "{color=#4E3376}{size=30}[pronoun_uppercase]{/size}{/color}" at pronoun_namecard
    
    
    python:

        main_char = renpy.input("", "", allow=None, exclude='"!@#$%^&*()_+{}|:<>?/\][=`1234567890;.,', length=15, pixel_width=None, mask=None)
        main_char = main_char.strip()

        if not main_char:
            main_char = "John Doe"
    window hide
    jump scene1continue