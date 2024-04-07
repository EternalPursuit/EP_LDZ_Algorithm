while True:
    try:
        tot_l = list(map(int, input().split()))
        n = tot_l.pop(0)
        root_val = tot_l.pop(0)
        tar_ind = tot_l.pop()

        res = [root_val]
        print(f"res: {res}")

        while tot_l:
            print(f"tot_l is {tot_l}")
            insert_val = tot_l[0]
            insert_pos = tot_l[1]
            if insert_pos not in res:
                continue
            else:
                ind = res.index(insert_pos)
                res.insert(ind+1, insert_val)

                tot_l.pop(0)
                tot_l.pop(0)

        print(f"res: {res}")

        res.remove(tar_ind)
        res_last = [str(i) for i in res]
        print(' '.join(res_last))

    except:
        break