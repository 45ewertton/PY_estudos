from Copo import Copo
from Xicara import Xicara
class Main:
    copo1 = Copo('', '')
    xic1 = Xicara('', '')
    copo1.setMaterial('ferro')
    copo1.setEstado('seco')
    xic1.setMaterial('porcelana')
    xic1.setEstado('seco')
    
    print("O copo é feito de: " + copo1.getMaterial() + " e ele está " + copo1.getEstado())
    print('----------------------------------------')
    copo1.encher()
    print("O copo é feito de: " + copo1.getMaterial() + " e ele está " + copo1.getEstado())
    print('----------------------------------------')
    copo1.secar()
    print("O copo é feito de: " + copo1.getMaterial() + " e ele está " + copo1.getEstado())
    print('-------------------------------------------------------------------')
    print("A xícara é feita de: " + xic1.getMaterial() + " e ela está " + xic1.getEstado())
    print('----------------------------------------')
    xic1.encher()
    print("A xícara é feita de: " + xic1.getMaterial() + " e ela está " + xic1.getEstado())
    print('----------------------------------------')
    xic1.secar()
    print("A xícara é feita de: " + xic1.getMaterial() + " e ela está " + xic1.getEstado())