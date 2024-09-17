define red_character = Character("Red", color = "#ff0000", outlines = [ (absolute(2), "#fff", absolute(0), absolute(0)) ])

define e = Character("Kavya")
define slowdissolve = Dissolve(1.0)
define shockdissolve = Dissolve(0.5)
# image looping_animation = Animation("kavya unhappy.png", 0.1, "eileen shock.png", 0.1)
label blue_start:
    # label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    play music "Benson Boone.mp3" fadeout 1

    # scene bg cave

    # scene bg room
    # with slowdissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show looping_animation:
    #     xalign -0.3
    #     yalign 1.0
    # with slowdissolve

    show kavya serious:
        xalign -0.3
        yalign 1.0
    with slowdissolve

# These display lines of dialogue.

    # voice "rebecca/train.mp3"
    e "Hi! I am Kavya."
    # voice "rebecca/young.mp3"
    e "A young, passionate environmental scientist."
    # scene bg room
    # with slowdissolve

    scene intro1 
    with slowdissolve
    show kavya serious:
        xalign -0.3
        yalign 1.0
    with slowdissolve

    show kavya unhappy:
        xalign -0.3
        yalign 1.0
    with slowdissolve

    e "I grew up in a small village where water was always scarce. The wells ran dry often, and it became clear that poor groundwater management was the cause."

    scene intro2  
    with slowdissolve
    show kavya unhappy:
        xalign -0.3
        yalign 1.0
    with slowdissolve
    e "... Seeing my family and neighbors struggle for something as basic as water left a deep mark on me. That's when I knew I wanted to dedicate my life to solving these issues."
    scene intro3
    with slowdissolve
    show kavya serious:
        xalign -0.3
        yalign 1.0
    with slowdissolve
    e "... My experiences growing up pushed me to become an environmental scientist, and now I focus on finding sustainable solutions for water conservation."

    e "... I also believe in the power of education, so I make it my mission to teach others how we can manage water better and preserve this precious resource for future generations."

    # This ends the game.
 
    # set red to true to indicate red's ending was completed.
    $ persistent.blue = True

    # hide bg room
    show black
    with slowdissolve
    
    show aqua:
        xalign 0.5
        yalign 0.3
    with slowdissolve

    e "Let's begin the journey, the Aqua Guardian, an educational game on groundwater conservation and management"
    return
 