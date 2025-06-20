class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        area=0
        n=len(points)
        for i in range(n):
            x1,y1=points[i]
            for j in range(i+1,n):
                x2,y2=points[j]
                for k in range(j+1,n):
                    x3,y3=points[k]
                    currentarea=abs(0.5*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))
                    area=max(area,currentarea)
        return area
    
from typing import List


#the time complexity of this solution is O(n^3) where n is the number of points.
#the space complexity is O(1) since we are using a constant amount of space for the area variable.#this solution is not optimal for large inputs, but it works for small inputs.
#we can optimize this solution using the shoelace formula or by using a convex hull algorithm to reduce the number of points we need to consider.#however, this solution is simple and easy to understand.
#the largest triangle area can be found by iterating through all combinations of three points and calculating the area using the formula:
#area = 0.5 * |x1(y2-y3) + x2(y3-y1) + x3(y1-y2)|
#where (x1, y1), (x2, y2), and (x3, y3) are the coordinates of the three points.#this formula is derived from the determinant of a matrix that represents the triangle formed by the three points
#the absolute value is used to ensure the area is non-negative, and we multiply by 0.5 to get the actual area of the triangle.
#this solution is straightforward and works well for small inputs, but it can be improved for larger inputs by using more efficient algorithms.
#the solution iterates through all combinations of three points, calculates the area for each combination,