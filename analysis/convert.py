# CIDR Notation to Regex Tool
# Original: http://d.xenowire.net/cidr2regex.php
# Converted to Python by 112buddyd

def cidr_to_regex(cidr):
    import re
    
    # Validation
    cidr_regex = r'^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/([0-9]|[1-2][0-9]|3[0-2]))$'
    if not re.match(cidr_regex, cidr):
        return 'Input not valid CIDR notation. Ex. 192.168.1.0/24'
    
    # Setup Regex string dictionary
    map = {}
    # 255
    map[0] = {}
    map[0][0] = '[0-9]{1,3}'
    # 128
    map[1] = {}
    map[1][0] = '([0-9]{0,1}[0-9]|1[0-1][0-9]|12[0-7])'
    map[1][128] = '(12[8-9]|1[3-9][0-9]|2[0-5][0-9])'
    # 64
    map[2] = {}
    map[2][0] = '([0-5]{0,1}[0-9]|6[0-3])'
    map[2][64] = '(6[4-9]|[7-9][0-9]|1[0-1][0-9]|12[0-7])'
    map[2][128] = '(12[8-9]|1[3-8][0-9]|19[0-1])'
    map[2][192] = '(19[2-9]|2[0-5][0-9])'
    # 32
    map[3] = {}
    map[3][0] = '([0-2]{0,1}[0-9]|3[0-1])'
    map[3][32] = '(3[2-9]|[4-5][0-9]|6[0-3])'
    map[3][64] = '(6[4-9]|[7-8][0-9]|9[0-5])'
    map[3][96] = '(9[6-9]|1[0-1][0-9]|12[0-7])'
    map[3][128] = '(12[8-9]|1[3-5][0-9])'
    map[3][160] = '(1[6-8][0-9]|19[0-1])'
    map[3][192] = '(19[2-9]|2[0-1][0-9]|22[0-3])'
    map[3][224] = '(22[4-9]|2[3-5][0-9])'
    # 16
    map[4] = {}
    map[4][0] = '([0-9]|1[0-5])'
    map[4][16] = '(1[6-9]|2[0-9]|3[0-1])'
    map[4][32] = '(3[2-9]|4[0-7])'
    map[4][48] = '(4[8-9]|5[0-9]|6[0-3])'
    map[4][64] = '(6[4-9]|7[0-9])'
    map[4][80] = '(8[0-9]|9[0-5])'
    map[4][96] = '(9[6-9]|10[0-9]|11[0-1])'
    map[4][112] = '(11[2-9]|12[0-7])'
    map[4][128] = '(12[8-9]|13[0-9]|14[0-3])'
    map[4][144] = '(14[4-9]|15[0-9])'
    map[4][160] = '(16[0-9]|17[0-5])'
    map[4][176] = '(17[6-9]|18[0-9]|19[0-1])'
    map[4][192] = '(19[2-9]|20[0-7])'
    map[4][208] = '(20[8-9]|21[0-9]|22[0-3])'
    map[4][224] = '(22[4-9]|23[0-9])'
    map[4][240] = '2[4-5][0-9]'
    # 8
    map[5] = {}
    map[5][0] = '[0-7]'
    map[5][8] = '([8-9]|1[0-5])'
    map[5][16] = '(1[6-9]|2[0-3])'
    map[5][24] = '(2[4-9]|3[0-1])'
    map[5][32] = '3[2-9]'
    map[5][40] = '4[0-7]'
    map[5][48] = '(4[8-9]|5[0-5])'
    map[5][56] = '(5[6-9]|6[0-3])'
    map[5][64] = '(6[4-9]|7[0-1])'
    map[5][72] = '7[2-9]'
    map[5][80] = '8[0-7]'
    map[5][88] = '(8[8-9]|9[0-5])'
    map[5][96] = '(9[6-9]|10[0-3])'
    map[5][104] = '(10[4-9]|11[0-1])'
    map[5][112] = '11[2-9]'
    map[5][120] = '12[0-7]'
    map[5][128] = '(12[8-9]|13[0-5])'
    map[5][136] = '(13[6-9]|14[0-3])'
    map[5][144] = '(14[4-9]|15[0-1])'
    map[5][152] = '15[2-9]'
    map[5][160] = '16[0-7]'
    map[5][168] = '(16[8-9]|17[0-5])'
    map[5][176] = '(17[6-9]|18[0-3])'
    map[5][184] = '(18[4-9]|19[0-1])'
    map[5][192] = '19[2-9]'
    map[5][200] = '20[0-7]'
    map[5][208] = '(20[8-9]|21[0-5])'
    map[5][216] = '(21[6-9]|22[0-3])'
    map[5][224] = '(22[4-9]|23[0-1])'
    map[5][232] = '23[2-9]'
    map[5][240] = '24[0-7]'
    map[5][248] = '(24[8-9]|25[0-5])'
    # 4
    map[6] = {}
    map[6][0] = '[0-3]'
    map[6][4] = '[4-7]'
    map[6][8] = '([8-9]|1[0-1])'
    map[6][12] = '1[2-5]'
    map[6][16] = '1[6-9]'
    map[6][20] = '2[0-3]'
    map[6][24] = '2[4-7]'
    map[6][28] = '(2[8-9]|3[0-1])'
    map[6][32] = '3[2-5]'
    map[6][36] = '3[6-9]'
    map[6][40] = '4[0-3]'
    map[6][44] = '4[4-7]'
    map[6][48] = '(4[8-9]|5[0-1])'
    map[6][52] = '5[2-5]'
    map[6][56] = '5[6-9]'
    map[6][60] = '6[0-3]'
    map[6][64] = '6[4-7]'
    map[6][68] = '(6[8-9]|7[0-1])'
    map[6][72] = '7[2-5]'
    map[6][76] = '7[6-9]'
    map[6][80] = '8[0-3]'
    map[6][84] = '8[4-7]'
    map[6][88] = '(8[8-9]|9[0-1])'
    map[6][92] = '9[2-5]'
    map[6][96] = '9[6-9]'
    map[6][100] = '10[0-3]'
    map[6][104] = '10[4-7]'
    map[6][108] = '(10[8-9]|11[0-1])'
    map[6][112] = '11[2-5]'
    map[6][116] = '11[6-9]'
    map[6][120] = '12[0-3]'
    map[6][124] = '12[4-7]'
    map[6][128] = '(12[8-9]|13[0-1])'
    map[6][132] = '13[2-5]'
    map[6][136] = '13[6-9]'
    map[6][140] = '14[0-3]'
    map[6][144] = '14[4-7]'
    map[6][148] = '(14[8-9]|15[0-1])'
    map[6][152] = '15[2-5]'
    map[6][156] = '15[6-9]'
    map[6][160] = '16[0-3]'
    map[6][164] = '16[4-7]'
    map[6][168] = '(16[8-9]|17[0-1])'
    map[6][172] = '17[2-5]'
    map[6][176] = '17[6-9]'
    map[6][180] = '18[0-3]'
    map[6][184] = '18[4-7]'
    map[6][188] = '(18[8-9]|19[0-1])'
    map[6][192] = '19[2-5]'
    map[6][196] = '19[6-9]'
    map[6][200] = '20[0-3]'
    map[6][204] = '20[4-7]'
    map[6][208] = '(20[8-9]|21[0-1])'
    map[6][212] = '21[2-5]'
    map[6][216] = '21[6-9]'
    map[6][220] = '22[0-3]'
    map[6][224] = '22[4-7]'
    map[6][228] = '(22[8-9]|23[0-1])'
    map[6][232] = '23[2-5]'
    map[6][236] = '23[6-9]'
    map[6][240] = '24[0-3]'
    map[6][244] = '24[4-7]'
    map[6][248] = '(24[8-9]|25[0-1])'
    map[6][252] = '25[2-5]'
    
    # Setup some vars
    network = cidr.split('/')[0]
    n1 = network.split('.')[0]
    n2 = network.split('.')[1]
    n3 = network.split('.')[2]
    n4 = network.split('.')[3]
    mask = cidr.split('/')[1]
    bip = 0
    
    # Logic based on subnet mask
    if mask == '0':
        return map[0][0] + '\.' + map[0][0] + '\.' + map[0][0] + '\.' + map[0][0]
    elif mask == '1':
        bip = int((int(n1)/128)*128)
        map[1][bip] + '\.' + map[0][0] + '\.' + map[0][0] + '\.' + map[0][0]
    elif mask == '2':
        bip = int((int(n1)/64)*64)
        return map[2][bip] + '\.' + map[0][0] + '\.' + map[0][0] + '\.' + map[0][0]
    elif mask == '3':
        bip = int((int(n1)/32)*32)
        return map[3][bip] + '\.' + map[0][0] + '\.' + map[0][0] + '\.' + map[0][0]
    elif mask == '4':
        bip = int((int(n1)/16)*16)
        return map[4][bip] + '\.' + map[0][0] + '\.' + map[0][0] + '\.' + map[0][0]
    elif mask == '5':
        bip = int((int(n1)/8)*8)
        return map[5][bip] + '\.' + map[0][0] + '\.' + map[0][0] + '\.' + map[0][0]
    elif mask == '6':
        bip = int((int(n1)/4)*4)
        return map[6][bip] + '\.' + map[0][0] + '\.' + map[0][0] + '\.' + map[0][0]
    elif mask == '7':
        bip = int((int(n1)/2)*2)
        if len(str(bip)) == 2:
            return str(bip)[0] + '[' + str(bip)[1] + '-' + str(bip+1)[1] + ']' + '\.' + map[0][0] + '\.' + map[0][0] + '\.' + map[0][0]
        elif len(str(bip)) == 3:
            return str(bip)[:2] + '[' + str(bip)[2] + '-' + str(bip+1)[2] + ']' + '\.' + map[0][0] + '\.' + map[0][0] + '\.' + map[0][0]
        else:
            return '[' + str(bip) + '-' + str(bip+1) + ']' + '\.' + map[0][0] + '\.' + map[0][0] + '\.' + map[0][0]
        
    elif mask == '8':
        return n1 + '\.' + map[0][0] + '\.' + map[0][0] + '\.' + map[0][0]
    elif mask == '9':
        bip = int((int(n2)/128)*128)
        return n1 + '\.' + map[1][bip] + '\.' + map[0][0] + '\.' + map[0][0]
    elif mask == '10':
        bip = int((int(n2)/64)*64)
        return n1 + '\.' + map[2][bip] + '\.' + map[0][0] + '\.' + map[0][0]
    elif mask == '11':
        bip = int((int(n2)/32)*32)
        return n1 + '\.' + map[3][bip] + '\.' + map[0][0] + '\.' + map[0][0]
    elif mask == '12':
        bip = int((int(n2)/16)*16)
        return n1 + '\.' + map[4][bip] + '\.' + map[0][0] + '\.' + map[0][0]
    elif mask == '13':
        bip = int((int(n2)/8)*8)
        return n1 + '\.' + map[5][bip] + '\.' + map[0][0] + '\.' + map[0][0]
    elif mask == '14':
        bip = int((int(n2)/4)*4)
        return n1 + '\.' + map[6][bip] + '\.' + map[0][0] + '\.' + map[0][0]
    elif mask == '15':
        bip = int((int(n2)/2)*2)
        if len(str(bip)) == 2:
            return n1 + '\.' + str(bip)[0] + '[' + str(bip)[1] + '-' + str(bip+1)[1] + ']' + '\.' + map[0][0] + '\.' + map[0][0]
        elif len(str(bip)) == 3:
            return n1 + '\.' + str(bip)[:2] + '[' + str(bip)[2] + '-' + str(bip+1)[2] + ']' + '\.' + map[0][0] + '\.' + map[0][0]
        else:
            return n1 + '\.' + '[' + str(bip) + '-' + str(bip+1) + ']' + '\.' + map[0][0] + '\.' + map[0][0]
    elif mask == '16':
        return n1 + '\.' + n2 + '\.' + map[0][0] + '\.' + map[0][0]
    elif mask == '17':
        bip = int((int(n3)/128)*128)
        return n1 + '\.' + n2 + '\.' + map[1][bip] + '\.' + map[0][0]
    elif mask == '18':
        bip = int((int(n3)/64)*64)
        return n1 + '\.' + n2 + '\.' + map[2][bip] + '\.' + map[0][0]
    elif mask == '19':
        bip = int((int(n3)/32)*32)
        return n1 + '\.' + n2 + '\.' + map[3][bip] + '\.' + map[0][0]
    elif mask == '20':
        bip = int((int(n3)/16)*16)
        return n1 + '\.' + n2 + '\.' + map[4][bip] + '\.' + map[0][0]
    elif mask == '21':
        bip = int((int(n3)/8)*8)
        return n1 + '\.' + n2 + '\.' + map[5][bip] + '\.' + map[0][0]
    elif mask == '22':
        bip = int((int(n3)/4)*4)
        return n1 + '\.' + n2 + '\.' + map[6][bip] + '\.' + map[0][0]
    elif mask == '23':
        bip = int((int(n3)/2)*2)
        if len(str(bip)) == 2:
            return n1 + '\.' + n2 + '\.' + str(bip)[0] + '[' + str(bip)[1] + '-' + str(bip+1)[1] + ']' + '\.' + map[0][0]
        elif len(str(bip)) == 3:
            return n1 + '\.' + n2 + '\.' + str(bip)[:2] + '[' + str(bip)[2] + '-' + str(bip+1)[2] + ']' + '\.' + map[0][0]
        else:
            return n1 + '\.' + n2 + '\.' + '[' + str(bip) + '-' + str(bip+1) + ']' + '\.' + map[0][0]
    elif mask == '24':
        return n1 + '\.' + n2 + '\.' + n3 + '\.' + map[0][0]
    elif mask == '25':
        bip = int((int(n4)/128)*128)
        return n1 + '\.' + n2 + '\.' + n3 + '\.' + map[1][bip]
    elif mask == '26':
        bip = int((int(n4)/64)*64)
        return n1 + '\.' + n2 + '\.' + n3 + '\.' + map[2][bip]
    elif mask == '27':
        bip = int((int(n4)/32)*32)
        return n1 + '\.' + n2 + '\.' + n3 + '\.' + map[3][bip]
    elif mask == '28':
        bip = int((int(n4)/16)*16)
        return n1 + '\.' + n2 + '\.' + n3 + '\.' + map[4][bip]
    elif mask == '29':
        bip = int((int(n4)/8)*8)
        return n1 + '\.' + n2 + '\.' + n3 + '\.' + map[5][bip]
    elif mask == '30':
        bip = int((int(n4)/4)*4)
        return n1 + '\.' + n2 + '\.' + n3 + '\.' + map[6][bip]
    elif mask == '31':
        bip = int((int(n4)/2)*2)
        if len(str(bip)) == 2:
            return n1 + '\.' + n2 + '\.' + n3 + '\.' + str(bip)[0] + '[' + str(bip)[1] + '-' + [string](bip+1)[1] + ']'
        elif len(str(bip)) == 3:
            return n1 + '\.' + n2 + '\.' + n3 + '\.' + str(bip)[:2] + '[' + str(bip)[2] + '-' + [string](bip+1)[2] + ']'
        else:
            return n1 + '\.' + n2 + '\.' + n3 + '\.' + '[' + str(bip) + '-' + str(bip+1) + ']'
    elif mask == '32':
        return n1 + '\.' + n2 + '\.' + n3 + '\.' + n4
    else:
        return 'Invalid Subnet Mask.'
        
        
if __name__ == '__main__':
    print('RegEx: ' + cidr_to_regex(input('CIDR:  ')))






