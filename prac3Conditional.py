pofB = float(input("Enter number of C programmers in percentage"))
pofAandB = float(input("Enter number of C and Java programmers in percentage"))
pofB =pofB/100
pofAandB = pofAandB/100
print("Event A that student is Java programmer=?")
print("event B that student is C programmer =",pofB)
print("event A and B that is student knowing both C and Java is =", pofAandB)
print("Lets Calulate P(A|B)=P(A and B)/p(B)")
pAgivenB=pofAandB/pofB
print("P(A|B)=",pAgivenB)
print("there are ",pAgivenB*100,"%chance that the student known C and java")


