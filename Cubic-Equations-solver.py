xs = [x*0.01 for x in range(2*-100000, 2*100000+1)]

print("This app solve equations like : ")
print("Ax^3 + Bx^2 + Cx + D = E")
print("")

A = float(input("Enter A : "))
B = float(input("Enter B : "))
C = float(input("Enter C : "))
D = float(input("Enter D : "))
E = float(input("Enter E : "))

for l in xs :
    if ((A*l ** 3) + (B*l**2) + (C * l) + (D) == E) :
        print("x = " + str(l))
        break
    else :
        continue

input()