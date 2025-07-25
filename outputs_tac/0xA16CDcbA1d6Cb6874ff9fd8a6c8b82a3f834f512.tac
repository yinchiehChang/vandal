Block 0x0
[0x0:0xa]
---
Predecessors: []
Successors: [0xb, 0x67]
---
0x0 PUSH1 0x60
0x2 PUSH1 0x40
0x4 MSTORE
0x5 CALLDATASIZE
0x6 ISZERO
0x7 PUSH2 0x67
0xa JUMPI
---
0x0: V0 = 0x60
0x2: V1 = 0x40
0x4: M[0x40] = 0x60
0x5: V2 = CALLDATASIZE
0x6: V3 = ISZERO V2
0x7: V4 = 0x67
0xa: JUMPI 0x67 V3
---
Entry stack: []
Stack pops: 0
Stack additions: []
Exit stack: []

================================

Block 0xb
[0xb:0x24]
---
Predecessors: [0x0]
Successors: [0x25, 0x78]
---
0xb PUSH4 0xffffffff
0x10 PUSH1 0xe0
0x12 PUSH1 0x2
0x14 EXP
0x15 PUSH1 0x0
0x17 CALLDATALOAD
0x18 DIV
0x19 AND
0x1a PUSH4 0x2d2c44f2
0x1f DUP2
0x20 EQ
0x21 PUSH2 0x78
0x24 JUMPI
---
0xb: V5 = 0xffffffff
0x10: V6 = 0xe0
0x12: V7 = 0x2
0x14: V8 = EXP 0x2 0xe0
0x15: V9 = 0x0
0x17: V10 = CALLDATALOAD 0x0
0x18: V11 = DIV V10 0x100000000000000000000000000000000000000000000000000000000
0x19: V12 = AND V11 0xffffffff
0x1a: V13 = 0x2d2c44f2
0x20: V14 = EQ V12 0x2d2c44f2
0x21: V15 = 0x78
0x24: JUMPI 0x78 V14
---
Entry stack: []
Stack pops: 0
Stack additions: [V12]
Exit stack: [V12]

================================

Block 0x25
[0x25:0x2f]
---
Predecessors: [0xb]
Successors: [0x30, 0x82]
---
0x25 DUP1
0x26 PUSH4 0x2e1a7d4d
0x2b EQ
0x2c PUSH2 0x82
0x2f JUMPI
---
0x26: V16 = 0x2e1a7d4d
0x2b: V17 = EQ 0x2e1a7d4d V12
0x2c: V18 = 0x82
0x2f: JUMPI 0x82 V17
---
Entry stack: [V12]
Stack pops: 1
Stack additions: [S0]
Exit stack: [V12]

================================

Block 0x30
[0x30:0x3a]
---
Predecessors: [0x25]
Successors: [0x3b, 0x8f]
---
0x30 DUP1
0x31 PUSH4 0x3ee2d7c2
0x36 EQ
0x37 PUSH2 0x8f
0x3a JUMPI
---
0x31: V19 = 0x3ee2d7c2
0x36: V20 = EQ 0x3ee2d7c2 V12
0x37: V21 = 0x8f
0x3a: JUMPI 0x8f V20
---
Entry stack: [V12]
Stack pops: 1
Stack additions: [S0]
Exit stack: [V12]

================================

Block 0x3b
[0x3b:0x45]
---
Predecessors: [0x30]
Successors: [0x46, 0xc0]
---
0x3b DUP1
0x3c PUSH4 0x41c0e1b5
0x41 EQ
0x42 PUSH2 0xc0
0x45 JUMPI
---
0x3c: V22 = 0x41c0e1b5
0x41: V23 = EQ 0x41c0e1b5 V12
0x42: V24 = 0xc0
0x45: JUMPI 0xc0 V23
---
Entry stack: [V12]
Stack pops: 1
Stack additions: [S0]
Exit stack: [V12]

================================

Block 0x46
[0x46:0x50]
---
Predecessors: [0x3b]
Successors: [0x51, 0xd5]
---
0x46 DUP1
0x47 PUSH4 0x9e281a98
0x4c EQ
0x4d PUSH2 0xd5
0x50 JUMPI
---
0x47: V25 = 0x9e281a98
0x4c: V26 = EQ 0x9e281a98 V12
0x4d: V27 = 0xd5
0x50: JUMPI 0xd5 V26
---
Entry stack: [V12]
Stack pops: 1
Stack additions: [S0]
Exit stack: [V12]

================================

Block 0x51
[0x51:0x5b]
---
Predecessors: [0x46]
Successors: [0x5c, 0xee]
---
0x51 DUP1
0x52 PUSH4 0xb4a99a4e
0x57 EQ
0x58 PUSH2 0xee
0x5b JUMPI
---
0x52: V28 = 0xb4a99a4e
0x57: V29 = EQ 0xb4a99a4e V12
0x58: V30 = 0xee
0x5b: JUMPI 0xee V29
---
Entry stack: [V12]
Stack pops: 1
Stack additions: [S0]
Exit stack: [V12]

================================

Block 0x5c
[0x5c:0x66]
---
Predecessors: [0x51]
Successors: [0x67, 0x11d]
---
0x5c DUP1
0x5d PUSH4 0xd0e30db0
0x62 EQ
0x63 PUSH2 0x11d
0x66 JUMPI
---
0x5d: V31 = 0xd0e30db0
0x62: V32 = EQ 0xd0e30db0 V12
0x63: V33 = 0x11d
0x66: JUMPI 0x11d V32
---
Entry stack: [V12]
Stack pops: 1
Stack additions: [S0]
Exit stack: [V12]

================================

Block 0x67
[0x67:0x6a]
---
Predecessors: [0x0, 0x5c]
Successors: [0x6b]
---
0x67 JUMPDEST
0x68 PUSH2 0x76
---
0x67: JUMPDEST 
0x68: V34 = 0x76
---
Entry stack: [V12]
Stack pops: 0
Stack additions: [0x76]
Exit stack: [V12, 0x76]

================================

Block 0x6b
[0x6b:0x72]
---
Predecessors: [0x67]
Successors: [0x127]
---
0x6b JUMPDEST
0x6c PUSH2 0x73
0x6f PUSH2 0x127
0x72 JUMP
---
0x6b: JUMPDEST 
0x6c: V35 = 0x73
0x6f: V36 = 0x127
0x72: JUMP 0x127
---
Entry stack: [V12, 0x76]
Stack pops: 0
Stack additions: [0x73]
Exit stack: [V12, 0x76, 0x73]

================================

Block 0x73
[0x73:0x73]
---
Predecessors: [0x74, 0x127, 0x18c, 0x298]
Successors: [0x74]
---
0x73 JUMPDEST
---
0x73: JUMPDEST 
---
Entry stack: [V12, S1, S0]
Stack pops: 0
Stack additions: []
Exit stack: [V12, S1, S0]

================================

Block 0x74
[0x74:0x75]
---
Predecessors: [0x73]
Successors: [0x73, 0x76]
---
0x74 JUMPDEST
0x75 JUMP
---
0x74: JUMPDEST 
0x75: JUMP S0
---
Entry stack: [V12, S1, S0]
Stack pops: 1
Stack additions: []
Exit stack: [V12, S1]

================================

Block 0x76
[0x76:0x77]
---
Predecessors: [0x74, 0x18c, 0x283, 0x3b6]
Successors: []
---
0x76 JUMPDEST
0x77 STOP
---
0x76: JUMPDEST 
0x77: STOP 
---
Entry stack: [V12, S0]
Stack pops: 0
Stack additions: []
Exit stack: [V12, S0]

================================

Block 0x78
[0x78:0x7f]
---
Predecessors: [0xb]
Successors: [0x18e]
---
0x78 JUMPDEST
0x79 PUSH2 0x76
0x7c PUSH2 0x18e
0x7f JUMP
---
0x78: JUMPDEST 
0x79: V37 = 0x76
0x7c: V38 = 0x18e
0x7f: JUMP 0x18e
---
Entry stack: [V12]
Stack pops: 0
Stack additions: [0x76]
Exit stack: [V12, 0x76]

================================

Block 0x80
[0x80:0x81]
---
Predecessors: []
Successors: []
---
0x80 JUMPDEST
0x81 STOP
---
0x80: JUMPDEST 
0x81: STOP 
---
Entry stack: []
Stack pops: 0
Stack additions: []
Exit stack: []

================================

Block 0x82
[0x82:0x8c]
---
Predecessors: [0x25]
Successors: [0x1c1]
---
0x82 JUMPDEST
0x83 PUSH2 0x76
0x86 PUSH1 0x4
0x88 CALLDATALOAD
0x89 PUSH2 0x1c1
0x8c JUMP
---
0x82: JUMPDEST 
0x83: V39 = 0x76
0x86: V40 = 0x4
0x88: V41 = CALLDATALOAD 0x4
0x89: V42 = 0x1c1
0x8c: JUMP 0x1c1
---
Entry stack: [V12]
Stack pops: 0
Stack additions: [0x76, V41]
Exit stack: [V12, 0x76, V41]

================================

Block 0x8d
[0x8d:0x8e]
---
Predecessors: []
Successors: []
---
0x8d JUMPDEST
0x8e STOP
---
0x8d: JUMPDEST 
0x8e: STOP 
---
Entry stack: []
Stack pops: 0
Stack additions: []
Exit stack: []

================================

Block 0x8f
[0x8f:0x95]
---
Predecessors: [0x30]
Successors: [0x96, 0x9a]
---
0x8f JUMPDEST
0x90 CALLVALUE
0x91 ISZERO
0x92 PUSH2 0x9a
0x95 JUMPI
---
0x8f: JUMPDEST 
0x90: V43 = CALLVALUE
0x91: V44 = ISZERO V43
0x92: V45 = 0x9a
0x95: JUMPI 0x9a V44
---
Entry stack: [V12]
Stack pops: 0
Stack additions: []
Exit stack: [V12]

================================

Block 0x96
[0x96:0x99]
---
Predecessors: [0x8f]
Successors: []
---
0x96 PUSH1 0x0
0x98 DUP1
0x99 REVERT
---
0x96: V46 = 0x0
0x99: REVERT 0x0 0x0
---
Entry stack: [V12]
Stack pops: 0
Stack additions: []
Exit stack: [V12]

================================

Block 0x9a
[0x9a:0xad]
---
Predecessors: [0x8f]
Successors: [0x286]
---
0x9a JUMPDEST
0x9b PUSH2 0xae
0x9e PUSH1 0x1
0xa0 PUSH1 0xa0
0xa2 PUSH1 0x2
0xa4 EXP
0xa5 SUB
0xa6 PUSH1 0x4
0xa8 CALLDATALOAD
0xa9 AND
0xaa PUSH2 0x286
0xad JUMP
---
0x9a: JUMPDEST 
0x9b: V47 = 0xae
0x9e: V48 = 0x1
0xa0: V49 = 0xa0
0xa2: V50 = 0x2
0xa4: V51 = EXP 0x2 0xa0
0xa5: V52 = SUB 0x10000000000000000000000000000000000000000 0x1
0xa6: V53 = 0x4
0xa8: V54 = CALLDATALOAD 0x4
0xa9: V55 = AND V54 0xffffffffffffffffffffffffffffffffffffffff
0xaa: V56 = 0x286
0xad: JUMP 0x286
---
Entry stack: [V12]
Stack pops: 0
Stack additions: [0xae, V55]
Exit stack: [V12, 0xae, V55]

================================

Block 0xae
[0xae:0xbf]
---
Predecessors: [0x286]
Successors: []
---
0xae JUMPDEST
0xaf PUSH1 0x40
0xb1 MLOAD
0xb2 SWAP1
0xb3 DUP2
0xb4 MSTORE
0xb5 PUSH1 0x20
0xb7 ADD
0xb8 PUSH1 0x40
0xba MLOAD
0xbb DUP1
0xbc SWAP2
0xbd SUB
0xbe SWAP1
0xbf RETURN
---
0xae: JUMPDEST 
0xaf: V57 = 0x40
0xb1: V58 = M[0x40]
0xb4: M[V58] = V224
0xb5: V59 = 0x20
0xb7: V60 = ADD 0x20 V58
0xb8: V61 = 0x40
0xba: V62 = M[0x40]
0xbd: V63 = SUB V60 V62
0xbf: RETURN V62 V63
---
Entry stack: [V12, 0xae, V224]
Stack pops: 1
Stack additions: []
Exit stack: [V12, 0xae]

================================

Block 0xc0
[0xc0:0xc6]
---
Predecessors: [0x3b]
Successors: [0xc7, 0xcb]
---
0xc0 JUMPDEST
0xc1 CALLVALUE
0xc2 ISZERO
0xc3 PUSH2 0xcb
0xc6 JUMPI
---
0xc0: JUMPDEST 
0xc1: V64 = CALLVALUE
0xc2: V65 = ISZERO V64
0xc3: V66 = 0xcb
0xc6: JUMPI 0xcb V65
---
Entry stack: [V12]
Stack pops: 0
Stack additions: []
Exit stack: [V12]

================================

Block 0xc7
[0xc7:0xca]
---
Predecessors: [0xc0]
Successors: []
---
0xc7 PUSH1 0x0
0xc9 DUP1
0xca REVERT
---
0xc7: V67 = 0x0
0xca: REVERT 0x0 0x0
---
Entry stack: [V12]
Stack pops: 0
Stack additions: []
Exit stack: [V12]

================================

Block 0xcb
[0xcb:0xd2]
---
Predecessors: [0xc0]
Successors: [0x298]
---
0xcb JUMPDEST
0xcc PUSH2 0x76
0xcf PUSH2 0x298
0xd2 JUMP
---
0xcb: JUMPDEST 
0xcc: V68 = 0x76
0xcf: V69 = 0x298
0xd2: JUMP 0x298
---
Entry stack: [V12]
Stack pops: 0
Stack additions: [0x76]
Exit stack: [V12, 0x76]

================================

Block 0xd3
[0xd3:0xd4]
---
Predecessors: []
Successors: []
---
0xd3 JUMPDEST
0xd4 STOP
---
0xd3: JUMPDEST 
0xd4: STOP 
---
Entry stack: []
Stack pops: 0
Stack additions: []
Exit stack: []

================================

Block 0xd5
[0xd5:0xeb]
---
Predecessors: [0x46]
Successors: [0x2b8]
---
0xd5 JUMPDEST
0xd6 PUSH2 0x76
0xd9 PUSH1 0x1
0xdb PUSH1 0xa0
0xdd PUSH1 0x2
0xdf EXP
0xe0 SUB
0xe1 PUSH1 0x4
0xe3 CALLDATALOAD
0xe4 AND
0xe5 PUSH1 0x24
0xe7 CALLDATALOAD
0xe8 PUSH2 0x2b8
0xeb JUMP
---
0xd5: JUMPDEST 
0xd6: V70 = 0x76
0xd9: V71 = 0x1
0xdb: V72 = 0xa0
0xdd: V73 = 0x2
0xdf: V74 = EXP 0x2 0xa0
0xe0: V75 = SUB 0x10000000000000000000000000000000000000000 0x1
0xe1: V76 = 0x4
0xe3: V77 = CALLDATALOAD 0x4
0xe4: V78 = AND V77 0xffffffffffffffffffffffffffffffffffffffff
0xe5: V79 = 0x24
0xe7: V80 = CALLDATALOAD 0x24
0xe8: V81 = 0x2b8
0xeb: JUMP 0x2b8
---
Entry stack: [V12]
Stack pops: 0
Stack additions: [0x76, V78, V80]
Exit stack: [V12, 0x76, V78, V80]

================================

Block 0xec
[0xec:0xed]
---
Predecessors: []
Successors: []
---
0xec JUMPDEST
0xed STOP
---
0xec: JUMPDEST 
0xed: STOP 
---
Entry stack: []
Stack pops: 0
Stack additions: []
Exit stack: []

================================

Block 0xee
[0xee:0xf4]
---
Predecessors: [0x51]
Successors: [0xf5, 0xf9]
---
0xee JUMPDEST
0xef CALLVALUE
0xf0 ISZERO
0xf1 PUSH2 0xf9
0xf4 JUMPI
---
0xee: JUMPDEST 
0xef: V82 = CALLVALUE
0xf0: V83 = ISZERO V82
0xf1: V84 = 0xf9
0xf4: JUMPI 0xf9 V83
---
Entry stack: [V12]
Stack pops: 0
Stack additions: []
Exit stack: [V12]

================================

Block 0xf5
[0xf5:0xf8]
---
Predecessors: [0xee]
Successors: []
---
0xf5 PUSH1 0x0
0xf7 DUP1
0xf8 REVERT
---
0xf5: V85 = 0x0
0xf8: REVERT 0x0 0x0
---
Entry stack: [V12]
Stack pops: 0
Stack additions: []
Exit stack: [V12]

================================

Block 0xf9
[0xf9:0x100]
---
Predecessors: [0xee]
Successors: [0x3bb]
---
0xf9 JUMPDEST
0xfa PUSH2 0x101
0xfd PUSH2 0x3bb
0x100 JUMP
---
0xf9: JUMPDEST 
0xfa: V86 = 0x101
0xfd: V87 = 0x3bb
0x100: JUMP 0x3bb
---
Entry stack: [V12]
Stack pops: 0
Stack additions: [0x101]
Exit stack: [V12, 0x101]

================================

Block 0x101
[0x101:0x11c]
---
Predecessors: [0x3bb]
Successors: []
---
0x101 JUMPDEST
0x102 PUSH1 0x40
0x104 MLOAD
0x105 PUSH1 0x1
0x107 PUSH1 0xa0
0x109 PUSH1 0x2
0x10b EXP
0x10c SUB
0x10d SWAP1
0x10e SWAP2
0x10f AND
0x110 DUP2
0x111 MSTORE
0x112 PUSH1 0x20
0x114 ADD
0x115 PUSH1 0x40
0x117 MLOAD
0x118 DUP1
0x119 SWAP2
0x11a SUB
0x11b SWAP1
0x11c RETURN
---
0x101: JUMPDEST 
0x102: V88 = 0x40
0x104: V89 = M[0x40]
0x105: V90 = 0x1
0x107: V91 = 0xa0
0x109: V92 = 0x2
0x10b: V93 = EXP 0x2 0xa0
0x10c: V94 = SUB 0x10000000000000000000000000000000000000000 0x1
0x10f: V95 = AND V363 0xffffffffffffffffffffffffffffffffffffffff
0x111: M[V89] = V95
0x112: V96 = 0x20
0x114: V97 = ADD 0x20 V89
0x115: V98 = 0x40
0x117: V99 = M[0x40]
0x11a: V100 = SUB V97 V99
0x11c: RETURN V99 V100
---
Entry stack: [V12, 0x101, V363]
Stack pops: 1
Stack additions: []
Exit stack: [V12, 0x101]

================================

Block 0x11d
[0x11d:0x124]
---
Predecessors: [0x5c]
Successors: [0x127]
---
0x11d JUMPDEST
0x11e PUSH2 0x76
0x121 PUSH2 0x127
0x124 JUMP
---
0x11d: JUMPDEST 
0x11e: V101 = 0x76
0x121: V102 = 0x127
0x124: JUMP 0x127
---
Entry stack: [V12]
Stack pops: 0
Stack additions: [0x76]
Exit stack: [V12, 0x76]

================================

Block 0x125
[0x125:0x126]
---
Predecessors: []
Successors: []
---
0x125 JUMPDEST
0x126 STOP
---
0x125: JUMPDEST 
0x126: STOP 
---
Entry stack: []
Stack pops: 0
Stack additions: []
Exit stack: []

================================

Block 0x127
[0x127:0x136]
---
Predecessors: [0x6b, 0x11d, 0x18e]
Successors: [0x73, 0x137]
---
0x127 JUMPDEST
0x128 PUSH8 0xde0b6b3a7640000
0x131 CALLVALUE
0x132 LT
0x133 PUSH2 0x73
0x136 JUMPI
---
0x127: JUMPDEST 
0x128: V103 = 0xde0b6b3a7640000
0x131: V104 = CALLVALUE
0x132: V105 = LT V104 0xde0b6b3a7640000
0x133: V106 = 0x73
0x136: JUMPI 0x73 V105
---
Entry stack: [V12, S1, {0x73, 0x76}]
Stack pops: 0
Stack additions: []
Exit stack: [V12, S1, {0x73, 0x76}]

================================

Block 0x137
[0x137:0x18a]
---
Predecessors: [0x127]
Successors: [0x18b]
---
0x137 PUSH1 0x1
0x139 PUSH1 0xa0
0x13b PUSH1 0x2
0x13d EXP
0x13e SUB
0x13f CALLER
0x140 AND
0x141 PUSH1 0x0
0x143 SWAP1
0x144 DUP2
0x145 MSTORE
0x146 PUSH1 0x2
0x148 PUSH1 0x20
0x14a MSTORE
0x14b PUSH1 0x40
0x14d SWAP1
0x14e DUP2
0x14f SWAP1
0x150 SHA3
0x151 DUP1
0x152 SLOAD
0x153 CALLVALUE
0x154 SWAP1
0x155 DUP2
0x156 ADD
0x157 SWAP1
0x158 SWAP2
0x159 SSTORE
0x15a PUSH32 0x4d6ce1e535dbade1c23defba91e23b8f791ce5edc0cc320257a2b364e4e38426
0x17b SWAP2
0x17c MLOAD
0x17d SWAP1
0x17e DUP2
0x17f MSTORE
0x180 PUSH1 0x20
0x182 ADD
0x183 PUSH1 0x40
0x185 MLOAD
0x186 DUP1
0x187 SWAP2
0x188 SUB
0x189 SWAP1
0x18a LOG1
---
0x137: V107 = 0x1
0x139: V108 = 0xa0
0x13b: V109 = 0x2
0x13d: V110 = EXP 0x2 0xa0
0x13e: V111 = SUB 0x10000000000000000000000000000000000000000 0x1
0x13f: V112 = CALLER
0x140: V113 = AND V112 0xffffffffffffffffffffffffffffffffffffffff
0x141: V114 = 0x0
0x145: M[0x0] = V113
0x146: V115 = 0x2
0x148: V116 = 0x20
0x14a: M[0x20] = 0x2
0x14b: V117 = 0x40
0x150: V118 = SHA3 0x0 0x40
0x152: V119 = S[V118]
0x153: V120 = CALLVALUE
0x156: V121 = ADD V120 V119
0x159: S[V118] = V121
0x15a: V122 = 0x4d6ce1e535dbade1c23defba91e23b8f791ce5edc0cc320257a2b364e4e38426
0x17c: V123 = M[0x40]
0x17f: M[V123] = V120
0x180: V124 = 0x20
0x182: V125 = ADD 0x20 V123
0x183: V126 = 0x40
0x185: V127 = M[0x40]
0x188: V128 = SUB V125 V127
0x18a: LOG V127 V128 0x4d6ce1e535dbade1c23defba91e23b8f791ce5edc0cc320257a2b364e4e38426
---
Entry stack: [V12, S1, {0x73, 0x76}]
Stack pops: 0
Stack additions: []
Exit stack: [V12, S1, {0x73, 0x76}]

================================

Block 0x18b
[0x18b:0x18b]
---
Predecessors: [0x137]
Successors: [0x18c]
---
0x18b JUMPDEST
---
0x18b: JUMPDEST 
---
Entry stack: [V12, S1, {0x73, 0x76}]
Stack pops: 0
Stack additions: []
Exit stack: [V12, S1, {0x73, 0x76}]

================================

Block 0x18c
[0x18c:0x18d]
---
Predecessors: [0x18b]
Successors: [0x73, 0x76]
---
0x18c JUMPDEST
0x18d JUMP
---
0x18c: JUMPDEST 
0x18d: JUMP {0x73, 0x76}
---
Entry stack: [V12, S1, {0x73, 0x76}]
Stack pops: 1
Stack additions: []
Exit stack: [V12, S1]

================================

Block 0x18e
[0x18e:0x1bd]
---
Predecessors: [0x78]
Successors: [0x127]
---
0x18e JUMPDEST
0x18f PUSH1 0x1
0x191 DUP1
0x192 SLOAD
0x193 PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x1a8 NOT
0x1a9 AND
0x1aa CALLER
0x1ab PUSH1 0x1
0x1ad PUSH1 0xa0
0x1af PUSH1 0x2
0x1b1 EXP
0x1b2 SUB
0x1b3 AND
0x1b4 OR
0x1b5 SWAP1
0x1b6 SSTORE
0x1b7 PUSH2 0x73
0x1ba PUSH2 0x127
0x1bd JUMP
---
0x18e: JUMPDEST 
0x18f: V129 = 0x1
0x192: V130 = S[0x1]
0x193: V131 = 0xffffffffffffffffffffffffffffffffffffffff
0x1a8: V132 = NOT 0xffffffffffffffffffffffffffffffffffffffff
0x1a9: V133 = AND 0xffffffffffffffffffffffff0000000000000000000000000000000000000000 V130
0x1aa: V134 = CALLER
0x1ab: V135 = 0x1
0x1ad: V136 = 0xa0
0x1af: V137 = 0x2
0x1b1: V138 = EXP 0x2 0xa0
0x1b2: V139 = SUB 0x10000000000000000000000000000000000000000 0x1
0x1b3: V140 = AND 0xffffffffffffffffffffffffffffffffffffffff V134
0x1b4: V141 = OR V140 V133
0x1b6: S[0x1] = V141
0x1b7: V142 = 0x73
0x1ba: V143 = 0x127
0x1bd: JUMP 0x127
---
Entry stack: [V12, 0x76]
Stack pops: 0
Stack additions: [0x73]
Exit stack: [V12, 0x76, 0x73]

================================

Block 0x1be
[0x1be:0x1be]
---
Predecessors: []
Successors: [0x1bf]
---
0x1be JUMPDEST
---
0x1be: JUMPDEST 
---
Entry stack: []
Stack pops: 0
Stack additions: []
Exit stack: []

================================

Block 0x1bf
[0x1bf:0x1c0]
---
Predecessors: [0x1be]
Successors: []
Has unresolved jump.
---
0x1bf JUMPDEST
0x1c0 JUMP
---
0x1bf: JUMPDEST 
0x1c0: JUMP S0
---
Entry stack: []
Stack pops: 1
Stack additions: []
Exit stack: []

================================

Block 0x1c1
[0x1c1:0x1d8]
---
Predecessors: [0x82]
Successors: [0x1d9, 0x280]
---
0x1c1 JUMPDEST
0x1c2 PUSH1 0x0
0x1c4 SLOAD
0x1c5 CALLER
0x1c6 PUSH1 0x1
0x1c8 PUSH1 0xa0
0x1ca PUSH1 0x2
0x1cc EXP
0x1cd SUB
0x1ce SWAP1
0x1cf DUP2
0x1d0 AND
0x1d1 SWAP2
0x1d2 AND
0x1d3 EQ
0x1d4 ISZERO
0x1d5 PUSH2 0x280
0x1d8 JUMPI
---
0x1c1: JUMPDEST 
0x1c2: V144 = 0x0
0x1c4: V145 = S[0x0]
0x1c5: V146 = CALLER
0x1c6: V147 = 0x1
0x1c8: V148 = 0xa0
0x1ca: V149 = 0x2
0x1cc: V150 = EXP 0x2 0xa0
0x1cd: V151 = SUB 0x10000000000000000000000000000000000000000 0x1
0x1d0: V152 = AND 0xffffffffffffffffffffffffffffffffffffffff V146
0x1d2: V153 = AND V145 0xffffffffffffffffffffffffffffffffffffffff
0x1d3: V154 = EQ V153 V152
0x1d4: V155 = ISZERO V154
0x1d5: V156 = 0x280
0x1d8: JUMPI 0x280 V155
---
Entry stack: [V12, 0x76, V41]
Stack pops: 0
Stack additions: []
Exit stack: [V12, 0x76, V41]

================================

Block 0x1d9
[0x1d9:0x1f8]
---
Predecessors: [0x1c1]
Successors: [0x1f9, 0x216]
---
0x1d9 PUSH1 0x1
0x1db PUSH1 0xa0
0x1dd PUSH1 0x2
0x1df EXP
0x1e0 SUB
0x1e1 CALLER
0x1e2 AND
0x1e3 PUSH1 0x0
0x1e5 SWAP1
0x1e6 DUP2
0x1e7 MSTORE
0x1e8 PUSH1 0x2
0x1ea PUSH1 0x20
0x1ec MSTORE
0x1ed PUSH1 0x40
0x1ef DUP2
0x1f0 SHA3
0x1f1 SLOAD
0x1f2 GT
0x1f3 DUP1
0x1f4 ISZERO
0x1f5 PUSH2 0x216
0x1f8 JUMPI
---
0x1d9: V157 = 0x1
0x1db: V158 = 0xa0
0x1dd: V159 = 0x2
0x1df: V160 = EXP 0x2 0xa0
0x1e0: V161 = SUB 0x10000000000000000000000000000000000000000 0x1
0x1e1: V162 = CALLER
0x1e2: V163 = AND V162 0xffffffffffffffffffffffffffffffffffffffff
0x1e3: V164 = 0x0
0x1e7: M[0x0] = V163
0x1e8: V165 = 0x2
0x1ea: V166 = 0x20
0x1ec: M[0x20] = 0x2
0x1ed: V167 = 0x40
0x1f0: V168 = SHA3 0x0 0x40
0x1f1: V169 = S[V168]
0x1f2: V170 = GT V169 0x0
0x1f4: V171 = ISZERO V170
0x1f5: V172 = 0x216
0x1f8: JUMPI 0x216 V171
---
Entry stack: [V12, 0x76, V41]
Stack pops: 0
Stack additions: [V170]
Exit stack: [V12, 0x76, V41, V170]

================================

Block 0x1f9
[0x1f9:0x215]
---
Predecessors: [0x1d9]
Successors: [0x216]
---
0x1f9 POP
0x1fa PUSH1 0x1
0x1fc PUSH1 0xa0
0x1fe PUSH1 0x2
0x200 EXP
0x201 SUB
0x202 CALLER
0x203 AND
0x204 PUSH1 0x0
0x206 SWAP1
0x207 DUP2
0x208 MSTORE
0x209 PUSH1 0x2
0x20b PUSH1 0x20
0x20d MSTORE
0x20e PUSH1 0x40
0x210 SWAP1
0x211 SHA3
0x212 SLOAD
0x213 DUP2
0x214 GT
0x215 ISZERO
---
0x1fa: V173 = 0x1
0x1fc: V174 = 0xa0
0x1fe: V175 = 0x2
0x200: V176 = EXP 0x2 0xa0
0x201: V177 = SUB 0x10000000000000000000000000000000000000000 0x1
0x202: V178 = CALLER
0x203: V179 = AND V178 0xffffffffffffffffffffffffffffffffffffffff
0x204: V180 = 0x0
0x208: M[0x0] = V179
0x209: V181 = 0x2
0x20b: V182 = 0x20
0x20d: M[0x20] = 0x2
0x20e: V183 = 0x40
0x211: V184 = SHA3 0x0 0x40
0x212: V185 = S[V184]
0x214: V186 = GT V41 V185
0x215: V187 = ISZERO V186
---
Entry stack: [V12, 0x76, V41, V170]
Stack pops: 2
Stack additions: [S1, V187]
Exit stack: [V12, 0x76, V41, V187]

================================

Block 0x216
[0x216:0x21b]
---
Predecessors: [0x1d9, 0x1f9]
Successors: [0x21c, 0x280]
---
0x216 JUMPDEST
0x217 ISZERO
0x218 PUSH2 0x280
0x21b JUMPI
---
0x216: JUMPDEST 
0x217: V188 = ISZERO S0
0x218: V189 = 0x280
0x21b: JUMPI 0x280 V188
---
Entry stack: [V12, 0x76, V41, S0]
Stack pops: 1
Stack additions: []
Exit stack: [V12, 0x76, V41]

================================

Block 0x21c
[0x21c:0x247]
---
Predecessors: [0x216]
Successors: [0x248, 0x24c]
---
0x21c PUSH1 0x1
0x21e PUSH1 0xa0
0x220 PUSH1 0x2
0x222 EXP
0x223 SUB
0x224 CALLER
0x225 AND
0x226 DUP2
0x227 ISZERO
0x228 PUSH2 0x8fc
0x22b MUL
0x22c DUP3
0x22d PUSH1 0x40
0x22f MLOAD
0x230 PUSH1 0x0
0x232 PUSH1 0x40
0x234 MLOAD
0x235 DUP1
0x236 DUP4
0x237 SUB
0x238 DUP2
0x239 DUP6
0x23a DUP9
0x23b DUP9
0x23c CALL
0x23d SWAP4
0x23e POP
0x23f POP
0x240 POP
0x241 POP
0x242 ISZERO
0x243 ISZERO
0x244 PUSH2 0x24c
0x247 JUMPI
---
0x21c: V190 = 0x1
0x21e: V191 = 0xa0
0x220: V192 = 0x2
0x222: V193 = EXP 0x2 0xa0
0x223: V194 = SUB 0x10000000000000000000000000000000000000000 0x1
0x224: V195 = CALLER
0x225: V196 = AND V195 0xffffffffffffffffffffffffffffffffffffffff
0x227: V197 = ISZERO V41
0x228: V198 = 0x8fc
0x22b: V199 = MUL 0x8fc V197
0x22d: V200 = 0x40
0x22f: V201 = M[0x40]
0x230: V202 = 0x0
0x232: V203 = 0x40
0x234: V204 = M[0x40]
0x237: V205 = SUB V201 V204
0x23c: V206 = CALL V199 V196 V41 V204 V205 V204 0x0
0x242: V207 = ISZERO V206
0x243: V208 = ISZERO V207
0x244: V209 = 0x24c
0x247: JUMPI 0x24c V208
---
Entry stack: [V12, 0x76, V41]
Stack pops: 1
Stack additions: [S0]
Exit stack: [V12, 0x76, V41]

================================

Block 0x248
[0x248:0x24b]
---
Predecessors: [0x21c]
Successors: []
---
0x248 PUSH1 0x0
0x24a DUP1
0x24b REVERT
---
0x248: V210 = 0x0
0x24b: REVERT 0x0 0x0
---
Entry stack: [V12, 0x76, V41]
Stack pops: 0
Stack additions: []
Exit stack: [V12, 0x76, V41]

================================

Block 0x24c
[0x24c:0x27f]
---
Predecessors: [0x21c]
Successors: [0x280]
---
0x24c JUMPDEST
0x24d PUSH32 0x5b6b431d4476a211bb7d41c20d1aab9ae2321deee0d20be3d9fc9b1093fa6e3d
0x26e DUP2
0x26f PUSH1 0x40
0x271 MLOAD
0x272 SWAP1
0x273 DUP2
0x274 MSTORE
0x275 PUSH1 0x20
0x277 ADD
0x278 PUSH1 0x40
0x27a MLOAD
0x27b DUP1
0x27c SWAP2
0x27d SUB
0x27e SWAP1
0x27f LOG1
---
0x24c: JUMPDEST 
0x24d: V211 = 0x5b6b431d4476a211bb7d41c20d1aab9ae2321deee0d20be3d9fc9b1093fa6e3d
0x26f: V212 = 0x40
0x271: V213 = M[0x40]
0x274: M[V213] = V41
0x275: V214 = 0x20
0x277: V215 = ADD 0x20 V213
0x278: V216 = 0x40
0x27a: V217 = M[0x40]
0x27d: V218 = SUB V215 V217
0x27f: LOG V217 V218 0x5b6b431d4476a211bb7d41c20d1aab9ae2321deee0d20be3d9fc9b1093fa6e3d
---
Entry stack: [V12, 0x76, V41]
Stack pops: 1
Stack additions: [S0]
Exit stack: [V12, 0x76, V41]

================================

Block 0x280
[0x280:0x280]
---
Predecessors: [0x1c1, 0x216, 0x24c]
Successors: [0x281]
---
0x280 JUMPDEST
---
0x280: JUMPDEST 
---
Entry stack: [V12, 0x76, V41]
Stack pops: 0
Stack additions: []
Exit stack: [V12, 0x76, V41]

================================

Block 0x281
[0x281:0x281]
---
Predecessors: [0x280]
Successors: [0x282]
---
0x281 JUMPDEST
---
0x281: JUMPDEST 
---
Entry stack: [V12, 0x76, V41]
Stack pops: 0
Stack additions: []
Exit stack: [V12, 0x76, V41]

================================

Block 0x282
[0x282:0x282]
---
Predecessors: [0x281]
Successors: [0x283]
---
0x282 JUMPDEST
---
0x282: JUMPDEST 
---
Entry stack: [V12, 0x76, V41]
Stack pops: 0
Stack additions: []
Exit stack: [V12, 0x76, V41]

================================

Block 0x283
[0x283:0x285]
---
Predecessors: [0x282]
Successors: [0x76]
---
0x283 JUMPDEST
0x284 POP
0x285 JUMP
---
0x283: JUMPDEST 
0x285: JUMP 0x76
---
Entry stack: [V12, 0x76, V41]
Stack pops: 2
Stack additions: []
Exit stack: [V12]

================================

Block 0x286
[0x286:0x297]
---
Predecessors: [0x9a]
Successors: [0xae]
---
0x286 JUMPDEST
0x287 PUSH1 0x2
0x289 PUSH1 0x20
0x28b MSTORE
0x28c PUSH1 0x0
0x28e SWAP1
0x28f DUP2
0x290 MSTORE
0x291 PUSH1 0x40
0x293 SWAP1
0x294 SHA3
0x295 SLOAD
0x296 DUP2
0x297 JUMP
---
0x286: JUMPDEST 
0x287: V219 = 0x2
0x289: V220 = 0x20
0x28b: M[0x20] = 0x2
0x28c: V221 = 0x0
0x290: M[0x0] = V55
0x291: V222 = 0x40
0x294: V223 = SHA3 0x0 0x40
0x295: V224 = S[V223]
0x297: JUMP 0xae
---
Entry stack: [V12, 0xae, V55]
Stack pops: 2
Stack additions: [S1, V224]
Exit stack: [V12, 0xae, V224]

================================

Block 0x298
[0x298:0x2a9]
---
Predecessors: [0xcb]
Successors: [0x73, 0x2aa]
---
0x298 JUMPDEST
0x299 PUSH1 0x1
0x29b PUSH1 0xa0
0x29d PUSH1 0x2
0x29f EXP
0x2a0 SUB
0x2a1 ADDRESS
0x2a2 AND
0x2a3 BALANCE
0x2a4 ISZERO
0x2a5 ISZERO
0x2a6 PUSH2 0x73
0x2a9 JUMPI
---
0x298: JUMPDEST 
0x299: V225 = 0x1
0x29b: V226 = 0xa0
0x29d: V227 = 0x2
0x29f: V228 = EXP 0x2 0xa0
0x2a0: V229 = SUB 0x10000000000000000000000000000000000000000 0x1
0x2a1: V230 = ADDRESS
0x2a2: V231 = AND V230 0xffffffffffffffffffffffffffffffffffffffff
0x2a3: V232 = BALANCE V231
0x2a4: V233 = ISZERO V232
0x2a5: V234 = ISZERO V233
0x2a6: V235 = 0x73
0x2a9: JUMPI 0x73 V234
---
Entry stack: [V12, 0x76]
Stack pops: 0
Stack additions: []
Exit stack: [V12, 0x76]

================================

Block 0x2aa
[0x2aa:0x2b4]
---
Predecessors: [0x298]
Successors: []
---
0x2aa CALLER
0x2ab PUSH1 0x1
0x2ad PUSH1 0xa0
0x2af PUSH1 0x2
0x2b1 EXP
0x2b2 SUB
0x2b3 AND
0x2b4 SELFDESTRUCT
---
0x2aa: V236 = CALLER
0x2ab: V237 = 0x1
0x2ad: V238 = 0xa0
0x2af: V239 = 0x2
0x2b1: V240 = EXP 0x2 0xa0
0x2b2: V241 = SUB 0x10000000000000000000000000000000000000000 0x1
0x2b3: V242 = AND 0xffffffffffffffffffffffffffffffffffffffff V236
0x2b4: SELFDESTRUCT V242
---
Entry stack: [V12, 0x76]
Stack pops: 0
Stack additions: []
Exit stack: [V12, 0x76]

================================

Block 0x2b5
[0x2b5:0x2b5]
---
Predecessors: []
Successors: [0x2b6]
---
0x2b5 JUMPDEST
---
0x2b5: JUMPDEST 
---
Entry stack: []
Stack pops: 0
Stack additions: []
Exit stack: []

================================

Block 0x2b6
[0x2b6:0x2b7]
---
Predecessors: [0x2b5]
Successors: []
Has unresolved jump.
---
0x2b6 JUMPDEST
0x2b7 JUMP
---
0x2b6: JUMPDEST 
0x2b7: JUMP S0
---
Entry stack: []
Stack pops: 1
Stack additions: []
Exit stack: []

================================

Block 0x2b8
[0x2b8:0x2d0]
---
Predecessors: [0xd5]
Successors: [0x2d1, 0x3b3]
---
0x2b8 JUMPDEST
0x2b9 PUSH1 0x0
0x2bb DUP1
0x2bc SLOAD
0x2bd CALLER
0x2be PUSH1 0x1
0x2c0 PUSH1 0xa0
0x2c2 PUSH1 0x2
0x2c4 EXP
0x2c5 SUB
0x2c6 SWAP1
0x2c7 DUP2
0x2c8 AND
0x2c9 SWAP2
0x2ca AND
0x2cb EQ
0x2cc ISZERO
0x2cd PUSH2 0x3b3
0x2d0 JUMPI
---
0x2b8: JUMPDEST 
0x2b9: V243 = 0x0
0x2bc: V244 = S[0x0]
0x2bd: V245 = CALLER
0x2be: V246 = 0x1
0x2c0: V247 = 0xa0
0x2c2: V248 = 0x2
0x2c4: V249 = EXP 0x2 0xa0
0x2c5: V250 = SUB 0x10000000000000000000000000000000000000000 0x1
0x2c8: V251 = AND 0xffffffffffffffffffffffffffffffffffffffff V245
0x2ca: V252 = AND V244 0xffffffffffffffffffffffffffffffffffffffff
0x2cb: V253 = EQ V252 V251
0x2cc: V254 = ISZERO V253
0x2cd: V255 = 0x3b3
0x2d0: JUMPI 0x3b3 V254
---
Entry stack: [V12, 0x76, V78, V80]
Stack pops: 0
Stack additions: [0x0]
Exit stack: [V12, 0x76, V78, V80, 0x0]

================================

Block 0x2d1
[0x2d1:0x322]
---
Predecessors: [0x2b8]
Successors: [0x323, 0x327]
---
0x2d1 DUP3
0x2d2 PUSH1 0x1
0x2d4 PUSH1 0xa0
0x2d6 PUSH1 0x2
0x2d8 EXP
0x2d9 SUB
0x2da AND
0x2db PUSH4 0x70a08231
0x2e0 ADDRESS
0x2e1 PUSH1 0x0
0x2e3 PUSH1 0x40
0x2e5 MLOAD
0x2e6 PUSH1 0x20
0x2e8 ADD
0x2e9 MSTORE
0x2ea PUSH1 0x40
0x2ec MLOAD
0x2ed PUSH1 0xe0
0x2ef PUSH1 0x2
0x2f1 EXP
0x2f2 PUSH4 0xffffffff
0x2f7 DUP5
0x2f8 AND
0x2f9 MUL
0x2fa DUP2
0x2fb MSTORE
0x2fc PUSH1 0x1
0x2fe PUSH1 0xa0
0x300 PUSH1 0x2
0x302 EXP
0x303 SUB
0x304 SWAP1
0x305 SWAP2
0x306 AND
0x307 PUSH1 0x4
0x309 DUP3
0x30a ADD
0x30b MSTORE
0x30c PUSH1 0x24
0x30e ADD
0x30f PUSH1 0x20
0x311 PUSH1 0x40
0x313 MLOAD
0x314 DUP1
0x315 DUP4
0x316 SUB
0x317 DUP2
0x318 PUSH1 0x0
0x31a DUP8
0x31b DUP1
0x31c EXTCODESIZE
0x31d ISZERO
0x31e ISZERO
0x31f PUSH2 0x327
0x322 JUMPI
---
0x2d2: V256 = 0x1
0x2d4: V257 = 0xa0
0x2d6: V258 = 0x2
0x2d8: V259 = EXP 0x2 0xa0
0x2d9: V260 = SUB 0x10000000000000000000000000000000000000000 0x1
0x2da: V261 = AND 0xffffffffffffffffffffffffffffffffffffffff V78
0x2db: V262 = 0x70a08231
0x2e0: V263 = ADDRESS
0x2e1: V264 = 0x0
0x2e3: V265 = 0x40
0x2e5: V266 = M[0x40]
0x2e6: V267 = 0x20
0x2e8: V268 = ADD 0x20 V266
0x2e9: M[V268] = 0x0
0x2ea: V269 = 0x40
0x2ec: V270 = M[0x40]
0x2ed: V271 = 0xe0
0x2ef: V272 = 0x2
0x2f1: V273 = EXP 0x2 0xe0
0x2f2: V274 = 0xffffffff
0x2f8: V275 = AND 0x70a08231 0xffffffff
0x2f9: V276 = MUL 0x70a08231 0x100000000000000000000000000000000000000000000000000000000
0x2fb: M[V270] = 0x70a0823100000000000000000000000000000000000000000000000000000000
0x2fc: V277 = 0x1
0x2fe: V278 = 0xa0
0x300: V279 = 0x2
0x302: V280 = EXP 0x2 0xa0
0x303: V281 = SUB 0x10000000000000000000000000000000000000000 0x1
0x306: V282 = AND V263 0xffffffffffffffffffffffffffffffffffffffff
0x307: V283 = 0x4
0x30a: V284 = ADD V270 0x4
0x30b: M[V284] = V282
0x30c: V285 = 0x24
0x30e: V286 = ADD 0x24 V270
0x30f: V287 = 0x20
0x311: V288 = 0x40
0x313: V289 = M[0x40]
0x316: V290 = SUB V286 V289
0x318: V291 = 0x0
0x31c: V292 = EXTCODESIZE V261
0x31d: V293 = ISZERO V292
0x31e: V294 = ISZERO V293
0x31f: V295 = 0x327
0x322: JUMPI 0x327 V294
---
Entry stack: [V12, 0x76, V78, V80, 0x0]
Stack pops: 3
Stack additions: [S2, S1, S0, V261, 0x70a08231, V286, 0x20, V289, V290, V289, 0x0, V261]
Exit stack: [V12, 0x76, V78, V80, 0x0, V261, 0x70a08231, V286, 0x20, V289, V290, V289, 0x0, V261]

================================

Block 0x323
[0x323:0x326]
---
Predecessors: [0x2d1]
Successors: []
---
0x323 PUSH1 0x0
0x325 DUP1
0x326 REVERT
---
0x323: V296 = 0x0
0x326: REVERT 0x0 0x0
---
Entry stack: [V12, 0x76, V78, V80, 0x0, V261, 0x70a08231, V286, 0x20, V289, V290, V289, 0x0, V261]
Stack pops: 0
Stack additions: []
Exit stack: [V12, 0x76, V78, V80, 0x0, V261, 0x70a08231, V286, 0x20, V289, V290, V289, 0x0, V261]

================================

Block 0x327
[0x327:0x333]
---
Predecessors: [0x2d1]
Successors: [0x334, 0x338]
---
0x327 JUMPDEST
0x328 PUSH2 0x2c6
0x32b GAS
0x32c SUB
0x32d CALL
0x32e ISZERO
0x32f ISZERO
0x330 PUSH2 0x338
0x333 JUMPI
---
0x327: JUMPDEST 
0x328: V297 = 0x2c6
0x32b: V298 = GAS
0x32c: V299 = SUB V298 0x2c6
0x32d: V300 = CALL V299 V261 0x0 V289 V290 V289 0x20
0x32e: V301 = ISZERO V300
0x32f: V302 = ISZERO V301
0x330: V303 = 0x338
0x333: JUMPI 0x338 V302
---
Entry stack: [V12, 0x76, V78, V80, 0x0, V261, 0x70a08231, V286, 0x20, V289, V290, V289, 0x0, V261]
Stack pops: 6
Stack additions: []
Exit stack: [V12, 0x76, V78, V80, 0x0, V261, 0x70a08231, V286]

================================

Block 0x334
[0x334:0x337]
---
Predecessors: [0x327]
Successors: []
---
0x334 PUSH1 0x0
0x336 DUP1
0x337 REVERT
---
0x334: V304 = 0x0
0x337: REVERT 0x0 0x0
---
Entry stack: [V12, 0x76, V78, V80, 0x0, V261, 0x70a08231, V286]
Stack pops: 0
Stack additions: []
Exit stack: [V12, 0x76, V78, V80, 0x0, V261, 0x70a08231, V286]

================================

Block 0x338
[0x338:0x34a]
---
Predecessors: [0x327]
Successors: [0x34b, 0x3b3]
---
0x338 JUMPDEST
0x339 POP
0x33a POP
0x33b POP
0x33c PUSH1 0x40
0x33e MLOAD
0x33f DUP1
0x340 MLOAD
0x341 SWAP2
0x342 POP
0x343 POP
0x344 DUP2
0x345 DUP2
0x346 LT
0x347 PUSH2 0x3b3
0x34a JUMPI
---
0x338: JUMPDEST 
0x33c: V305 = 0x40
0x33e: V306 = M[0x40]
0x340: V307 = M[V306]
0x346: V308 = LT V307 V80
0x347: V309 = 0x3b3
0x34a: JUMPI 0x3b3 V308
---
Entry stack: [V12, 0x76, V78, V80, 0x0, V261, 0x70a08231, V286]
Stack pops: 5
Stack additions: [S4, V307]
Exit stack: [V12, 0x76, V78, V80, V307]

================================

Block 0x34b
[0x34b:0x399]
---
Predecessors: [0x338]
Successors: [0x39a, 0x39e]
---
0x34b DUP3
0x34c PUSH1 0x1
0x34e PUSH1 0xa0
0x350 PUSH1 0x2
0x352 EXP
0x353 SUB
0x354 AND
0x355 PUSH4 0xa9059cbb
0x35a CALLER
0x35b DUP5
0x35c PUSH1 0x40
0x35e MLOAD
0x35f PUSH1 0xe0
0x361 PUSH1 0x2
0x363 EXP
0x364 PUSH4 0xffffffff
0x369 DUP6
0x36a AND
0x36b MUL
0x36c DUP2
0x36d MSTORE
0x36e PUSH1 0x1
0x370 PUSH1 0xa0
0x372 PUSH1 0x2
0x374 EXP
0x375 SUB
0x376 SWAP1
0x377 SWAP3
0x378 AND
0x379 PUSH1 0x4
0x37b DUP4
0x37c ADD
0x37d MSTORE
0x37e PUSH1 0x24
0x380 DUP3
0x381 ADD
0x382 MSTORE
0x383 PUSH1 0x44
0x385 ADD
0x386 PUSH1 0x0
0x388 PUSH1 0x40
0x38a MLOAD
0x38b DUP1
0x38c DUP4
0x38d SUB
0x38e DUP2
0x38f PUSH1 0x0
0x391 DUP8
0x392 DUP1
0x393 EXTCODESIZE
0x394 ISZERO
0x395 ISZERO
0x396 PUSH2 0x39e
0x399 JUMPI
---
0x34c: V310 = 0x1
0x34e: V311 = 0xa0
0x350: V312 = 0x2
0x352: V313 = EXP 0x2 0xa0
0x353: V314 = SUB 0x10000000000000000000000000000000000000000 0x1
0x354: V315 = AND 0xffffffffffffffffffffffffffffffffffffffff V78
0x355: V316 = 0xa9059cbb
0x35a: V317 = CALLER
0x35c: V318 = 0x40
0x35e: V319 = M[0x40]
0x35f: V320 = 0xe0
0x361: V321 = 0x2
0x363: V322 = EXP 0x2 0xe0
0x364: V323 = 0xffffffff
0x36a: V324 = AND 0xa9059cbb 0xffffffff
0x36b: V325 = MUL 0xa9059cbb 0x100000000000000000000000000000000000000000000000000000000
0x36d: M[V319] = 0xa9059cbb00000000000000000000000000000000000000000000000000000000
0x36e: V326 = 0x1
0x370: V327 = 0xa0
0x372: V328 = 0x2
0x374: V329 = EXP 0x2 0xa0
0x375: V330 = SUB 0x10000000000000000000000000000000000000000 0x1
0x378: V331 = AND V317 0xffffffffffffffffffffffffffffffffffffffff
0x379: V332 = 0x4
0x37c: V333 = ADD V319 0x4
0x37d: M[V333] = V331
0x37e: V334 = 0x24
0x381: V335 = ADD V319 0x24
0x382: M[V335] = V80
0x383: V336 = 0x44
0x385: V337 = ADD 0x44 V319
0x386: V338 = 0x0
0x388: V339 = 0x40
0x38a: V340 = M[0x40]
0x38d: V341 = SUB V337 V340
0x38f: V342 = 0x0
0x393: V343 = EXTCODESIZE V315
0x394: V344 = ISZERO V343
0x395: V345 = ISZERO V344
0x396: V346 = 0x39e
0x399: JUMPI 0x39e V345
---
Entry stack: [V12, 0x76, V78, V80, V307]
Stack pops: 3
Stack additions: [S2, S1, S0, V315, 0xa9059cbb, V337, 0x0, V340, V341, V340, 0x0, V315]
Exit stack: [V12, 0x76, V78, V80, V307, V315, 0xa9059cbb, V337, 0x0, V340, V341, V340, 0x0, V315]

================================

Block 0x39a
[0x39a:0x39d]
---
Predecessors: [0x34b]
Successors: []
---
0x39a PUSH1 0x0
0x39c DUP1
0x39d REVERT
---
0x39a: V347 = 0x0
0x39d: REVERT 0x0 0x0
---
Entry stack: [V12, 0x76, V78, V80, V307, V315, 0xa9059cbb, V337, 0x0, V340, V341, V340, 0x0, V315]
Stack pops: 0
Stack additions: []
Exit stack: [V12, 0x76, V78, V80, V307, V315, 0xa9059cbb, V337, 0x0, V340, V341, V340, 0x0, V315]

================================

Block 0x39e
[0x39e:0x3aa]
---
Predecessors: [0x34b]
Successors: [0x3ab, 0x3af]
---
0x39e JUMPDEST
0x39f PUSH2 0x2c6
0x3a2 GAS
0x3a3 SUB
0x3a4 CALL
0x3a5 ISZERO
0x3a6 ISZERO
0x3a7 PUSH2 0x3af
0x3aa JUMPI
---
0x39e: JUMPDEST 
0x39f: V348 = 0x2c6
0x3a2: V349 = GAS
0x3a3: V350 = SUB V349 0x2c6
0x3a4: V351 = CALL V350 V315 0x0 V340 V341 V340 0x0
0x3a5: V352 = ISZERO V351
0x3a6: V353 = ISZERO V352
0x3a7: V354 = 0x3af
0x3aa: JUMPI 0x3af V353
---
Entry stack: [V12, 0x76, V78, V80, V307, V315, 0xa9059cbb, V337, 0x0, V340, V341, V340, 0x0, V315]
Stack pops: 6
Stack additions: []
Exit stack: [V12, 0x76, V78, V80, V307, V315, 0xa9059cbb, V337]

================================

Block 0x3ab
[0x3ab:0x3ae]
---
Predecessors: [0x39e]
Successors: []
---
0x3ab PUSH1 0x0
0x3ad DUP1
0x3ae REVERT
---
0x3ab: V355 = 0x0
0x3ae: REVERT 0x0 0x0
---
Entry stack: [V12, 0x76, V78, V80, V307, V315, 0xa9059cbb, V337]
Stack pops: 0
Stack additions: []
Exit stack: [V12, 0x76, V78, V80, V307, V315, 0xa9059cbb, V337]

================================

Block 0x3af
[0x3af:0x3b2]
---
Predecessors: [0x39e]
Successors: [0x3b3]
---
0x3af JUMPDEST
0x3b0 POP
0x3b1 POP
0x3b2 POP
---
0x3af: JUMPDEST 
---
Entry stack: [V12, 0x76, V78, V80, V307, V315, 0xa9059cbb, V337]
Stack pops: 3
Stack additions: []
Exit stack: [V12, 0x76, V78, V80, V307]

================================

Block 0x3b3
[0x3b3:0x3b3]
---
Predecessors: [0x2b8, 0x338, 0x3af]
Successors: [0x3b4]
---
0x3b3 JUMPDEST
---
0x3b3: JUMPDEST 
---
Entry stack: [V12, 0x76, V78, V80, S0]
Stack pops: 0
Stack additions: []
Exit stack: [V12, 0x76, V78, V80, S0]

================================

Block 0x3b4
[0x3b4:0x3b4]
---
Predecessors: [0x3b3]
Successors: [0x3b5]
---
0x3b4 JUMPDEST
---
0x3b4: JUMPDEST 
---
Entry stack: [V12, 0x76, V78, V80, S0]
Stack pops: 0
Stack additions: []
Exit stack: [V12, 0x76, V78, V80, S0]

================================

Block 0x3b5
[0x3b5:0x3b5]
---
Predecessors: [0x3b4]
Successors: [0x3b6]
---
0x3b5 JUMPDEST
---
0x3b5: JUMPDEST 
---
Entry stack: [V12, 0x76, V78, V80, S0]
Stack pops: 0
Stack additions: []
Exit stack: [V12, 0x76, V78, V80, S0]

================================

Block 0x3b6
[0x3b6:0x3ba]
---
Predecessors: [0x3b5]
Successors: [0x76]
---
0x3b6 JUMPDEST
0x3b7 POP
0x3b8 POP
0x3b9 POP
0x3ba JUMP
---
0x3b6: JUMPDEST 
0x3ba: JUMP 0x76
---
Entry stack: [V12, 0x76, V78, V80, S0]
Stack pops: 4
Stack additions: []
Exit stack: [V12]

================================

Block 0x3bb
[0x3bb:0x3c9]
---
Predecessors: [0xf9]
Successors: [0x101]
---
0x3bb JUMPDEST
0x3bc PUSH1 0x1
0x3be SLOAD
0x3bf PUSH1 0x1
0x3c1 PUSH1 0xa0
0x3c3 PUSH1 0x2
0x3c5 EXP
0x3c6 SUB
0x3c7 AND
0x3c8 DUP2
0x3c9 JUMP
---
0x3bb: JUMPDEST 
0x3bc: V356 = 0x1
0x3be: V357 = S[0x1]
0x3bf: V358 = 0x1
0x3c1: V359 = 0xa0
0x3c3: V360 = 0x2
0x3c5: V361 = EXP 0x2 0xa0
0x3c6: V362 = SUB 0x10000000000000000000000000000000000000000 0x1
0x3c7: V363 = AND 0xffffffffffffffffffffffffffffffffffffffff V357
0x3c9: JUMP 0x101
---
Entry stack: [V12, 0x101]
Stack pops: 1
Stack additions: [S0, V363]
Exit stack: [V12, 0x101, V363]

================================

Block 0x3ca
[0x3ca:0x3f5]
---
Predecessors: []
Successors: []
---
0x3ca STOP
0x3cb LOG1
0x3cc PUSH6 0x627a7a723058
0x3d3 SHA3
0x3d4 MISSING 0xe2
0x3d5 MSTORE8
0x3d6 ORIGIN
0x3d7 MISSING 0xb9
0x3d8 MISSING 0xc9
0x3d9 DUP5
0x3da MISSING 0xb9
0x3db SWAP14
0x3dc SWAP11
0x3dd MISSING 0xdb
0x3de ISZERO
0x3df MISSING 0xac
0x3e0 EQ
0x3e1 MISSING 0xde
0x3e2 MISSING 0xb4
0x3e3 LOG4
0x3e4 MULMOD
0x3e5 SELFDESTRUCT
0x3e6 SDIV
0x3e7 MISSING 0xc9
0x3e8 MISSING 0xda
0x3e9 PUSH2 0x8349
0x3ec MISSING 0xee
0x3ed AND
0x3ee MISSING 0x49
0x3ef STATICCALL
0x3f0 CALLDATALOAD
0x3f1 MSTORE8
0x3f2 MISSING 0xb8
0x3f3 MISSING 0x24
0x3f4 STOP
0x3f5 MISSING 0x29
---
0x3ca: STOP 
0x3cb: LOG S0 S1 S2
0x3cc: V364 = 0x627a7a723058
0x3d3: V365 = SHA3 0x627a7a723058 S3
0x3d4: MISSING 0xe2
0x3d5: M8[S0] = S1
0x3d6: V366 = ORIGIN
0x3d7: MISSING 0xb9
0x3d8: MISSING 0xc9
0x3da: MISSING 0xb9
0x3dd: MISSING 0xdb
0x3de: V367 = ISZERO S0
0x3df: MISSING 0xac
0x3e0: V368 = EQ S0 S1
0x3e1: MISSING 0xde
0x3e2: MISSING 0xb4
0x3e3: LOG S0 S1 S2 S3 S4 S5
0x3e4: V369 = MULMOD S6 S7 S8
0x3e5: SELFDESTRUCT V369
0x3e6: V370 = SDIV S0 S1
0x3e7: MISSING 0xc9
0x3e8: MISSING 0xda
0x3e9: V371 = 0x8349
0x3ec: MISSING 0xee
0x3ed: V372 = AND S0 S1
0x3ee: MISSING 0x49
0x3ef: V373 = STATICCALL S0 S1 S2 S3 S4 S5
0x3f0: V374 = CALLDATALOAD V373
0x3f1: M8[V374] = S6
0x3f2: MISSING 0xb8
0x3f3: MISSING 0x24
0x3f4: STOP 
0x3f5: MISSING 0x29
---
Entry stack: []
Stack pops: 0
Stack additions: [V365, V366, S4, S0, S1, S2, S3, S4, S11, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S14, S12, S13, S0, V367, V368, V370, 0x8349, V372]
Exit stack: []

================================

Function 0:
Public function signature: 0x2d2c44f2
Entry block: 0x78
Exit block: 0x76
Body: 0x73, 0x74, 0x76, 0x78, 0x18e

Function 1:
Public function signature: 0x2e1a7d4d
Entry block: 0x82
Exit block: 0x76
Body: 0x76, 0x82, 0x1c1, 0x1d9, 0x1f9, 0x216, 0x21c, 0x248, 0x24c, 0x280, 0x281, 0x282, 0x283

Function 2:
Public function signature: 0x3ee2d7c2
Entry block: 0x8f
Exit block: 0xae
Body: 0x8f, 0x96, 0x9a, 0xae, 0x286

Function 3:
Public function signature: 0x41c0e1b5
Entry block: 0xc0
Exit block: 0x76
Body: 0x73, 0x74, 0x76, 0xc0, 0xc7, 0xcb, 0x298, 0x2aa

Function 4:
Public function signature: 0x9e281a98
Entry block: 0xd5
Exit block: 0x3ab
Body: 0x76, 0xd5, 0x2b8, 0x2d1, 0x323, 0x327, 0x334, 0x338, 0x34b, 0x39a, 0x39e, 0x3ab, 0x3af, 0x3b3, 0x3b4, 0x3b5, 0x3b6

Function 5:
Public function signature: 0xb4a99a4e
Entry block: 0xee
Exit block: 0x101
Body: 0xee, 0xf5, 0xf9, 0x101, 0x3bb

Function 6:
Public function signature: 0xd0e30db0
Entry block: 0x11d
Exit block: 0x76
Body: 0x76, 0x11d

Function 7:
Public fallback function
Entry block: 0x67
Exit block: 0x76
Body: 0x67, 0x6b, 0x73, 0x74, 0x76

Function 8:
Private function
Entry block: 0x127
Exit block: 0x18c
Body: 0x127, 0x137, 0x18b, 0x18c

