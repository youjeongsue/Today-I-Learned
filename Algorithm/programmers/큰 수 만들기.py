number="4177252841"
k=4

index=0
print(number, k, index)
while k>0:
    if number[index]<number[index+1]:
        number=number[index+1:]
        k-=1
        index=0
        print(number, k, index)
    elif number[index]>number[index+1]:
        number=number[:index+1]+number[index+2:]
        k-=1
        index=0
        print(number, k, index)
    elif number[index]==number[index+1]:
        index+=1
        print(number, k, index)

print("answer:", number)