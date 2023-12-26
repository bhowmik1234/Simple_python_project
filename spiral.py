
def spiralform(matrix):  
    k = 0  
    m = len(matrix)  
    l = 0  
    n = len(matrix[0])  
  
    while (k < m and l < n):   
        for i in range(l, n):  
            print(matrix[k][i], end = " ")  
        k = k + 1  
     
        for i in range(k, m):  
            print(matrix[i][n - 1], end = " ")  
    
        n = n - 1  
        if (k < m):  
            for i in range(n - 1, (l - 1), -1):  
                print(matrix[m - 1][i], end = " ")  
            m = m - 1  

        if (l < n):  
            for i in range(m - 1, k - 1, -1):  
                print(matrix[i][l], end = " ")  
    
            l = l + 1  
    
matrix = [[1, 2, 3, 4],  
          [5, 6, 7, 8],  
          [9, 10, 11, 12],  
          [13, 14, 15, 16]]  
  
spiralform(matrix)  