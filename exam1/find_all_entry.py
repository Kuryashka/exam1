def find_all_entry (a, symb):
    l = []
    for i in a:
        if i == symb:
            l.append(a.index(i))
    return(l)
print(find_all_entry(string, 'p'))