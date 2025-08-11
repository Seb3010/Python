#importamos NumPy para manejar
#calculos de matrices y vectores
import numpy as np

#definimos una clase llamada Neuron
#representara una neurona artificial
class Neuron:

    #metodo que inicializa la neurona con un numero de entradas 
    def __init__(self, num_inputs):
        #creamos pesos aleatorios para cada entrada (entre 0 y 1)
        self.weights = np.random.rand(num_inputs)
        #añadimos un sesgo aleatorio (un solo valor para ajustar la salida)
        self.bias = np.random.rand()
        #inicializamos la salida en 0 (se actualizara despues)
        self.output = 0
        #almacenamos las entradas para usarlas despues si es necesario
        self.input = None
        #creamos un array de ceros para almacenar los cambios en los pesos
        self.dweights = np.zeros_like(self.weights)
        #inicializamos el cambio en el sesgo a 0 (se actualizara durante el entrenamiento)
        self.dbias = 0

    #metodo que define la funcion de activacion (sigmoide)
    #la sigmoide convierte cualquier numero en un valor entre 0 y 1
    #esto ayuda a que la neurona decida si activarse o no
    def activate(self, x):
        #formula de la sigmoide
        #sigmoide: 1 / (1 + e^(-x))
        return 1 / (1 + np.exp(-x))

    #metodo que calcula la derivada de la sigmoide
    #la derivada se usa para ajustar los pesos durante el entrenamiento
    def derivate_activate(self, x):
        #primero calculamos la salida de la sigmoide
        activated = self.activate(x)
        #formula de la derivada de la sigmoide
        #la derivada de la sigmoide es: sigmoide * (1 - sigmoide)
        return activated * (1 - activated)

    #metodo que calcula la salida de la neurona
    #"inputs" es un array con los valores de entrada (datos que le damos)
    def forward(self, inputs):
        #guardamos las entradas para usarlas despues si es necesario
        self.input = inputs
        #np.dot multiplica las entradas por los pesos y los suma
        #a esto le sumamos el sesgo para ajustar el resultado
        self.output = self.activate(np.dot(inputs, self.weights) + self.bias)
        #devolvemos la salida despues de activar aplicar la activacion
        return self.output

    #metodo para entrenar la neurona
    #"inputs" son los datos de entrada 
    #"target" es el valor que queremos predecir
    #"learning_rate" controla que tan rapido se ajustan los pesos
    def train(self, inputs, target, learning_rate=0.1):
        #forward pass: calculamos la salida
        output = self.forward(inputs)
        #calculamos el error: diferencia entre el valor esperado (target) y la salida
        error = target - output
        #calculamos el ajuste usando la derivada de la funcion de activacion
        total_input = np.dot(inputs, self.weights) + self.bias
        #backpropagation: ajustamos los pesos segun el error
        #adjustment: usa la derivada para saber como cambiar los pesos
        adjustment = error * self.derivate_activate(total_input)
        #calculamos el cambio en los pesos usando las entradas guardadas
        self.dweights = learning_rate * adjustment * self.input
        #actualizamos los pesos sumando el cambio
        self.weights += self.dweights
        #calculamos el cambio en el sesgo
        self.dbias = learning_rate * adjustment
        #actualizamos el sesgo sumando el cambio
        self.bias += self.dbias

        #devolvemos el error para ver como mejora el modelo
        return error

#definimos una clase de capa
class Layer:
    #metodo que inicializa la capa 
    def __init__(self, num_inputs, num_neurons):
        # Creamos una lista de neuronas llamada "neurons" que contiene "num_neurons" objetos de la clase Neuron
        #cada neurona se inicializa con "num_inputs_per_neuron" entradas (pesos)
        self.neurons = [Neuron(num_inputs) for _ in range(num_neurons)]
    #metodo que calcula la salida de la capa
    def forward(self, inputs):
        #esta funcion envia las mismas entradas a cada neurona de la capa
        #usamos una lista por compresion para llamar al metodo "forward" de cada neurona
        #cada neurona calcula su salida de forma independiente
        outputs = [neuron.forward(inputs) for neuron in self.neurons]
        #convertimos la lista de salidas en un array de numpy para facilitar posteriores
        return np.array(outputs)

    #metodo que entrena la capa
    def train(self, inputs, targets, learning_rate=0.1):
        #esta funcion entrena cada neurona de la capa
        #"inputs" son las entradas comunes para todas las neuronas
        #"targets" son los valores que queremos predecir para cada neurona
        errors = [] #aqui guardamos el error de cada neurona
        #iteramos simultaneamente sobre las neuronas y su target correspondiente
        for neuron, target in zip(self.neurons, targets):
            #entrenamos la neurona con los inputs y su target
            error = neuron.train(inputs, target, learning_rate)
            #guardamos el error de la neurona
            errors.append(error)
            #devolvemos los errores como un array para poder analizarlos facilmente
        return np.array(errors)

#ejemplo de uso
#esto se ejecuta si corremos este archivo directamente
if __name__ == "__main__":
    #creamos una neurona con 4 entradas (puedes cambiar el numero)
    neuron = Neuron(4)
    #definimos un ejemplo de entradas (cuatro valores)
    inputs = np.array([0.2, 0.5, 0.1, 0.9])
    #este es el valor que queremos predecir
    target = 1

    #parametros  para el learning rate dinamico
    initial_lr = 0.1    #learning rate inicial
    decay_rate = 1e-8   #tasa a la que se reduce el learning rate cada iteracion
    
    #entrenamos la neurona por 100000 iteraciones
    #el "_" se usa cuando no necesitamos el valor de la iteracion
    for _ in range(100_000_000):   
        #llamamos al metodo train
        error = neuron.train(inputs, target)
        #cada 10000 iteraciones mostramos el error
        if _ % 1_000_000 == 0:
            #mostramos el error
            print(f"Error en la iteracion {_}: {error}")
    #mostramos los resultados finales
    print(f"Pesos finales: {neuron.weights}, Sesgo: {neuron.bias}, Salida: {neuron.forward(inputs)}")