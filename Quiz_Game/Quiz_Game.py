print("Let's play a quiz game X)")

play = input('Play or Not ? ')

if play.lower() != 'yes':
    print('LEE')
    quit()

print('YAY!!!!!')
score = 0


answer = input("What does CPU stand for ? ")
if answer.lower() == "central processing unit":
    print('CORRECT!!!!!')
    score+=1
else:
    print("BOOOOOOOO!!!!!!!!")


answer = input("What does GPU stand for ? ")
if answer.lower() == "graphics processing unit":
    print('GREAT!!!!!')
    score+=1
else:
    print("TRY AGAIN!!!!!!!!")


answer = input("What does PSU stand for ? ")
if answer.lower() == "power supply":
    print('FANTASTIC!!!!!')
    score+=1
else:
    print("SORRY!!!!!!!!")


answer = input("How much bandwith does port Gi0/1 have ? ")
if answer.lower() == "1 GBPS":
    print('NICE!!!!!')
    score+=1
else:
    print("SHAWWWWWW!!!!!!!!")


answer = input("What is the alternative name for layer 3 switch ? ")
if answer.lower() == "multi layer switch":
    print('GREAT!!!!!')
    score+=1
else:
    print("GOODNESS GRACIOUS!!!!!!!!")

print('You got '+ str(score) + " questions correct")
print("You got " + str((score/4)*100) + "%")
