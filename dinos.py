import csv
import pandas as pd

data_set = pd.read_csv("Top Trumps - Dinosaurs - Top Trumps - Dinosaurs.csv")

Cards = data_set["Individual"].tolist()
Height = data_set["Height (ft)"].tolist()
Weight = data_set["Weight (lbs)"].tolist()
Legnth = data_set["Length (ft)"].tolist()
Killer = data_set["Killer rating"].tolist()
Intelligence = data_set["Intelligence"].tolist()
Age = data_set["Age (millions of yrs)"].tolist()

print(len(Cards))

while True:
    card = input("Enter card name here: ")
    if card == "b":
        exit()
    card_position = Cards.index(card)
    # For each below assume the value eg. H = Height_Value
    h, w, l, k, i, a = Height[card_position], Weight[card_position], Legnth[card_position], Killer[card_position], Intelligence[card_position], Age[card_position]
    wrate = []
    current_wins = 0
    for num in Height:
        if h > num:
            current_wins += 1
    ans = ((current_wins / 29) * 100)
    wrate.append(ans)
    current_wins = 0

    for num in Weight:
        if w > num:
            current_wins += 1
    ans = ((current_wins / 29) * 100)
    wrate.append(ans)
    current_wins = 0

    for num in Legnth:
        if l > num:
            current_wins += 1
    ans = ((current_wins / 29) * 100)
    wrate.append(ans)
    current_wins = 0

    for num in Killer:
        if k > num:
            current_wins += 1
    ans = ((current_wins / 29) * 100)
    wrate.append(ans)
    current_wins = 0


    for num in Intelligence:
        if i > num:
            current_wins += 1
    ans = ((current_wins / 29) * 100)
    wrate.append(ans)
    current_wins = 0

    for num in Age:
        if a > num:
            current_wins += 1
    ans = ((current_wins / 29) * 100)
    wrate.append(ans)
    current_wins = 0

    print("If you play Height you have a", round(wrate[0], 2), "% chance of winning.")
    print("If you play Weight you have a", round(wrate[1], 2), "% chance of winning.")
    print("If you play Legnth you have a", round(wrate[2], 2), "% chance of winning.")
    print("If you play Killer Rating you have a", round(wrate[3], 2), "% chance of winning.")
    print("If you play Intelligence you have a", round(wrate[4], 2), "% chance of winning.")
    print("If you play Age you have a", round(wrate[5], 2), "% chance of winning.")
    print("")



data_set.close()