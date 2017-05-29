import sys
from integrate import integrate

if __name__ == '__main__':
    if len(sys.argv) > 1:
        url = sys.argv[1]

print(integrate(url))
