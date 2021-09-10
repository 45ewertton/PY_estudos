class Copo:
    def __init__(self, material, estado):
        self._material = material
        self._estado = estado

    def getMaterial(self):
        return self._material
    
    def setMaterial(self, material):
        self._material = material

    def getEstado(self):
        return self._estado

    def setEstado(self, estado):
        self._estado = estado

    def encher(self, liquido = 'água'):
        print('Enchendo o copo')
        self.setEstado(f'cheio de {liquido}')
    
    def secar(self):
        print('Secando o copo')
        self.setEstado('seco')