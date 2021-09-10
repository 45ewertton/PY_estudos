from Copo import Copo

class Xicara(Copo):
    
    def encher(self, liquido = 'café'):
        print('Enchendo a xícara')
        self.setEstado(f'cheio de {liquido}')
    def secar(self):
        print('Secando a xícara')
        self.setEstado('seco')