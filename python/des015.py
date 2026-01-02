import math

angulo = float(input('Digite o ângulo: '))

radianos = math.radians(angulo)

seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente= math.tan(radianos)

print(f'O Seno de {angulo}° é {seno:.4f}')
print(f'O cosseno de {angulo}° é {cosseno:.4f}')
print(f'O tangente de {angulo}° é {tangente:.4f}')


