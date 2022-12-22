from extension import find_rlc



RLC_adr = find_rlc()
if RLC_adr != 0:
    print(RLC_adr)
else:
    print('no RLC device found\n')
    exit(-1)




