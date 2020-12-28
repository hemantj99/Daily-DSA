test=si()
for _ in range(test):
    n=si()
    string1=st()
    attendance=90
    count=120-n
    for i in string1:
        if i=='1':
            count+=1
    if count>=90:
        print("YES")
    else:
        print("NO")
    
