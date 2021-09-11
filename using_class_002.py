class Carro():
    def __init__(self, marca, cor, placa ):
        self.marca = marca
        self.cor = cor
        self.placa = placa

    def ligar_carro(self):
        print('Ligando o carro...')

    def desligando_carro(self):
        print('Desligando o carro...')

    def buzinar(self):
        print('Buzinando, BI BI BI')

    def propriedades(self):
        print('| Marca: ' + self.marca + '| Cor: ' + self.cor + '| Placa: ' + self.placa +'|')

print('----------INICIALIZANDO----------')
carro1 = Carro('Fiat', 'Vermelho', '123abc')
carro1.ligar_carro()
carro1.buzinar()
carro1.desligando_carro()
carro1.propriedades()
print('--------------------')
carro2 = Carro('Toyota', 'Preto', '647hjt')
carro2.ligar_carro()
carro2.buzinar()
carro2.desligando_carro()
carro2.propriedades()
print('--------------------')
carro3 = Carro('Jeep', 'Branco', '908ikl')
carro3.ligar_carro()
carro3.buzinar()
carro3.desligando_carro()
carro3.propriedades()
print('----------FINALIZANDO----------')