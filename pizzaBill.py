print("Welcome to pizza deliveries")
size=input("what size of pizza do you want? S,M,L?")
if size=="S":
    bill=15
elif size=="M":
    bill=20
else:
    bill=25
pep=input("do you want pepparoni? Y/N?")
if pep=="Y":
    if size=="S":
        bill+=2
    else:
        bill+=3
cheese=input("do you want extra cheeze? Y/N?")
if cheese=="Y":
    bill+=1
print(f"total bill: {bill}")
# S=15
# M=20
# L=25
# pepS=2
# pepML=3
# extracheese=1
