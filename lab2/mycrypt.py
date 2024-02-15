import codecs

def encode(s):
    if not isinstance(s,str):
        raise TypeError
    origlen = len(s)
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

    return crypted

def decode(s):
    decrypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=', '!"#€%&/()=1234567890'))
    for c in s:
        if c.isalpha():
            if c.isupper():
                c=c.lower()
            #Rot-13 decryption
            decrypted += codecs.decode(c, 'rot-13')
        elif c in digitmapping:
            decrypted += digitmapping[c]
    return decrypted

