from ask import Ask
from content import If, And, Or

# Rules Definition for the Expert System
rules = {
    # Default rule asking a basic yes/no question
    'default': Ask(['y', 'n']),

    # Rules for asking about color and pattern
    'color': Ask(['red-brown', 'black and white', 'other']),
    'pattern': Ask(['dark stripes', 'dark spots']),

    # Defining rules for categorizing animals
    'mammal': If(Or(['hair', 'gives milk'])),
    'carnivore': If(Or([And(['sharp teeth', 'claws', 'forward-looking eyes']), 'eats meat'])),
    'ungulate': If(['mammal', Or(['has hooves', 'chews cud'])]),
    'bird': If(Or(['feathers', And(['flies', 'lays eggs'])])),

    # Specific animal identification rules
    'animal:monkey': If(['mammal', 'carnivore', 'color:red-brown', 'pattern:dark spots']),
    'animal:tiger': If(['mammal', 'carnivore', 'color:red-brown', 'pattern:dark stripes']),
    'animal:giraffe': If(['ungulate', 'long neck', 'long legs', 'pattern:dark spots']),
    'animal:zebra': If(['ungulate', 'pattern:dark stripes']),
    'animal:ostrich': If(['bird', 'long neck', 'color:black and white', 'cannot fly']),
    'animal:penguin': If(['bird', 'swims', 'color:black and white', 'cannot fly']),
    'animal:albatross': If(['bird', 'flies well'])
}

