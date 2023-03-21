# NICOLE UCHÔA 12211ECP020
import time
class Classificacoes:
    def __init__(self, relacao_binaria, conjunto_dominio) -> None:
        self.relacao_binaria = relacao_binaria
        self.conjunto_dominio = conjunto_dominio
        self.propriedade = ""

    def define_propriedades(self):
        self.eh_funcao()
        self.eh_simetrica()
        self.eh_reflexiva()
        self.eh_transitiva()
        self.eh_equivalente()
        self.eh_irreflexiva()
        return self.propriedade

    def eh_funcao(self):
        for x in self.conjunto_dominio:
            par_dominio_imagem_unico = 0
            for (i, j) in self.relacao_binaria:
                if x == i:
                    par_dominio_imagem_unico += 1
            if par_dominio_imagem_unico != 1:
                return
        self.propriedade += "Fu"
        self.eh_injetora()
        self.eh_sobrejetora()
        self.eh_bijetora()

    def eh_injetora(self):
        contradominio = []
        for x, y in self.relacao_binaria:
            contradominio.append(y)
        set_list = set(contradominio)
        if len(contradominio) != len(set_list):
            return
        self.propriedade += "Fi"

    def eh_sobrejetora(self):
        # no caso dessa atividade o contradominio == imagem, que nesse caso deve ter todos os elementos do dominio
        imagem = []
        for x, y in self.relacao_binaria:
            imagem.append(y)
        if all(item in imagem for item in self.conjunto_dominio):
            self.propriedade += "Fs"

    def eh_bijetora(self):
        if "Fi" in self.propriedade and "Fs" in self.propriedade:
            self.propriedade += "Fb"

    def eh_simetrica(self):
        if all((y, x) in self.relacao_binaria for (x, y) in self.relacao_binaria):
            self.propriedade += "S"

    def eh_reflexiva(self):
        if all((x, x) in self.relacao_binaria for x in self.conjunto_dominio):
            self.propriedade += "R"

    def eh_transitiva(self):
        for par in self.relacao_binaria:
            for (i, j) in self.relacao_binaria:
                if (par[1] == i) and ((par[0], j) not in self.relacao_binaria):
                    return False
        self.propriedade += "T"

    def eh_equivalente(self):
        if "SRT" in self.propriedade:
            self.propriedade += 'E'

    def eh_irreflexiva(self):
        for x in self.conjunto_dominio:
            if (x, x) in self.relacao_binaria:
                return
        self.propriedade += 'I'


start_time = time.time()

def main(A: list, path: str):
    # utilizando o raciocínio feito em sala de aula
    with open(path, 'w') as f:
        num_elementos = len(A)
        for i in range(2 ** (num_elementos*num_elementos)):
                relacao_binaria = []
                for j in range(num_elementos):
                    for k in range(num_elementos):
                        bit = (j*num_elementos) + k
                        # verificamos se os números estão ligados, através da análise binária, deslocando os bits de bit_relacao
                        # fazendo um bitwise and com o número 1 e o resultado for 1, o par (j, k) estão ligados, pertencendo ao conjunto de relações binárias
                        if (i >> bit) & 1:
                            relacao_binaria.append((A[j], A[k]))
                classificacao = Classificacoes(relacao_binaria, A)
                propriedade = classificacao.define_propriedades()
                f.write(str(relacao_binaria) + ' ' + propriedade + '\n')
    f.close()

main([1, 2, 3, 4], "./4_elementos.txt")
print("--- %s seconds ---" % (time.time() - start_time))
# time python estrutura_relacoes_binarias.py