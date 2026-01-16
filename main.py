from fractions import Fraction as frac

inf=float("inf")
nan=inf-inf
def f2_2(a1,b1,c1,a2,b2,c2):
    a=[a1,b1,c1]
    b=[a2,b2,c2]
    a=list(map(lambda x:x*a2,a))
    b=list(map(lambda x:x*a1,b))
    b=[b[i]-a[i] for i in range(3)]
    a1,b1,c1=a
    a2,b2,c2=b
    a=list(map(lambda x:x*b2,a))
    b=list(map(lambda x:x*b1,b))
    a=[a[i]-b[i] for i in range(3)]
    a1,b1,c1=a
    a2,b2,c2=b
    if a1==0 or b2==0:
        if c1==0 and c2==0:
            return (inf,inf)
        else:
            return (nan,nan)
    else:
        return (frac(c1,a1),frac(c2,b2))


def f2(a1,b1,c1,a2,b2,c2):
    a1,b1,c1,a2,b2,c2=map(frac,[a1,b1,c1,a2,b2,c2])
    l=[[a1,b1,c1],[a2,b2,c2]]
    for i in range(1):
        for j in range(i+1,2):
            xx=frac(l[i][i],l[j][i])
            l[j]=[l[j][e]*xx-l[i][e] for e in range(3)]
    for i in range(1,0,-1):
        for j in range(0,i):
            xx=frac(l[i][i],l[j][i])
            l[j]=[l[j][e]*xx-l[i][e] for e in range(3)]
    a11,b11,c11=l[0]
    a22,b22,c22=l[1]
    if a11==0 or b22==0:
        if c11==0 and c22==0:
            return (inf,inf)
        else:
            return (nan,nan)
    else:
        return (frac(c11,a11),frac(c22,b22))


def f3(a1,b1,c1,d1,a2,b2,c2,d2,a3,b3,c3,d3):
    a1,b1,c1,d1,a2,b2,c2,d2,a3,b3,c3,d3=map(frac,[a1,b1,c1,d1,a2,b2,c2,d2,a3,b3,c3,d3])
    l=[[a1,b1,c1,d1],[a2,b2,c2,d2],[a3,b3,c3,d3]]
    for i in range(2):
        for j in range(i+1,3):
            xx=frac(l[i][i],l[j][i])
            l[j]=[l[j][e]*xx-l[i][e] for e in range(4)]
    for i in range(2,0,-1):
        for j in range(0,i):
            xx=frac(l[i][i],l[j][i])
            l[j]=[l[j][e]*xx-l[i][e] for e in range(4)]
    a11,b11,c11,d11=l[0]
    a22,b22,c22,d22=l[1]
    a33,b33,c33,d33=l[2]
    if a11==0 or b22==0 or c33==0:
        if d11==0 and d22==0 and d33==0:
            return (inf,inf,inf)
        else:
            return (nan,nan,nan)
    else:
        return (frac(d11,a11),frac(d22,b22),frac(d33,c33))

ty=int(input("unknowns >> "))
if ty==2:
    print("A1x+B1y=C1\nA2x+B2y=C2")
    a1,b1,c1=map(int,input("A1 B1 C1 >>> ").split())
    a2,b2,c2=map(int,input("A2 B2 C2 >>> ").split())
    x,y=f2(a1,b1,c1,a2,b2,c2)
    if x==inf and y==inf:
        print("Countless solutions")
    elif x==nan and y==nan:
        print("No solutions")
    else:
        print(f"x={x}  y={y}")
elif ty==3:
    print("A1x+B1y+C1z=D1\nA2x+B2y+C2z=D2\nA3x+B3y+C3z=D3")
    a1,b1,c1,d1=map(int,input("A1 B1 C1 D1 >>> ").split())
    a2,b2,c2,d2=map(int,input("A2 B2 C2 D2 >>> ").split())
    a3,b3,c3,d3=map(int,input("A3 B3 C3 D3 >>> ").split())
    x,y,z=f3(a1,b1,c1,d1,a2,b2,c2,d2,a3,b3,c3,d3)
    if x==inf and y==inf and z==inf:
        print("Countless solutions")
    elif x==nan and y==nan and z==nan:
        print("No solutions")
    else:
        print(f"x={x}  y={y}  z={z}")