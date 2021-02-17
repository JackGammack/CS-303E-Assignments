def main():
    nums= [1,2,3,4]
    A = []
    A.append([])
    for i in range(0,len(nums)):
        for j in range(0,len(A)):
            print(A)
            B = list( A[j] )
            B.append(nums[i])
            A.append( B )
    print(A)

main()
