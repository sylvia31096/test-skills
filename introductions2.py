test_cases = int(input())
for i in range(1, test_cases+1):

    m, n, p = list(map(int, input().split()))
    
    
    know_list = []
    for i in range(m+n):
        know_list.append(input().split())
    
    for p_i in range(p):
        a, b = list(map(int, input().split()))
        a = a-1
        b = b-1
        prev = []
        after = [a, b]
        count=0
        can_continue = True
        

        while(can_continue):
           
           prev = after
           after = []

           for i,pr in enumerate(prev):
            if i+1<len(prev):
                if know_list[prev[i+1]][pr]=='Y':
                    can_continue = False           
            for i in range(m):
                if i!=pr and know_list[pr][i]=='Y':
                    if i in after:
                       can_continue = False
                       count +=1
                    after.append(i)
           count +=1
        print(count)
        


           
