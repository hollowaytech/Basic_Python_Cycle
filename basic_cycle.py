data_packet = int(input("Enter packet amount here: "))
positive = False
for counter in range (1,6):
    if data_packet % 2 == 0:
        data_packet -= 10
    else:
        data_packet += 15
    print(f"Cycle: {counter}")
    print(f"Data Amount: {data_packet}")
    counter+=1
if data_packet > 0:
    positive = True
print(f"Final data amount: {data_packet}")
print(f"Data amount positive: {positive}")
