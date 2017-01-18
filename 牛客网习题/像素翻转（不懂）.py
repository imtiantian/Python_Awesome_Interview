# -*- coding:utf-8 -*-
class Transform:
    def transformImage(self, mat, n):
        for layer in range(0, n / 2):
            first = layer
            last = n - 1 - first
            for i in range(first, last):
                mapd = n - 1 -i
                top = mat[first][i]
                mat[first][i] = mat[mapd][first]
                mat[mapd][first] = mat[last][mapd]
                mat[last][mapd] = mat[i][last]
                mat[i][last] = top
        return mat