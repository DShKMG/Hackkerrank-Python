def kangaroo(x1, v1, x2, v2):
    if (x1 < x2 and v1 <= v2): 
        return "NO"
    if (x1 > x2 and v1 >= v2): 
        return "NO"
    if (x1 < x2): 
  
        x1, x2 = x2,x1; 
        v1, v2 = v2,v1; 
    while (x1 >= x2):  
      
        if (x1 == x2):  
            return "YES"; 
        x1 = x1 + v1;  
        x2 = x2 + v2;  
    return "NO"

