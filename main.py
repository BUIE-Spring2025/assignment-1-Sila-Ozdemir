def int_to_roman(num):
    my_dict = {1000:"M",500:"D",100:"C",50:"L",10:"X",5:"V",1:"I"}
    roman_string = ""
    my_second_dict = {900:"CM",400:"CD",90:"XC",40:"XL",9:"IX",4:"IV"}
    for key in my_dict.keys():
        bolum = num // key
        if not bolum ==4 or bolum== 9:
            if bolum >= 1 : 
                roman_string += bolum * my_dict[key]
            num = num - (bolum * key)
        else:
            if bolum * key in my_second_dict.keys():
                roman_string += my_second_dict[bolum *key]
            num = num - (bolum*key)
    return roman_string
                






    """
    Convert an integer to a Roman numeral.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
    """
