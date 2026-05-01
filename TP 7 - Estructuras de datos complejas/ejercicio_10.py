original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}

invertido = {}

for pais, capital in original.items():
    invertido[capital] = pais

print(f"Original {original}")
print(f"Invertido {invertido}")