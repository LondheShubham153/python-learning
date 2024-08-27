"""
fruits  = {
    "apple":2,
    "banana":3,
    "chikoo":3,
    "pineapple":1
}
"""

list_of_fruits = ['apple',
                  'apple',
                  'banana',
                  'banana',
                  'banana',
                  'chikoo',
                  'chikoo',
                  'chikoo',
                  'pineapple'
                ]

fruits_basket = {}

for fruit in list_of_fruits:
    if fruit in fruits_basket:
        fruits_basket.update({fruit:fruits_basket[fruit]+1})
    else:
        fruits_basket.update({fruit:1})

print(fruits_basket)