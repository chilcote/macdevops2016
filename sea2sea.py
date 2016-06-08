#!/usr/bin/python

import json, os

pathname = os.path.join(os.path.dirname(__file__), 'hosers')
d = {}

name = raw_input('Enter your first and last name: ')
d['home'] = raw_input('Enter a noun: ')
d['native'] = raw_input('Enter an adjective: ')
d['hearts'] = raw_input('Enter a plural noun: ')
d['rise'] = raw_input('Enter a verb: ')
d['strong'] = raw_input('Enter an adjective: ')
d['far'] = raw_input('Enter a plural noun: ')
d['wide'] = raw_input('Enter a plural noun: ')
d['stand1'] = raw_input('Enter a verb: ')
d['land'] = raw_input('Enter a noun: ')
d['free'] = raw_input('Enter an adjective: ')
d['stand2'] = raw_input('Enter a verb: ')
d['stand3'] = raw_input('Enter a verb: ')

with open(os.path.join(pathname, name + '.json'), 'w') as f:
    json.dump(d, f, indent=4, separators=(',', ': '))

print 'Thanks!'
