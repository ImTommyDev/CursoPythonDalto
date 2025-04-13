class MiExcepcion(Exception):
    def __init__(self, err):
        print("Vaya liada primico: ", err)
        
try:
    raise MiExcepcion("Error de prueba")
except MiExcepcion as e:
    print("Capturada la excepción personalizada:", e)