def response(hey_bob):
    if hey_bob.endswith('?') and hey_bob.isupper() == True:
        return("Calm down, I know what I'm doing!")
    if hey_bob.strip().endswith('?') == True:
        return ('Sure.')
    if hey_bob.isupper() == True:
        return ('Whoa, chill out!')
    if hey_bob.isspace() == True or hey_bob == "":
        return ('Fine. Be that way!')
    else:
        return ('Whatever.')


