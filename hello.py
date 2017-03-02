import tensorflow as tf

#hello = tf.constant('Hello, TensorFlow!!!!!')

a = tf.placeholder("float")
b = tf.placeholder("float")

y = tf.multiply(a, b)

sess = tf.Session()

#print(sess.run(hello))
print(sess.run(y, feed_dict={a: 3, b: 3}))
