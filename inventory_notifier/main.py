import pandas as pd
from colorama import Fore

df = pd.read_csv("inventory_data.csv")

print("Reorder Suggestions:\n")

for index, row in df.iterrows():
    item = row["Item"]
    usage = [row["Week 1"], row["Week 2"], row["Week 3"], row["Week 4"]]
    current_stock = row["Current Stock"]

    avg_usage = sum(usage) / len(usage)

    weeks_left = current_stock / avg_usage

    if weeks_left < 2:
        reorder_qty = avg_usage * 4 - current_stock
        print(Fore.RED + f'{item}: Low stock. Suggest reordering about {int(reorder_qty)} units.')
    else:
        print(Fore.GREEN + f'{item}: Stock level okay. {weeks_left:.1f} weeks of stock remaining.')