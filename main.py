#Ethan Garnica
#Subnet calculator finds first/last host, broadcast addr, subnet mask, usable hosts, valid addr, and subnet class
# 10/1/2022
# CST 412
# subnet.py



import socket
import struct


if __name__=="__main__":
    input = input("Enter an IP Address:")
    addr = ''
    cidr = 0
    valid = True
    inRange = [0,0,0,0]
    
    
    (addr,cidr) = input.split('/');
    
    addr = addr.split('.')
    addr = list(map(int, addr))
    cidr = int(cidr)
    if cidr<16:
        netClass = 'A'
    elif cidr>15 & cidr <24:
        netClass = 'B'
    else:
        netClass = 'C'
    host_bits = 32 - cidr
    mask = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
    mask = mask.split('.')
    mask = list(map(int, mask))
    
    broadcast = [(addr[i] & mask[i]) | (255^mask[i]) for i in range(4)]
    firstHost = [addr[i] & mask[i] for i in range(4)]
    firstHost[3]+=1
    lastHost = [(addr[i] & mask[i]) | (255^mask[i]) for i in range(4)]
    lastHost[3]-=1

    for x in range(4):
        if addr[x] > lastHost[x] or addr[x] < firstHost[x]:
            inRange[x] = 1
            
    
    
    mask = list(map(str, mask))
    firstHost = list(map(str, firstHost))
    lastHost = list(map(str, lastHost))
    broadcast = list(map(str, broadcast))

    for x in range(4):
        if inRange[x] == 1:
            valid = False

    
    print ('Mask: {}'.format('.'.join(mask)))
    print ('First Host: {}'.format('.'.join(firstHost)))
    print ('Last Host: {}'.format('.'.join(lastHost)))
    print ('Broadcast: {}'.format('.'.join(broadcast)))
    print ('Usable: ', pow(2,host_bits)-2)
    print ('Valid Host:', valid)
    print('Subnet Class:', netClass)
    

    #convert cidr to the mask