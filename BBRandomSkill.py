""" Python CLI App to generate random skills 

Usage: run the application. At the prompt, type `gen [Normals] [Doubles]` or just `[Normals] [Doubles]`. Type `exit` to exit 
For example, a Chaos Beastman has normal access to General, Strength and Mutation skills, and doubles access to Agility skills.
Therefore, to generate random skills for a Chaos Beastman you would input `gen GSM A` or just `GSM A`

"""

import random

""" List of all of the skills available to be gained (IE not Extraordinary) in BB2 """

generals = [
    "Block",
    "Dauntless",
    "Dirty Player",
    "Fend",
    "Frenzy",
    "Kick",
    "Kick Off Return",
    "Pass Block",
    "Pro",
    "Shadowing",
    "Strip Ball",
    "Sure Hands",
    "Tackle",
    "Wrestle"
]


agility = [
    "Catch",
    "Diving Catch",
    "Diving Tackle",
    "Dodge",
    "Jump Up",
    "Leap",
    "Side Step",
    "Sneaky Git",
    "Sprint",
    "Sure Feet"
]


passing = [
    "Accurate",
    "Dump Off",
    "Hail Mary Pass",
    "Leader",
    "Nerves of Steel",
    "Pass",
    "Safe Throw"
]


strength = [
    "Break Tackle",
    "Grab",
    "Guard",
    "Juggernaut",
    "Mighty Blow",
    "Multiple Block",
    "Piling On",
    "Stand Firm",
    "Strong Arm",
    "Thick Skull"
    ]


mutation = [
    "Big Hand",
    "Claw",
    "Disturbing Presence",
    "Extra Arms",
    "Foul Appearance",
    "Horns",
    "Prehensile Tail",
    "Tentacles",
    "Two Heads",
    "Very Long Legs"
    ]


letter_to_skill_list = {
        'G': generals, # general is a keyword...
        'A': agility,
        'P': passing,
        'S': strength,
        'M': mutation
    }


def gen_skill_from_accesses(accesses):
    """ Pick a random skill list from the given skill accesses, then a random skill from that list """
    letter = random.choice(accesses)
    skill_list = letter_to_skill_list[letter]
    return random.choice(skill_list)


def gen_random_skill(accesses):
    """ Pick a random skill, prioritising stat ups and doubles """
    normals = accesses[0]
    # Some players have no double access
    doubles = ""
    if len(accesses) > 1:
        doubles = accesses[1]

    roll_1 = random.randint(1,6)
    roll_2 = random.randint(1,6)

    print("Rolls: " + str(roll_1) + ", " + str(roll_2))

    skill = "None"

    # Stat ups are taken as a priority
    if roll_1 + roll_2 == 12:
        skill = "STR+"
    elif roll_1 + roll_2 == 11:
        skill = "AGI+"
    elif roll_1 + roll_2 == 10:
        # AV+ on a further 4-6, MA+ on a 1-3
        roll_3 = random.randint(1,6)
        skill = "AV+" if roll_3 > 3 else "MA+"
    elif roll_1 == roll_2 and doubles:
        # Take a doubles skill, if we have any doubles skill accesses
        skill = gen_skill_from_accesses(doubles)
    else:
        # No stat up or double, take the normal skill access
        skill = gen_skill_from_accesses(normals)

    return skill


def parse_gen_command(command):
    """ Parse a list of normal/double skill accesses from the gen command 
        Assumes that the command begins with 'gen' or nothing
        Returns list of strings, normally of length two
    """
    if command.startswith("gen"):
        command = command[4::]
    return command.split(' ')      # Split into (hopefully) two lists delimited by spaces


if __name__ == "__main__":
    """ In a loop, parse commands and generate the appropriate skill."""

    command = ""
    while True:
        command = input()
        if "exit" in command:
            break
        accesses = parse_gen_command(command)
        if accesses:
            print(gen_random_skill(accesses))
            print("")
    
