import string
k=0
u=0

A = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
B = []
C = []
D = []
E = []
F = []

print "Durudurudud"
print A[0]

chave = raw_input('Digite a chave: ')
mensagem = raw_input('Digite sua mensagem: ')

a = chave.lower()
b = mensagem.lower()

if a.isalpha() and b.isalpha():

    for i in a:
        
        C.append(i)

    for i in b:

        B.append(i)

    while k<len(C):

        while u<len(A):

            if C[k] == A[u]:
                x = u
                #print 'sim'
           # else:
               # print 'no'

            u+=1

        u=0
        D.append(x)
        print x
        #print A[x]
        k+=1

    k=0
    print 'fim chave'

    while k<len(B):

        while u<len(A):

            if B[k] == A[u]:
                y = u
                #print 'sim'
           # else:
               # print 'no'

            u+=1

        u=0
        E.append(y)
        print y
        #print A[y]
        k+=1

    k =0
    print 'fim mensagem'

    if len(D) < len(E):# se o tamanho da chave for menor que o da mensagem

        q = len(E) - len(D)

        while k < q:
            D.append(D[k])
            k+=1

    k=0

    while k<len(D) or k<len(E):

        x = D[k]
        y = E[k]
        z=x+y
        z = z%26
        print A[z]

        k+=1
