from random import randint

def generate_captcha_text():
    captcha_size = randint(5,10)
    captcha = ''
    for x in range(1, captcha_size+1):
        random_2, random_3 = randint(1,10), 99
        
        if random_2 < 6:
            random_3 = str(randint(1,9))
        else:
            random_3 = chr(randint(65,91))

        captcha += random_3
    return captcha