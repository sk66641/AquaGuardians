# # The script of the game goes in this file.

# # Declare characters used by this game. The color argument colorizes the
# # name of the character.

# define e = Character("Eileen")
define slowdissolve = Dissolve(1.0)
# define shockdissolve = Dissolve(0.5)

# # The game starts here.
image splash = "NeuroWarriors.png"
label splashscreen:
    


    show splash with dissolve:
        xalign 0.5
        yalign 0.5
    with Pause(2.0)

    play music "load.mp3" fadeout 1
    
    hide splash with dissolve
    with Pause(1.0)

    # scene black
    # with Pause(1.0)

    show text "NeuroWarriors presents AquaGuardians" with dissolve
    with Pause(2.0)
    
    hide text with dissolve
    with Pause(1.0)

    # $ renpy.movie_cutscene("videos/videoplayback.mp4")
    return 

# label start:

#     # Show a background. This uses a placeholder by default, but you can
#     # add a file (named either "bg room.png" or "bg room.jpg") to the
#     # images directory to show it.
#     play music "nature.mp3" fadeout 1

#     scene bg cave
#     with slowdissolve

#     scene bg room

#     # This shows a character sprite. A placeholder is used, but you can
#     # replace it by adding a file named "eileen happy.png" to the images
#     # directory.

#     show eileen happy:
#         xalign -0.3
#         yalign 1.0
#     with slowdissolve

#     # These display lines of dialogue.

#     e "You've created a new Ren'Py game."

#     show elien shock transp:
#         xalign -0.05
#         yalign 0.25
#     with shockdissolve

#     e "Once you add a story, pictures, and music, you can release it to the world!"

#     # This ends the game.

#     menu:

#         "Yes, I do.":
#             jump choice1_yes

#         "No, I don't.":
#             jump choice1_no

#     label choice1_yes:

#         $ menu_flag = True

#         e "While creating a multi-path visual novel can be a bit more work, it can yield a unique experience."

#         jump choice1_done

#     label choice1_no:

#         $ menu_flag = False

#         e "Games without menus are called kinetic novels, and there are dozens of them available to play."

#         jump choice1_done

#     label choice1_done:

#         # ... the game continues here.
 

#     return


label start:
    call screen choose_route
    return