import random


def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>abcdefghijklm123456789"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password


def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923",]
    
    return random.choice(emodji)


def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "Cara"
    else:
        return "Cruz"
 
def gif():
    gifs = ["https://tenor.com/view/totoro-gif-24991987", "https://tenor.com/view/ghibli-gif-23680058", "https://tenor.com/view/studio-ghibli-anime-gif-22884010", "https://tenor.com/view/porco-rosso-thumbs-up-nausicaa-studio-ghibli-ghibli-gif-25407298",]
    
    return random.choice(gifs)
