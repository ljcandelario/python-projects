# NZ_quiz.py
#
# by Louie Candelario
# 13.10.2022

import time

start_time = time.time()
score = 0

print("Kia Ora! Welcome to New Zealand! Let's have a trivia quiz about the land of the long white cloud.")
input("Hit enter when you are ready.")

print("Sweet as.")

# first question

question_1 = input("""In spring and summer, which city in New Zealand gets to see the sunrise first? 
[A] Wellington 
[B] Gisborne 
[C] Queenstown """)

answer_1 = question_1.lower()

if answer_1 == "a":
    print("""Sorry. Wellington might be the southernmost capital in the world, but Gisborne is the first city in NZ, 
    and sometimes the world, that gets the first sunrise""")
elif answer_1 == "b":
    print("""Sweet! You are correct. Gisborne is the first city in NZ, 
    and sometimes the world, that gets the first sunrise""")
    score += 1
elif answer_1 == "c":
    print("""Oops. Sorry, wrong answer mate. but Gisborne is the first city in NZ, and sometimes the world, 
    that gets the first sunrise""")
else:
    print("No point for you. The correct answer is Gisborne!")

# 2nd question
question_2 = input("""What movie franchise is New Zealand most famous for?
[A] Harry Potter 
[B] The Avengers
[C] The Lord of the Rings """)

answer_2 = question_2.lower()

if answer_2 == "a":
    print("""Avada Kedavra! Wrong! No way is Harry Potter THAT famous in New Zealand!" The Lord of the Rings franchise 
              is essentially a 12 hour tourism commercial that showcases the beauty of Aotearoa, with some hobbits, 
              elves, dragons and a wizard too. Don't forget about the one ring to rule them all.""")
elif answer_2 == "b":
    print("""Yeah nah, mate. The Avengers didn't assemble in New Zealand. The Lord of the Rings franchise 
    is essentially a 12 hour tourism commercial that showcases the beauty of Aotearoa, with some hobbits, 
    elves, dragons and a wizard too. Don't forget about the one ring to rule them all.""")
elif answer_2 == "c":
    print("""My precious! You are correct! The Lord of the Rings franchise is essentially a 12 hour tourism commercial 
    that showcases the beauty of Aotearoa, with some hobbits, elves, dragons and a wizard too. Don't forget about the 
    one ring to rule them all.""")
    score += 1
else:
    print("""No point for you. The correct answer is The Lord of the Rings.
    The Lord of the Rings franchise is essentially a 12 hour tourism commercial that showcases the beauty of Aotearoa, 
    with some Hobbits, elves, dragons and a wizard too. Don't forget about the one ring to rule them all.""")

# 3rd question
question_3 = input("""Is it true that there are more sheep than people in New Zealand? 
[A] True 
[B] False """)

answer_3 = question_3.lower()

if answer_3 == "a":
    print("That is true! It is estimated that there are about 9 sheep for every person New Zealand.")
    score += 1
elif answer_3 == "b":
    print("""Sorry. There really are more sheep than people in New Zealand. There are 9 sheep for every person in 
    New Zealand""")
else:
    print("No point for you. The correct answer is True. There are 9 sheep for every person in New Zealand")

# 4th Question

question_4 = input("""What is the team name of New Zealand's famous national rugby team?
[A] Tall Blacks
[B] Black Caps
[C] All Blacks """)

answer_4 = question_4.lower()

if answer_4 == "a":
    print("""Yeah nah, mate. The Tall Blacks are the national Basketball team. 
    The All Blacks are New Zealand's national rugby team famous for their dominance and the Haka!""")
elif answer_4 == "b":
    print("""Yeah nah, mate. The Black Caps are the national cricket team. 
    The All Blacks are New Zealand's national rugby team famous for their dominance and the Haka!""")
elif answer_4 == "c":
    print("You got it! The All Blacks are New Zealand's national rugby team famous for their dominance and the Haka!")
    score += 1
else:
    print("""No point for you. The correct answer is The All Blacks. They are New Zealand's national rugby team famous 
    for their dominance and the Haka!""")

# question 5
question_5 = input("""What is the largest lake in New Zealand?
[A] Lake Taupo
[B] Lake Wakatipu
[C] Lake Pukaki """)
answer_5 = question_5.lower()

if answer_5 == "a":
    print("Correct! Lake Taupo, which is also an active volcanic crater, is the largest lake in New Zealand.")
    score += 1
elif answer_5 == "b":
    print("""Yeah nah, Lake Wakatipu might be one of the most beautiful, but not the largest. Lake Taupo, 
    which is also an active volcanic crater, is the largest lake in New Zealand.""")
elif answer_5 == "c":
    print("""Yeah nah, Lake Pukaki might be one of the most beautiful, but not the largest. Lake Taupo, 
    which is also an active volcanic crater, is the largest lake in New Zealand.""")
else:
    print("""No point for you. The correct answer is Lake Taupo, 
    which is also an active volcanic crater, is the largest lake in New Zealand.""")

end_time = time.time()
total_time = float(end_time - start_time)
final_time = round(total_time, 2)

print("Your time in taking this quiz is ", final_time, "seconds")
print("Your score is", int(score))
print("That is the end of the trivia quiz. Hope you learned more about our beautiful country!")