from fractions import Fraction as frac

def simp(poly): #化简多项式
    ans=[]
    for i in poly:
        # print(i)
        if i[1]==0:
            continue
        bb=[]
        for j in i[0]:
            if j[1]!=0:
                bb.append(j)
        bb=sorted(bb)
        # if bb==[]:
        #     continue
        # print('  ',bb)
        for j in range(len(ans)):
            if ans[j][0]==bb:
                ans[j][1]+=i[1]
                break
        else:
            ans.append([bb,i[1]])
    ans=sorted(ans)
    # print(ans)
    return ans

def printpoly(poly): #输出多项式
    fi=1
    sp=simp(poly)
    for i in sp:
        if i[1]==1 and not fi and i[0]!=[]:
            print('+',end='')
        elif i[1]==-1 and i[0]!=[]:
            print('-',end='')
        elif i[1]>=0 and i[1]!=1 and not fi:
            print(f'+{i[1]}',end='')
        elif i[1]>=0 and i[1]!=1 and fi:
            print(f'{i[1]}',end='')
        elif not fi:
            print(i[1],end='')
        for j in i[0]:
            if j[1]==1:
                print(f'{j[0]}',end='')
            else:
                print(f'{j[0]}^{j[1]}',end='')
        fi=0
    print()

def polyadd(poly1,poly2): #多项式相加
    ans=poly1+poly2
    ans=simp(ans)
    return ans

def polyneg(poly): #多项式取反
    ans=[[i[0],-i[1]] for i in poly]
    ans=simp(ans)
    return ans

def polymin(poly1,poly2): #多项式相减
    ans=poly1+polyneg(poly2)
    ans=simp(ans)
    return ans

def monomul(mono1,mono2): #单项式相乘
    ans=[[[j for j in i] for i in mono1[0]],mono1[1]*mono2[1]]
    for i in mono2[0]:
        for j in range(len(ans[0])):
            if i[0]==ans[0][j][0]:
                ans[0][j][1]+=i[1]
                break
        else:
            ans[0].append(i)
    return ans

def polymul(poly1,poly2): #多项式相乘
    # ans=[monomul(i,j) for i in poly1 for j in poly2]
    ans=[]
    for i in poly1:
        for j in poly2:
            ccc=monomul(i,j)
            # print(i,'  ',j,'  ',ccc)
            ans.append(ccc)
    ans=simp(ans)
    return ans

def monodiv(mono1,mono2): #单项式相除
    ans=[[[j for j in i] for i in mono1[0]],frac(mono1[1],mono2[1])]
    for i in mono2[0]:
        for j in range(len(ans[0])):
            if i[0]==ans[0][j][0] and i[1]<=ans[0][j][1]:
                ans[0][j][1]-=i[1]
                break
        else:
            return "ERROR"
    return ans

def polydiv(poly1,mono1): #多项式除以单项式
    # ans=[monomul(i,j) for i in poly1 for j in poly2]
    ans=[]
    for i in poly1:
        ccc=monodiv(i,mono1)
        if ccc=="ERROR":
            return "ERROR"
        ans.append(ccc)
    ans=simp(ans)
    return ans

def rfi(s,p): #Read First Int in str s from pos p , ret [end pos of the int,the int]
    f=0
    n=0
    p2=0
    if p>=len(s):
        return [p,0]
    if s[p]=='+':
        f=1
        p+=1
    elif s[p]=='-':
        f=-1
        p+=1
    else:
        if s[p] in '0123456789':
            f=1
        else:
            return [p,0]
    p2=p
    for i in range(p,len(s)):
        if s[i] in '0123456789':
            n=n*10+int(s[i])
            p2=i+1
        else:
            break
    return [p2,n*f]

def parsemono(s): #解析单项式
    if s=='':
        # print("WTF?")
        return [[],0]
    p,c=rfi(s,0)
    ns=s[0:p]
    # print(p,c,ns)
    if ns=='':
        c=1
        p=0
    elif ns=='+':
        c=1
        p=1
    elif ns=='-':
        c=-1
        p=1
    ans=[[],c]
    # p-=1
    while p<len(s):
        nc=s[p]
        np=0
        if p+1<len(s) and s[p+1]=='^':
            p,np=rfi(s,p+2)
        else:
            np=1
            p=p+1
        ans[0].append([nc,np])
    return ans

def parsepoly(s): #解析多项式
    # if s[0]=='+':
    #     s.pop(0)
    s=s.split('+')
    # print(s)
    s=[i.split('-') for i in s]
    # print(s)
    s2=[]
    for i in s:
        s2.append(i[0])
        for j in range(1,len(i)):
            s2.append('-'+i[j])
    # print(s2)
    s2=[parsemono(i) for i in s2]
    # print(s2)
    return simp(s2)

def ev(poly,evdict): #多项式求值
    ans=0
    for i in poly:
        ans1=i[1]
        for j in i[0]:
            ans1*=(evdict[j[0]]**j[1])
        ans+=ans1
    return ans



# 本程序在处理所有多项式时都会化简
# 请您在处理多项式前化简

# ev  : dict[str:int]
# mono: list[list[list[str,int]],int]
# poly: list[list[list[list[str,int]],int]]  /  list[mono]

# a=[ [[['x',1]],8] , [[],5] ]                          # 8x+5
# b=[ [[['y',1]],3] , [[['x',1]],6] , [[],11] ]         # 3y+6x+11
# c=[ [[['x',3],['y',2],['z',1]],3] , [[['x',1]],1] ]   # 3x^3y^2z+x
# monoa=[[['x',1]],8]                                   # 8x
# monob=[[['y',1]],3]                                   # 3y
# monoc=[[['x',3],['y',2],['z',1]],3]                   # 3x^3y^2z
# aa=[[[['x',1]],2],[[['y',1]],-4]]                     # 2x-4y
# bb=[[[['x',1]],1],[[['y',1]],3]]                      # x+3y
# cc=[[[['x',1]],5],[[['y',1]],-2]]                     # 5x-2y
# n3=[[[],3]]                                           # 3
# nn2=[[[],-2]]                                         # -2

