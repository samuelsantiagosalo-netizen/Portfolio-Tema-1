"""EUR/USD converter.
    Author : Samuel Santiago
    Date : 2026-10-05
    Version: 1.0
    Description:exercise of conversions
"""

#cogemos la variable de grados en C
gradosC=int(input("grados celsius:")) 

#hacemos el cambio a faren
cambio_de_grados= (gradosC*9/5)+32
print(cambio_de_grados, ("grados faren"))

#esto es lo mismo, un cambio pero en euros 
RATE_EUR_USD = 1.12
euros = float(input("EUR: "))
usd = euros * RATE_EUR_USD
print(f"{euros:.2f} EUR = {usd:.2f} USD")
