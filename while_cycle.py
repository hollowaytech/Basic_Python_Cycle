counter = 1
print("=============================================")
data_pack_one = int(input("Enter data packet one amount here:"))
print("=============================================")
data_pack_two = int(input("Enter data packet two amount here:"))
print("=============================================")
data_amounts_pos = False

while counter <= 4:
    if data_pack_one % 2 == 0:
        data_pack_one+=2
    else:
        data_pack_one-=2
    if not data_pack_two % 2 == 0:
        data_pack_two+=3
    else:
        data_pack_two-=3
    print("=========================")
    print(f"Cycle: {counter}")
    print(f"Dataone: {data_pack_one}")
    print(f"Datatwo: {data_pack_two}")
    print("=========================")
    counter+=1

if data_pack_one >= 0 and data_pack_two >= 0:
    data_amounts_pos = True

print("===============================")
print(f"Dataone: {data_pack_one}")
print(f"Datatwo: {data_pack_two}")
print(f"Data amounts positive: {data_amounts_pos}")
print("===============================")
