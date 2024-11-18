import random
import matplot.pyplot as plt
import os
import datetime as datetime
import numpy as np



# List of fun facts
fun_facts = [
    "Honey never spoils; edible honey has been found in ancient Egyptian tombs.",
    "Bananas are berries, but strawberries aren’t.",
    "A day on Venus is longer than a year on Venus.",
    "An octopus has three hearts.",
    "Cows have best friends and can become stressed when separated from them.",
    "The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after 38 minutes.",
    "The inventor of the Pringles can, Fred Baur, had his ashes buried in one.",
    "There are more stars in the universe than grains of sand on Earth.",
    "A jiffy is an actual unit of time. It's 1/100th of a second.",
    "Some cats are allergic to humans."
]

# Function to get a random fact
def get_random_fact():
    return random.choice(fun_facts)

# Display a random fun fact
print("Did you know? " + get_random_fact())
