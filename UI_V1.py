
def show():
    import time
    index_position=None
    choice=[1,2,3]
    main_list=[6,2,5]
    print('This is the current default list:{}'.format(main_list))

    time.sleep(3)




    while index_position not in choice:
        index_position=input('Choose an index position(1-3)')
        if int(index_position) not in choice:
                print('Invalid Position please try again')
        elif int(index_position) in choice:
            print('Valid Position!')
            print(index_position)
            return(index_position+' accepted')




def input_position():
    input_value=input('Choose a value to put in index position {}'.format(index_position))
    return(input_value+' accepted!')

show()

input_position()






















