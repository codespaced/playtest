#!../bin python3
# -*- coding: utf-8 -*-

# generator.py

import time
from random import randint

from character import Character, choose_ancestry, choose_background, choose_class
from menus import Menu


def main():
    character = None
    choice = ""
    main_menu = Menu("Main Menu", options={"N": "Create new character", "D": "Display character", "L": "Load character",
                                           "A": "Auto create", "q": "Quit"})

    while choice.lower() != "q":
        main_menu.display()
        choice = input("Please choose an option: ")
        if choice not in main_menu.options.keys():
            print("Invalid option, please choose again")
            continue
        elif choice in ["q", "Q"]:
            continue

        if choice in ["N", "n"]:
            """
            1. choose ancestry
                size, speed, hit points, languages, ability score boosts and flaws
                select ancestry feat
            """
            character = Character("TEST")
            choice = choose_ancestry()
            character.assign_ancestry(choice.upper())
            """
            2. choose background
                boosts to 2 abilities, skill training, background skill feat
            """
            choice = choose_background()
            character.assign_background(choice.upper())
            """
            3. choose class
                boost to key ability
            """
            choice = choose_class()
            character.assign_class(choice.upper())
            """
            4. ability scores
                base score of 10, boost +2, flaw -2
                ancestry gives free boost, humans gain 2
                background gives 2 free boosts (1 predetermined, 1 chosen)
                class boost
                4 free boosts
            """
            character.assign_ability_scores()
            """
            5. calculate hit points
                ancestry, class, CON mod
            6. Assign proficiency levels
                U: level -2, T: level, E: level + 1
            7. choose skills
                ranks from class + INT mod
                assign signature skills
            8. assign class features and feats
            9. buy gear
                150 SP to start
            """

        elif choice in ["L", "l"]:
                    print("That option not implemented, please try again.")
                    time.sleep(1)

        elif choice in ["d", "D"]:
            character.display()

        elif choice in ["a", "A"]:
            # Choose ancestry
            """
            choose ancestry randomly
            set character ancestry to Enum by choice
            for every bonus in ancestry.bonuses
                add to list in bonuses["ancestry"]
            for every flaw in ancestry.flaws
                add to list in bonuses["flaws"]
            set maxHP to ancestry HP value
            set character.size to ancestry.size
            set speed to ancestry.speed
            set languages to ancestry.languages
            for every ability in ancestry.special_abilities
                apply ability to character
            choose random ancestry feat
            """
            character = Character("auto")
            choice = choose_ancestry(rand=True)
            character.assign_ancestry(choice.upper())
            # Choose background
            """
            choose background randomly, weighted by ancestry
            set character background to Enum by choice
            for every bonus in background.bonuses
                add to list in bonuses["background"]
            add background.skill_feat to list of character feats
            add background.lore to dict of character skills
            set proficiency of skills[background.lore] to TRAINED
            """
            choice = choose_background(rand=True)
            character.assign_background(choice.upper())
            # Choose class
            """
            choose class randomly, weighted by ancestry + background
            set character class to Enum by choice
            set level to 1
            add class.bonus to list in bonuses["class"]
            """
            # Finalize Ability Scores
            """
            create named tuple of stats
            set all ability scores to 10
            for every flaw in bonuses["flaws"]
                apply flaw to ability score
            for every bonus in bonuses["ancestry"]
                remove bonus from stat list
                add bonus to ability score
                if bonus is free
                    choose appropriate ability from remaining stats
                    apply bonus to ability
            for bonus in bonuses["background"]
                choose bonus from options
                remove bonus from remaining ability
                add bonus to ability score
                if bonus is free
                    choose ability from remaining stats
                    apply bonus to ability
            for i in range(1, 5):
                choose ability from remaining stats
                apply bonus to ability
                remove ability from remaining stats
            apply class bonus to ability
            set ability scores to temp values
            """
            # Apply class to character
            """
            assign key ability score
            classDC = 10 + key ability mod + level
            add class HP + CON mod to HP total
            for proficiency in class.proficiencies
                assign proficiency to character
            for skill in signature skills
                assign skill as signature
            for i in range (1, class skills + 1)
                choose skill training
            """
            # skill modifier = ability mod + proficiency + other mods + feat + item
            # Buy Equipment
            """
            set starting money to 150 sp
            purchase weapon
            purchase armor
            purchase adventuring gear
            for purchase in purchases
                if melee, then assign strike
                elif ranged, then assign strike
                elif armor, then assign armor
                else, assign item to inventory
            set current money to remaining coins
            """
            # Fill in finishing details
            """
            set Armor Class
            set Touch Armor Class
            set maxBulk and encumbered values
            calculate current Bulk
            if current Bulk >= encumbered
                then assign encumbered condition
            assign melee and ranged strikes
            assign Perception modifier
            set Resonance Points total to CHA mod + level
            set current RP to maxRP value
            assign modifier for saving throws
            """
            ...


if __name__ == '__main__':
    main()
