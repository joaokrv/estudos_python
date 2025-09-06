
# Atividade Prática — Perceptron

## Resumo
Esta atividade tem por objetivo reproduzir e executar um exemplo simples de Perceptron em Python, analisar seu funcionamento e versionar o código em um repositório GitHub/GitLab.

## Checklist de requisitos
- [ ] Baixar o código disponibilizado no PDF do professor.
- [ ] Reproduzir o código e garantir que execute em Python.
- [ ] Versionar o código no seu repositório GitHub (ou GitLab).
- [ ] Postar o link do repositório no ULife até 07/09/2025 23:59.

## Objetivo
Compreender, de forma aplicada, o funcionamento do Perceptron — um dos modelos mais simples de redes neurais artificiais — por meio da execução e análise do código em Python.

## 1) Conceito
O Perceptron é um modelo de neurônio artificial. Ele recebe inputs, pesos e bias, calcula uma soma ponderada (inputs·peso + bias) e aplica uma função de ativação do tipo step, produzindo uma saída binária (0 ou 1). O perceptron foi importante por mostrar que máquinas podem aprender a classificar padrões de acordo com exemplos, algoritmos, dados.

## 2) Funcionamento — classificador linear e limitações
- Classificador linear: o perceptron separa as classes. A decisão é baseada em uma combinação linear das entradas.
- Limitações: Um perceptron só resolve problemas linearmente separáveis, ou seja AND ou OR. Outra limitação é a função de ativação step, por não ser diferenciável, dificultando otimizações.

## 3) Código — etapas principais do treinamento
1. Inicializar pesos e bias (valores pequenos aleatórios ou zero).
2. Para cada epochs (ou até convergir):
   - Para cada exemplo: calcular a saída usando a soma ponderada e a função de ativação.
   - Calcular o erro: erro = valor esperado - valor previsto.
   - Atualizar os pesos: w_i <- w_i + taxa_aprendizado * erro * x_i.
   - Atualizar o bias: bias <- bias + taxa_aprendizado * erro.
3. Parar ao atingir número máximo de epochs ou quando o erro total for aceitável.

## 4) Aplicação real
Sistema embarcado para detecção de condições de alarme que utiliza duas "variáveis" (temperatura e presença). Se a combinação linear dessas leituras ultrapassar um limiar, o sistema ativa um alarme (0 = desligado, 1 = ligado).

## Descrição do repositório
Este repositório contém um exemplo de perceptron implementado em Python. O código demonstra funções para calcular a entrada (soma ponderada) e a saída (função degrau) do perceptron.

### Arquivos principais
- `Ativdade_05-09/main.py` — exemplo com `perceptron_input` e `perceptron_output`.

### Trecho ilustrativo do código

```python
def perceptron_input(inputs, weights, bias):
	"""Calcula a soma ponderada das entradas e adiciona o bias."""
	weighted_sum = sum(i * w for i, w in zip(inputs, weights))
	return weighted_sum + bias

def perceptron_output(inputs, weights, bias):
	"""Retorna 1 se soma ponderada + bias >= 0, caso contrário 0."""
	return 1 if perceptron_input(inputs, weights, bias) >= 0 else 0

def main():
	print("Hello, World!")
	print("This is the main file.")
	print("The result of the perceptron input is:", perceptron_input([1, 2, 3], [0.1, 0.2, 0.3], 0.4))

if __name__ == "__main__":
	main()
```

## Como executar
No Windows PowerShell com Python 3 instalado, rode:

```pwsh
python Ativdade_05-09/main.py
```

Se preferir, crie um ambiente virtual e instale dependências (não obrigatórias para este exemplo simples):

```pwsh
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

## Como versionar no GitHub (passos rápidos)
1. Inicialize o repositório local (se ainda não):

```pwsh
git init
git add .
git commit -m "Adiciona exemplo de Perceptron"
```

2. Crie o repositório remoto no GitHub/GitLab e faça o push:

```pwsh
git remote add origin <URL_DO_REPOSITORIO>
git branch -M main
git push -u origin main
```

3. Copie o link e poste no ULife antes do prazo.

## Licença
MIT

---

*README gerado com base na atividade prática de Perceptron para a disciplina de Inteligência Artificial.*

