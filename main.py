def int_to_roman(num):
    my_dict = {1000:"M",500:"D",100:"C",50:"L",10:"X",5:"V",1:"I"}
    roman_string = ""
    for key in my_dict.keys():
        bolum = num // key
        if bolum >= 1 : 
            roman_string += bolum * my_dict[key]
        num = num - (bolum * key)
    return roman_string
                






    """
    Convert an integer to a Roman numeral.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
    """
