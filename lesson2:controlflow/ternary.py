score = int(input('Enter a score between 0 and 100 : '))

# conditional assignments / ternary

is_top_score = True if score >= 90 else False
print('is_top_score : ', is_top_score)

# nested ternary

temp = float(input('Enter a temperature between 0 and 40 degree celsius : '))

weather = "hot" if temp >= 35 else ("mild" if temp >=15 else "cold")
print('Weather is : ', weather)