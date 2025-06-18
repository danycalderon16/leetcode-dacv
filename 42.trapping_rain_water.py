def trapping_rain_water(height):
    l_wall = 0
    r_wall = 0
    n = len(height)
    max_left  = [0] * n
    max_right = [0] * n
    
    for i in range(n):
        j = -i - 1
        max_left[i] = l_wall
        max_right[j] = r_wall
        
        l_wall = max(l_wall,height[i])
        r_wall = max(r_wall,height[j])
        
        
    summ = 0
    
    for i in range(n):
        pot = min(max_left[i],max_right[i])
        summ += max(0, pot - height[i])
      
    return summ
    
if "__main__" == __name__:
    res = trapping_rain_water(height=[4,2,0,3,2,5])
    print(res)