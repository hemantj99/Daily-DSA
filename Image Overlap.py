'''
You are given two images img1 and img2 both of size n x n, represented as binary, square matrices of the same size. (A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.

(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?
'''
class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        count = 0
        if not A:
            return 0
        n = len(A)
        for v in range(n):
            for h in range(n):
                cover1,cover2 = 0,0
                for i in range(n-v):
                    for j in range(n-h):
                        cover1+=A[i+v][j+h]*B[i][j]
                        cover2+=B[i+v][j+h]*A[i][j]
                count = max(count,cover1,cover2)
        
        return count
