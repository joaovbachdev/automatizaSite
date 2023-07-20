import time

class NovaOs:
    def __init__(self) -> None:
        print("testando NOVA O.S")

    def adicionaPedido(self, **kwargs):
        kwargs['pagina'].goto("https://painel-homol.matrixcargo.com.br/loads-planning/service-orders")
        time.sleep(3)
        kwargs['pagina'].locator("text=Nova O.S").click()
        time.sleep(5)
        kwargs['pagina'].locator("text=Voltar para Modo de Planejamento").click()
        time.sleep(1)
        kwargs['pagina'].locator("text=Voltar para pedidos").click()
        time.sleep(3)
        quantidade = kwargs['pagina'].query_selector_all("div[data-rowindex]")
        quantidade[0].query_selector("button").click()
        time.sleep(3)
        quantidade2 = kwargs['pagina'].query_selector_all("div[data-rowindex]")
        time.sleep(1)
        if quantidade == quantidade2:
            with open("relatorio.txt","a") as f:
                f.write("falha ao adicionar um item para a O.S \n")

                f.close()
        else:
            with open("relatorio.txt","a") as f:
                f.write("sucesso em adicionar um pedido para a O.S \n")
                f.close()


    def adicionaTodos(self, **kwargs):
        kwargs['pagina'].goto("https://painel-homol.matrixcargo.com.br/loads-planning/service-orders")
        time.sleep(3)
        kwargs['pagina'].locator("text=Nova O.S").click()
        time.sleep(5)
        kwargs['pagina'].locator("text=Voltar para Modo de Planejamento").click()
        time.sleep(1)
        kwargs['pagina'].locator("text=Voltar para pedidos").click()
        time.sleep(3)

        quantidade1 = kwargs['pagina'].query_selector_all("div[data-rowindex]")
        if len(quantidade1) > 0:
            kwargs['pagina'].locator('text=Adicionar todos').click()
            time.sleep(3)

            if len(kwargs['pagina'].query_selector_all("div[data-rowindex]")) == 0:
                with open("relatorio.txt","a") as f:
                    f.write("sucesso em adicionar todos os pedidos para a O.S \n")
                    f.close()

            else:
                 with open("relatorio.txt","a") as f:
                     f.write("falha em adicionar todos os pedidos para a O.S \n")
                     f.close()