def nested(li, level):
    
    if isinstance(li, list):
        for each in li:
            
            nested(each, level + 1)
    else: print "{0}{1}".format(("\t")*(level-1), li) 
lis2= 2
lis = [1,2,[1,2,[1,2,[1,2,[1,2,[1,2,[1,2]]]]]],3,[4,5,6,[7,8,9]]]
nested(lis, 0)