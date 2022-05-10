import tensorflow as tf

dataset = tf.data.Dataset.range(2)


(
dataset
.interleave(  # Parallelize data reading
    dataset_generator_fun,
    num_parallel_calls=tf.data.AUTOTUNE
)
.batch(  # Vectorize your mapped function
    _batch_map_num_items,
    drop_remainder=True)
.map(  # Parallelize map transformation
    time_consuming_map,
    num_parallel_calls=tf.data.AUTOTUNE
)
.cache()  # Cache data
.map(  # Reduce memory usage
    memory_consuming_map,
    num_parallel_calls=tf.data.AUTOTUNE
)
.prefetch(  # Overlap producer and consumer works
    tf.data.AUTOTUNE
)
.unbatch()
)