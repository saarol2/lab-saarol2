import codecs

def encode(s):
    if not isinstance(s,str):
        raise TypeError
    origlen = len(s)
    #Pad the string to max length
    s += "x" * (1000 - len(s))
    crypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    invalid_char = {'\xe5', '\xe4', '\xf6'}
    if len(s) > 1000:
        raise ValueError
    for c in s:
        if c in invalid_char:
            #Character is invalid
            raise ValueError
        elif c.isalpha():
            if c.islower():
                c=c.upper()
            # Rot13 the character for maximum security
            crypted+=codecs.encode(c,'rot13')
        elif c in digitmapping:
          crypted+=digitmapping[c]
        #else, the character is invalid
        else:
            raise ValueError

    return crypted[:origlen]

def decode(s):
    return encode(s).lower()

