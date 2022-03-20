perguntas = {
    'Pergunta 1': {
        'pergunta': 'Dicionário são definidos como um(a)...',
        'respostas': { 'A': 'Função', 'B': 'Objeto', 'C': 'Classe', 'D': 'Dado Primitivo' },
        'resposta_certa': 'B'
    },
    'Pergunta 2': {
        'pergunta': 'Qual das alternativas mostram a maneira correta de realizar o cast de uma String para int?',
        'respostas': { 'A': 'Integer.parse("String")', 'B': 'int = "String"', 'C': 'int("String")', 'D': 'Nenhuma das alternativas'},
        'resposta_certa': 'C'
    },
    'Pergunta 3': {
        'pergunta': 'Analise a afirmação a seguir: "É possível realizar a alteração de um elemento em uma tupla"\nEssa afirmação é Verdadeira ou Falsa?',
        'respostas': {'A': 'Verdadeira', 'B': 'Falsa' },
        'resposta_certa': 'B'
    },
    'Pergunta 4': {
        'pergunta': 'Em Python é possível criar uma expressão lambda a partir de qual método?',
        'respostas': { 'A': '(a,b) -> a + b', 'B': 'lambda (a,b) = a + b', 'C': 'lambda (a,b): a + b', 'D': '(a,b): a + b' },
        'resposta_certa': 'C'
    },
    'Pergunta 5':{
        'pergunta': 'Quais são os tipos de estruturas de repetição que existem em Python?',
        'respostas': { 'A': 'while e for', 'B': 'while e do...while', 'C': 'for e do...while', 'D': 'for, while e do...while'},
        'resposta_certa': 'A'
    }
}

print('Bem Vindo ao Quiz sobre Python')
acertos = 0
for keys, values in perguntas.items():
    print(f'{keys} -  {values["pergunta"]}')

    for resp_keys, resp_values in values['respostas'].items():
        print(f'({resp_keys}) - {resp_values}')
    else:
        print()
        resposta_usuario = input('Resposta: ').upper()

    if resposta_usuario == values['resposta_certa']:
        print('Resposta Correta')
        acertos += 1
    else:
        print('Resposta Errada')
    print()

else:
    print(f'Você acertou {acertos}/5')
    if acertos <= 2:
        print('Você precisa estudar mais!')
    elif acertos == 3:
        print('Você foi mediano, ainda precisa estudar mais!')
    elif acertos == 4:
        print('Parabéns, você quase acertou tudo!')
    else:
        print('Parabéns, você acertou todas as questões!\nVocê é um ótimo aluno!')