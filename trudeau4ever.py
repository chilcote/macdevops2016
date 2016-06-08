#!/usr/bin/python

import argparse, json, os, random, subprocess

strange_brew = True
poutine = {}
mckenzies = []
hosers = os.path.join(os.path.dirname(__file__), 'hosers')
toque = 'canada-national-anthem-mp3-free-download.mp3'
serviette = ['/usr/bin/afplay', os.path.join(os.path.dirname(__file__), toque)]

pints = [
        'I have a fleshy-headed mutant in sector 16B.',
        'The power of the force has stopped you, you hosers.',
        'Hey we found a dead mouse in our beer eh. That means you owe us a free case.',
        'Don\'t make me steamroll you.',
        'If I didn\'t have puke breath, I\'d kiss you.',
        'Hosehead, once you get there you can have all the free beer and sausages you want.',
        'I gotta take a leak so bad I can taste it!',
        'No point in steering now.',
        'Gimmie a toasted back bacon, hold the toast.',
        'Lawyers are for sucks.'
    ]

mckenzies.extend(pints)

maple_syrup = subprocess.Popen(serviette)

subprocess.call('clear')

for hoser in os.listdir(hosers):
    if 'DS_Store' in hoser:
        continue
    with open(os.path.join(hosers, hoser), 'r') as f:
        poutine = json.load(f)

    canuck = hoser.split('.')[0].title()
    print '\n' + canuck + ' sings the Canadian National Anthem!\n'

    print '''O Canada!
Our %s and %s land!
True patriot love in all thy sons command.
With glowing %s we see thee %s,
The True North %s and free!
From %s and %s,
O Canada, we %s on guard for thee.
God keep our %s glorious and %s!
O Canada, we %s on guard for thee.
O Canada, we %s on guard for thee.
''' % (poutine['home'].upper(),
       poutine['native'].upper(),
       poutine['hearts'].upper(),
       poutine['rise'].upper(),
       poutine['strong'].upper(),
       poutine['far'].upper(),
       poutine['wide'].upper(),
       poutine['stand1'].upper(),
       poutine['land'].upper(),
       poutine['free'].upper(),
       poutine['stand2'].upper(),
       poutine['stand3'].upper()
       )

    print '---------\n'
    if not mckenzies:
        mckenzies.extend(pints)
    if strange_brew or not mckenzies:
        take_off = raw_input('Press RETURN to continue, eh (type Q to take off, you hoser):').upper()
    else:
        elsinore = random.choice(mckenzies)
        take_off = raw_input(elsinore).upper()
        mckenzies.pop(mckenzies.index(elsinore))
    strange_brew = False
    subprocess.call('clear')
    if take_off == 'Q':
        maple_syrup.kill()
        exit(0)

#print 'God Save the Queen'
print '   ______          __   _____                     __  __            ____                       '
print '  / ____/___  ____/ /  / ___/____ __   _____     / /_/ /_  ___     / __ \__  _____  ___  ____  '
print ' / / __/ __ \/ __  /   \__ \/ __ `/ | / / _ \   / __/ __ \/ _ \   / / / / / / / _ \/ _ \/ __ \ '
print '/ /_/ / /_/ / /_/ /   ___/ / /_/ /| |/ /  __/  / /_/ / / /  __/  / /_/ / /_/ /  __/  __/ / / / '
print '\____/\____/\__,_/   /____/\__,_/ |___/\___/   \__/_/ /_/\___/   \___\_\__,_/\___/\___/_/ /_/  '

print '\n' * 10

raw_input('We hope you enjoyed the beer, oh, like I mean the script, eh.'.upper())
maple_syrup.kill()
print 'Fifty-Four Forty or Fight!'
