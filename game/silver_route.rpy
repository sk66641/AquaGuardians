define silver_character = Character("Silver", color = "#C0C0C0", outlines = [ (absolute(2), "#000", absolute(0), absolute(0)) ])

label silver_start:
    silver_character "Yo. I'm [silver_character]."
    jump silver_scene1

label silver_scene1:
    # This is where silver's route will be.
    jump silver_ending

label silver_ending:
    silver_character "Coming soon!"
    
    # set silver to true to indicate silver's ending was completed.
    $ persistent.silver = True
    "THE END"
    return
 