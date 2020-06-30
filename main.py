
# Funktionsdefinitionen --------------------------------------


# Funktion die "player_hp" formatiert in der Konsole ausgibt
def print_player_hp(player_hp):
    print(f"Remaining HP: {player_hp}")


# Funktion, welche den Betrag "damage_points" von "player_hp"
# abzieht und den neuen Wert von "player_hp" zurück gibt
def hit_player(player_hp, damage_points):
    player_hp -= damage_points

    # player_hp soll nie kleiner als 0 sein!
    if player_hp < 0:
        player_hp = 0

    print_player_hp(player_hp)
    return player_hp


# Unser Program ----------------------------------------------


# Initialisierung von player_hp
player_hp = 100
print(f"Initial HP: {player_hp}")

# "Dem Spieler Schaden zufügen"
player_hp = hit_player(player_hp, 15)
player_hp = hit_player(player_hp, 25)
player_hp = hit_player(player_hp, 20)
while (player_hp > 0):
    player_hp = hit_player(player_hp, 10)


# ------------------------------------------------------------
