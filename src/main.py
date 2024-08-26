from frota import *
import pickle

def operar_carro(carro: Carro):
    print('1- Ligar motor')
    print('2- Desligar motor')
    print('3- Acelerar')

    op = 0
    while op not in (1, 2, 3):
        op = int(input("Digite as opcoes[1-3]: "))

    if op == 1:
        carro.ligar()
    elif op == 2:
        carro.desligar()
    elif op == 3:
        v = float(input("Informe a velocidade: "))
        t = float(input("Informe o tempo: "))
        carro.acelerar(v, t)

if __name__ == "__main__":
    print('Cadastre um carro')

    try:
        with open("carros.pkl", 'rb') as arquivo:
            carros = pickle.load(arquivo)
            print(carros)
    except Exception as e:
        print(e)

    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    consumo = float(input("Digite o consumo medio"))

    carro1 = Carro(nm_modelo, nm_marca, nm_cor, 0,  False, consumo, 100)

    nm_modelo2 = input('Digite o modelo 2: ')
    nm_marca2 = input('Digite a marca 2: ')
    nm_cor2 = input('Digite a cor 2: ')
    consumo = float(input("Digite o consumo medio"))
    carro2 = Carro(nm_modelo2, nm_marca2, nm_cor2, 0, False, consumo, 100)

    carros = {}
    carros[id(carro1)] = carro1
    carros[id(carro2)] = carro2

    try:
        with open("carros.pkl", 'wb') as arquivo:
            pickle.dump(carros, arquivo)
    except Exception as e:
        print(e)

    '''
    Controlando o carro até ele atingir 10000 Km
    '''
    while (carro1.get_odometro() < 600 and carro2.get_odometro() < 600) and (carro1.get_tanque() > 0 or carro2.get_tanque() > 0):
        try:
            op = 0
            while op not in (1, 2):
                op = int(input("Qual carro? 1 ou 2?"))
                if op == 1:
                    operar_carro(carro1)
                    print('Infos atuais do carro 1')
                    print(carro1)
                else:
                    operar_carro(carro2)
                    print('Infos atuais do carro 2')
                    print(carro2)
        except Exception as e:
            print("Erro!")
            print(e)

    carro1.desligar()
    carro2.desligar()
    print(carro1)
    print(carro2)
