define yellow_character = Character("Yellow", color = "#FFFF00", outlines = [ (absolute(2), "#000", absolute(0), absolute(0)) ])

label yellow_start:
    yellow_character "Yo. I'm [yellow_character]."
    jump yellow_scene1

label yellow_scene1:
    # This is where yellow's route will be.
    jump yellow_ending

label yellow_ending:
    yellow_character "Coming soon!"
    
    # set yellow to true to indicate yellow's ending was completed.
    $ persistent.yellow = True
    "THE END"
    return
 