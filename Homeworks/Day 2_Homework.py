#Question 1
#The program that swaps the second half of the list and the first half of the list

A = [1,2,3,4,5,6,7,8]
B = A[:len(A)//2]
C = A[len(A)//2:]

reverseA = C + B
print(reverseA)
