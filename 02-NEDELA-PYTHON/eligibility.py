# eligibility.py - Atbilstības pārbaudītājs

vecums = int(input("Ievadi savu vecumu: "))
ir_students = input("Vai esi students? (j/n): ").lower() == 'j'

# Kompleksā loģika: Pārbaudām vecumu un statusu
if vecums >= 65:
    print("Tu kvalificējies senioru atlaidei!")
elif vecums >= 18 and vecums <= 26 and ir_students:
    print("Tu kvalificējies studentu atlaidei!")
elif vecums >= 18:
    print("Tu esi pilngadīgs, bet atlaides nav.")
else:
    print("Tu esi nepilngadīgs.")