class matriks:
    def __init__(self, data):
        self.data = data

#penjumlahan 
    def m0(self):
        try:
            mat1 = self.data['mat1']
            mat2 = self.data['mat2']
            hasil = []
            for x in range(0, len(mat1)):
                for y in range(0, len(mat1[0])):
                    hasil.append(mat1[x][y] + mat2[x][y], end=' ')
            return hasil
        except:
            return 'data input salah'



    def mat1(self):
        try:
            mat1 = self.data['mat1']
            mat2 = self.data['mat2']
            hasil = []
            for x in range(0, len(mat1)):
                for y in range(0, len(mat1[0])):
                    hasil.append(mat1[x][y] + mat2[x][y], end=' ')
            return hasil
        except:
            return 'data input salah'


    def mat2(self):
        try:
            mat1 = self.data['mat1']
            mat2 = self.data['mat2']
            hasil = []
            for x in range(0, len(mat1)):
                row = []
                for y in range(0, len(mat1[0])):
                    total = 0
                    for z in range(0, len(mat1)):
                        total = total + (mat1[x][z] * mat2[z][y])
                    row.append(total)
                hasil.append(row)
            for x in range(0, len(hasil)):
                for y in range(0, len(hasil[0])):
                    print (hasil[x][y], end=' ')
            return hasil
        except:
            return 'data input salah'



    def m3(self):
        try:
            mat1 = self.data['mat1']
            mat2 = self.data['mat2']
            m3 = self.data['m3']
            hasil = (mat1[0]*mat2[1]*m3[2] + mat1[1]*mat2[2]*m3[0] + mat1[2]*mat2[0]*m3[1] - m3[0]*mat2[1]*mat1[2] - m3[1]*mat2[2]*mat1[0] - m3[2]*mat2[0]*mat1[1])
            return hasil
        except:
            return 'data input salah'


#transpose 
    def m4(self):
        try:
            mat1 = self.data['mat1']
            hasil = []
            for i in range(len(mat1)):
                for j in range(len(mat1)):
                    hasil.append(mat1[j][i])
            return hasil
        except:
            return 'data input salah'



matriks = matriks({'mat1': [ [1,3,6,4,7], 
                             [3,2,4,8,1]
                             ]
                        }
                    )
print(str(matriks.m4()))