from binascii import unhexlify

file = open('out_bin.txt')
lines = [l.strip() for l in file]
print 'decoding: \n', lines[0], '\n'

n = int(lines[0].encode('ascii'),2)
print 'output: \n', unhexlify( '%x' % n ), '\n'
