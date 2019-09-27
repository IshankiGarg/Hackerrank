if __name__ == '__main__':
    n = int(input())
    arr=list(map(int, input().split())) 
    '''
    for i in range (n):
        num=int(input())
        arr.append(num)
    '''
    #print(arr)
    arr.sort(reverse=True)
    #print(arr)
    for i in range (n):
        if(arr[i]!=arr[i+1]):
            print(arr[i+1])
            break
        elif(arr[i]==arr[i-1]):
            continue