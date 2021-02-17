def rot(input,target):
    infile = open(input,'r')
    ctr=0
    for line in infile:
        ctr+=line.count(target)
    return ctr

        

def main():
    print(rot('isbn.txt','abc'))
main()
