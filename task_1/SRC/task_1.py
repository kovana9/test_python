def main(*args):
    if len(args) == 3:
        nb, base_src, base_dst = args
        for i in nb:
            if i not in base_src:
                print('usage')
                return
        nb_list = list(nb)
        for i in range(len(nb)):
            nb_list[i] = str(base_src.index(nb_list[i]))
        nb = int(''.join(nb_list), len(base_src))
    elif len(args) == 2:
        nb, base_dst = args
        if not nb.isdigit():
            print('usage')
            return
        nb = int(nb)
    else:
        print('usage')
        return
    base = len(base_dst)
    sp = []
    while nb > 0:
        sp.append(nb % base)
        nb = nb // base
    for i in range(len(sp)):
        sp[i] = base_dst[sp[i]]
    print(''.join(reversed(sp)))
