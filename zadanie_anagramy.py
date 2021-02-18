# -*- coding: utf-8 -*-


def are_anagrams(s1, s2, s3):
    s1, s2, s3 = sorted(list(s1)), sorted(list(s2)), sorted(list(s3))
    if s1 == s2 == s3:
        return True
    else:
        return False
        
   
s1 = 'ranty'    
s2 = 'tyran' 
s3 = 'narty'  
print(are_anagrams(s1, s2, s3))

