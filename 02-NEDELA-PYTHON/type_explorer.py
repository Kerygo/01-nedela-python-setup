# Mainīgo definēšana
vards = "Gvido"          # Teksts (string)
vecums = 30              # Vesels skaitlis (integer)
temperatura = 36.6       # Daļskaitlis (float)
ir_ziema = False         # Loģiskais tips (boolean)
rezultats = None         # Tukša vērtība (NoneType)

# 1. Parādām katra mainīgā tipu
print(f"Mainīgais 'vards' ir {type(vards)}")
print(f"Mainīgais 'vecums' ir {type(vecums)}")
print(f"Mainīgais 'temperatura' ir {type(temperatura)}")

# 2. Tipu konvertēšana (Explicit conversion)
skaitlis_kā_teksts = "100"
istais_skaitlis = int(skaitlis_kā_teksts)
print(f"Pārvērsts un saskaitīts: {istais_skaitlis + 50}")

# 3. Truthy/Falsy piemērs
print(f"Vai tukšs teksts ir True? {bool('')}")
print(f"Vai tukšs teksts ir True? {bool('')}")
print(f"Vai skaitlis 0 ir True? {bool(0)}")
mana_ievade = input("Ievadi kaut ko: ")
print(f"Tu ierakstīji: {mana_ievade}")