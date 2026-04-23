# Izstrādes žurnāls (DEVLOG)

### Projekta mērķis
Izveidot personīgo finanšu izsekotāju, kas ļauj pievienot izdevumus, skatīt kopsavilkumu un eksportēt datus.

### Veiktie labojumi un koda skaidrojums

**1. Datu ielādes loģika (storage.py)**
Sākotnēji programma meklēja `expenses.json` failu saknes mapē, kas radīja kļūdas.
*Risinājums:* Definēts relatīvais ceļš, lai fails tiktu meklēts tajā pašā mapē, kur atrodas skripts.
```python
import json
FILE_NAME = "expenses.json"

def load_expenses():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


### Programmas darbības plūsma
[Sākums] -> [Ielādēt JSON datus] -> [Parādīt Izvēlni] 
   -> [Lietotāja izvēle]
      1. Pievienot -> [Ievadīt datus] -> [Saglabāt JSON]
      2. Skatīt -> [Izvade tabulā]
      3. Eksports -> [Izveidot CSV]
   -> [Iziet] -> [Beigas]
