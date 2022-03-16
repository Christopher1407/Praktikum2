print('Program menghitung luas, volume, dan keliling balok')
p = float(input('masukan panjang balok: '))
l = float(input('masukan lebar balok: '))
t = float(input('masukan tinggi balok: '))
 
def volume(p,l,t):
    V = p * l * t
    return V
 
print('volume:{}'.format(volume(p,l,t)))