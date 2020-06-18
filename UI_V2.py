Game_On=True
while Game_On==True:
    mlist=[0,0,0]
    def display_game(mlist):
        print('This is the default list:{}'.format(mlist))
    display_game(mlist)


    def choose_index_position():
        index_choice = None
        while index_choice not in['0','1','2']:
            index_choice = input(' Choose an index position(0-2): ')
            if index_choice not in['0','1','2']:
                print('Invalid Choice. Choose an index position(0-2)')
        return(int(index_choice))


    choose_index_position()
    Index_Choice = choose_index_position()



    def choose_input_value(Index_Choice):
        input_choice = input('Choose what you would like to input for index position {}'.format(Index_Choice))
        return (input_choice)
    choose_input_value(Index_Choice)


    Input_Choice = choose_input_value(Index_Choice)


    def replace_action(Index_Choice, Input_Choice,mlist):
        mlist[Index_Choice] = Input_Choice
        print(mlist)
    replace_action(Index_Choice,Input_Choice,mlist)



    def keep_playing():
        keep_choice = None

        while keep_choice not in ['Y', 'N']:
            keep_choice = input('Would you like to keep playing(Y or N)')
            if keep_choice == 'Y':
                return (True)
            elif keep_choice == 'N':
                return (False)
            if keep_choice not in ['Y', 'N']:
                print('Invalid Choice. Y or N')


    keep_playing()
    Game_On = keep_playing()






