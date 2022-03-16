p = float(input('panjang : '))
l = float(input('lebar : '))
t = float(input('tinggi : '))
 
def volume(p,l,t):
    V = p * l * t
    return V
 
print('volume:{}'.format(volume(p,l,t)))