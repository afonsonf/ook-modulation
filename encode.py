from binascii import hexlify

file = open('input_text.txt')
lines = [l for l in file]
s = ''.join(lines)
print 'encoding: \n', s, '\n'

sb = bin(int(hexlify(s), 16))[2:]
file = open('input_bin.txt','w')
file.write(sb)
file.close()
print 'output: \n', sb, '\n'
