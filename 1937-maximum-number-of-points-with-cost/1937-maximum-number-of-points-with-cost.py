class Solution:
    def maxPoints(self, points):
        rows = len(points)
        cols = len(points[0])
        def find(r):
            if r == 0:
                return points[0][:]
            prev = find(r - 1)
            left = [0] * cols
            left[0] = prev[0]
            for c in range(1, cols):
                left[c] = max(left[c - 1] - 1, prev[c])
            right = [0] * cols
            right[-1] = prev[-1]
            for c in range(cols - 2, -1, -1):
                right[c] = max(right[c + 1] - 1, prev[c])
            curr = [0] * cols
            for c in range(cols):
                curr[c] = points[r][c] + max(left[c], right[c])
            return curr
        return max(find(rows - 1))