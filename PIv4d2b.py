# Description:
#    Checks is a given string is a valid IPv4 address.
#
# Return:
#    Returns True if the address is valid, False otherwise.
#
def isIPv4(addr: str) -> bool:

    bytes = addr.split(".")
    
    if len(bytes) != 4: return False
    
    for byte in bytes:
    
        if ( not byte.isnumeric() or\
             not (int(byte) >= 0 and int(byte) <= 255) ):
           
           return False
           
    return True
            
# Description:
#    Converts a checked valid dotted decimal IPv4 address in
#    dotted binary.
#
# Return:
#    Returns the binary IPv4 address in a string.
#
def IPv4_d2b(addr: str) -> str:

    assert(isIPv4(addr))
    
    bs = addr.split(".")
    bs = [int(b) for b in bs]
    
    return f"{bs[0]:b}.{bs[1]:b}.{bs[2]:b}.{bs[3]:b}"
 
# Test cases:
def tests():

    print("TEST 1/4: ", IPv4_d2b("255.255.255.255") == "11111111.11111111.11111111.11111111")
    print("TEST 2/4: ", IPv4_d2b("0.0.0.0") == "0.0.0.0")
    print("TEST 3/4: ", IPv4_d2b("0.255.255.0") == "0.11111111.11111111.0")
    print("TEST 4/4: ", IPv4_d2b("111.2.123.255") == "1101111.10.1111011.11111111")
    
    
test()

# Usage:      
#       
#addr = input("Inserire un indirizzo IPv4: ")
#print(IPv4_d2b(addr))
#
