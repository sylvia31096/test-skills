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
        visited_list = []
        introduction_times = []
        introduction_time = 0
        j=0
        k=0 
        a_start = a
        b_start = b
        while(k<m):
            
            
            #if [a,b] not in visited_list and [b,a] not in visited_list and a!=b:
            #visited_list.append([a,b])
            if a!=j and a!=b:
                if know_list[a][b] != 'Y' and j<m:

                    if know_list[a][j] == 'Y':
                        print("Yes",a,j)
                        introduction_time += 1
                        
                        
                        if know_list[b][j] == 'N':
                            j = 0
                        a = b
              
                else:
                    if know_list[a][b] == 'Y':
                        print(a, b, "introduced")
                        introduction_times.append(introduction_time)
                    k+=1
                    j=k                    
                    a=a_start
                    b=b_start
                    introduction_time = 0
            b = j   
            print(a,b)
                        
            j+=1
        print(introduction_times)
        

# def get_intro(a, b, m):
#     if know_list[a][b] == 'Y':
#         return 1
#     else:
#         for j in range(m):
#             if a!=j or b!=j:
#                 if know_list[a][j] == 'Y' :
#                     if (a<=m):
#                         m = a
#                     return 1 + get_intro(b, j, m)
#                 elif know_list[b][j] == 'Y':
#                     if (b<=m):
#                         m = b 
#                     return 1 + get_intro(a, j, m)
