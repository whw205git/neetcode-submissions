class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        size = m * n

        l, r = 0, size - 1
        while l <= r:
            mid = l + (r - l) // 2
            x, y = mid // n, mid % n
            print(f"x {x} y {y}")
            if target < matrix[x][y]:
                r = mid - 1
            elif target > matrix[x][y]:
                l = mid + 1
            else:
                return True
        return False

        

        