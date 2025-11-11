from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, finalidade):
        super().__init__(marca,modelo)
        self.finalidade = finalidade

    def __str__(self):
        return f'{self._modelo} - {self._marca} - {self.finalidade}'
    
    ligar()