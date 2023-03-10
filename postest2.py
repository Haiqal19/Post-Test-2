import math

def lompat_cari(arr, x):
    panjangd = len(arr)
    jump = int(math.sqrt(panjangd))
    dakir = 0
    dakan = 0
    while dakir < panjangd and arr[dakir] <= x:
        dakan = min(panjangd - 1, dakir + jump)
        if arr[dakir] <= x and arr[dakan] >= x:
            break
        dakir += jump

    if dakir >= panjangd or arr[dakir] > x:
        return -1
    
    dakan = min(panjangd - 1, dakan)
    i = dakir
    while i <= dakan and arr[i] <= x:
        if arr[i] == x:
            return i
        i += 1
    return -1

var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]


temuin_arsel = lompat_cari(var, "Arsel")
if temuin_arsel != -1:
    print("Arsel ada di Index", temuin_arsel)
else:
    print("Arsel tidak ditemukan")

temuin_avivah = lompat_cari(var, "Avivah")
if temuin_avivah != -1:
    print("Avivah ada di Index", temuin_avivah)
else:
    print("Avivah tidak ditemukan")

temuin_daiva = lompat_cari(var, "Daiva")
if temuin_daiva != -1:
    print("Daiva ada di Index", temuin_daiva)
else:
    print("Daiva tidak ditemukan")

temuin_wahyu = lompat_cari(var[3], "Wahyu")
if temuin_wahyu != -1:
    print("Wahyu ada di Index 3, kolom ", temuin_wahyu)
else:
    print("Wahyu tidak ditemukan")

temuin_wibi = lompat_cari(var[3], "Wibi")
if temuin_wibi != -1:
    print("Wibi ada Index 3, kolom", temuin_wibi)
else:
    print("Wibi tidak ditemukan")