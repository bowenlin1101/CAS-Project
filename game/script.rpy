# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define mc = Character("Richard Long", color = "#2c85de")
define dk = Character("Demon King", color = "#ff0000")
define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy


    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

label scam:
    scene logcabin
    #In a remote log cabin at a writing desk with a quill and ink and paper
    #offering the innocent souls of first-borns as a professional and gourmet chef
    #show quill_and_ink

    #devil sees scam and sends the information back RVSP at your latest conveinence
    scene reception

    #information is received by mc
    scene successful bait

    return

label infiltration:

    return

label decryption:

    return

label library:

    return

label pugna_ultima:

    return

label bash_into_the_future:

    return

label ending_chance_for_konami:

    return

label credits:
    #Might want to switch to NVL for the credits
    "Coded in Ren\'Py"
    "Most of the artwork is from opengameart.com"
    "Developer team: Bowen Lin and Christopher Bardari"
    "Music:"
    return
