def calcular_imc(altura, peso):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 24.9:
        return "Peso normal"
    elif imc < 29.9:
        return "Sobrepeso"
    elif imc < 34.9:
        return "Obesidade Grau 1"
    elif imc < 39.9:
        return "Obesidade Grau 2"
    else:
        return "Obesidade Grau 3"

altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em quilogramas: "))

imc = calcular_imc(altura, peso)
classificacao = classificar_imc(imc)

print(f"Seu IMC é: {imc}")
print(f"Classificação: {classificacao}")
