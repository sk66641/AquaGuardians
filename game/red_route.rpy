define blue_character = Character("Blue", color = "#0000ff", outlines = [ (absolute(2), "#fff", absolute(0), absolute(0)) ])

define e = Character("Kavya")
define slowdissolve = Dissolve(0.2)
define shockdissolve = Dissolve(0.0)

label red_start:
    # label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    play music "nature.mp3" fadeout 1

    # scene bg cave

    scene start
    with slowdissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy:
        xalign -0.3
        yalign 1.0
    with slowdissolve

    # These display lines of dialogue.
    e "Rahul, a villager boy, is determined to reduce water usage in agriculture."

    scene beforefirst
    with slowdissolve

    show eileen happy:
        xalign -0.3
        yalign 1.0
    with slowdissolve
    e "He plans to
implement sustainable practices like drip irrigation, rainwater harvesting, and efficient crop
rotation, aiming to conserve water resources. "

    e "However, he is confused about which method
is most appropriate. Can you suggest one for him?"

    hide eileen happy
    with slowdissolve

    # show first
    # with slowdissolve


    show kavya serious:
        xalign -0.3
        yalign 1.0
    with slowdissolve
    # This ends the game.
label question1:
    menu:
        e "PUZZLE!\nCan you find out the most effective measures for reducing water usage in agriculture?"
        "Building new residential areas":
            jump wrong1
        " Implementing drip irrigation systems":
            jump correct1
        "Constructing skyscrapers":
            jump wrong1
        "Using water fountains in public parks":
            jump wrong1



    label correct1:

        $ menu_flag = True
        # hide kavya serious
        show eileen shock transp:
            xalign -0.3
            yalign 1.0
        with slowdissolve

        e "You are correct! Drip irrigation systems deliver water directly to the roots of plants, minimizing water wastage and ensuring efficient use of water resources. This method significantly reduces evaporation and runoff compared to traditional irrigation methods."
        # hide elieen shock transp
        # hide eileen shock transp
        # with slowdissolve

        # show eileen happy:
        #     xalign -0.3
        #     yalign 1.0
        # with slowdissolve

        jump choice1_done

    label wrong1:

        $ menu_flag = False
        show kavya unhappy:
            xalign -0.3
            yalign 1.0
        with slowdissolve
        e "It seems your choice didn’t quite fit Rahul’s needs. Review the options again. With each attempt, you'll help Rahul get closer to his dream of a more sustainable future. Keep trying!"
        show kavya serious:
            xalign -0.3
            yalign 1.0
        with slowdissolve

        jump question1

    label choice1_done:
        # hide kavya shock transp
        # show kavya happy:
        #     xalign -0.3
        #     yalign 1.0
        # with slowdissolve

        scene beforesecond
        with slowdissolve
        show eileen happy:
            xalign -0.3
            yalign 1.0
        with slowdissolve
        e "Rahul, is keen on selecting crops suitable for drought-prone areas."
        e "However, he is unsure about which method would be the most suitable."
        e "Could you provide a recommendation for him?"
    hide eileen happy
    with slowdissolve
    show kavya serious:
        xalign -0.3
        yalign 1.0
    with shockdissolve

label question2:
    menu:
        e "PUZZLE!\nCan you find out the crops, best suited for cultivation in drought-prone areas due to its low water requirement?"
        "Rice":
            jump wrong2
        "Okra":
            jump correct2
        "Sugarcane":
            jump wrong2
        "Watermelon":
            jump wrong2

    label correct2:

        $ menu_flag = True
        show eileen shock transp:
            xalign -0.3
            yalign 1.0
        with slowdissolve

        e "You are right! Okra is known for its ability to grow in hot and dry conditions, making it a suitable choice for drought-prone areas. It requires less water compared to crops like rice, sugarcane, and watermelon."
        # show eileen happy:
        #     xalign -0.3
        #     yalign 1.0
        # with slowdissolve
        jump choice2_done

    label wrong2:

        $ menu_flag = False
        show kavya unhappy:
            xalign -0.3
            yalign 1.0
        with slowdissolve
        e "It seems your choice didn’t quite fit Rahul’s needs. Review the options again. With each attempt, you'll help Rahul get closer to his dream of a more sustainable future. Keep trying!"
        show kavya serious:
            xalign -0.3
            yalign 1.0
        with slowdissolve
        jump question2

    label choice2_done:
        scene beforethird
        with slowdissolve
        show eileen happy:
            xalign -0.3
            yalign 1.0
        with slowdissolve
        e "Rahul is implementing sustainable methods for improving groundwater recharge."
        e "He
is considering building rooftop water harvesting systems to capture rainwater, aiming to
enhance water availability ."
        e "However, he's uncertain about which method would be the best
choice. Could you offer him some guidance?"
    hide eileen happy
    with slowdissolve

    show kavya serious:
        xalign -0.3
        yalign 1.0
    with shockdissolve

label question3:
    menu:
        e "PUZZLE!\nCan you figure out the sustainable method best suited for improving groundwater recharge?"
        "Using only chemical fertilizers":
            jump wrong3
        "Building rooftop water harvesting systems":
            jump correct3
        "Cutting down trees to make space for water storage":
            jump wrong3
        "Lining irrigation channels with plastic":
            jump wrong3

    label correct3:

        $ menu_flag = True
        show eileen shock transp:
            xalign -0.3
            yalign 1.0
        with slowdissolve
        e "You are right! Rooftop water harvesting systems collect and store rainwater, which can then be used to recharge groundwater. This practice helps in conserving water and ensuring its availability during dry periods."
        # show eileen happy:
        #     xalign -0.3
        #     yalign 1.0
        # with slowdissolve
        jump choice3_done

    label wrong3:

        $ menu_flag = False
        show kavya unhappy:
            xalign -0.3
            yalign 1.0
        with slowdissolve
        e "It seems your choice didn’t quite fit Rahul’s needs. Review the options again. With each attempt, you'll help Rahul get closer to his dream of a more sustainable future. Keep trying!"
        show kavya serious:
            xalign -0.3
            yalign 1.0
        with slowdissolve
        jump question3

    label choice3_done:
        scene beforefourth
        with slowdissolve
        show eileen happy:
            xalign -0.3
            yalign 1.0
        with slowdissolve
        e "He is passionate about involving local communities in water conservation projects. "
        e "He
believes that such efforts can lead to strengthened social cohesion and sustainable water
resource management."
        e "He's not sure which approach would work best. Could you give him
some recommendations?
"
    hide eileen happy
    with slowdissolve

    show kavya serious:
        xalign -0.3
        yalign 1.0
    with shockdissolve
label question4:
    menu:
        e "PUZZLE!\nWhat do you think could happen if local communities got involved in water conservation projects?"
        "Fragmentation of water resources and management efforts":
            jump wrong4
        "Short-term water availability but long-term ecological degradation":
            jump wrong4
        "Strengthened social cohesion and sustainable water resource management":
            jump correct4
        "Increased conflicts over water usage and distribution":
            jump wrong4

    label correct4:

        $ menu_flag = True
        show eileen shock transp:
            xalign -0.3
            yalign 1.0
        with slowdissolve
        e "You are right! When local communities are actively engaged in water conservation efforts, they are more likely to take ownership of the projects, leading to better maintenance and sustainable management of water resources"
        # show eileen happy:
        #     xalign -0.3
        #     yalign 1.0
        # with slowdissolve
        jump choice4_done

    label wrong4:

        $ menu_flag = False
        show kavya unhappy:
            xalign -0.3
            yalign 1.0
        with slowdissolve
        e "It seems your choice didn’t quite fit Rahul’s needs. Review the options again. With each attempt, you'll help Rahul get closer to his dream of a more sustainable future. Keep trying!"
        show kavya serious:
            xalign -0.3
            yalign 1.0
        with slowdissolve
        jump question4

    label choice4_done:
        scene beforefifth
        with slowdissolve
        show eileen happy:
            xalign -0.3
            yalign 1.0
        with slowdissolve

        e "Rahul, a villager boy, aims to desilt ponds and lakes as part of his water conservation efforts."
        e "He focuses on the primary ecological benefit of enhancing water storage capacity and
improving aquatic ecosystems ."
        e "he is uncertain about the most effective approach. Could
you suggest some options for him?"
    hide eileen happy
    with slowdissolve

    show kavya serious:
        xalign -0.3
        yalign 1.0
    with shockdissolve
label question5:
    show kavya serious:
        xalign -0.3
        yalign 1.0
    with slowdissolve
    menu:
        e "PUZZLE!\nfind out the primary ecological benefit of desilting ponds and lakes as part of a community-based water conservation strategy?"
        "Increased sedimentation downstream":
            jump wrong5
        "Enhanced water storage capacity and improved aquatic ecosystems":
            jump correct5
        "Expansion of urban infrastructure around water bodies":
            jump wrong5
        "Diversion of water resources to industrial use":
            jump wrong5

    label correct5:

        $ menu_flag = True
        show eileen shock transp:
            xalign -0.3
            yalign 1.0
        with slowdissolve
        e "Correct! by Enhancing water storage capacity and improved aquatic ecosystems Desilting helps to remove accumulated sediments, which increases the water storage capacity of ponds and lakes. This process also improves water quality and creates a healthier environment for aquatic life"
        # show eileen happy:
        #     xalign -0.3
        #     yalign 1.0
        # with slowdissolve
        jump choice5_done

    label wrong5:

        $ menu_flag = False
        show kavya unhappy:
            xalign -0.3
            yalign 1.0
        with slowdissolve
        e "It seems your choice didn’t quite fit Rahul’s needs. Review the options again. With each attempt, you'll help Rahul get closer to his dream of a more sustainable future. Keep trying!"
        show kavya serious:
            xalign -0.3
            yalign 1.0
        with slowdissolve
        jump question5

    label choice5_done:
        show black
        with slowdissolve

        show aqua:
            xalign 0.5
            yalign 0.3
        with slowdissolve
        e "Thank you for playing and supporting Rahul's mission for a better tomorrow."
        e " Your guidance has made a difference in his journey towards sustainable water management. Together, we can create a greener, more sustainable future!"

    # ... the game continues here.
    # set blue to true to indicate blue's ending was completed.
    $ persistent.red = True
    "Let's move to the next level."
    return
 