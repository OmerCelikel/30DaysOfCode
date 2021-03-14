import sys

if __name__ == '__main__':
    n = int(input())
    if n <2 and n > 20:
        sys.exit()
        
    for i in range(1,11):
        multip = n * i
        print(n,"x",i,"=",multip)