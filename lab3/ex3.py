import random

def normalize_data(data):
    if not data:
        return []

    min_val = min(data)
    max_val = max(data)

    if min_val == max_val:
        return [0.0 for _ in data]

    normalized = [(x - min_val) / (max_val - min_val) for x in data]
    return normalized

data = [10, 20, 30, 40, 50]
normalized_data = normalize_data(data)

print("Date initiale:", data)
print("Date normalizate:", normalize_data(data))