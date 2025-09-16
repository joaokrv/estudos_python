import numpy as np

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

inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
outputs = np.array([0, 0, 0, 1])

p = Perceptron()
print(f"Pesos iniciais: w1={p.w1:.2f}, w2={p.w2:.2f}, bias={p.bias:.2f}")

p.treino(inputs, outputs, epochs=100)

print("\n--- Testando o Perceptron AND ---")
print(f"Previsão para [0, 0]: {p.predict([0, 0])} (Esperado: {outputs[0]})")
print(f"Previsão para [0, 1]: {p.predict([0, 1])} (Esperado: {outputs[1]})")
print(f"Previsão para [1, 0]: {p.predict([1, 0])} (Esperado: {outputs[2]})")
print(f"Previsão para [1, 1]: {p.predict([1, 1])} (Esperado: {outputs[3]})")
print("\n")


inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]]) # entrada
outputs = np.array([0, 0, 0, 1]) # saída esperada

print(f"Pesos iniciais: w1={p.w1:.2f}, w2={p.w2:.2f}, bias={p.bias:.2f}")

p.treino(inputs, outputs, epochs=100)

print("\n--- Testando o Perceptron OR ---")
print(f"Previsão para [0, 0]: {p.predict([0, 0])} (Esperado: {outputs[0]})")
print(f"Previsão para [0, 1]: {p.predict([0, 1])} (Esperado: {outputs[1]})")
print(f"Previsão para [1, 0]: {p.predict([1, 0])} (Esperado: {outputs[2]})")
print(f"Previsão para [1, 1]: {p.predict([1, 1])} (Esperado: {outputs[3]})")