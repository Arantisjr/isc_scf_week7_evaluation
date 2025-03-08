salary = int(input("Enter your salary: "))
if salary > 50000 :
    bonus1= salary*(1/10)
    print("Bonus:",bonus1 )
    print("Total salary after bonus:", bonus1+salary)
else:
    bonus2 = salary*(1/20)
    print("Bomus:",bonus2)
    print("Total salary after bonus:", bonus2+salary)

