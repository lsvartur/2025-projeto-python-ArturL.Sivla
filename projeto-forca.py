'''
Projeto python: Jogo Forca
Autor: Artur Lacerda da Silva
30/06/2025
'''

import random as rd # Importa o módulo random para escolher palavras aleatoriamente.

def jogo_da_forca(): # Define a função principal do jogo.
    # Exibe as mensagens de boas-vindas do jogo.
    print('\n----x----x---- JOGO DA FORCA ----x----x----')
    print('----- ADIVINHE A PALAVRA SECRETA -----\n') # Mensagem ajustada para refletir a lista de palavras
    
    # Lista de palavras para o jogo.
    lista_palavras = ['QUINA', 'PONTA', 'PROLIXO', 'VOZ', 
                      'UNIAO', 'ANTAGONISTA', 'MORANGO', 'TERCA',
                      'EXIMIO', 'CORRETO', 'FELIZ', 'ASSASSINO'] # Mantendo a lista original
    
    def escolher_palavra(lista): # Função para escolher uma palavra aleatória da lista
        return rd.choice(lista) # Retorna uma palavra escolhida aleatoriamente
    
    def localizar_letras(palavra, letra): # Função para encontrar todas as posições de uma letra na palavra
        # Retorna uma lista com os índices onde a letra aparece
        return [i for i, char in enumerate(palavra) if char == letra]
    
    def exibir_resultado(venceu, palavra_secreta): # Função auxiliar para exibir o resultado final
        if venceu:
            print('\n-------- X -------- X --------') 
            print(f'Parabéns!! A palavra correta é {palavra_secreta}!') 
            print('-------- X -------- X --------') 
        else:
            print('\n-------- X GAME OVER X --------') 
            print(f'A palavra correta era: {palavra_secreta}') 
            print('-------- X -------- X --------') 
    
    # VARIAVEIS DO JOGO:
    palavra_secreta = escolher_palavra(lista_palavras) # A palavra a ser adivinhada
    pal_secreta = ['_'] * len(palavra_secreta) 
    erros_cometidos = 0 # Contador de erros cometidos.
    max_erros = 6 # Número máximo de erros permitidos (comum no jogo da forca)
    letras_erradas = [] # Lista pra armazenar as letras erradas
    
    # Exibe uma dica sobre o número de letras da palavra
    print(f'DICA: A palavra tem {len(palavra_secreta)} letras\n')
    
    # Loop principal do jogo, continua enquanto houver erros_cometidos e a palavra não for adivinhada
    while erros_cometidos < max_erros: 
        # Mostra os erros restantes e o estado atual da palavra
        print(f'Erros restantes: {max_erros - erros_cometidos}') 
        print('Palavra: ' + ' '.join(pal_secreta))
        # Exibe as letras erradas já tentadas, se houver
        if letras_erradas:
            print(f'Letras erradas: {", ".join(letras_erradas)}\n')
        else:
            print() # Apenas uma linha em branco para manter o espaçamento
        
        letra = input('Digite uma letra (ou "sair" para encerrar): ').upper() # Pede uma letra ao jogador
        
        # Verifica se o jogador quer sair do jogo.
        if letra == 'SAIR':
            print('\nVocê saiu do jogo. Até a próxima!')
            break # Encerra o loop e o jogo
        
        # verifica se é uma única letra.
        if len(letra) != 1 or not letra.isalpha(): 
            print('Por favor, digite apenas UMA letra válida.\n') 
            continue # Volta para o início do loop.

        # Verifica se a letra já foi tentada.
        if letra in pal_secreta or letra in letras_erradas:
            print(f'Você já tentou a letra "{letra}". Tente outra.\n')
            continue # Volta para o início do loop sem perder uma chance.
            
        # Verifica se a letra está na palavra.
        if letra in palavra_secreta: 
            posicoes = localizar_letras(palavra_secreta, letra) # Encontra as posições da letra
            for pos in posicoes: # Preenche as letras corretas na palavra visível
                pal_secreta[pos] = letra 
            print(f'\nAcertou! A letra {letra} está na palavra.') # Mensagem de acerto
        else: # Se a letra não estiver na palavra.
            print(f'\nErrou! A letra {letra} não está na palavra.') # Mensagem de erro
            erros_cometidos += 1 # Incrementa erros_cometidos apenas em caso de erro
            letras_erradas.append(letra) # Adiciona a letra à lista de letras erradas
            
        print('\n' + ' '.join(pal_secreta) + '\n') # Exibe a palavra atualizada
        
        # Verifica se o jogador venceu (todas as letras foram adivinhadas)
        if '_' not in pal_secreta: 
            exibir_resultado(True, palavra_secreta)
            break # Encerra o jogo quando o jogador ganha
            
        # Opção para o jogador tentar adivinhar a palavra inteira.
        opcao = input('Quer tentar adivinhar a palavra? (S/N): ').upper() 
        if opcao == 'S': # Se o jogador optar por tentar.
            tentativa = input('Digite a palavra: ').upper() # Pede a tentativa da palavra.
            if tentativa == palavra_secreta: # Verifica se a tentativa está correta.
                exibir_resultado(True, palavra_secreta)
                break # Encerra o jogo por vitória.
            else: # Se a tentativa estiver incorreta.
                print('\nErrou! Continue tentando as letras...\n') 
                # Você pode optar por adicionar: erros_cometidos += 1 aqui se quiser que errar a palavra inteira conte como um erro.
    
    # Verifica se o jogo terminou por Game Over (erros esgotados) e ainda não acertou a palavra.
    if '_' in pal_secreta and erros_cometidos >= max_erros: 
        exibir_resultado(False, palavra_secreta)

jogo_da_forca() # Inicia o jogo chamando a função principal.