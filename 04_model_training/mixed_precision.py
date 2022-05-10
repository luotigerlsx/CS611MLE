
import tensorflow as tf


layers = tf.keras.layers
mixed_precision = tf.keras.mixed_precision

mixed_precision.set_global_policy('mixed_float16')

inputs = tf.keras.Input(shape=(784,), name='digits')
dense1 = layers.Dense(4096, activation='relu', name='dense_1')
x = dense1(inputs)
dense2 = layers.Dense(4096, activation='relu', name='dense_2')
x = dense2(x)

print('x.dtype: %s' % x.dtype.name)
print(dense1.dtype_policy)
# 'kernel' is dense1's variable
print('dense1.kernel.dtype: %s' % dense1.kernel.dtype.name)

x = layers.Dense(10, name='dense_logits')(x)
outputs = layers.Activation('softmax', dtype='float32', name='predictions')(x)
print('Outputs dtype: %s' % outputs.dtype.name)


loss_scale = 1024
loss = model(inputs)
loss *= loss_scale
# Assume `grads` are float32. You do not want to divide float16 gradients.
grads = compute_gradient(loss, model.trainable_variables)
grads /= loss_scale
