cardnumber = input("enter number of Card")
cardcolor = input("enter color of card")
pofA = 4/52
pofB = 26/52
print("p(A) => probability of drawing card with number ",cardnumber,"=",round(pofA,2))
print("p(B)=> probability of drawing card with color ",cardcolor,"=",round(pofB,2))
print("joint probability of A and B = p(A)*p(B)")
pAandB = round(pofA * pofB,2)
print("P(A and B) =",pAandB)
print("there are ",pAandB * 100,"% chances of getting ",cardcolor,"card with number",cardnumber)
