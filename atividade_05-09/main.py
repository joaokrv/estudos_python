def main():
    print("Hello, World!")
    print("This is the main file.")
    print("The result of the perceptron input is: ", perceptron_input([1, 2, 3], [0.1, 0.2, 0.3], 0.4))
    
def perceptron_input(inputs, weights, bias):
    """
    Calculo do input perceptron.
    :param inputs: Lista de valores input 
    :param weights: Lista de weights correspondentes para os inputs
    :param bias: Valor bias
    :return: A soma dos inputs ponderados mais o bias
    """
    weighted_sum = sum(i * w for i, w in zip(inputs, weights))
    return weighted_sum + bias

def perceptron_output(inputs, weights, bias):
    """
    Calculo do output perceptron.
    :param inputs: List of input values
    :param weights: List of weights corresponding to the inputs
    :param bias: Bias value
    :return: The output of the perceptron
    """
    return 1 if perceptron_input(inputs, weights, bias) >= 0 else 0

if __name__ == "__main__":
 main()