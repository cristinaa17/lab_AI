prices = [100, 250, None, 320, None, 510]

filtered_prices = list(filter(lambda x: x is not None, prices))

discounted_prices = list(map(lambda x: x * 0.9, filtered_prices))

print("Preturi initiale:", prices)
print("Dupa filtrare:", filtered_prices)
print("Dupa reducere:", discounted_prices)