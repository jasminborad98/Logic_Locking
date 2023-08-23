from z3 import *

# function to create array with given data elements
def create_array(solver, arr, data):
    for i in range(len(data)):
        arr = Store(arr, i, data[i])
    return arr

# function to create 2d array with given data elements
def create_2D_array(solver, arr, data):
    for i in range(len(data)):
        a = Select(arr, i)
        for j in range(len(data)):
            a = Store(a, j, data[i][j])
        arr = Store(arr, i, a) 
    return arr

# function in obfuscated.c file implementated in z3
def ByteSub_ShiftRow(solver, statemt, Sbox, nb, n, key1, key2, key3, key4, key5, key6, key7):
    temp = If(key5, Sbox[statemt[8] >> 4][statemt[8] & 0xf] , Sbox[statemt[1] >> 4][statemt[1] & 0xf], 0)
    s1 = Sbox[statemt[key1] >> 4][statemt[key1] & 0xf]
    statemt = Store(statemt, 1, s1)
    skey1 = Sbox[statemt[9] >> 4][statemt[9] & 0xf]
    statemt = Store(statemt, key1, skey1)
    s9 = Sbox[statemt[13] >> 4][statemt[13] & 0xf]
    statemt = Store(statemt, 9, s9)
    statemt = Store(statemt, 13, temp)
    
    temp2 = If(key6, Sbox[statemt[6] >> 4][statemt[6] & 0xf] , Sbox[statemt[2] >> 4][statemt[2] & 0xf], 0)
    s2 = Sbox[statemt[10] >> 4][statemt[10] & 0xf]
    statemt = Store(statemt, 2,  s2)
    statemt = Store(statemt, 10, temp2)    
    
    temp3 = Sbox[statemt[6] >> 4][statemt[6] & 0xf]
    s6 = Sbox[statemt[14] >> 4][statemt[14] & 0xf]
    statemt = Store(statemt, 6, s6)
    statemt = Store(statemt, 14, temp3)
    
    temp4 = If(key7, Sbox[statemt[15] >> 4][statemt[15] & 0xf], Sbox[statemt[3] >> 4][statemt[3] & 0xf], 0)
    s3 = Sbox[statemt[key2] >> 4][statemt[key2] & 0xf]
    statemt = Store(statemt, 3, s3)
    skey2 = Sbox[statemt[11] >> 4][statemt[11] & 0xf]
    statemt = Store(statemt, key2, skey2)
    s11 = Sbox[statemt[key3] >> 4][statemt[key3] & 0xf]
    statemt = Store(statemt, 11, s11)
    statemt = Store(statemt, key3, temp4)
    
    s0 = Sbox[statemt[0] >> 4][statemt[0] & 0xf]
    statemt = Store(statemt, 0, s0)
    skey4 = Sbox[statemt[key4] >> 4][statemt[key4] & 0xf]
    statemt = Store(statemt, key4, skey4)
    s8 = Sbox[statemt[8] >> 4][statemt[8] & 0xf]
    statemt = Store(statemt, 8, s8)
    s12 = Sbox[statemt[12] >> 4][statemt[12] & 0xf]
    statemt = Store(statemt, 12, s12)
    solver.add(statemt[12] == s12)

    statemt = Store(statemt, 1, Select(statemt, 1) + n)
    statemt = Store(statemt, 0, Select(statemt, 0) + n)
    statemt = Store(statemt, 2, Select(statemt, 2) + n)
    statemt = Store(statemt, 3, Select(statemt, 3) + n)
    statemt = Store(statemt, 4, Select(statemt, 4) + n)
    statemt = Store(statemt, 5, Select(statemt, 5) + n)
    statemt = Store(statemt, 6, Select(statemt, 6) + n)
    statemt = Store(statemt, 7, Select(statemt, 7) + n)
    statemt = Store(statemt, 8, Select(statemt, 8) + n)
    statemt = Store(statemt, 9, Select(statemt, 9) + n)
    statemt = Store(statemt, 10, Select(statemt, 10) + n)
    statemt = Store(statemt, 11, Select(statemt, 11) + n)
    statemt = Store(statemt, 12, Select(statemt, 12) + n)
    statemt = Store(statemt, 13, Select(statemt, 13) + n)
    statemt = Store(statemt, 14, Select(statemt, 14) + n)
    statemt = Store(statemt, 15, Select(statemt, 15) + n)

    return statemt


# creating z3 solver
s = Solver()

# creating statemt array with initial values
statemt = Array('statemt', BitVecSort(32), BitVecSort(32))
dataStatements = [50,67,246,168,136,90,48,141,49,49,152,162,224,55,7,52,50,67,246,168,136,90,48,141,49,49,152,162,224,55,7,52]
statemt = create_array(s, statemt, dataStatements)

# creating Sbox array with initial values
Sbox = Array('Sbox',  BitVecSort(32), ArraySort( BitVecSort(32),  BitVecSort(32)))
dataSbox =  [[0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],[0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],[0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],[0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],[0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],[0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],[0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],[0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],[0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],[0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],[0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],[0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],[0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],[0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],[0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],[0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]]
Sbox = create_2D_array(s, Sbox, dataSbox)

#====================================    Array value checking    ========================================
#code to check whether values are stores in array or not.
# print(Sbox1[0][0].val())
# for i in range(16):
#     s.add(statemt[i] == dataStatements[i])
#     for j in range(16):
#         s.add(Sbox[i][j] == dataSbox[i][j])

# print(s)
# if s.check() == sat:
#     print("aray values are Correct")
#     # print(s.model())
# else :
#     print('aray values are NOT Correct')
# exit()
#========================================================================================================

# variables inputs
nb = BitVec('nb', 32)
n = BitVec('n', 32)

# First set of keys
key11 = BitVec('key11', 32)
key12 = BitVec('key12', 32)
key13 = BitVec('key13', 32)
key14 = BitVec('key14', 32)
key15 = Bool('key15')
key16 = Bool('key16')
key17 = Bool('key17')

#second set of keys
key21 = BitVec('key21', 32)
key22 = BitVec('key22', 32)
key23 = BitVec('key23', 32)
key24 = BitVec('key24', 32)
key25 = Bool('key25')
key26 = Bool('key26')
key27 = Bool('key27')

#====================================    Function output checking    ========================================
# s.add(n == 488)
# s.add(key11 == 5) 
# s.add(key12 == 15) 
# s.add(key13 == 7) 
# s.add(key14 == 4)
# s.add(key15 == False)
# s.add(key16 == False)
# s.add(key17 == False)

# output = [523,678,558,512,684,687,685,682,687,642,554,581,713,514,492,546]
# op1 = ByteSub_ShiftRow(s, op1, statemt1, Sbox1, 4, 488, key11, key12, key13, key14, key15, key16, key17)

# for i in range(16):
#     s.add(op1[i] == output[i])

# testing function output
# if s.check() == sat:
#     print("Function Output is correct")
#     print(s.model())
# else :
#     print('Function Output is NOT correct')
# exit()
#============================================================================================================



# adding constraints
s.add(nb == 4)
s.add(n>0, n < 2000000000)    # int +ve range
s.add(key11 >= 0, key11 < 32) # statemt array size = 32
s.add(key12 >= 0, key12 < 32) # statemt array size = 32
s.add(key13 >= 0, key13 < 32) # statemt array size = 32
s.add(key14 >= 0, key14 < 32) # statemt array size = 32
s.add(key21 >= 0, key21 < 32) # statemt array size = 32
s.add(key22 >= 0, key22 < 32) # statemt array size = 32
s.add(key23 >= 0, key23 < 32) # statemt array size = 32
s.add(key24 >= 0, key24 < 32) # statemt array size = 32



# ================================   iteration 1, n = 67108769    ========================================
output = [67108804, 67108959, 67108839, 67108793, 67108965, 67108968, 67108966, 67108963, 67108968, 67108923, 67108835, 67108862, 67108994, 67108795, 67108773, 67108827]
# adding constraint for first set of keys
out_test = ByteSub_ShiftRow(s, statemt, Sbox, 4, 67108769, key11, key12, key13, key14, key15, key16, key17)
for i in range(16):
    s.add(out_test[i] == output[i])
# adding constraint for second set of keys
out_test = ByteSub_ShiftRow(s, statemt, Sbox, 4, 67108769, key21, key22, key23, key24, key25, key26, key27)
for i in range(16):
    s.add(out_test[i] == output[i])
#============================================================================================================





#========================   Keys should be same after iteration 1 unsat   ===============================
s.add(key11 == key21)
s.add(key12 == key22)
s.add(key13 == key23)
s.add(key14 == key24)
s.add(key15 == key25)
s.add(key16 == key26)
s.add(key17 == key27)
#=========================================================================================================

#===============================   output for 2 set of keys     ==========================================
out1 = ByteSub_ShiftRow(s, statemt, Sbox, nb, n, key11, key12, key13, key14, key15, key16, key17)
out2 = ByteSub_ShiftRow(s, statemt, Sbox, nb, n, key21, key22, key23, key24, key25, key26, key27)
# s.add(out1 != out2) # checking for DIP
s.add(out1 == out2) # checking after unsat final key value
#=========================================================================================================

#===============================   Final values     ==========================================
if (s.check() == sat):
    print("sat")
    print("nb : ", s.model()[nb])
    print("n : ", s.model()[n])
    print("key11 : ", s.model()[key11])
    print("key12 : ", s.model()[key12])
    print("key13 : ", s.model()[key13])
    print("key14 : ", s.model()[key14])
    print("key15 : ", s.model()[key15])
    print("key16 : ", s.model()[key16])
    print("key17 : ", s.model()[key17])
    print("key21 : ", s.model()[key21])
    print("key22 : ", s.model()[key22])
    print("key23 : ", s.model()[key23])
    print("key24 : ", s.model()[key24])
    print("key25 : ", s.model()[key25])
    print("key26 : ", s.model()[key26])
    print("key27 : ", s.model()[key27])
    
else:
    print("unsat")
#=====================================   END     ==============================================


