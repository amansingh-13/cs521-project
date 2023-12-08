```assert (isinstance(l, list) and
        all(isinstance(x, int) for x in l) and
        (len(l) == 0 or return_val == max(l)))```