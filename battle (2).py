# Initialize the player's Pokémon
player_pokemon = "Mew"
player_hp = 80
player_attack = 125
player_defense = 80
player_heal = 45

# Initialize the enemy Pokémon
enemy_pokemon = "Mewtwo"
enemy_hp = 120
enemy_attack = 120
enemy_defense = 120

# Start the battle
print("A wild " + enemy_pokemon + " appeared!")
while player_hp > 0 and enemy_hp > 0:
    # Print the current status
    print("Player's HP: " + str(player_hp))
    print("Enemy's HP: " + str(enemy_hp))
    
    # Get the player's command
    command = input("What will you do? (attack/heal)")
    
    # Handle the player's command
    if command == "attack":
        # Calculate the damage
        damage = player_attack - enemy_defense
        if damage < 0:
            damage = 0
        enemy_hp -= damage
        print("You attacked for " + str(damage) + " damage!")
    elif command == "heal":
        player_hp += player_heal
        if player_hp > 100:
            player_hp = 100
        print("You healed for " + str(player_heal) + " HP!")
    else:
        print("Invalid command!")
    
    # Handle the enemy's attack
    if enemy_hp > 0:
        damage = enemy_attack - player_defense
        if damage < 0:
            damage = 0
        player_hp -= damage
        print("The wild " + enemy_pokemon + " attacked for " + str(damage) + " damage!")

# Print the results of the battle
if player_hp <= 0:
    print("You were defeated!")
else:
    print("You defeated the wild " + enemy_pokemon + "!")
