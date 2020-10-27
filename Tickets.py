films = {
    'Matilda':[9,7],
    'The Blue Duck':[5,10],
    'The Bfg':[15,5],
    'Sky High':[20,3],
    'Finding Dory':[3,15],
    'Ask The Story Bots':[5,10],
    'Peppa Pig':[1,20],
    'Paw Patrol':[7,6],
    'Shimer And Shine':[6,5],
    'My Little Pony':[8,4],
    'Banana World':[2,12],
    'When I Grow Up':[4,8],
    'Candy Land':[7,5],
    'Santa':[3,6]
    }
while True:
    choice = input('what film do YOU want to watch?--->    ').strip().title()
    if choice in films:
        age=int(input('How old are you?--->    ').strip())
        if age >=films[choice][0]:
            num_seat = films[choice][1]
            if num_seat > 0:
              print('Enjoy the film!')
              films[choice][1] = films[choice][1] - 1
              num_seat = films[choice][1]
            else:
                print('No more tickets!')
        else:
            print('Film inapropiate :C')
    else:
        print("Sorry, we don't have that film...")