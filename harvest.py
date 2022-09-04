############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, name):
        """Initialize a melon type."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    muskmelon.add_pairing("mint")
    all_melon_types.append(muskmelon)

    casaba = MelonType("cas", 2003, "orange", False, False, "Casaba")
    casaba.add_pairing("strawberries")
    casaba.add_pairing("mint")
    all_melon_types.append(casaba)

    crenshaw = MelonType("cren", 1996, "green", False, False, "Crenshaw")
    crenshaw.add_pairing("prosciutto")
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType(
        "yw", 2013, "yellow", False, True, "Yellow Watermelon"
    )
    yellow_watermelon.add_pairing("ice cream")
    all_melon_types.append(yellow_watermelon)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pairing in melon.pairings:
            print(f"- {pairing}")
        print("")


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_lookup = {}

    for melon in melon_types:
        melon_lookup[melon.code] = melon

    return melon_lookup


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, field, harvester):
        """Initialize a melon."""
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester

    def is_sellable(self):
        """Checks if melon is sellable."""
        if self.shape_rating > 5 and self.color_rating > 5 and self.field != 3:
            return True
        return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melons = []
    melons_by_id = make_melon_type_lookup(melon_types)

    melon_1 = Melon(melons_by_id["yw"], 8, 7, 2, "Sheila")
    melons.append(melon_1)

    melon_2 = Melon(melons_by_id["yw"], 3, 4, 2, "Sheila")
    melons.append(melon_2)

    melon_3 = Melon(melons_by_id["yw"], 9, 8, 3, "Sheila")
    melons.append(melon_3)

    melon_4 = Melon(melons_by_id["cas"], 10, 6, 35, "Sheila")
    melons.append(melon_4)

    melon_5 = Melon(melons_by_id["cren"], 8, 9, 35, "Michael")
    melons.append(melon_5)

    melon_6 = Melon(melons_by_id["cren"], 8, 2, 35, "Michael")
    melons.append(melon_6)

    melon_7 = Melon(melons_by_id["cren"], 2, 3, 4, "Michael")
    melons.append(melon_7)

    melon_8 = Melon(melons_by_id["musk"], 6, 7, 4, "Michael")
    melons.append(melon_8)

    melon_9 = Melon(melons_by_id["yw"], 7, 10, 3, "Sheila")
    melons.append(melon_9)

    return melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable():
            sellability = "(CAN BE SOLD)"
        else:
            sellability = "(NOT SELLABLE)"
        print(
            f"{melon.melon_type.name} was harvested by",
            f"{melon.harvester} from Field {melon.field} {sellability}",
        )


def make_melons_from_file(filename, melon_types):

    melons_by_id = make_melon_type_lookup(melon_types)
    melons_from_file = []

    harvest_log = open(filename)

    for line in harvest_log:
        line = line.rstrip()
        elements = line.split(" ")
        shape_rating = int(elements[1])
        color_rating = int(elements[3])
        melon_type = elements[5]
        harvester = elements[8]
        field = int(elements[11])
        melons_from_file.append(
            Melon(
                melons_by_id[melon_type], shape_rating, color_rating, field, harvester
            )
        )

    return melons_from_file


# get the sellability report of the melons from file
get_sellability_report(make_melons_from_file("harvest_log.txt", make_melon_types()))
