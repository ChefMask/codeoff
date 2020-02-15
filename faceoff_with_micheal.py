#score converter created on 15 Feb 2020 by 4:16 A.M GMT+1
score = input("What is your score?")
score = int(score)
if score > 100:
    print ("Invalid score... You can't be that brilliant")

elif score >= 70:
    print ("Your grade is A")

    if score >= 80 and score <= 100:
        print ("Fantastic job.But try and get a social life...Trust me you won't regret it")
     

elif 60<= score and score < 70:
    print ("Your grade is B")

elif 50<= score and score < 60:
    print ("Your grade is C")

elif 45<= score and score < 50:
    print ("Your grade is D")

elif 40<= score and score < 45:
#Shout to Unilag lecturers that will upgrade by 10 and you would still get 7 over 100. 
    print ("Your grade is E. You know you most likely got upgraded to this grade, right? ")
    

elif score < 40:
    print ("Your grade is F. Don't sweat it,it just means that your best wasn't enough, which is OK, unless your school fees are over One mil...Then you are in some real shit")
