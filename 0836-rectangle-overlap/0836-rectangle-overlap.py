class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        ax1, ay1, ax2, ay2 = rec1
        bx1, by1, bx2, by2 = rec2
        
        hor_int = [max(ax1, bx1), min(ax2,bx2)]
        ver_int = [max(ay1, by1), min(ay2,by2)]
        
        
        hor_dif, ver_dif = hor_int[1] - hor_int[0], ver_int[1] - ver_int[0]
        
        intersection_area = hor_dif * ver_dif
        
        if hor_dif <= 0 or ver_dif <= 0:
            intersection_area = 0
        
        return intersection_area > 0