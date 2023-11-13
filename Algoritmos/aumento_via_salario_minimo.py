SalMin = float(input("Digite o salário mínimo: "))
Sal=float(input("Digite seu salário: "))
if Sal<SalMin*3:
    NovoSal=Sal*1.50
else:
    if Sal>=SalMin*3 and Sal<=SalMin*10:
        NovoSal=Sal*1.20
    else:
        NovoSal=Sal*1.15
print ("%.2f" % (NovoSal))
