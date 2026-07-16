import random
import os  # Biblioteca necessária para interagir com o sistema operativo (limpar terminal)

# Lista de desenhos da forca (do índice 0 ao 6, correspondendo aos erros)
ESTÁGIOS_FORCA = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

palavras = ['piersica', 'strur', 'mar', 'libenitza', 'pepene', 'lemaie', 'supa', 'para', 'capchun','ape','latte','puine','oua']
palavra_random = random.choice(palavras)
letras_descobertas = ['_'] * len(palavra_random)

tentativas = 6
letras_tentadas = []
mensagem_feedback = "" 


while tentativas > 0 and '_' in letras_descobertas:
    # --- FUNÇÃO PARA LIMPAR O TERMINAL ---
    # No Windows usa 'cls', no Mac/Linux usa 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
    erros = 6 - tentativas
    print(ESTÁGIOS_FORCA[erros])
    
    # 2. Mostra as informações do jogo limpas
    print('Palavra: ' + ' '.join(letras_descobertas))
    print(f'Tentativas restantes: {tentativas}')
    print(f'Letras já tentadas: {letras_tentadas}')
    
    # 3. Exibe o feedback da jogada anterior (se acertou ou errou)
    if mensagem_feedback:
        print(f"\n-> {mensagem_feedback}")
        mensagem_feedback = "" # Limpa a mensagem para a próxima rodada

    palpite = input('\nDigite uma letra: ').lower().strip()

    if len(palpite) > 1 or not palpite.isalpha():
        mensagem_feedback = 'Apenas podes pôr uma letra válida!'
        continue
        
    if palpite in letras_tentadas:
        mensagem_feedback = 'Esta letra já foi tentada!'
        continue

    letras_tentadas.append(palpite)

    if palpite in palavra_random:
        mensagem_feedback = f'Acertaste numa letra! ({palpite})'
        for x, letra in enumerate(palavra_random):
            if palpite == letra:
                letras_descobertas[x] = palpite
    else:
        mensagem_feedback = f'Erraste, "{palpite}" não está na palavra.'
        tentativas -= 1


os.system('cls' if os.name == 'nt' else 'clear')

if '_' not in letras_descobertas:
    print(ESTÁGIOS_FORCA[6 - tentativas]) # Desenha o estado final
    print(f'Ganhaste o jogo, acertaste na palavra {palavra_random}!!!! :)\n')
else:
    print(ESTÁGIOS_FORCA[6]) # Desenha o boneco enforcado completo
    print(f'Que pena, perdeste o jogo :(, a palavra era {palavra_random}\n')