#while
#whle dipakai ketika tau kapan berhenti
#while syarat berhenti:
    #apa yg akan diulango:
    
print("====================while===============")
index = 0
while index <= 200:
    print(f"index of value{index}")
    index += 1
#for
#dipake ketika kita tau awalan sama akhir
print("===========for===========")
#for index in range(0,201):
    #print(f"index of value{index}")
    
makanan = ["baso","mi","sayur","daging"]
for value in makanan:
    print(f"{value}")
    
#break dan continue

bilangan = 1
while bilangan <= 100:
    if bilangan % 2 == 0 :
        bilangan += 1
        continue
    print(f"{bilangan}")
    bilangan += 1
    
    if bilangan > 40:
        break
    