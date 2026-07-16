
with open ('analisar_texto/texto.txt','r', encoding='utf-8') as ficheiro:
    conteudo= ficheiro.read()

c=0
c=conteudo.count('.')
print(conteudo)

palavras_c=conteudo.lower().split()
palavras_li=[]
for palavras in palavras_c:
    palavra_l=palavras.strip('.,!?;:"()')
    if palavra_l:
        palavras_li.append(palavra_l)
total_p=len(palavras_li)



frequencia={}

for p in palavras_li:
    if p in frequencia:
        frequencia[p]+=1
    else:
        frequencia[p]=1

palavras_or=sorted(frequencia.items(), key=lambda item: item[1], reverse=True)
top_3= palavras_or[:3]





print('*****IMPRESSAO DE RESULTADOS*****')
print(f'Total de frases: {c}')
print(f'Total de palavras: {total_p}')
print('_'*30)
print(f'Palavras mais frequentes:')
for s,f in top_3:
    print(f'{s}: repetida: {f} vezes')

print('_'*30)

