import Sort


def Comparison_Sort (test_case: list) -> list : 

    measure_list = []
  
    test_list = test_case[:]

    Sort.bubble_sort(test_list)

    """
    if (Check(test_case)) : measure_list.append(false)
    else : measure_list.append(end - start)
    """

    return measure_list


def Check (check_case: list) -> bool :

    answer = [1, 2, 3, 4, 5]
    size = len(answer)
    
    for i in range (size) : 
        if (check_case[i] != answer[i]) :
            return False

    return True

if (__name__ == "__main__") :
    
    """
    random_list = []
    insert_list = []
    reversed_list = []
    duplicated_list = []
    check_list = []
    """

    test = [5, 4, 3, 2, 1]
    print(Comparison_Sort(test))
    
