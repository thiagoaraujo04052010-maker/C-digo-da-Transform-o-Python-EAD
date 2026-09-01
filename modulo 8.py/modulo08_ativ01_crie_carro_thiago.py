'''

'''


class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"

print("🚗 CADASTRO DE VEÍCULO 🚗\n")

marca_digitada = input("Digite a marca do carro: ")
modelo_digitado = input("Digite o modelo do carro: ")

meu_carro = Carro(marca_digitada, modelo_digitado)

print("\n--- Informações do Carro Cadastrado ---")
print(meu_carro.exibir_info())

# Cria uma classe chamada Carro
class Carro:

    # Método construtor: é executado quando um objeto Carro é criado
    def __init__(self, marca, modelo):
        # Guarda a marca recebida no objeto
        self.marca = marca

        # Guarda o modelo recebido no objeto
        self.modelo = modelo

    # Método responsável por exibir as informações do carro
    def exibir_info(self):
        # Retorna uma string com marca e modelo
        return f"Marca: {self.marca}, Modelo: {self.modelo}"


# Cria uma classe CarroEletrico que herda as características de Carro
class CarroEletrico(Carro):

    # Construtor do carro elétrico
    def __init__(self, marca, modelo, autonomia_bateria):

        # Chama o construtor da classe Carro
        super().__init__(marca, modelo)

        # Guarda a autonomia da bateria no objeto
        self.autonomia = autonomia_bateria

    # Sobrescreve o método exibir_info da classe Carro
    def exibir_info(self):

        # Chama o exibir_info da classe Carro para obter marca e modelo
        info_base = super().exibir_info()

        # Retorna as informações do carro junto com a autonomia da bateria
        return f"{info_base} | Autonomia da Bateria: {self.autonomia} km"


# Cria um objeto da classe CarroEletrico
meu_carro = CarroEletrico("BYD", "Dolphin", 60)