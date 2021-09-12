def main(a, b):
    if not b.startswith('*') and not b.endswith('*'):
        return 'OK' if a == b else 'KO'
    elif b.startswith('*') and b.startswith('*'):
        return 'OK' if b.strip('*') in a else 'KO'
    elif b.startswith('*'):
        return 'OK' if a.endswith(b.strip('*')) else 'KO'
    elif b.endswith('*'):
        return 'OK' if a.startswith(b.strip('*')) else 'KO'


