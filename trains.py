import csv
import pandas as pd

data_set = pd.read_csv("Top Trumps - Trains.csv")

Cards = data_set["Train"].tolist()
Year = data_set["Debut Year"].tolist()
Speed = data_set["Speed"].tolist()
Range = data_set["Range"].tolist()
Fame = data_set["Fame Rank"].tolist()
Top = data_set["Top Trumps Rating"].tolist()

print(len(Cards))

while True:
    card = input("Enter card name here: ").lower()
    if card == "b":
        exit()
    card_position = Cards.index(card)
    # For each below assume the value eg. H = Height_Value
    y, s, r, f, t = Year[card_position], Speed[card_position], Range[card_position], Fame[card_position], Top[card_position]
    wrate = []
    current_wins = 0
    for num in Year:
        if y < num:
            current_wins += 1
    ans = ((current_wins / 29) * 100)
    wrate.append(ans)
    current_wins = 0

    for num in Speed:
        if s > num:
            current_wins += 1
    ans = ((current_wins / 29) * 100)
    wrate.append(ans)
    current_wins = 0

    for num in Range:
        if r > num:
            current_wins += 1
    ans = ((current_wins / 29) * 100)
    wrate.append(ans)
    current_wins = 0

    for num in Fame:
        if f < num:
            current_wins += 1
    ans = ((current_wins / 29) * 100)
    wrate.append(ans)
    current_wins = 0


    for num in Top:
        if t > num:
            current_wins += 1
    ans = ((current_wins / 29) * 100)
    wrate.append(ans)
    current_wins = 0



    print("If you play Debut Year you have a", round(wrate[0], 2), "% chance of winning.")
    print("If you play Speed you have a", round(wrate[1], 2), "% chance of winning.")
    print("If you play Range you have a", round(wrate[2], 2), "% chance of winning.")
    print("If you play Fame Rank Rating you have a", round(wrate[3], 2), "% chance of winning.")
    print("If you play Top Trumps Rating you have a", round(wrate[4], 2), "% chance of winning.")
    print("")



data_set.close()