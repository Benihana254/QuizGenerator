"""
I attempt to create a set of random auiz file for 35
students. The question numbers as well as answers are randomized
"""
# Python 3
import random
capitals = {
    "Afghanistan": "Kabul",
    "Argentina": "Buenos Aires",
    "Australia": "Canberra",
    "Brazil": "Brasília",
    "Canada": "Ottawa",
    "China": "Beijing",
    "Colombia": "Bogotá",
    "Denmark": "Copenhagen",
    "Egypt": "Cairo",
    "Ethiopia": "Addis Ababa",
    "Finland": "Helsinki",
    "France": "Paris",
    "Germany": "Berlin",
    "Ghana": "Accra",
    "Greece": "Athens",
    "Hungary": "Budapest",
    "India": "New Delhi",
    "Indonesia": "Jakarta",
    "Iran": "Tehran",
    "Iraq": "Baghdad",
    "Ireland": "Dublin",
    "Israel": "Jerusalem",
    "Italy": "Rome",
    "Japan": "Tokyo",
    "Kenya": "Nairobi",
    "Malaysia": "Kuala Lumpur",
    "Mexico": "Mexico City",
    "Morocco": "Rabat",
    "Nepal": "Kathmandu",
    "Netherlands": "Amsterdam",
    "New Zealand": "Wellington",
    "Nigeria": "Abuja",
    "Norway": "Oslo",
    "Pakistan": "Islamabad",
    "Peru": "Lima",
    "Philippines": "Manila",
    "Poland": "Warsaw",
    "Portugal": "Lisbon",
    "Russia": "Moscow",
    "Saudi Arabia": "Riyadh",
    "South Africa": "Pretoria",
    "South Korea": "Seoul",
    "Spain": "Madrid",
    "Sweden": "Stockholm",
    "Switzerland": "Bern",
    "Thailand": "Bangkok",
    "Turkey": "Ankara",
    "Uganda": "Kampala",
    "Ukraine": "Kyiv",
    "United Kingdom": "London",
    "United States": "Washington, D.C.",
    "Vietnam": "Hanoi"
}
 # a list of states and their capital stored in a dictionary named capital
for quizNum in range(35):
    # Writing out the header for the quiz files
    quiz_file = open(f'capitals_quiz_{quizNum+ 1}.txt', 'w')
    answer_key = open(f'capitals_answer_{quizNum+1}.txt', 'w')
    quiz_file.write('Name: \n\n Email: \n\n Date: \n\n ')
    quiz_file.write(' '* 20 + f'Form{quizNum}\n\n')
    quiz_file.write('\n\n')
    #shuffling the states
    states = list(capitals.keys()) # the key is the state, the key value the ans; the capital city
    random.shuffle(states)
    for question_num in range(50):
        correct_answer  = capitals[states[question_num]]
        wrong_answers = list(capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)] # delete the correct answer from the list
        wrong_answers = random.sample(wrong_answers, 3)
        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)
        quiz_file.write(f' {question_num+1} What is the capital of {states[question_num]}?\n')
        for i in range(4):
            quiz_file.write(f'{'ABCD'[i]} {answer_options[i]}\n')
        quiz_file.write('\n')
        #writing the answer key to a file
        answer_key.write(f'{question_num+1} {'ABCD'[answer_options.index(correct_answer)]}' )
        # quiz_file.close()
        # answer_key.close()
