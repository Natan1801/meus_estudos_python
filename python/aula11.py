nome = 'Guanabara'
cores = {'limpa' : '\033[m',
         'azul' : '\033[34m',
         'amarelo' : '\033[33m',
         'pretoebranco' :'\033[7;30m'}
print('Seja bem vindo, {} {} {}!!').format(cores['amarelo'], nome, cores['azul'])