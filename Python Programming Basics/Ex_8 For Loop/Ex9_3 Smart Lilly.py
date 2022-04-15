"""
Input           Output
10              Yes! 5.00
170.00
6

21              No! 997.98
1570.98
3
"""
n = int(input())
cena_peralnq = float(input())
cena_igrachka = float(input())

chetni = 0
nechetni = 0
pari_chetni = 0
broi_chetni = 0

for i in range(1, n+1):
    if i % 2 == 0:
        broi_chetni += 1
        pari = broi_chetni*10
        pari_chetni += pari
    elif i % 2 != 0:
        nechetni += 1
        
pari_chetni = (pari_chetni) - (broi_chetni)
pari_nechetni = (nechetni*cena_igrachka)

if cena_peralnq > (pari_chetni+pari_nechetni):
    print(f"No! {cena_peralnq-(pari_chetni+pari_nechetni):.2f}")
else:
    print(f"Yes! {(pari_chetni + pari_nechetni)-cena_peralnq:.2f}")