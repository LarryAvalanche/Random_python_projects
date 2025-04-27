address = ["198.223.XX.XX","189.56.XXX.XX","234.12.XX.XXX"]
network_portion = []
for i in address:
    network_portion.append(i[0:3])
print(network_portion)
