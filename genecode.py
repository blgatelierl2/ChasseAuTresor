#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Image, random, bz2, gzip
random.seed(42)

f = open('qr','w')
f.write('Almost there!\nOne last hint: 21x21\n')
l = []
img = Image.open('qrcode.png')
pix = img.load()
for i in range(21):
    for j in range(21):
        if pix[i*8,j*8]==(0,0,0,255):
            l.append('%d,%d'%(i,j))
#img.save('toto.png')
random.shuffle(l)
f.write('\n'.join(l))
f.close()

random.seed(45)
# chameleon
f = open('qr','r')
indic = f.read()
f.close()
f = open('chameleon','w')
f.write(indic)
f.close()
for i in range(30):
    f0 = open('chameleon','r')
    data = f0.read()
    f0.close()
    r = random.randint(0,1)
    if r==0:
        f = gzip.open('chameleon','wb')
        f.write(data)
        f.close()
    else:
        f = open('chameleon','wb')
        f.write(bz2.compress(data))
        f.close()
