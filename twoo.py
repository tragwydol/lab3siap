import os
import codecs

def get_total_cost(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File '{filename}' does not exist.")

    with codecs.open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    total_cost = 0
    for line in lines:
        if line is None:
            continue
        arr = line.split()
        quantity, price = arr[-2],arr[-1]
        total_cost += float(price) * int(quantity)
        
    return total_cost


if __name__ == "__main__":
    filename = "prices.txt"
    try:
        total_cost = get_total_cost(filename)
    except FileNotFoundError as e:
        print(e)
    else:
        print(f"Общая стоимость заказа: {total_cost}")