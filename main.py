from classes.game import Persons, bcolors
from classes.inventory import Item
from classes.magic import Spell

# create black magic(damage)

fire = Spell("Fire", 10, 600, "black")
thunder = Spell("Thunder", 10, 600, "black")
blizzard = Spell("Blizzard", 10, 600, "black")
meteor = Spell("Meteor", 20, 1200, "black")
quake = Spell("Quake", 14, 140, "black")

# create white magic (heal)

cure = Spell("Cure", 25, 620, "white")
cura = Spell("Cura", 50, 1500, "white")

# create some item
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super-potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restore HP/MP of one party member", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restore party's HP/MP", 9999)
grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

# Instantiate people
player_spells = [fire, thunder, blizzard, meteor, cure, cura]  # list of spell object
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5},
                {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 2},
                {"item": grenade, "quantity": 5}]  # list of object with item object as data

player1 = Persons("Valos:", 3260, 132, 300, 34, player_spells, player_items)
player2 = Persons("Nick :", 4160, 180, 311, 34, player_spells, player_items)
player3 = Persons("Robot:", 3089, 174, 288, 34, player_spells, player_items)

players = [player1, player2, player3]
# Instantiate enemy

enemy = Persons("Enemy:", 11200, 701, 525, 25, [], [])

# start game

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACK!" + bcolors.ENDC)
running = True  # get false when one loses
i = 0
while running:
    print("=============================")
    print("\n")
    print("NAME                   HP                                   MP")
    for player in players:
        player.get_stats()
    print("\n")

    enemy.get_enemystats()

    for player in players:

        player.choose_action()  # ask player to choose action - magic or attack (choose action function)
        choice = input("      Choose action: ")
        index = int(choice) - 1
        if index == 0:  # if chosen attack
            dmg = player.generate_damage()  # generate damage based on his attack points
            enemy.take_damage(dmg)  # reduce enemy hp
            print("you attacked for", dmg, "points of damage.")
        elif index == 1:  # if chosen magic
            player.choose_magic()
            magic_choice = int(input("       Choose magic: ")) - 1  # ask player to choose type of magic or attack
            if magic_choice == -1:
                continue
            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_spell_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(
                    bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)  # if there is no sufficient mp , then no action
                continue

            player.reduce_mp(spell.cost)  # else reduce mp of player

            # heal
            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n", spell.name, "heals for", str(magic_dmg), bcolors.ENDC)
            elif spell.type == "black":
                enemy.take_damage(magic_dmg)  # reduce hp of enemy
                print(bcolors.OKBLUE + "\n", spell.name, "deals", str(magic_dmg), "points of damage", bcolors.ENDC)
        elif index == 2:
            player.choose_item()
            item_choice = int(input("        Choose item: ")) - 1
            if item_choice == -1:
                continue
            item = player.items[item_choice]["item"]
            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n" + "None left....." + bcolors.ENDC)
                continue
            player.items[item_choice]["quantity"] -= 1
            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKBLUE + "\n", item.name, "heals for", str(item.prop), bcolors.ENDC)
            elif item.type == "elixir":
                player.hp = player.maxhp
                player.mp = player.maxmp
                print(bcolors.OKGREEN + "\n", item.name, "fully restores HP/MP", bcolors.ENDC)
            elif item.type == "attack":
                enemy.take_damage(item.prop)
                print(bcolors.FAIL + "\n", item.name, "deals", str(item.prop) + "points of damage" + bcolors.ENDC)

    # now its enemy turn (always choose to attack)

    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player1.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, "points of damage")
    print("-----------------------------------")

    # status of both hp

    # print("Enemy HP", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC)
    # print("Your HP", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
    # print("Your MP", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC)

    # if anyone's hp becomes 0 he lost

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win!!" + bcolors.ENDC)
        running = False
    elif player1.get_hp() == 0:
        print(bcolors.FAIL + "You enemy has defeated you " + bcolors.ENDC)
        running = False
