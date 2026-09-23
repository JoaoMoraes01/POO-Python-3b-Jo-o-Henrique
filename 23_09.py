class Pagamento:
    def processar(self):
        print("Processando pagamento")

class Pix(Pagamento):
    def processar(self):
        print("Pagamento via PIX")

class Cartao(Pagamento):
    def processar(self):
        print("Pagamento via cartao")

class Boleto(Pagamento):
    def processar(self):
        print("Pagamento via Boleto")

class CarteriaDigital(Pagamento):
    def processar(self):
        print("Pagamento via Carteira Digital")

class ValePresente(Pagamento):
    def processar(self):
        print("Pagamento via Vale Presente")

class PagamentoNaEntrega(Pagamento):
    def processar(self):
        print("Pagamento via Pagamento na Entrada")


# Instanciamento
pagamentos =[
    Pix(),
    Cartao(),
    Boleto(),
    CarteriaDigital(),
    ValePresente(),
    PagamentoNaEntrega()
]

for pagamento in pagamentos:
    pagamento.processar()