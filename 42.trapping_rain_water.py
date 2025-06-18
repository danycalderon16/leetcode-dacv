def trapping_rain_water(height):
    left = 0
    total = 0
    
    while left < len(height):
        for right in range(left+1, len(height)):
            if height[left] <= height[right]:
                for i in range(left + 1, right):
                    total += height[left] - height[i]
                
                left = right
                break
        else:
            if left + 1 < len(height):
                max_right = left + 1
                for k in range(left + 1, len(height)):
                    if height[k] > height[max_right]:
                        max_right = k
                
                for i in range(left + 1, max_right):
                    total += height[max_right] - height[i]
                
                left = max_right
            else:
                break
            
    return total

if "__main__" == __name__:
    res = trapping_rain_water(height=[4,2,0,3,2,5])
    print(res)