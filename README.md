# automato_DellaMura
trabalho de Introdução à Teoria da Computação

O objetivo deste script é simular o funcionamento de um Autômato Finito. Ele foi projetado para ser uma ferramenta de linha de comando que automatiza o teste de múltiplas palavras, verificando se elas são aceitas ou não por um determinado autômato."

O funcionamento do código pode ser dividido em três etapas principais:
Carregamento e Preparação dos Dados:
Primeiro, o programa lê e interpreta os dois arquivos de entrada. Ele usa a biblioteca json para decodificar o arquivo .aut e carregar as regras do autômato — o estado inicial, os estados finais e todas as transições — para a memória. Em paralelo, ele lê o arquivo .in e cria uma lista com todas as palavras que precisamos testar.

Em segundo lugar, o script entra em um loop, processando cada palavra da lista de testes. Para cada palavra, a função de simulação faz o seguinte:

Ela começa no estado inicial definido pelo autômato.

Lê a palavra, caractere por caractere.

A cada caractere, ela busca na lista de transições uma regra que corresponda ao estado atual e ao caractere lido.

Se uma regra é encontrada, o simulador avança para o próximo estado. Se nenhuma regra é encontrada, a palavra é imediatamente rejeitada.

Ao final da palavra, o script verifica se o estado em que paramos está na lista de estados finais. Se estiver, a palavra é aceita; caso contrário, é rejeitada.

Por fim, para cada palavra testada, o script mede o tempo exato que a simulação levou. Ele então formata uma linha com a palavra original, o resultado que era esperado, o resultado que o nosso simulador obteve e o tempo de execução. Todos esses resultados são escritos no arquivo de saída .out.

