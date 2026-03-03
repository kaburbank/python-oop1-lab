#!/usr/bin/env python3

class Coffee:
    def __init__(self):
        self.size = input("Enter coffee size (Small, Medium, Large): ")
        if self.size not in ["Small", "Medium", "Large"]:
            print("size must be Small, Medium, or Large.")
        price_input = input("Enter coffee price: ")
        try:
            self.price = float(price_input)
        except ValueError:
            print("price must be a number.")

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1