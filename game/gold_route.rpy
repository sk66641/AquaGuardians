define gold_character = Character("Gold", color = "#FFD700", outlines = [ (absolute(2), "#000", absolute(0), absolute(0)) ])

label gold_start:
    gold_character "Yo. I'm [gold_character]."
    jump gold_scene1

label gold_scene1:
    # This is where gold's route will be.
    jump gold_ending

label gold_ending:
    gold_character "Coming soon!"

    # set gold to true to indicate gold's ending was completed.
    $ persistent.gold = True
    "THE END"
    return