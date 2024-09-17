screen choose_route:
    add "bg/bg_choose.png"
    # This button will delete any persistent variable
    button:
        text "Reset": 
            idle_color "#ff0000"
            hover_color "#0000ff"
        action Function(renpy.game.persistent._clear)

    # horizontal box containing the 5 image buttons
    hbox:
        xalign 0.5
        yalign 0.5
        yoffset 30  
        spacing 20

        imagebutton:
            auto "choices/blue_%s.png"
            action Jump("blue_start")
        imagebutton:
            auto "choices/red_%s.png"
            action Jump("red_start")
            sensitive persistent.blue == True
        imagebutton:
            auto "choices/yellow_%s.png"
            action Jump("yellow_start")
            sensitive persistent.blue == True and persistent.red == True
        imagebutton:
            auto "choices/silver_%s.png"
            action Jump("silver_start")
            # The imagebutton will be enabled if blue, red and yellow are true and disabled when at least one is false.
            sensitive persistent.blue == True and persistent.red == True and persistent.yellow == True  

        imagebutton:
            auto "choices/gold_%s.png"
            action Jump("gold_start")
            # The imagebutton will be enabled if blue, red, yellow and silver are true and disabled when at least one is false.
            sensitive persistent.blue == True and persistent.red == True and persistent.yellow == True and persistent.silver == True 