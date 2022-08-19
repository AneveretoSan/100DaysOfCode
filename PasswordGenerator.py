'''Password generator v0.1.0'''
'''Future adds: GUI'''

import random

characters = '0123456789abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPKRSTUVWXYZ‑‒–—―‗‘’‚‛“”„‟•‣․‥…‧′″‴‵‶‷❛❜❝❞ʹʺʻʼʽʾʿˀˁ˂˃˄˅ˆˇˈˉˊˋˌˍˎˏːˑ˒˓˔˕˖˗˘˙˚˛˜˝ˠˡ～¿﹐﹒﹔﹕！＃＄％＆＊，．：；？＠、。〃〝〞︰〈〉《》「」『』【 〔〕︵︶︷︸︹︺︻︼︽︾︿﹀﹁﹂﹃﹄﹙﹚﹛﹜﹝﹞﹤﹥（）＜＞｛｝〖〗〘〙〚〛«»‹›〈〉〱'

print("Welcome to the password generator")
amount = int(input("Please set your amount of paswords: "))
length = int(input("Please set the length of your paswords: "))

# este if está para si has elegido más de una contraseña te envie el mesanje en plural y en caso contrario, en singular
if amount > 1:
    print("There is your password\n")
else:
    print("There is yours passwords\n")

#el primer for es para generar la cantidad de contraseñlas pedidas, y el segundo se encarga de generarlas
for i in range(amount):
    password = ""
    for j in range(length):
        password += random.choice(characters)
    print(password + "\n")

