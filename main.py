import random
import hangman_words_list
import art

chosen_word=random.choice(hangman_words_list.word_list)
blank_list=[]
guessed_letters=[]
live=6
for letter in chosen_word:
  blank_list.append("_")
print(art.logo)
print(*blank_list , sep = " ")
end_game= False
while not end_game:
  chosen_letter= input('Guess A letter:\n').lower()
  if chosen_letter<='z' and chosen_letter>='a':
    if chosen_letter in guessed_letters:
      print("you already guessed this letter try another one")
      continue
    else:
      guessed_letters.append(chosen_letter)
    if chosen_letter in chosen_word:
      for i in range(0, len(chosen_word)):
        if chosen_word[i]==chosen_letter:
          blank_list[i]=chosen_letter
          
      print(*blank_list , sep = " ")
      print(art.stages[live])
    
    else: 
      print('chosen letter "'+ chosen_letter + '" is not in the given word you loose a life')
      print(*blank_list , sep = " ")
      live-=1
      print(art.stages[live])
      
      
      if live==0 :
        print('You Loose!! Game Over\ncorrect word is: '+ chosen_word)
        end_game=True
        
    
    if not '_' in blank_list:
      print('Congratulations You Won 🥳🥳🥳🥳')
      end_game=True
  
  else: 
    print('letter choosen is invalid please choose again')