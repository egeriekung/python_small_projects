from random import choice
questions = ["Why do we catch a cold?: ","Why is the sky blue?: ",
             "why am i here?: ","Why do people look diffrent?: ",
             "Why does it rain?: ","Why do we need to eat?: ",
             "Where are all the dinosaurs?: ","Why is red red?: ",
             "Is Egerie a coder?: ","Is python great?: ",
             "When will Egerie create a game with Python?: ",
             "Why does mommy wear glasses?: ","Why are there cloulds?: ",
             "Why do i ask why?: ","Why are you SOO anoying?: "]
while True:
    question = choice(questions)
    answer = input(question).strip().lower()

    while answer != 'just because':
        answer = input('Why?: ').strip().lower()
    print('Oh...Okay')
    
    