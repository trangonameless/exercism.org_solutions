def is_isogram(string):
    lower_case_string = string.lower().replace("-", "").replace(" ", "")
    result = "".join(dict.fromkeys(lower_case_string))
    print(result)
    print(string.replace("-", "").replace(" ", ""))
    if string.replace("-", "").replace(" ", "").lower() == result:
        return True
    else:
        return False


