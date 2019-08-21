from Quiz import Quiz

questions_answers = [

   [ "What year Mr.  Blare become the PM\n a) 1997 \n b) 2010 ", "a"],
   ["What year Mr.  Blare become the PM\n a) 1997 \n b) 2010 ", "a"],
   ["What year Mr.  Blare become the PM\n a) 1997 \n b) 2010 ", "a"],
   ["What year Mr.  Blare become the PM\n a) 1997 \n b) 2010 ", "a"],
   ["What year Mr.  Blare become the PM\n a) 1997 \n b) 2010 ", "a"]

]

round = []

for i in range(len(questions_answers)):
    entry = Quiz("","")
    for j in range(len(questions_answers[i])):
        entry.promt = questions_answers[i][0]
        entry.answer = questions_answers[i][1]
    round.append(entry)


score = 0
# e2c160dd0b490bc4213ea21afcf1de93b92bd027
for i in range(len(round)):
    print(round[i].promt)
    given_answer = input("\n\n please select :     ")
    if given_answer == round[i].answer:
        score += 1

print("\n\n you have scored  :" + str(score) + "  out of possible " + str(len(round)) )