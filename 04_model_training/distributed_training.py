import tensorflow as tf

try:  # detect TPUs
    tpu = tf.distribute.cluster_resolver.TPUClusterResolver()
    strategy = tf.distribute.TPUStrategy(tpu)
except ValueError:  # detect GPUs
    strategy = tf.distribute.MirroredStrategy()  # for GPU or multi-GPU machines

with strategy.scope():
    model = tf.keras.models.Sequential()  # standard tf.keras code from here

# Global batch size to use in tf.data.Dataset.batch()
# Batches are automatically split between TPU cores.
BATCH_SIZE = 32 * strategy.num_replicas_in_sync

# Good starting point for a learning rate corresponding to new batch size.
# Ideal learning rate for each batch size must be determined by hp-tuning.
LEARNING_RATE = 0.001 * strategy.num_replicas_in_sync

mirrored_strategy = tf.distribute.MirroredStrategy(devices=["/gpu:0", "/gpu:1"])

with mirrored_strategy.scope():
    model = tf.keras.Model(inputs=inputs, outputs=x)
    model.compile(...)
    model.fit(...)
