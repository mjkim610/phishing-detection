import sys
from integrate import integrate

l = []

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file = sys.argv[1]

with open(file) as f:
    content = f.readlines()

content = [x.strip() for x in content]

for url in content:
    print url
    r = integrate(url)
    print r
    if r == 'U':
        l.append(url)

print "====== Unknown list ======"
print '\n'.join(l)
