import ip_funcs as ip

def tests():
    '''
    Test cases:
    '''
    # Tests passed by execution succeded
    print("TEST 1/8: ", ip.IPv4_d2b("255.255.255.255") == "11111111.11111111.11111111.11111111")
    print("TEST 2/8: ", ip.IPv4_d2b("0.0.0.0") == "0.0.0.0")
    print("TEST 3/8: ", ip.IPv4_d2b("0.255.255.0") == "0.11111111.11111111.0")
    print("TEST 4/8: ", ip.IPv4_d2b("111.2.123.255") == "1101111.10.1111011.11111111")
    
    # Tests passed by execution failed
    print("TEST 5/8: ", ip.IPv4_d2b(12345) == None)
    print("TEST 6/8: ", ip.IPv4_d2b("1.1.1.1.1.1") == None)
    print("TEST 7/8: ", ip.IPv4_d2b("aa.aa.aa.aa") == None)
    print("TEST 8/8: ", ip.IPv4_d2b("256.256.256.256") == None)


tests()

