import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    BOLD = '\033[1m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


# mp=magic point(used to do magic)
# hp=high point
# atk= how much damage you can cause depends on atk
# magic= it's a list of dictionary (defines magic) with 3 types of magic , which cost some mp and provide dmg

class Persons:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["attack", "magic", "Items"]

    def generate_damage(self):  # generate damage based on attacking power of person
        return random.randrange(self.atkl, self.atkh)

    # def generate_spell_manage(self, i):  # generate damage based on magic chosen  by person
    #     mgl = self.magic[i]["dmg"] - 5
    #     mgh = self.magic[i]["dmg"] + 5
    #     return random.randrange(mgl, mgh)

    def take_damage(self, dmg):  # it decreases the high point by minus generated damage
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):  # cost used by magic
        self.mp -= cost

    # def get_spell_name(self, i):  # spell name of the chosen magic
    #     return self.magic[i]["name"]
    #
    # def get_spell_mp_cost(self, i):  # cost  of the chosen magic which decreases the mp
    #     return self.magic[i]["cost"]

    def choose_action(self):  # which action you are choosing -magic(heal or attack) or attack or item(heal)
        i = 1
        print("\n" + "       " + bcolors.BOLD + self.name + bcolors.ENDC)  # show name of player
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "      ACTIONS:" + bcolors.ENDC)
        for item in self.actions:
            print("            " + str(i) + ".", item)
            i += 1
        print()

    def choose_magic(self):  # which magic use are using
        i = 1

        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "      MAGIC:" + bcolors.ENDC)
        for spell in self.magic:
            print("            " + str(i) + ".", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1
        print()

    def choose_item(self):  # which magic use are using
        i = 1
        print("\n" + bcolors.OKGREEN + bcolors.BOLD + "       ITEMS:" + bcolors.ENDC)
        for item in self.items:
            print("            " + str(i) + ".", item["item"].name, ":", item["item"].description,
                  "(x" + str(item["quantity"]) + ")")
            i += 1
        print()
    def get_enemystats(self):
        hp_bar = ""
        bar_ticks = self.hp / self.maxhp * 100 / 2
        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1
        while len(hp_bar) < 50:
            hp_bar += ' '

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""
        if len(hp_string) < 11:
            decreased = 11 - len(hp_string)
            while decreased > 0:
                current_hp += ' '
                decreased -= 1
            current_hp += hp_string
        else:
            current_hp = hp_string


        print(
            bcolors.BOLD + bcolors.FAIL + "                         __________________________________________________ "+ bcolors.ENDC)
        print(bcolors.BOLD + self.name + "        " +
              current_hp + bcolors.FAIL + hp_bar + bcolors.OKGREEN + bcolors.ENDC)


    def get_stats(self):
        hp_bar = ""
        bar_ticks = self.hp / self.maxhp * 100 / 4
        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1
        while len(hp_bar) < 25:
            hp_bar += ' '

        mp_bar = ""
        mpbar_ticks = self.mp / self.maxmp * 100 / 10
        while mpbar_ticks > 0:
            mp_bar += "█"
            mpbar_ticks -= 1
        while len(mp_bar) < 10:
            mp_bar += ' '

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""
        if len(hp_string) < 9:
            decreased = 9 - len(hp_string)
            while decreased > 0:
                current_hp += ' '
                decreased -= 1
            current_hp += hp_string
        else:
            current_hp = hp_string

        mp_string = str(self.mp) + "/" + str(self.maxmp)
        current_mp = ""
        if len(mp_string) < 7:
            decreased = 7 - len(hp_string)
            while decreased > 0:
                current_mp += ' '
                decreased -= 1
            current_mp += mp_string
        else:
            current_mp = mp_string

        print(
            bcolors.BOLD + bcolors.OKGREEN + "                       _________________________ " + bcolors.OKBLUE + "           __________" + bcolors.ENDC)
        print(bcolors.BOLD + self.name + "        " +
              current_hp + bcolors.OKGREEN + hp_bar + bcolors.OKGREEN + bcolors.ENDC +
              "     " + current_mp + bcolors.OKBLUE + mp_bar + bcolors.OKBLUE + bcolors.ENDC)
