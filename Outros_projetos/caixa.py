import os
produtos={
    'banana': 1.20,
    'maca': 1.80,
    'leite': 0.95,
    'pao': 0.25
}

lista_compras={}
custo=0.0
total=0.0
subt=0.0
sair=False
while sair==False:
    while True:
    
        n_produto= input('Digite o produto que deseja comprar: ')
        if n_produto not in produtos:
            print('O produto nao esta na lista de produtos disponiveis')
            continue
        break  
    
    while True:

        quantidadei=input('Digite a quantidade que deseja comprar: ').strip()
        try:
            quantidade=int(quantidadei)
            if quantidade<=0:
                print('A quantidade tem que ser maior que 0')
                continue
            break
        except ValueError:
            print('Tem de digitar um numero')
    if n_produto in lista_compras:
        lista_compras[n_produto] += quantidade
    else:
        lista_compras[n_produto] = quantidade
    resposta=input('Deseja adicionar mais algum produto?(s/n)').lower().strip()   
    if resposta=='n' or resposta=='nao':
        sair=True
os.system('cls' if os.name == 'nt' else 'clear')
print("\n--- O TEU TALÃO DE COMPRAS ---")
for n_produtos,quantidade in lista_compras.items():
    custo=produtos[n_produto]
    subt+=(custo*quantidade)
    total+=subt
    print(f'{n_produto.capitalize()} x {quantidade} : {subt:.2f}€')
print("-" * 30)
print(f"TOTAL A PAGAR: {total:.2f}€")