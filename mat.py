def p(a,b):
    """

    Permütasyon bulma işlemi için "p(toplam eleman sayısı , seçilecek eleman sayısı)"

    """
    perm = 1
    if a <= 0 or b <= 0 or b > a:
            hata = "Geçersiz Rakam ! Yeniden Deneyiniz ..."
            return hata
    else:
        while b > 0:
            perm*=a
            a-=1
            b-=1
        return perm
def c(a,b):
    """
    Kombinasyon bulma işlemi için "c(toplam eleman sayısı , seçilecek eleman sayısı)"

    """ 
    if b > a or a < 0 or b < 0:
        hata = "Geçersiz Rakam !"
        return hata
    else:
        com = p(a,b) / faktoriyel(b)
        return com
def faktoriyel(a):
    """
    faktoriyel bulma işlemi için "faktoriyel(sayı)"

    """
    if a < 0:
        hata = "Geçersiz Rakam !"
        return hata
    else:
        fac = 1
        i = 1
        while i <= a:
            fac*=i
            i+=1
        return fac
def karekok(a):
    """
    karekök bulma işlemi için "karekök(sayı)"
    """
    c = a ** (1 / 2)
    return c
def dairealan(r,pi):
    """

    Daire Alan Bulma İşlemi İçin " dairealan(yarıçap,pi sayısı)"

    """
    alan = pi * (r ** 2)
    return alan
def cembercevre(r,pi):
    """
    çemberin çevresini bulma işlemi için "cembercevre(yarıçap,pi sayısı)"
    """
    cevre = 2 * pi * r
    return cevre
def dortgenalan(a,b):
    """
    dörtgen Alanını Bulmak İçin "dortgenalan(kenar,kenar)"

    """
    c = a * b
    return c
def ucgenalan(k,h):
    """
    Üçgenin Alanını Bulma İşlemi için "ucgenalan(taban,yükseklik)"
    """
    alan = (k * h) / 2
    return alan
def kokbul(sayi,kok):
    """
    kök bulma işlemi için "kokbul(sayı,kök)"
    """
    kok=sayi**(1/kok)
    return kok
def usbul(sayi,us):
    """
    üs bulma işlemi için "usbul(sayı,üs)"
    """
    ussayi=sayi**us
    return ussayi
def sayacart(sayi,art):
    """
    Artan Sayaç işlemi için "sayacart(sayı,artacak değer)"
    """
    sayi+=art
    return sayi
def sayacazal(sayi,azal):
    """
    Azalan Sayaç İşlemi için "sayacazal(sayı,azalacak değer)"
    """
    sayi-=azal
    return sayi
