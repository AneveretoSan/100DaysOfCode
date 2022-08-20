'''MadLibs v1.0'''

'''Future adds: GUI, different texts to choice, mores requests, find a way to do it more short'''

requests = ["writte an name: ", "writte an accion: ",  "writte an singular animal: ", "writte an sport: "]

text = "Hi, my name is {} and i like {}. My favourite animal is {} and i'm very good at {}."

user_words = ["", "", "", ""]
#almacena en la lista "user_words" cada palabra que recoge del imput en la posición que le corresponde según la petición
for i in range(len(requests)):
    user_words[i] = input(requests[i]).lower()

print(text.format(user_words[0].title(), user_words[1], user_words[2], user_words[3])) # con el text formar indicamos en cada {} que palabra le corresponde poner de la variable user_words