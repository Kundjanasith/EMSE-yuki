import tensorflow as tf
import keras

sbt = open('data/sbt.txt','r').readlines()
caller_method = open('data/caller_method.txt','r').readlines()
method_name = open('data/method_name.txt','r').readlines()

max_len = 200
rnn_cell_size = 128
vocab_size=250

class Attention(tf.keras.Model):
    def __init__(self, units):
        super(Attention, self).__init__()
        self.W1 = tf.keras.layers.Dense(units)
        self.W2 = tf.keras.layers.Dense(units)
        self.V = tf.keras.layers.Dense(1)
    def call(self, features, hidden):
        hidden_with_time_axis = tf.expand_dims(hidden, 1)
        score = tf.nn.tanh(self.W1(features) + self.W2(hidden_with_time_axis))
        attention_weights = tf.nn.softmax(self.V(score), axis=1)
        context_vector = attention_weights * features
        context_vector = tf.reduce_sum(context_vector, axis=1)
        return context_vector, attention_weights

sequence_input = tf.keras.layers.Input(shape=(max_len,), dtype='int32')
embedded_sequences = tf.keras.layers.Embedding(vocab_size, 128, input_length=max_len)(sequence_input)
lstm = tf.keras.layers.Bidirectional(tf.keras.layers.LSTM
                                     (rnn_cell_size,
                                      dropout=0.3,
                                      return_sequences=True,
                                      return_state=True,
                                      recurrent_activation='relu',
                                      recurrent_initializer='glorot_uniform'), name="bi_lstm_0")(embedded_sequences)
lstm, forward_h, forward_c, backward_h, backward_c = tf.keras.layers.Bidirectional \
    (tf.keras.layers.LSTM
     (rnn_cell_size,
      dropout=0.2,
      return_sequences=True,
      return_state=True,
      recurrent_activation='relu',
      recurrent_initializer='glorot_uniform'))(lstm)
state_h = tf.keras.layers.Concatenate()([forward_h, backward_h])
state_c = tf.keras.layers.Concatenate()([forward_c, backward_c])

#  PROBLEM IN THIS LINE
context_vector, attention_weights = Attention(32)(lstm, state_h)
output = keras.layers.Dense(1, activation='sigmoid')(context_vector)
model = keras.Model(inputs=sequence_input, outputs=output)

# summarize layers
# print(model.summary())

print(model.input_shape)
print(model.output_shape)
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
