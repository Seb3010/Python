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
        #backpropagation: ajustamos los pesos segun el error
        #adjustment: usa la derivada para saber como cambiar los pesos
        adjustment = error * self.derivate_activate(np.dot(inputs, self.weights) + self.bias)
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

#ejomplo de uso
#esto se ejecuta si corremos este archivo directamente
if __name__ == "__main__":
    #creamos una neurona con 2 entradas (puedes cambiar el numero)
    neuron = Neuron(2)
    #definimos un ejemplo de entradas (dos valores)
    inputs = np.array([0.5, 0.8])
    #este es el valor que queremos predecir
    target = 1
    #entrenamos la neurona por 100 iteraciones
    #el "_" se usa cuando no necesitamos el valor de la iteracion
    for _ in range(100):
        #llamamos al metodo train
        error = neuron.train(inputs, target)
        #cada 10 iteraciones mostramos el error
        if _ % 10 == 0:
            #mostramos el error
            print(f"Error en la iteracion {_}: {error}")
    #mostramos los resultados finales
    print(f"Pesos finales: {neuron.weights}, Sesgo: {neuron.bias}, Salida: {neuron.forward(inputs)}")