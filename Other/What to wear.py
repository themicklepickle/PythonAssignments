sunny = input("Is it sunny? (yes/no): ")
if sunny == "no":
    rainy = input("Is it rainy? (yes/no): ")
    if rainy == "no":
        snowy = input("Is it snowy? (yes/no): ")

if sunny == "yes":
    print("You should wear a t-shirt, shorts, a hat, sunglasses and sandals.")
elif rainy == "yes":
    print("You should wear a rain jacket, long pants, rain boots and bring an umbrella.")
elif snowy == "yes":
    print("You should wear a winter jacket, snow pants, winter boots, mittens and a touque.")
else:
    print("That's an uncommon weather condition! Look outside and decide for yourself!")
