def isIPv4(addr: str) -> bool:
    '''
    Description:
        Checks if a given string is a valid IPv4 address.

    Return:
        Returns True if the address is valid, False otherwise.
    '''
    if type(addr) != str: return False
    
    bytes = addr.split(".")
    
    if len(bytes) != 4: return False
    
    for byte in bytes:
    
        if ( not byte.isnumeric() or\
             not (0 <= int(byte) <= 255) ):
           
           return False
           
    return True
 

 

def isNetv4(netmask: str) -> bool:

    '''
    Description:
        Checks of a given string is a valid IPv4 netmask.
    Returns:
        Returns True if the netmask is valid, False otherwise.
    '''

    if isIPv4(netmask) == False:
        return False

    ints = [int(byte) for byte in netmask.split(".")]
    net_int = (2**24 * ints[0]) + (2**16 * ints[1])+ (2**8 * ints[2]) + ints[3]
    net_bin = bin(net_int)[2:]

    if(len(net_bin) != 32): return False

    i = 0
    while i < 32 and net_bin[i] == '1': i += 1

    if(i == 32): return True

    net_first  = net_bin[:i]
    net_second = net_bin[i::]

    return  int(net_second) == 0 \
            and \
            net_first == ''.join(['1' for _ in range(i)])



 
def IPv4_d2b(addr: str) -> str:
    '''         
    Description:
        Converts a checked valid dotted decimal IPv4 address in
        dotted binary.

    Return:
        Returns the binary IPv4 address in a string if IPv4 address is valid, None otherwise.
    '''
    if not isIPv4(addr): return None #can't fail
    
    bs = addr.split(".")
    bs = [int(b) for b in bs]
    
    return f"{bs[0]:b}.{bs[1]:b}.{bs[2]:b}.{bs[3]:b}"

# Usage:      
#       
#addr = input("Inserire un indirizzo IPv4: ")
#print(IPv4_d2b(addr))
#
