#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random, hashlib, gzip, bz2
random.seed(42)

base = './sheep'

# dico et chaines
f = open('mondico','r')
dico = [m.strip() for m in f.readlines()]
f.close()
random.shuffle(dico)
chaine1 = dico[:143]
fakechaine1 = dico[-300:]

# depart
c = open('icone','r')
meu = [m[:-1] for m in c.readlines()]
c.close()
L = max(map(len,meu))
f = open('%s/sheep'%(base),'w')
for j in range(L):
    for i in range(len(meu)):
        if j>=len(meu[i]):
            f.write(' \n')
        else:
            f.write(meu[i][j]+'\n')
f.close()

quit()

# chaine1
pred = 'cow'
for m in chaine1:
    f = open('%s/%s'%(base,pred),'w')
    f.write('-->%s\n'%m)
    f.close()
    pred = m
f = open('%s/stop'%(base),'w')
f.write('too far!\n')
f.close()
print pred
f = open('%s/%s'%(base,pred),'w')
f.write('-->stop\n')
brouill = '&~#{(|_@$*%!/:;,?*+'
cache = 'Go to snake112!'
t0 = [[random.choice(brouill) for j in range(80)] for i in range(80)]
indcache = random.sample(range(80),len(cache))
indcache.sort()
print indcache
for i in range(len(cache)):
    t0[indcache[i]][random.randint(10,70)] = cache[i]
t1 = [''.join(l) for l in t0]
t2 = '\n'.join(t1)
f.write(t2)
f.close()

for m in fakechaine1:
    f = open('%s/%s'%(base,m),'w')
    f.write('-->%s\n'%(random.choice(fakechaine1)))
    f.close()

def tobin(n):
    l = []
    while n>0:
        l.append(str(n%2))
        n /= 2
    return ''.join(l)[::-1]

print tobin(110)

random.seed(43)
# chaine2
ind = range(500)
random.shuffle(ind)
chaine2 = ind[:100]
reste = ind[100:]
print chaine2[0], chaine2[99]
for i in range(len(chaine2)-1):
    f = open('%s/snake%d'%(base,chaine2[i]),'w')
    r = random.randint(0,2)
    if i==0 or r==0:
        f.write('-->snake%d\n'%(chaine2[i+1]))
    elif r==1:
        f.write('-->snake%d\nIt\'s a trap!\n-->snake%d\n'%(random.choice(reste),chaine2[i+1]))
    else:
        f.write('-->snake<%s>\n'%(tobin(chaine2[i+1])))
    f.close()
for i in range(len(reste)):
    f = open('%s/snake%d'%(base,reste[i]),'w')
    r = random.randint(0,3)
    if r==0:
        f.write('-->snake%d\n'%(random.choice(reste)))
    elif r==1:
        f.write('-->snake%d\nIt\'s a trap!\n-->snake%d\n'%(random.choice(reste),random.choice(reste)))
    elif r==2:
        f.write('-->snake<%s>\n'%(tobin(random.choice(reste))))
    else:
        f.write(hashlib.sha1(str(random.random())).hexdigest()+'\n')
    f.close()

f = open('%s/snake%d'%(base,chaine2[99]),'w')
f.write('474442b06c2c2d75c7eda1bde7c4a324e1bda72f\n')
f.close()

for m in dico[300:320]:
    f = open('%s/%s'%(base,m),'w')
    f.write(str(random.random()))
    f.close()
    for i in range(30):
        f0 = open('%s/%s'%(base,m),'r')
        data = f0.read()
        f0.close()
        r = random.randint(0,1)
        if r==0:
            f = gzip.open('%s/%s'%(base,m),'wb')
            f.write(data)
            f.close()
        else:
            f = open('%s/%s'%(base,m),'wb')
            f.write(bz2.compress(data))
            f.close()
