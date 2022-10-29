desimal = int(input("masukan angka desimal = "))

biner = bin(desimal).replace("0b",'binernya adalah = ')
oktal = oct(desimal).replace("0o",'oktalnya adalah = ')
hexa = hex(desimal).replace("0x",'hexanya adalah = ')

print(biner)
print(oktal)
print(hexa)

# print("======dengan formating======")

# format_binary = f"binary = {bin(desimal)}"
# format_octal = f"octal = {oct(desimal)}"
# format_hex =  f"hex = {hex(desimal)}"

# print(format_binary)
# print(format_octal)
# print(format_hex)