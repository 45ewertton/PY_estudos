#Class
#Syntaxe

#Attributes Marca, Memória Ram e Placa de Vídeo
class Computador:
    def __init__(self, marca, m_ram, placa_de_video):
        self.marca = marca
        self.m_ram = m_ram
        self.placa_de_video = placa_de_video

#Actions
    def on(self):
        print('Ligando...')
    
    def off(self):
        print('Desligando...')

    def properties(self):
        print(self.marca, self.m_ram, self.placa_de_video)

print('----------INICIALIZANDO----------')
computador1 = Computador('Asus', '8gb', 'Nvidia')
computador1.on()
computador1.off()
computador1.properties()
print('--------------------')
computador2 = Computador('Dell', '10gb', 'GeForce')
computador2.on()
computador2.off()
computador2.properties()
print('--------------------')
computador3 = Computador('Acer', '16gb', 'ATM')
computador3.on()
computador3.off()
computador3.properties()
print('----------FINALIZANDO----------')