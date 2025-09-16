# Atividade Prática — Perceptron com Extensões

## Resumo

Esta atividade tem por objetivo implementar e executar exemplos de Perceptron em Python para portas lógicas AND e OR, analisar seu funcionamento, adicionar extensões como um terceiro peso e alterar a função de ativação para step, e versionar o código em um repositório GitHub/GitLab.

## Objetivo

Compreender, de forma aplicada, o funcionamento do Perceptron — um dos modelos mais simples de redes neurais artificiais — por meio da execução, análise e extensão do código em Python, incluindo modificações na função de ativação e adição de pesos.

## 1) Conceito

O Perceptron é um modelo de neurônio artificial. Ele recebe inputs, pesos e bias, calcula uma soma ponderada (inputs·peso + bias) e aplica uma função de ativação (sigmoid ou step), produzindo uma saída binária (0 ou 1). O perceptron foi importante por mostrar que máquinas podem aprender a classificar padrões de acordo com exemplos.

## 2) Funcionamento — classificador linear e limitações

- Classificador linear: o perceptron separa as classes. A decisão é baseada em uma combinação linear das entradas.
- Limitações: Um perceptron só resolve problemas linearmente separáveis, como AND ou OR. A função de ativação step é simples, mas não diferenciável, enquanto sigmoid facilita otimizações.

## 3) Código — etapas principais do treinamento

1. Inicializar pesos e bias (valores aleatórios entre -1 e 1).
2. Para cada epoch (até 100):
   - Para cada exemplo: calcular a saída usando soma ponderada e função de ativação.
   - Calcular o erro: erro = esperado - previsto.
   - Atualizar os pesos: `w_i += taxa_aprendizado * erro * x_i`.
   - Atualizar o bias: bias += taxa_aprendizado * erro.
3. Parar ao atingir número máximo de epochs.

## 4) Extensões Implementadas

- **Adição de terceiro peso:** Implementado em `perceptron2.py` para aceitar 3 entradas, treinando em portas lógicas com 3 bits.
- **Alteração da função de ativação:** Mudança de sigmoid para step implementada em `perceptron2.py`.

## 5) Aplicação real

Sistema para classificação binária em problemas como detecção de padrões em dados de sensores, onde múltiplas entradas influenciam uma decisão binária.

## Descrição do repositório

Este repositório contém implementações de perceptron em Python para portas AND e OR, com variações. O código demonstra a classe Perceptron, métodos de treinamento e predição.

### Arquivos principais

- `perceptron1.py` — implementação básica com 2 pesos, função sigmoid, para portas AND e OR com 2 entradas.
- `perceptron2.py` — implementação com 3 pesos, função step, para portas AND e OR com 3 entradas.

### Trecho ilustrativo do código (perceptron1.py)

```python
class Perceptron:
  def __init__(self):
    self.w1 = np.random.uniform(-1, 1)
    self.w2 = np.random.uniform(-1, 1)
    self.bias = np.random.uniform(-1, 1)

  def treino(self, inputs, outputs, learning_rate=0.1, epochs=100):
    for _ in range(epochs):
      for j in range(len(inputs)):
        soma_ponderada = self.w1 * inputs[j][0] + self.w2 * inputs[j][1] + self.bias
        previsao = 1 / (1 + np.exp(-soma_ponderada))
        erro = outputs[j] - previsao
        self.w1 += learning_rate * erro * inputs[j][0]
        self.w2 += learning_rate * erro * inputs[j][1]
        self.bias += learning_rate * erro
    print("Treinamento concluído!")
    print(f"Pesos finais: w1={self.w1:.2f}, w2={self.w2:.2f}, bias={self.bias:.2f}")

  def predict(self, input_data):
    soma_ponderada = self.w1 * input_data[0] + self.w2 * input_data[1] + self.bias
    previsao_sigmoid = 1 / (1 + np.exp(-soma_ponderada))
    if previsao_sigmoid >= 0.5:
      return 1
    else:
      return 0
```

### Trecho ilustrativo do código (perceptron2.py)

```python
class Perceptron:
  def __init__(self):
    self.w1 = np.random.uniform(-1, 1)
    self.w2 = np.random.uniform(-1, 1)
    self.w3 = np.random.uniform(-1, 1)
    self.bias = np.random.uniform(-1, 1)

  def _funcao_degrau(self, soma_ponderada):
    return 1 if soma_ponderada >= 0 else 0

  def treino(self, inputs, outputs, learning_rate=0.1, epochs=100):
    for _ in range(epochs):
      for j in range(len(inputs)):
        soma_ponderada = (self.w1 * inputs[j][0] +
                          self.w2 * inputs[j][1] +
                          self.w3 * inputs[j][2] +
                          self.bias)
        previsao = self._funcao_degrau(soma_ponderada)
        erro = outputs[j] - previsao
        self.w1 += learning_rate * erro * inputs[j][0]
        self.w2 += learning_rate * erro * inputs[j][1]
        self.w3 += learning_rate * erro * inputs[j][2] 
        self.bias += learning_rate * erro
    print("Treinamento concluído!")
    print(f"Pesos finais: w1={self.w1:.2f}, w2={self.w2:.2f}, w3={self.w3:.2f}, bias={self.bias:.2f}")

  def predict(self, input_data):
    soma_ponderada = (self.w1 * input_data[0] +
                      self.w2 * input_data[1] +
                      self.w3 * input_data[2] +
                      self.bias)
    return self._funcao_degrau(soma_ponderada)
```

### Mudar as epochs faz diferença?

Sim. Mais epochs significam mais atualizações dos pesos e, em geral, maior convergência. Por exemplo, com `10` epochs os pesos podem não ter convergido; com `500` epochs geralmente haverá muito mais estabilidade nas atualizações (dependendo do problema).

Observações rápidas:

- Taxa de aprendizado: uma `learning rate` alta pode causar oscilações mesmo com muitas epochs; uma taxa muito baixa torna a convergência lenta.
- Overfitting (ajuste excessivo): o modelo passa a memorizar ruído ou erros nos dados (dados ruidosos/inconsistentes), reduzindo sua capacidade de generalizar para novos exemplos.

### Diferença entre Step/Sigmoid

- **Step (degrau):** retorna 1 se a soma ponderada >= 0, caso contrário 0. É simples e rápida, indicada para classificadores binários básicos, mas não é diferenciável, o que impede o uso de métodos de otimização baseados em gradiente.

- **Sigmoid:** função contínua que mapeia a soma ponderada para (0, 1) pela fórmula `1/(1+e^{-x})`. É diferenciável, permitindo treinamento por gradiente e atualizações mais suaves dos pesos, mas pode saturar para valores extremos e é ligeiramente mais custosa computacionalmente.

## Notebook interativo (Colab)

Você pode executar uma versão interativa do código no Google Colab: [Abrir no Colab](https://colab.research.google.com/drive/1e4Z64OmyRb-gvcg46zSsJELKHmlZAlA9#scrollTo=CQqnfQ8p5yOs)
