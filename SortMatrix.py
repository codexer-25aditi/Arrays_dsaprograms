# User function Template for python3

class Solution:
    def sortedMatrix(self, N, Mat):
        # code here
        arr = []
        for i in range(0, N):
            for j in range(0, N):
                arr.append(Mat[i][j])

        arr = sorted(arr)
        Matrix = []
        I = 0
        for a in range(0, N):
            arr1 = []
            for b in range(0, N):
                arr1.append(arr[I])
                I = I + 1
            Matrix.append(arr1)
        return Matrix





