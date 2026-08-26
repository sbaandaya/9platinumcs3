zodiac_signs = ["Rat (鼠 / Shǔ)", "Ox (牛 / Niú)", "Tiger (虎 / Hǔ)", "Rabbit (兔 / Tù)", "Dragon (龙 / Lóng)", "Snake (蛇 / Shé)", "Horse (马 / Mǎ)", "Goat (羊 / Yáng)", "Monkey (猴 / Hóu)", "Rooster (鸡 / Jī)", "Dog (狗 / Gǒu)", "Pig (猪 / Zhū)"]

b_day = int(input("Please enter your Birth Year: "))
if b_day < 1900:
    print("Invalid year, it should not be below 1900. Please start again")
else:
    zodiac_sign_ans = int((b_day - 1900) % 12)
    print(f"Your Chinese Zodiac Sign is: {zodiac_signs[zodiac_sign_ans]}")
