mac_sujo = "   00:1A:2b:3C:4D:5E   "
mac_limpo = mac_sujo.strip().lower()

bytes_enviados = 1024
pacotes = 5
total_trafego = bytes_enviados * pacotes    

print(f"MAC detectado: '{mac_sujo}'")
print(f"MAC para o banco: {mac_limpo}")
print(f"Trafego anômalo: {total_trafego} bytes")
