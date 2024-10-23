import keras
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.losses import SparseCategoricalCrossentropy
from keras.optimizers import Adam

mnist = keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = keras.utils.normalize(x_train, axis=1)
x_test = keras.utils.normalize(x_test, axis=1)

model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(50, activation='relu'),
    Dense(25, activation='relu'),
    Dense(10, activation='linear')
    
])

model.compile(
    loss = SparseCategoricalCrossentropy(from_logits=True),
    optimizer = Adam(learning_rate=0.01),
    metrics=['accuracy']
)

model.fit(x_train, y_train, epochs=100)

model.save('handwritten.model')

loss,accuracy = model.evaluate(x_test, y_test)
print(loss)
print(accuracy)
