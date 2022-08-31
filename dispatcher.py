def are_integers(base, exp):
    if not is_int(base):
        if not is_int(exp):
            print('Base', base, 'e expoente', exp, 'não estão no formato devido')
        else:
            print('Base', base, 'não está no formato devido')
        return False
    elif not is_int(exp):
        print('Expoente', exp, 'não está no formato devido')
        return False
    else:
        return True

def is_int(data):
    try:
        int(data)
        return True
    except:
        return False