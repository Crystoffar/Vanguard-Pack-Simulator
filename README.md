# Vanguard Pack Simulator

This script simulates the opening of a Cardfight!! Vanguard Booster Box, composed of 30 individual booster packs. Cardfight!! Vanguard cards come in 4 rarities: Common, Rare, Double Rare, and Triple Rare. Each booster pack contains 6 cards, with one card guaranteed as a Rare or higher rarity.

The script imports a csv file containing the rarity as well as the card name of each card in a booster set. It then opens each pack, with 5 cards being a normal chance and 1 being a chance with a minimum of Rare rarity. The script adds each card to a dictionary that tracks the quantity of each card pulled. This dictionary is then exported to a csv file after opening all 30 booster packs.
