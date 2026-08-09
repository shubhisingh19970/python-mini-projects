import random
potions = [
    {
        "name": "Polyjuice Potion",
        "ingredients": [
            "Lacewing flies",
            "Leeches",
            "Powdered bicorn horn",
            "Fluxweed",
            "Knotgrass",
            "Boomslang skin",
            "A piece of the person you want to become"
        ],
        "use": "Transforms the drinker into the physical likeness of another person for one hour."
    },
    {
        "name": "Felix Felicis",
        "ingredients": [
            "Ashwinder eggs",
            "Squill bulb",
            "Murtlap tentacle",
            "Tincture of thyme",
            "Occamy eggshell",
            "Powdered common rue"
        ],
        "use": "Grants the drinker a limited period of good luck."
    },
    {
        "name": "Amortentia",
        "ingredients": [
            "Rose thorns",
            "Peppermint oil",
            "Moonstone",
            "Ashwinder egg"
        ],
        "use": "Causes a powerful infatuation or obsession in the drinker."
    },
    {
        "name": "Draught of Living Death",
        "ingredients": [
            "Valerian root",
            "Peppermint oil",
            "Hellebore"
        ],
        "use": "Induces a deep, almost death-like sleep in the drinker."
    }   ]
print("Welcome to the Potion Lab")
potion = random.choice(potions)

print("Your potion is:", potion["name"])
print("Your potion ingredients are:", potion["ingredients"])
print("Your potion use is:", potion["use"])