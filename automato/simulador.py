import json
import sys
import time

def carregar_automato(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Erro: O arquivo do autômato '{caminho_arquivo}' não foi encontrado.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não é um JSON válido.")
        sys.exit(1)

def carregar_entradas(caminho_arquivo):
    entradas = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            for linha in f:
                linha_limpa = linha.strip()
                if linha_limpa:
                    partes = linha_limpa.split(';')
                    if len(partes) == 2:
                        entradas.append((partes[0], partes[1]))
    except FileNotFoundError:
        print(f"Erro: O arquivo de entradas '{caminho_arquivo}' não foi encontrado.")
        sys.exit(1)
    return entradas

def simular_automato(automato, palavra):
    estado_inicial = automato.get("initial")
    estados_finais = automato.get("final", [])
    transicoes = automato.get("transitions", [])

    if estado_inicial is None:
        print("Erro: Estado inicial não definido no autômato.")
        return 0

    mapa_transicoes = {}
    for t in transicoes:
        estado_de = str(t["from"])
        simbolo = t["read"]
        if estado_de not in mapa_transicoes:
            mapa_transicoes[estado_de] = {}
        mapa_transicoes[estado_de][simbolo] = str(t["to"])

    estado_atual = str(estado_inicial)

    for simbolo in palavra:
        if estado_atual in mapa_transicoes and simbolo in mapa_transicoes[estado_atual]:
            estado_atual = mapa_transicoes[estado_atual][simbolo]
        else:
            return 0

    if int(estado_atual) in estados_finais:
        return 1
    else:
        return 0

def main():
    if len(sys.argv) != 4:
        print("Uso: python simulador.py <arquivo_do_automato.aut> <arquivo_de_testes.in> <arquivo_de_saida.out>")
        sys.exit(1)

    caminho_automato = sys.argv[1]
    caminho_entradas = sys.argv[2]
    caminho_saida = sys.argv[3]

    automato = carregar_automato(caminho_automato)
    casos_de_teste = carregar_entradas(caminho_entradas)

    resultados = []

    for palavra, resultado_esperado in casos_de_teste:
        tempo_inicio = time.perf_counter()
        resultado_obtido = simular_automato(automato, palavra)
        tempo_fim = time.perf_counter()
        
        tempo_execucao = tempo_fim - tempo_inicio
        
        linha_resultado = f"{palavra};{resultado_esperado};{resultado_obtido};{tempo_execucao:.7f}"
        resultados.append(linha_resultado)

    try:
        with open(caminho_saida, 'w', encoding='utf-8') as f:
            f.write("\n".join(resultados))
        print(f"Simulação concluída. Resultados salvos em '{caminho_saida}'.")
    except IOError:
        print(f"Erro: Não foi possível escrever no arquivo de saída '{caminho_saida}'.")
        sys.exit(1)


if __name__ == "__main__":
    main()