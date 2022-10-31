n = []
q = []

while True:
    a = input('enter fruit name and quanitity: ').lower()
    if a == 'end':break
    else:
        a = a.split(' ')
        n.append(a[0])
        q.append(a[1])
        
        for k in range(0,len(n)-1):
            if n[k] == a[0]:
                n.pop()
                q[k] = str(int(q[k]) + int(a[1]))
                q.pop()

maxi = len(n[0])
for i in n:
    if maxi <  len(i):
        maxi = len(i)
if maxi < len('fruits'):
    maxi = len('fruits')
maxi_1 = len('count')
print('+'+maxi*'-'+'+'+maxi_1*'-'+'+')
print('|'+(maxi-len('fruits'))*' '+"fruits"+'|'+"count"+'|')
print('+'+maxi*'-'+'+'+maxi_1*'-'+'+')
for j in range(0,len(n)):
    print('|'+(maxi-len(n[j]))*' '+n[j]+'|'+(maxi_1-len(q[j]))*' '+q[j]+'|')
print('+'+maxi*'-'+'+'+maxi_1*'-'+'+')


                
                
            
