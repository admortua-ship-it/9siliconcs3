birthyear = int(input("Enter your birth year: "))

def get_zodiac_sign(year):

    if year > 1900:
        zodiacyear = (year - 1900) % 12
        if zodiacyear == 0:
            zodiac = "Rat (鼠 / Shǔ)"
        elif zodiacyear == 1:
            zodiac = "Ox (牛 / Niú)"
        elif zodiacyear == 2:
            zodiac = "Tiger (虎 / Hǔ)"
        elif zodiacyear == 3:
            zodiac = "Rabbit (兔 / Tù)"
        elif zodiacyear == 4:
            zodiac = "Dragon (龙 / Lóng)"
        elif zodiacyear == 5:
            zodiac = "Snake (蛇 / Shé)"
        elif zodiacyear == 6:
            zodiac = "Horse (马 / Mǎ)"
        elif zodiacyear == 7:
            zodiac = "Goat (羊 / Yáng)"
        elif zodiacyear == 8:
            zodiac = "Monkey (猴 / Hóu)"
        elif zodiacyear == 9:
            zodiac = "Rooster (鸡 / Jī)"
        elif zodiacyear == 10:
            zodiac = "Dog (狗 / Gǒu)"
        elif zodiacyear == 11:
            zodiac = "Pig (猪 / Zhū)"
        return f"Your Chinese Zodiac Sign is: {zodiac}"
    else:
        return "Invalid Year, it should not be earlier than 1900."

print(get_zodiac_sign(birthyear))