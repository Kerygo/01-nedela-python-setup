# 1. Izveido sarakstu
skaitli = [12, 25, 38, 41, 56, 70]

# 2. Pievieno un izdzēš elementus
skaitli.append(88)
skaitli.pop(0)

# 3. Summa un vidējais ar ciklu (bez sum/len)
kopeja_summa = 0
skaits = 0
for s in skaitli:
    kopeja_summa += s
    skaits += 1

videjais = kopeja_summa / skaits
print(f"Summa: {kopeja_summa}")
print(f"Vidējais: {videjais}")

# 4. Filtrēšana (tikai pāra skaitļi)
para_skaitli = []
for s in skaitli:
    if s % 2 == 0:
        para_skaitli.append(s)
print(f"Pāra skaitļi: {para_skaitli}")

# 5. Šķēlumi
print(f"Pirmie trīs: {skaitli[:3]}")
print(f"Pēdējie divi: {skaitli[-2:]}")
print(f"Katrs otrais: {skaitli[::2]}")