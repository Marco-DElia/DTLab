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
