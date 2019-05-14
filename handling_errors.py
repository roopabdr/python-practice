def party_planner(cookies, people):
    leftovers = None
    num_each = None

    try:
        if cookies >= 0 and people >= 0: 
            num_each = abs(cookies // people)
            leftovers = abs(cookies % people)
            print(num_each, leftovers)
        else:
            print('Please enter valid inputs')
    # except ZeroDivisionError as e:
    #     print('Please enter valid inputs \n {}'.format(e))
    except Exception as e:
        print('Exception occured: {}'.format(e))

party_planner(5,0)