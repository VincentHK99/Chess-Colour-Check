import pandas as pd
import random
import time

numbers = [1,2,3,4,5,6,7,8]
letters = ['a','b','c','d','e','f','g','h']

squares = []
num_list = [1,3,5,7]
colours=[]
for number in numbers:
  if number in num_list:
    colours.append(['b','w','b','w','b','w','b','w'])
  else:
    colours.append(['w','b','w','b','w','b','w','b'])
  for letter in letters:
    squares.append(letter + str(number))

quadrants = ['q1','q1','q1','q1','q2','q2','q2','q2',
             'q1','q1','q1','q1','q2','q2','q2','q2',
             'q1','q1','q1','q1','q2','q2','q2','q2',
             'q1','q1','q1','q1','q2','q2','q2','q2',
             'q3','q3','q3','q3','q4','q4','q4','q4',
             'q3','q3','q3','q3','q4','q4','q4','q4',
             'q3','q3','q3','q3','q4','q4','q4','q4',
             'q3','q3','q3','q3','q4','q4','q4','q4',]


colours_flattened=[]

for sublist in colours:
  for i in sublist:
    colours_flattened.append(i)


chess_dict = {'square':squares,'colour':colours_flattened,'quadrants':quadrants}
chess_df = pd.DataFrame(chess_dict)


start = time.time()
test_length = range(int(input('¿Cuantos preguntas quieres?')))
select_quad = input('¿Qué cuadrante quieres que te evalúen?')
chess_df = chess_df[chess_df['quadrants']==select_quad].reset_index()
number_correct=0
for i in test_length:
  random_square = chess_df.iloc[random.randint(0,15)]
  my_answer = input('¿De qué color es ' + random_square.square  + '? ')
  correct_answer = random_square.colour
  if my_answer == correct_answer:
    number_correct +=1
    print("¡Correcto!")
    print('¡Tienes ' + str(number_correct) +' preguntas correctas!')
  else:
    print('Incorrecto :(')
    print('Próxima pregunta...')

end = time.time()
perc_correct = number_correct / len(test_length) *100
print('¡Tienes ' + str(perc_correct)+'% de las preguntas correctas en ' + str(round(end-start)) +' segundos!')
print('¡Uno respuesta correcto cada ' + str(round((end-start)/number_correct)) + ' segundos!')
