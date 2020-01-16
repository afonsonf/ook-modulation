from binascii import unhexlify

file = open('out')
lines = [l.strip() for l in file]

n = int(lines[0].encode('ascii'),2)
print unhexlify( '%x' % n )
