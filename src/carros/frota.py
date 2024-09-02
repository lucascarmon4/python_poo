class Carro:
    modelo: str
    marca: str
    cor: str
    __odometro = 0.0
    __motor_on = False
    __tanque: float
    consumo_medio: float
    def __init__(self, modelo : str, marca : str, cor : str,
                       odometro : float, motor : bool, tanque: float, consumo_medio: float):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.__odometro = odometro
        self.__motor_on = motor
        self.__tanque = tanque
        self.consumo_medio = consumo_medio
    def ligar(self):
        if not self.__motor_on and self.__tanque > 0:
            self.__motor_on = True
        else:
            raise Exception("Erro: Motor já ligado ou tanque vazio.")

    def acelerar(self, velocidade : float, tempo : float):
        if self.__motor_on:
            space = velocidade * tempo

            litros = space/self.consumo_medio
            self.__tanque = litros
            if self.__tanque > 0 and self.__tanque >= litros:
                self.__odometro += space
                self.__tanque -= litros
            else:
                raise Exception("Erro: Não há gasolina no carro!")

        else:
            raise Exception("Erro: Não é possível acelerar! Motor desligado!")

    def desligar(self):
        if self.__motor_on:
            self.__motor_on = False
        else:
            raise Exception("Erro: Motor já desligado!")

    def get_odometro(self):
        return self.__odometro
    def get_tanque(self):
        return self.__tanque
    def __str__(self):
        info = (f'Carro {self.modelo}, marca {self.marca}, '
                f'cor {self.cor}\n{self.__odometro} Km, '
                f'motor {self.__motor_on}'
                f'consumo médio {self.consumo_medio}'
                f'tanque {self.__tanque}')
        return info
    def __repr__(self):
        return f'Carro(modelo= "{self.modelo}", marca= "{self.marca}", cor= "{self.cor}", motor= {self.__motor_on}, consumo_medio= {self.consumo_medio}, tanque= {self.__tanque})'




