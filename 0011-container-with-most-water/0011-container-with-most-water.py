class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area=0
        i,j=0,len(height)-1
        while i<j:
            x_value = j-i
            y_value = min(height[i],height[j])
            a = x_value*y_value
            max_area=max(max_area,a) 
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max_area