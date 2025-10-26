## Testes de Algoritmos — Estrutura de Dados

> Repositório com pequenos scripts para demonstrar e comparar algoritmos básicos estudados na disciplina de Estrutura de Dados.

Conteúdo
- `01.py` — compara desempenho de buscas (busca linear e busca binária) com plots.
- `02.py` — compara desempenho das implementações de Fibonacci (recursiva vs iterativa) com plots.
- `fibonachi.py` — exemplos simples das funções Fibonacci (recursiva e iterativa) e impressão do valor para n=10.
- `busca_linear.py` — implementação da função `busca_linear(lista, elemento)`.
- `busca_binaria.py` — implementação da função `busca_binaria(lista, elemento)`.

Requisitos
- Python 3.8+ (qualquer versão moderna do Python 3 serve)
- Bibliotecas Python:
  - numpy
  - matplotlib

Instalação rápida (PowerShell):

# Instalar dependências
pip install numpy matplotlib
```

Como executar
- Executar o script de buscas (gera um gráfico comparando tempos):

```powershell
python 01.py
```

- Executar o script de Fibonacci comparativo (gera um gráfico comparando tempos):

```powershell
python 02.py
```

- Executar o exemplo simples de Fibonacci (imprime valores no console):

```powershell
python fibonachi.py
```

Observações
- Os arquivos `busca_linear.py` e `busca_binaria.py` contêm apenas as definições das funções; são usados por `01.py` (que contém os testes e plots). Você também pode importar essas funções em outros scripts para testes unitários.
- A implementação recursiva de Fibonacci cresce exponencialmente em tempo — para n maiores que ~30 pode demorar bastante. Use a versão iterativa (`fibonacci_int` / `Fibonacci_int`) para n grandes.
- Os gráficos usam escala logarítmica no eixo Y para facilitar a comparação entre tempos pequenos e grandes.

