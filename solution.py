x = [165, 248, 94, 346, 299, 73, 198, 221, 313, 137, 205, 87, 336, 110, 186, 69, 223, 213, 216, 216, 177, 138]
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
print(''.join(characters[i % 37] for i in x))
