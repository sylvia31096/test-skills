def solution(string):
    disappear_string = ''
    old_string = string
    
    # if disappear_string==string:
    #     return string
    # else:
    #     return solution(disappear_string)
    while(disappear_string!=old_string):    
        if 'AA' in string:
            disappear_string = string.replace('AA','')
        if 'BB' in string:
            disappear_string = string.replace('BB','')
        if 'CC' in string:
            disappear_string = string.replace('CC','')
        old_string = string
        string = disappear_string
        
    return string

    

# def remove_pair(string):
#     disappear_string = string
#     if 'AA' in string:
#         disappear_string = string.replace('AA','')
#     if 'BB' in string:
#         disappear_string = string.replace('BB','')
#     if 'CC' in string:
#         disappear_string = string.replace('CC','')
#     return disappear_string
