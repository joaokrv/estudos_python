# Desafios:
# - Alterar função de ativação de sigmoid para step/degrau
# - Adicionar mais um peso(entrada)

import numpy as np

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

inputs = np.array([
    [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1],
    [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]
])

print("--- Iniciando Treinamento para Porta Lógica AND ---")
outputs_and = np.array([0, 0, 0, 0, 0, 0, 0, 1])

p_and = Perceptron()
print(f"Pesos iniciais (AND): w1={p_and.w1:.2f}, w2={p_and.w2:.2f}, w3={p_and.w3:.2f}, bias={p_and.bias:.2f}")

p_and.treino(inputs, outputs_and, epochs=100)

print("\n--- Testando o Perceptron AND ---")
for i in range(len(inputs)):
    # Usando list() para a formatação limpa da saída
    print(f"Previsão para {list(inputs[i])}: {p_and.predict(inputs[i])} (Esperado: {outputs_and[i]})")

print("\n\n--- Iniciando Treinamento para Porta Lógica OR ---")
outputs_or = np.array([0, 1, 1, 1, 1, 1, 1, 1])

p_or = Perceptron()
print(f"Pesos iniciais (OR): w1={p_or.w1:.2f}, w2={p_or.w2:.2f}, w3={p_or.w3:.2f}, bias={p_or.bias:.2f}")

p_or.treino(inputs, outputs_or, epochs=100)

print("\n--- Testando o Perceptron OR ---")
for i in range(len(inputs)):
    print(f"Previsão para {list(inputs[i])}: {p_or.predict(inputs[i])} (Esperado: {outputs_or[i]})")