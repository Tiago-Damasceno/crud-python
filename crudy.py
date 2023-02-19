class Client:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_de_plano = ['basico', 'premium']
        self.plano = plano

        #seo plano estiver dentro (in) de uma lista de planos ai temos um plano
        if plano in self.lista_de_plano:
            self.plano = plano
        #se não, então aparece o erro 'plano invalido'
        else:
            raise Exception ('plano invalido')

    def mudar_plano(self, novo_plano):
        #se o novo plano estiver dentro (in) da lista de planos
        if novo_plano in self.lista_de_plano:
            #o plano é igual ao novo plano
            self.plano = novo_plano
        else:
            print('comando invalido')

    def ver_filme(self,filme, plano_filme):
        #se o plano do cliente for igual ao plano do filme, 
        if self.plano == plano_filme:
            print(f'ver filme',{filme})
        #se o plano do cliente for o plano 'premium'    
        elif self.plano == 'premium':
            #pode ver o filme
            print(f'ver filme', {filme})
        #se o plano do cliente for os plano 'basico' e o plano do filme for 'premium'

        elif self.plano == 'basico' and plano_filme == 'premium':
            print('mude o plano pra ver esse filme') 
        else:
            print('plano errado')
            
           

            



cliente = Client('tiago', 'tiago@gmail.com', 'basico')
print(cliente.plano)
cliente.ver_filme('mascara', 'premium')

#não precisa colocar print na nova função
#estou inserindo uma nova função no programa 
cliente.mudar_plano('premium')
cliente.ver_filme('mascara', 'premium')
#print(cliente.plano)





