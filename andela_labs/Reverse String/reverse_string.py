

def reverse_string(string):

    """
     returns the reverse of the string provided. 
     If the reverse of the string is the same as 
     the original string, as in the case of 
     palindromes, return true 
    """
    if not isinstance(string, str):
        raise TypeError("Expected parameter string as string")

    str_length = len(string)
    
    if str_length == 0:         # string is empty 
        return None

    str_list = list(string)
    rev_list = []

    for i in xrange((str_length - 1), -1, -1): #reverse list
        rev_list.append(str_list[i])

    if str_list == rev_list:    #palindrome
        return True

    return ("").join(rev_list) #join array
