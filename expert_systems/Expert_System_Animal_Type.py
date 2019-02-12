# Question 2: Create an expert system if the animal type is
# protozoa (single cell animal), invertebrae, fish, bird, mammal, unknown


import sys
from pyknow import *

# Create a function that determines if the answer is true or false
def T_F(variable):
    if variable == "yes":
        answer = True
    else:
        answer = False
    return answer


# Set up the classes
class Cell(Fact):
    """Is it a multi-cell organism or not (only protozoa are single celled)"""

    pass


class Bones(Fact):
    """Does it have bones (only invertebraes do not have bones )"""

    pass


class Gills(Fact):
    "Does it have gills (only fish have gills)"
    pass


class Cover(Fact):
    "What is it's cover"
    pass


class Wings(Fact):
    "Does it have wings"
    pass


class AnimalType(KnowledgeEngine):
    # Determine if the animal is a protozoa using a yes or no question.
    @Rule(Cell(cell=False))
    def protozoa(self):
        print("It's a protozoa")

    # determine if the animal is an invertebrae using a yes or no question.
    @Rule(AND(Cell(cell=True), Bones(bones=False)))
    def bones(self):
        print("It's an invertebrae")

    # determine if the animal is a fish using a yes or no question
    @Rule(AND(Cell(cell=True), Bones(bones=True), Gills(gills=True)))
    def fish(self):
        print("It's a fish")

    # determine if the animal is a bird. Using the same questions from Q1. If it has wings and feathers then it is a bird.
    @Rule(
        AND(
            Cell(cell=True),
            Bones(bones=True),
            Gills(gills=False),
            Cover(cover="feathers"),
            Wings(wings=True),
        )
    )
    def bird(self):
        print("It's a bird")

    # determine if the animal is a mammal. Using the same questions from Q1. If it has fur it is a mammal.
    @Rule(
        AND(
            Cell(cell=True),
            Bones(bones=True),
            Gills(gills=False),
            Cover(cover="fur"),
            OR(Wings(wings=True), Wings(wings=False)),
        )
    )
    def mammal(self):
        print("It's a mammal")

    # determine if the animal is unknown using the same questions from Q1. If it has feathers, but not wings.
    @Rule(
        AND(
            Cell(cell=True),
            Bones(bones=True),
            Gills(gills=False),
            Cover(cover="feathers"),
            Wings(wings=False),
        )
    )
    def uknown(self):
        print("Uknown")


system = AnimalType()
system.reset()

# define all initial questions as false.
cell_q = False
bones_q = False
gills_q = False
cover_q = False
wings_q = False

# print("This program is case sensitive. Use 'Yes', 'No', 'fur', or 'feathers'")

cell_q = input("Is it multi-celled? (Yes or No) ").lower()
if (
    cell_q == "yes"
):  # if the animal is NOT multi-celled there is no reason to continue with the questions.
    bones_q = input("Does it have bones? (Yes or No) ").lower()
    if (
        bones_q == "yes"
    ):  # if the animal does NOT have bones there is no reason to continue with the questions.
        gills_q = input("Does it Gills? (Yes or No) ").lower()
        if (
            gills_q == "no"
        ):  # if the animal HAS gills there is no reason to continue with the questions.
            cover_q = input("Does it have fur or feathers? ").lower()
            wings_q = input("Does it have wings? (Yes or No) ").lower()

system.declare(
    Cell(cell=T_F(cell_q)),
    Bones(bones=T_F(bones_q)),
    Gills(gills=T_F(gills_q)),
    Cover(cover=cover_q),
    Wings(wings=T_F(wings_q)),
)
system.run()
