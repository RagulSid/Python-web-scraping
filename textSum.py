#transformers is a text summmarization library available in python ( tried some on hands on)

from transformers import pipeline
summarizer = pipeline('summarization')

article = """Here are 18 of the best foods to help you gain weight or add muscle, the healthy way.
Homemade protein smoothies. Drinking homemade protein smoothies can be a highly nutritious and quick way to gain weight. ...
Milk. ...
Rice. ...
Nuts and nut butters. ...
Red meats. ...
Potatoes and starches. ...
Salmon and oily fish. ...
Protein supplements. How to gain 2 kg in a week?
General tips for gaining weight safely
Eat three to five meals a day. Eating at least three meals a day can make it easier to increase calorie intake. ...
Weight training. ...
Eat enough protein. ...
Eat meals with fibrous carbohydrates and healthful fats. ...
Drink high-calorie smoothies or shakes. ...
Seek help where needed."""

summarizer(article, max_length=60, min_length=30, do_sample=False)