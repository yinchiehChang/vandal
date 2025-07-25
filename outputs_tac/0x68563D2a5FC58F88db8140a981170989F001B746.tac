Block 0x0
[0x0:0xa]
---
Predecessors: []
Successors: [0xb, 0x8b]
---
0x0 PUSH1 0x60
0x2 PUSH1 0x40
0x4 MSTORE
0x5 CALLDATASIZE
0x6 ISZERO
0x7 PUSH2 0x8b
0xa JUMPI
---
0x0: V0 = 0x60
0x2: V1 = 0x40
0x4: M[0x40] = 0x60
0x5: V2 = CALLDATASIZE
0x6: V3 = ISZERO V2
0x7: V4 = 0x8b
0xa: JUMPI 0x8b V3
---
Entry stack: []
Stack pops: 0
Stack additions: []
Exit stack: []

================================

Block 0xb
[0xb:0x3d]
---
Predecessors: [0x0]
Successors: [0x3e, 0x97]
---
0xb PUSH4 0xffffffff
0x10 PUSH29 0x100000000000000000000000000000000000000000000000000000000
0x2e PUSH1 0x0
0x30 CALLDATALOAD
0x31 DIV
0x32 AND
0x33 PUSH4 0x2e1a7d4d
0x38 DUP2
0x39 EQ
0x3a PUSH2 0x97
0x3d JUMPI
---
0xb: V5 = 0xffffffff
0x10: V6 = 0x100000000000000000000000000000000000000000000000000000000
0x2e: V7 = 0x0
0x30: V8 = CALLDATALOAD 0x0
0x31: V9 = DIV V8 0x100000000000000000000000000000000000000000000000000000000
0x32: V10 = AND V9 0xffffffff
0x33: V11 = 0x2e1a7d4d
0x39: V12 = EQ V10 0x2e1a7d4d
0x3a: V13 = 0x97
0x3d: JUMPI 0x97 V12
---
Entry stack: []
Stack pops: 0
Stack additions: [V10]
Exit stack: [V10]

================================

Block 0x3e
[0x3e:0x48]
---
Predecessors: [0xb]
Successors: [0x49, 0xa4]
---
0x3e DUP1
0x3f PUSH4 0x41c0e1b5
0x44 EQ
0x45 PUSH2 0xa4
0x48 JUMPI
---
0x3f: V14 = 0x41c0e1b5
0x44: V15 = EQ 0x41c0e1b5 V10
0x45: V16 = 0xa4
0x48: JUMPI 0xa4 V15
---
Entry stack: [V10]
Stack pops: 1
Stack additions: [S0]
Exit stack: [V10]

================================

Block 0x49
[0x49:0x53]
---
Predecessors: [0x3e]
Successors: [0x54, 0xb9]
---
0x49 DUP1
0x4a PUSH4 0x4fb2e45d
0x4f EQ
0x50 PUSH2 0xb9
0x53 JUMPI
---
0x4a: V17 = 0x4fb2e45d
0x4f: V18 = EQ 0x4fb2e45d V10
0x50: V19 = 0xb9
0x53: JUMPI 0xb9 V18
---
Entry stack: [V10]
Stack pops: 1
Stack additions: [S0]
Exit stack: [V10]

================================

Block 0x54
[0x54:0x5e]
---
Predecessors: [0x49]
Successors: [0x5f, 0xda]
---
0x54 DUP1
0x55 PUSH4 0xb4a99a4e
0x5a EQ
0x5b PUSH2 0xda
0x5e JUMPI
---
0x55: V20 = 0xb4a99a4e
0x5a: V21 = EQ 0xb4a99a4e V10
0x5b: V22 = 0xda
0x5e: JUMPI 0xda V21
---
Entry stack: [V10]
Stack pops: 1
Stack additions: [S0]
Exit stack: [V10]

================================

Block 0x5f
[0x5f:0x69]
---
Predecessors: [0x54]
Successors: [0x6a, 0x109]
---
0x5f DUP1
0x60 PUSH4 0xb7f9c4f6
0x65 EQ
0x66 PUSH2 0x109
0x69 JUMPI
---
0x60: V23 = 0xb7f9c4f6
0x65: V24 = EQ 0xb7f9c4f6 V10
0x66: V25 = 0x109
0x69: JUMPI 0x109 V24
---
Entry stack: [V10]
Stack pops: 1
Stack additions: [S0]
Exit stack: [V10]

================================

Block 0x6a
[0x6a:0x74]
---
Predecessors: [0x5f]
Successors: [0x75, 0x8b]
---
0x6a DUP1
0x6b PUSH4 0xd0e30db0
0x70 EQ
0x71 PUSH2 0x8b
0x74 JUMPI
---
0x6b: V26 = 0xd0e30db0
0x70: V27 = EQ 0xd0e30db0 V10
0x71: V28 = 0x8b
0x74: JUMPI 0x8b V27
---
Entry stack: [V10]
Stack pops: 1
Stack additions: [S0]
Exit stack: [V10]

================================

Block 0x75
[0x75:0x7f]
---
Predecessors: [0x6a]
Successors: [0x80, 0x12b]
---
0x75 DUP1
0x76 PUSH4 0xec8cb281
0x7b EQ
0x7c PUSH2 0x12b
0x7f JUMPI
---
0x76: V29 = 0xec8cb281
0x7b: V30 = EQ 0xec8cb281 V10
0x7c: V31 = 0x12b
0x7f: JUMPI 0x12b V30
---
Entry stack: [V10]
Stack pops: 1
Stack additions: [S0]
Exit stack: [V10]

================================

Block 0x80
[0x80:0x8a]
---
Predecessors: [0x75]
Successors: [0x8b, 0x150]
---
0x80 DUP1
0x81 PUSH4 0xfc7e286d
0x86 EQ
0x87 PUSH2 0x150
0x8a JUMPI
---
0x81: V32 = 0xfc7e286d
0x86: V33 = EQ 0xfc7e286d V10
0x87: V34 = 0x150
0x8a: JUMPI 0x150 V33
---
Entry stack: [V10]
Stack pops: 1
Stack additions: [S0]
Exit stack: [V10]

================================

Block 0x8b
[0x8b:0x8b]
---
Predecessors: [0x0, 0x6a, 0x80]
Successors: [0x8c]
---
0x8b JUMPDEST
---
0x8b: JUMPDEST 
---
Entry stack: [V10]
Stack pops: 0
Stack additions: []
Exit stack: [V10]

================================

Block 0x8c
[0x8c:0x93]
---
Predecessors: [0x8b]
Successors: [0x181]
---
0x8c JUMPDEST
0x8d PUSH2 0x94
0x90 PUSH2 0x181
0x93 JUMP
---
0x8c: JUMPDEST 
0x8d: V35 = 0x94
0x90: V36 = 0x181
0x93: JUMP 0x181
---
Entry stack: [V10]
Stack pops: 0
Stack additions: [0x94]
Exit stack: [V10, 0x94]

================================

Block 0x94
[0x94:0x94]
---
Predecessors: [0x1ef, 0x2aa, 0x33b, 0x3b6]
Successors: [0x95]
---
0x94 JUMPDEST
---
0x94: JUMPDEST 
---
Entry stack: [V10]
Stack pops: 0
Stack additions: []
Exit stack: [V10]

================================

Block 0x95
[0x95:0x96]
---
Predecessors: [0x94]
Successors: []
---
0x95 JUMPDEST
0x96 STOP
---
0x95: JUMPDEST 
0x96: STOP 
---
Entry stack: [V10]
Stack pops: 0
Stack additions: []
Exit stack: [V10]

================================

Block 0x97
[0x97:0xa1]
---
Predecessors: [0xb]
Successors: [0x1f1]
---
0x97 JUMPDEST
0x98 PUSH2 0x94
0x9b PUSH1 0x4
0x9d CALLDATALOAD
0x9e PUSH2 0x1f1
0xa1 JUMP
---
0x97: JUMPDEST 
0x98: V37 = 0x94
0x9b: V38 = 0x4
0x9d: V39 = CALLDATALOAD 0x4
0x9e: V40 = 0x1f1
0xa1: JUMP 0x1f1
---
Entry stack: [V10]
Stack pops: 0
Stack additions: [0x94, V39]
Exit stack: [V10, 0x94, V39]

================================

Block 0xa2
[0xa2:0xa3]
---
Predecessors: []
Successors: []
---
0xa2 JUMPDEST
0xa3 STOP
---
0xa2: JUMPDEST 
0xa3: STOP 
---
Entry stack: []
Stack pops: 0
Stack additions: []
Exit stack: []

================================

Block 0xa4
[0xa4:0xaa]
---
Predecessors: [0x3e]
Successors: [0xab, 0xaf]
---
0xa4 JUMPDEST
0xa5 CALLVALUE
0xa6 ISZERO
0xa7 PUSH2 0xaf
0xaa JUMPI
---
0xa4: JUMPDEST 
0xa5: V41 = CALLVALUE
0xa6: V42 = ISZERO V41
0xa7: V43 = 0xaf
0xaa: JUMPI 0xaf V42
---
Entry stack: [V10]
Stack pops: 0
Stack additions: []
Exit stack: [V10]

================================

Block 0xab
[0xab:0xae]
---
Predecessors: [0xa4]
Successors: []
---
0xab PUSH1 0x0
0xad DUP1
0xae REVERT
---
0xab: V44 = 0x0
0xae: REVERT 0x0 0x0
---
Entry stack: [V10]
Stack pops: 0
Stack additions: []
Exit stack: [V10]

================================

Block 0xaf
[0xaf:0xb6]
---
Predecessors: [0xa4]
Successors: [0x2ae]
---
0xaf JUMPDEST
0xb0 PUSH2 0x94
0xb3 PUSH2 0x2ae
0xb6 JUMP
---
0xaf: JUMPDEST 
0xb0: V45 = 0x94
0xb3: V46 = 0x2ae
0xb6: JUMP 0x2ae
---
Entry stack: [V10]
Stack pops: 0
Stack additions: [0x94]
Exit stack: [V10, 0x94]

================================

Block 0xb7
[0xb7:0xb8]
---
Predecessors: []
Successors: []
---
0xb7 JUMPDEST
0xb8 STOP
---
0xb7: JUMPDEST 
0xb8: STOP 
---
Entry stack: []
Stack pops: 0
Stack additions: []
Exit stack: []

================================

Block 0xb9
[0xb9:0xbf]
---
Predecessors: [0x49]
Successors: [0xc0, 0xc4]
---
0xb9 JUMPDEST
0xba CALLVALUE
0xbb ISZERO
0xbc PUSH2 0xc4
0xbf JUMPI
---
0xb9: JUMPDEST 
0xba: V47 = CALLVALUE
0xbb: V48 = ISZERO V47
0xbc: V49 = 0xc4
0xbf: JUMPI 0xc4 V48
---
Entry stack: [V10]
Stack pops: 0
Stack additions: []
Exit stack: [V10]

================================

Block 0xc0
[0xc0:0xc3]
---
Predecessors: [0xb9]
Successors: []
---
0xc0 PUSH1 0x0
0xc2 DUP1
0xc3 REVERT
---
0xc0: V50 = 0x0
0xc3: REVERT 0x0 0x0
---
Entry stack: [V10]
Stack pops: 0
Stack additions: []
Exit stack: [V10]

================================

Block 0xc4
[0xc4:0xd7]
---
Predecessors: [0xb9]
Successors: [0x2e7]
---
0xc4 JUMPDEST
0xc5 PUSH2 0x94
0xc8 PUSH1 0x1
0xca PUSH1 0xa0
0xcc PUSH1 0x2
0xce EXP
0xcf SUB
0xd0 PUSH1 0x4
0xd2 CALLDATALOAD
0xd3 AND
0xd4 PUSH2 0x2e7
0xd7 JUMP
---
0xc4: JUMPDEST 
0xc5: V51 = 0x94
0xc8: V52 = 0x1
0xca: V53 = 0xa0
0xcc: V54 = 0x2
0xce: V55 = EXP 0x2 0xa0
0xcf: V56 = SUB 0x10000000000000000000000000000000000000000 0x1
0xd0: V57 = 0x4
0xd2: V58 = CALLDATALOAD 0x4
0xd3: V59 = AND V58 0xffffffffffffffffffffffffffffffffffffffff
0xd4: V60 = 0x2e7
0xd7: JUMP 0x2e7
---
Entry stack: [V10]
Stack pops: 0
Stack additions: [0x94, V59]
Exit stack: [V10, 0x94, V59]

================================

Block 0xd8
[0xd8:0xd9]
---
Predecessors: []
Successors: []
---
0xd8 JUMPDEST
0xd9 STOP
---
0xd8: JUMPDEST 
0xd9: STOP 
---
Entry stack: []
Stack pops: 0
Stack additions: []
Exit stack: []

================================

Block 0xda
[0xda:0xe0]
---
Predecessors: [0x54]
Successors: [0xe1, 0xe5]
---
0xda JUMPDEST
0xdb CALLVALUE
0xdc ISZERO
0xdd PUSH2 0xe5
0xe0 JUMPI
---
0xda: JUMPDEST 
0xdb: V61 = CALLVALUE
0xdc: V62 = ISZERO V61
0xdd: V63 = 0xe5
0xe0: JUMPI 0xe5 V62
---
Entry stack: [V10]
Stack pops: 0
Stack additions: []
Exit stack: [V10]

================================

Block 0xe1
[0xe1:0xe4]
---
Predecessors: [0xda]
Successors: []
---
0xe1 PUSH1 0x0
0xe3 DUP1
0xe4 REVERT
---
0xe1: V64 = 0x0
0xe4: REVERT 0x0 0x0
---
Entry stack: [V10]
Stack pops: 0
Stack additions: []
Exit stack: [V10]

================================

Block 0xe5
[0xe5:0xec]
---
Predecessors: [0xda]
Successors: [0x33e]
---
0xe5 JUMPDEST
0xe6 PUSH2 0xed
0xe9 PUSH2 0x33e
0xec JUMP
---
0xe5: JUMPDEST 
0xe6: V65 = 0xed
0xe9: V66 = 0x33e
0xec: JUMP 0x33e
---
Entry stack: [V10]
Stack pops: 0
Stack additions: [0xed]
Exit stack: [V10, 0xed]

================================

Block 0xed
[0xed:0x108]
---
Predecessors: [0x33e]
Successors: []
---
0xed JUMPDEST
0xee PUSH1 0x40
0xf0 MLOAD
0xf1 PUSH1 0x1
0xf3 PUSH1 0xa0
0xf5 PUSH1 0x2
0xf7 EXP
0xf8 SUB
0xf9 SWAP1
0xfa SWAP2
0xfb AND
0xfc DUP2
0xfd MSTORE
0xfe PUSH1 0x20
0x100 ADD
0x101 PUSH1 0x40
0x103 MLOAD
0x104 DUP1
0x105 SWAP2
0x106 SUB
0x107 SWAP1
0x108 RETURN
---
0xed: JUMPDEST 
0xee: V67 = 0x40
0xf0: V68 = M[0x40]
0xf1: V69 = 0x1
0xf3: V70 = 0xa0
0xf5: V71 = 0x2
0xf7: V72 = EXP 0x2 0xa0
0xf8: V73 = SUB 0x10000000000000000000000000000000000000000 0x1
0xfb: V74 = AND V296 0xffffffffffffffffffffffffffffffffffffffff
0xfd: M[V68] = V74
0xfe: V75 = 0x20
0x100: V76 = ADD 0x20 V68
0x101: V77 = 0x40
0x103: V78 = M[0x40]
0x106: V79 = SUB V76 V78
0x108: RETURN V78 V79
---
Entry stack: [V10, 0xed, V296]
Stack pops: 1
Stack additions: []
Exit stack: [V10, 0xed]

================================

Block 0x109
[0x109:0x10f]
---
Predecessors: [0x5f]
Successors: [0x110, 0x114]
---
0x109 JUMPDEST
0x10a CALLVALUE
0x10b ISZERO
0x10c PUSH2 0x114
0x10f JUMPI
---
0x109: JUMPDEST 
0x10a: V80 = CALLVALUE
0x10b: V81 = ISZERO V80
0x10c: V82 = 0x114
0x10f: JUMPI 0x114 V81
---
Entry stack: [V10]
Stack pops: 0
Stack additions: []
Exit stack: [V10]

================================

Block 0x110
[0x110:0x113]
---
Predecessors: [0x109]
Successors: []
---
0x110 PUSH1 0x0
0x112 DUP1
0x113 REVERT
---
0x110: V83 = 0x0
0x113: REVERT 0x0 0x0
---
Entry stack: [V10]
Stack pops: 0
Stack additions: []
Exit stack: [V10]

================================

Block 0x114
[0x114:0x11e]
---
Predecessors: [0x109]
Successors: [0x34d]
---
0x114 JUMPDEST
0x115 PUSH2 0x94
0x118 PUSH1 0x4
0x11a CALLDATALOAD
0x11b PUSH2 0x34d
0x11e JUMP
---
0x114: JUMPDEST 
0x115: V84 = 0x94
0x118: V85 = 0x4
0x11a: V86 = CALLDATALOAD 0x4
0x11b: V87 = 0x34d
0x11e: JUMP 0x34d
---
Entry stack: [V10]
Stack pops: 0
Stack additions: [0x94, V86]
Exit stack: [V10, 0x94, V86]

================================

Block 0x11f
[0x11f:0x128]
---
Predecessors: []
Successors: [0x181]
---
0x11f JUMPDEST
0x120 STOP
0x121 JUMPDEST
0x122 PUSH2 0x94
0x125 PUSH2 0x181
0x128 JUMP
---
0x11f: JUMPDEST 
0x120: STOP 
0x121: JUMPDEST 
0x122: V88 = 0x94
0x125: V89 = 0x181
0x128: JUMP 0x181
---
Entry stack: []
Stack pops: 0
Stack additions: [0x94]
Exit stack: []

================================

Block 0x129
[0x129:0x12a]
---
Predecessors: []
Successors: []
---
0x129 JUMPDEST
0x12a STOP
---
0x129: JUMPDEST 
0x12a: STOP 
---
Entry stack: []
Stack pops: 0
Stack additions: []
Exit stack: []

================================

Block 0x12b
[0x12b:0x131]
---
Predecessors: [0x75]
Successors: [0x132, 0x136]
---
0x12b JUMPDEST
0x12c CALLVALUE
0x12d ISZERO
0x12e PUSH2 0x136
0x131 JUMPI
---
0x12b: JUMPDEST 
0x12c: V90 = CALLVALUE
0x12d: V91 = ISZERO V90
0x12e: V92 = 0x136
0x131: JUMPI 0x136 V91
---
Entry stack: [V10]
Stack pops: 0
Stack additions: []
Exit stack: [V10]

================================

Block 0x132
[0x132:0x135]
---
Predecessors: [0x12b]
Successors: []
---
0x132 PUSH1 0x0
0x134 DUP1
0x135 REVERT
---
0x132: V93 = 0x0
0x135: REVERT 0x0 0x0
---
Entry stack: [V10]
Stack pops: 0
Stack additions: []
Exit stack: [V10]

================================

Block 0x136
[0x136:0x13d]
---
Predecessors: [0x12b]
Successors: [0x3b9]
---
0x136 JUMPDEST
0x137 PUSH2 0x13e
0x13a PUSH2 0x3b9
0x13d JUMP
---
0x136: JUMPDEST 
0x137: V94 = 0x13e
0x13a: V95 = 0x3b9
0x13d: JUMP 0x3b9
---
Entry stack: [V10]
Stack pops: 0
Stack additions: [0x13e]
Exit stack: [V10, 0x13e]

================================

Block 0x13e
[0x13e:0x14f]
---
Predecessors: [0x3b9, 0x3bf]
Successors: []
---
0x13e JUMPDEST
0x13f PUSH1 0x40
0x141 MLOAD
0x142 SWAP1
0x143 DUP2
0x144 MSTORE
0x145 PUSH1 0x20
0x147 ADD
0x148 PUSH1 0x40
0x14a MLOAD
0x14b DUP1
0x14c SWAP2
0x14d SUB
0x14e SWAP1
0x14f RETURN
---
0x13e: JUMPDEST 
0x13f: V96 = 0x40
0x141: V97 = M[0x40]
0x144: M[V97] = S0
0x145: V98 = 0x20
0x147: V99 = ADD 0x20 V97
0x148: V100 = 0x40
0x14a: V101 = M[0x40]
0x14d: V102 = SUB V99 V101
0x14f: RETURN V101 V102
---
Entry stack: [V10, 0x13e, S0]
Stack pops: 1
Stack additions: []
Exit stack: [V10, 0x13e]

================================

Block 0x150
[0x150:0x156]
---
Predecessors: [0x80]
Successors: [0x157, 0x15b]
---
0x150 JUMPDEST
0x151 CALLVALUE
0x152 ISZERO
0x153 PUSH2 0x15b
0x156 JUMPI
---
0x150: JUMPDEST 
0x151: V103 = CALLVALUE
0x152: V104 = ISZERO V103
0x153: V105 = 0x15b
0x156: JUMPI 0x15b V104
---
Entry stack: [V10]
Stack pops: 0
Stack additions: []
Exit stack: [V10]

================================

Block 0x157
[0x157:0x15a]
---
Predecessors: [0x150]
Successors: []
---
0x157 PUSH1 0x0
0x159 DUP1
0x15a REVERT
---
0x157: V106 = 0x0
0x15a: REVERT 0x0 0x0
---
Entry stack: [V10]
Stack pops: 0
Stack additions: []
Exit stack: [V10]

================================

Block 0x15b
[0x15b:0x16e]
---
Predecessors: [0x150]
Successors: [0x3bf]
---
0x15b JUMPDEST
0x15c PUSH2 0x13e
0x15f PUSH1 0x1
0x161 PUSH1 0xa0
0x163 PUSH1 0x2
0x165 EXP
0x166 SUB
0x167 PUSH1 0x4
0x169 CALLDATALOAD
0x16a AND
0x16b PUSH2 0x3bf
0x16e JUMP
---
0x15b: JUMPDEST 
0x15c: V107 = 0x13e
0x15f: V108 = 0x1
0x161: V109 = 0xa0
0x163: V110 = 0x2
0x165: V111 = EXP 0x2 0xa0
0x166: V112 = SUB 0x10000000000000000000000000000000000000000 0x1
0x167: V113 = 0x4
0x169: V114 = CALLDATALOAD 0x4
0x16a: V115 = AND V114 0xffffffffffffffffffffffffffffffffffffffff
0x16b: V116 = 0x3bf
0x16e: JUMP 0x3bf
---
Entry stack: [V10]
Stack pops: 0
Stack additions: [0x13e, V115]
Exit stack: [V10, 0x13e, V115]

================================

Block 0x16f
[0x16f:0x180]
---
Predecessors: []
Successors: []
---
0x16f JUMPDEST
0x170 PUSH1 0x40
0x172 MLOAD
0x173 SWAP1
0x174 DUP2
0x175 MSTORE
0x176 PUSH1 0x20
0x178 ADD
0x179 PUSH1 0x40
0x17b MLOAD
0x17c DUP1
0x17d SWAP2
0x17e SUB
0x17f SWAP1
0x180 RETURN
---
0x16f: JUMPDEST 
0x170: V117 = 0x40
0x172: V118 = M[0x40]
0x175: M[V118] = S0
0x176: V119 = 0x20
0x178: V120 = ADD 0x20 V118
0x179: V121 = 0x40
0x17b: V122 = M[0x40]
0x17e: V123 = SUB V120 V122
0x180: RETURN V122 V123
---
Entry stack: []
Stack pops: 1
Stack additions: []
Exit stack: []

================================

Block 0x181
[0x181:0x190]
---
Predecessors: [0x8c, 0x11f]
Successors: [0x191, 0x1e9]
---
0x181 JUMPDEST
0x182 PUSH8 0x6f05b59d3b20000
0x18b CALLVALUE
0x18c LT
0x18d PUSH2 0x1e9
0x190 JUMPI
---
0x181: JUMPDEST 
0x182: V124 = 0x6f05b59d3b20000
0x18b: V125 = CALLVALUE
0x18c: V126 = LT V125 0x6f05b59d3b20000
0x18d: V127 = 0x1e9
0x190: JUMPI 0x1e9 V126
---
Entry stack: [V10, 0x94]
Stack pops: 0
Stack additions: []
Exit stack: [V10, 0x94]

================================

Block 0x191
[0x191:0x1e8]
---
Predecessors: [0x181]
Successors: [0x1ee]
---
0x191 PUSH1 0x1
0x193 PUSH1 0xa0
0x195 PUSH1 0x2
0x197 EXP
0x198 SUB
0x199 CALLER
0x19a AND
0x19b PUSH1 0x0
0x19d DUP2
0x19e DUP2
0x19f MSTORE
0x1a0 PUSH1 0x2
0x1a2 PUSH1 0x20
0x1a4 MSTORE
0x1a5 PUSH1 0x40
0x1a7 SWAP1
0x1a8 DUP2
0x1a9 SWAP1
0x1aa SHA3
0x1ab DUP1
0x1ac SLOAD
0x1ad CALLVALUE
0x1ae SWAP1
0x1af DUP2
0x1b0 ADD
0x1b1 SWAP1
0x1b2 SWAP2
0x1b3 SSTORE
0x1b4 PUSH32 0xe1fffcc4923d04b559f4d29a8bfc6cda04eb5b0d3c460751c2402c5c5cc9109c
0x1d5 SWAP2
0x1d6 MLOAD
0x1d7 SWAP1
0x1d8 DUP2
0x1d9 MSTORE
0x1da PUSH1 0x20
0x1dc ADD
0x1dd PUSH1 0x40
0x1df MLOAD
0x1e0 DUP1
0x1e1 SWAP2
0x1e2 SUB
0x1e3 SWAP1
0x1e4 LOG2
0x1e5 PUSH2 0x1ee
0x1e8 JUMP
---
0x191: V128 = 0x1
0x193: V129 = 0xa0
0x195: V130 = 0x2
0x197: V131 = EXP 0x2 0xa0
0x198: V132 = SUB 0x10000000000000000000000000000000000000000 0x1
0x199: V133 = CALLER
0x19a: V134 = AND V133 0xffffffffffffffffffffffffffffffffffffffff
0x19b: V135 = 0x0
0x19f: M[0x0] = V134
0x1a0: V136 = 0x2
0x1a2: V137 = 0x20
0x1a4: M[0x20] = 0x2
0x1a5: V138 = 0x40
0x1aa: V139 = SHA3 0x0 0x40
0x1ac: V140 = S[V139]
0x1ad: V141 = CALLVALUE
0x1b0: V142 = ADD V141 V140
0x1b3: S[V139] = V142
0x1b4: V143 = 0xe1fffcc4923d04b559f4d29a8bfc6cda04eb5b0d3c460751c2402c5c5cc9109c
0x1d6: V144 = M[0x40]
0x1d9: M[V144] = V141
0x1da: V145 = 0x20
0x1dc: V146 = ADD 0x20 V144
0x1dd: V147 = 0x40
0x1df: V148 = M[0x40]
0x1e2: V149 = SUB V146 V148
0x1e4: LOG V148 V149 0xe1fffcc4923d04b559f4d29a8bfc6cda04eb5b0d3c460751c2402c5c5cc9109c V134
0x1e5: V150 = 0x1ee
0x1e8: JUMP 0x1ee
---
Entry stack: [V10, 0x94]
Stack pops: 0
Stack additions: []
Exit stack: [V10, 0x94]

================================

Block 0x1e9
[0x1e9:0x1ed]
---
Predecessors: [0x181]
Successors: []
---
0x1e9 JUMPDEST
0x1ea PUSH1 0x0
0x1ec DUP1
0x1ed REVERT
---
0x1e9: JUMPDEST 
0x1ea: V151 = 0x0
0x1ed: REVERT 0x0 0x0
---
Entry stack: [V10, 0x94]
Stack pops: 0
Stack additions: []
Exit stack: [V10, 0x94]

================================

Block 0x1ee
[0x1ee:0x1ee]
---
Predecessors: [0x191, 0x2ae, 0x2c6]
Successors: [0x1ef]
---
0x1ee JUMPDEST
---
0x1ee: JUMPDEST 
---
Entry stack: [V10, 0x94]
Stack pops: 0
Stack additions: []
Exit stack: [V10, 0x94]

================================

Block 0x1ef
[0x1ef:0x1f0]
---
Predecessors: [0x1ee]
Successors: [0x94]
---
0x1ef JUMPDEST
0x1f0 JUMP
---
0x1ef: JUMPDEST 
0x1f0: JUMP 0x94
---
Entry stack: [V10, 0x94]
Stack pops: 1
Stack additions: []
Exit stack: [V10]

================================

Block 0x1f1
[0x1f1:0x209]
---
Predecessors: [0x97]
Successors: [0x20a, 0x2a6]
---
0x1f1 JUMPDEST
0x1f2 PUSH1 0x0
0x1f4 DUP1
0x1f5 SLOAD
0x1f6 CALLER
0x1f7 PUSH1 0x1
0x1f9 PUSH1 0xa0
0x1fb PUSH1 0x2
0x1fd EXP
0x1fe SUB
0x1ff SWAP1
0x200 DUP2
0x201 AND
0x202 SWAP2
0x203 AND
0x204 EQ
0x205 ISZERO
0x206 PUSH2 0x2a6
0x209 JUMPI
---
0x1f1: JUMPDEST 
0x1f2: V152 = 0x0
0x1f5: V153 = S[0x0]
0x1f6: V154 = CALLER
0x1f7: V155 = 0x1
0x1f9: V156 = 0xa0
0x1fb: V157 = 0x2
0x1fd: V158 = EXP 0x2 0xa0
0x1fe: V159 = SUB 0x10000000000000000000000000000000000000000 0x1
0x201: V160 = AND 0xffffffffffffffffffffffffffffffffffffffff V154
0x203: V161 = AND V153 0xffffffffffffffffffffffffffffffffffffffff
0x204: V162 = EQ V161 V160
0x205: V163 = ISZERO V162
0x206: V164 = 0x2a6
0x209: JUMPI 0x2a6 V163
---
Entry stack: [V10, 0x94, V39]
Stack pops: 0
Stack additions: [0x0]
Exit stack: [V10, 0x94, V39, 0x0]

================================

Block 0x20a
[0x20a:0x212]
---
Predecessors: [0x1f1]
Successors: [0x213, 0x2a6]
---
0x20a PUSH1 0x3
0x20c SLOAD
0x20d TIMESTAMP
0x20e LT
0x20f PUSH2 0x2a6
0x212 JUMPI
---
0x20a: V165 = 0x3
0x20c: V166 = S[0x3]
0x20d: V167 = TIMESTAMP
0x20e: V168 = LT V167 V166
0x20f: V169 = 0x2a6
0x212: JUMPI 0x2a6 V168
---
Entry stack: [V10, 0x94, V39, 0x0]
Stack pops: 0
Stack additions: []
Exit stack: [V10, 0x94, V39, 0x0]

================================

Block 0x213
[0x213:0x236]
---
Predecessors: [0x20a]
Successors: [0x237, 0x23c]
---
0x213 POP
0x214 PUSH1 0x1
0x216 PUSH1 0xa0
0x218 PUSH1 0x2
0x21a EXP
0x21b SUB
0x21c CALLER
0x21d AND
0x21e PUSH1 0x0
0x220 SWAP1
0x221 DUP2
0x222 MSTORE
0x223 PUSH1 0x2
0x225 PUSH1 0x20
0x227 MSTORE
0x228 PUSH1 0x40
0x22a SWAP1
0x22b SHA3
0x22c SLOAD
0x22d DUP1
0x22e DUP3
0x22f GT
0x230 DUP1
0x231 ISZERO
0x232 SWAP1
0x233 PUSH2 0x23c
0x236 JUMPI
---
0x214: V170 = 0x1
0x216: V171 = 0xa0
0x218: V172 = 0x2
0x21a: V173 = EXP 0x2 0xa0
0x21b: V174 = SUB 0x10000000000000000000000000000000000000000 0x1
0x21c: V175 = CALLER
0x21d: V176 = AND V175 0xffffffffffffffffffffffffffffffffffffffff
0x21e: V177 = 0x0
0x222: M[0x0] = V176
0x223: V178 = 0x2
0x225: V179 = 0x20
0x227: M[0x20] = 0x2
0x228: V180 = 0x40
0x22b: V181 = SHA3 0x0 0x40
0x22c: V182 = S[V181]
0x22f: V183 = GT V39 V182
0x231: V184 = ISZERO V183
0x233: V185 = 0x23c
0x236: JUMPI 0x23c V183
---
Entry stack: [V10, 0x94, V39, 0x0]
Stack pops: 2
Stack additions: [S1, V182, V184]
Exit stack: [V10, 0x94, V39, V182, V184]

================================

Block 0x237
[0x237:0x23b]
---
Predecessors: [0x213]
Successors: [0x23c]
---
0x237 POP
0x238 PUSH1 0x0
0x23a DUP2
0x23b GT
---
0x238: V186 = 0x0
0x23b: V187 = GT V182 0x0
---
Entry stack: [V10, 0x94, V39, V182, V184]
Stack pops: 2
Stack additions: [S1, V187]
Exit stack: [V10, 0x94, V39, V182, V187]

================================

Block 0x23c
[0x23c:0x241]
---
Predecessors: [0x213, 0x237]
Successors: [0x242, 0x2a6]
---
0x23c JUMPDEST
0x23d ISZERO
0x23e PUSH2 0x2a6
0x241 JUMPI
---
0x23c: JUMPDEST 
0x23d: V188 = ISZERO S0
0x23e: V189 = 0x2a6
0x241: JUMPI 0x2a6 V188
---
Entry stack: [V10, 0x94, V39, V182, S0]
Stack pops: 1
Stack additions: []
Exit stack: [V10, 0x94, V39, V182]

================================

Block 0x242
[0x242:0x2a5]
---
Predecessors: [0x23c]
Successors: [0x2a6]
---
0x242 PUSH1 0x1
0x244 PUSH1 0xa0
0x246 PUSH1 0x2
0x248 EXP
0x249 SUB
0x24a CALLER
0x24b AND
0x24c DUP3
0x24d ISZERO
0x24e PUSH2 0x8fc
0x251 MUL
0x252 DUP4
0x253 PUSH1 0x40
0x255 MLOAD
0x256 PUSH1 0x0
0x258 PUSH1 0x40
0x25a MLOAD
0x25b DUP1
0x25c DUP4
0x25d SUB
0x25e DUP2
0x25f DUP6
0x260 DUP9
0x261 DUP9
0x262 CALL
0x263 SWAP4
0x264 POP
0x265 POP
0x266 POP
0x267 POP
0x268 POP
0x269 CALLER
0x26a PUSH1 0x1
0x26c PUSH1 0xa0
0x26e PUSH1 0x2
0x270 EXP
0x271 SUB
0x272 AND
0x273 PUSH32 0x7fcf532c15f0a6db0bd6d0e038bea71d30d808c7d98cb3bf7268a95bf5081b65
0x294 DUP4
0x295 PUSH1 0x40
0x297 MLOAD
0x298 SWAP1
0x299 DUP2
0x29a MSTORE
0x29b PUSH1 0x20
0x29d ADD
0x29e PUSH1 0x40
0x2a0 MLOAD
0x2a1 DUP1
0x2a2 SWAP2
0x2a3 SUB
0x2a4 SWAP1
0x2a5 LOG2
---
0x242: V190 = 0x1
0x244: V191 = 0xa0
0x246: V192 = 0x2
0x248: V193 = EXP 0x2 0xa0
0x249: V194 = SUB 0x10000000000000000000000000000000000000000 0x1
0x24a: V195 = CALLER
0x24b: V196 = AND V195 0xffffffffffffffffffffffffffffffffffffffff
0x24d: V197 = ISZERO V39
0x24e: V198 = 0x8fc
0x251: V199 = MUL 0x8fc V197
0x253: V200 = 0x40
0x255: V201 = M[0x40]
0x256: V202 = 0x0
0x258: V203 = 0x40
0x25a: V204 = M[0x40]
0x25d: V205 = SUB V201 V204
0x262: V206 = CALL V199 V196 V39 V204 V205 V204 0x0
0x269: V207 = CALLER
0x26a: V208 = 0x1
0x26c: V209 = 0xa0
0x26e: V210 = 0x2
0x270: V211 = EXP 0x2 0xa0
0x271: V212 = SUB 0x10000000000000000000000000000000000000000 0x1
0x272: V213 = AND 0xffffffffffffffffffffffffffffffffffffffff V207
0x273: V214 = 0x7fcf532c15f0a6db0bd6d0e038bea71d30d808c7d98cb3bf7268a95bf5081b65
0x295: V215 = 0x40
0x297: V216 = M[0x40]
0x29a: M[V216] = V39
0x29b: V217 = 0x20
0x29d: V218 = ADD 0x20 V216
0x29e: V219 = 0x40
0x2a0: V220 = M[0x40]
0x2a3: V221 = SUB V218 V220
0x2a5: LOG V220 V221 0x7fcf532c15f0a6db0bd6d0e038bea71d30d808c7d98cb3bf7268a95bf5081b65 V213
---
Entry stack: [V10, 0x94, V39, V182]
Stack pops: 2
Stack additions: [S1, S0]
Exit stack: [V10, 0x94, V39, V182]

================================

Block 0x2a6
[0x2a6:0x2a6]
---
Predecessors: [0x1f1, 0x20a, 0x23c, 0x242]
Successors: [0x2a7]
---
0x2a6 JUMPDEST
---
0x2a6: JUMPDEST 
---
Entry stack: [V10, 0x94, V39, S0]
Stack pops: 0
Stack additions: []
Exit stack: [V10, 0x94, V39, S0]

================================

Block 0x2a7
[0x2a7:0x2a7]
---
Predecessors: [0x2a6]
Successors: [0x2a8]
---
0x2a7 JUMPDEST
---
0x2a7: JUMPDEST 
---
Entry stack: [V10, 0x94, V39, S0]
Stack pops: 0
Stack additions: []
Exit stack: [V10, 0x94, V39, S0]

================================

Block 0x2a8
[0x2a8:0x2a8]
---
Predecessors: [0x2a7]
Successors: [0x2a9]
---
0x2a8 JUMPDEST
---
0x2a8: JUMPDEST 
---
Entry stack: [V10, 0x94, V39, S0]
Stack pops: 0
Stack additions: []
Exit stack: [V10, 0x94, V39, S0]

================================

Block 0x2a9
[0x2a9:0x2a9]
---
Predecessors: [0x2a8]
Successors: [0x2aa]
---
0x2a9 JUMPDEST
---
0x2a9: JUMPDEST 
---
Entry stack: [V10, 0x94, V39, S0]
Stack pops: 0
Stack additions: []
Exit stack: [V10, 0x94, V39, S0]

================================

Block 0x2aa
[0x2aa:0x2ad]
---
Predecessors: [0x2a9]
Successors: [0x94]
---
0x2aa JUMPDEST
0x2ab POP
0x2ac POP
0x2ad JUMP
---
0x2aa: JUMPDEST 
0x2ad: JUMP 0x94
---
Entry stack: [V10, 0x94, V39, S0]
Stack pops: 3
Stack additions: []
Exit stack: [V10]

================================

Block 0x2ae
[0x2ae:0x2c5]
---
Predecessors: [0xaf]
Successors: [0x1ee, 0x2c6]
---
0x2ae JUMPDEST
0x2af PUSH1 0x0
0x2b1 SLOAD
0x2b2 CALLER
0x2b3 PUSH1 0x1
0x2b5 PUSH1 0xa0
0x2b7 PUSH1 0x2
0x2b9 EXP
0x2ba SUB
0x2bb SWAP1
0x2bc DUP2
0x2bd AND
0x2be SWAP2
0x2bf AND
0x2c0 EQ
0x2c1 ISZERO
0x2c2 PUSH2 0x1ee
0x2c5 JUMPI
---
0x2ae: JUMPDEST 
0x2af: V222 = 0x0
0x2b1: V223 = S[0x0]
0x2b2: V224 = CALLER
0x2b3: V225 = 0x1
0x2b5: V226 = 0xa0
0x2b7: V227 = 0x2
0x2b9: V228 = EXP 0x2 0xa0
0x2ba: V229 = SUB 0x10000000000000000000000000000000000000000 0x1
0x2bd: V230 = AND 0xffffffffffffffffffffffffffffffffffffffff V224
0x2bf: V231 = AND V223 0xffffffffffffffffffffffffffffffffffffffff
0x2c0: V232 = EQ V231 V230
0x2c1: V233 = ISZERO V232
0x2c2: V234 = 0x1ee
0x2c5: JUMPI 0x1ee V233
---
Entry stack: [V10, 0x94]
Stack pops: 0
Stack additions: []
Exit stack: [V10, 0x94]

================================

Block 0x2c6
[0x2c6:0x2d6]
---
Predecessors: [0x2ae]
Successors: [0x1ee, 0x2d7]
---
0x2c6 PUSH1 0x1
0x2c8 PUSH1 0xa0
0x2ca PUSH1 0x2
0x2cc EXP
0x2cd SUB
0x2ce ADDRESS
0x2cf AND
0x2d0 BALANCE
0x2d1 ISZERO
0x2d2 ISZERO
0x2d3 PUSH2 0x1ee
0x2d6 JUMPI
---
0x2c6: V235 = 0x1
0x2c8: V236 = 0xa0
0x2ca: V237 = 0x2
0x2cc: V238 = EXP 0x2 0xa0
0x2cd: V239 = SUB 0x10000000000000000000000000000000000000000 0x1
0x2ce: V240 = ADDRESS
0x2cf: V241 = AND V240 0xffffffffffffffffffffffffffffffffffffffff
0x2d0: V242 = BALANCE V241
0x2d1: V243 = ISZERO V242
0x2d2: V244 = ISZERO V243
0x2d3: V245 = 0x1ee
0x2d6: JUMPI 0x1ee V244
---
Entry stack: [V10, 0x94]
Stack pops: 0
Stack additions: []
Exit stack: [V10, 0x94]

================================

Block 0x2d7
[0x2d7:0x2e1]
---
Predecessors: [0x2c6]
Successors: []
---
0x2d7 CALLER
0x2d8 PUSH1 0x1
0x2da PUSH1 0xa0
0x2dc PUSH1 0x2
0x2de EXP
0x2df SUB
0x2e0 AND
0x2e1 SELFDESTRUCT
---
0x2d7: V246 = CALLER
0x2d8: V247 = 0x1
0x2da: V248 = 0xa0
0x2dc: V249 = 0x2
0x2de: V250 = EXP 0x2 0xa0
0x2df: V251 = SUB 0x10000000000000000000000000000000000000000 0x1
0x2e0: V252 = AND 0xffffffffffffffffffffffffffffffffffffffff V246
0x2e1: SELFDESTRUCT V252
---
Entry stack: [V10, 0x94]
Stack pops: 0
Stack additions: []
Exit stack: [V10, 0x94]

================================

Block 0x2e2
[0x2e2:0x2e2]
---
Predecessors: []
Successors: [0x2e3]
---
0x2e2 JUMPDEST
---
0x2e2: JUMPDEST 
---
Entry stack: []
Stack pops: 0
Stack additions: []
Exit stack: []

================================

Block 0x2e3
[0x2e3:0x2e3]
---
Predecessors: [0x2e2]
Successors: [0x2e4]
---
0x2e3 JUMPDEST
---
0x2e3: JUMPDEST 
---
Entry stack: []
Stack pops: 0
Stack additions: []
Exit stack: []

================================

Block 0x2e4
[0x2e4:0x2e4]
---
Predecessors: [0x2e3]
Successors: [0x2e5]
---
0x2e4 JUMPDEST
---
0x2e4: JUMPDEST 
---
Entry stack: []
Stack pops: 0
Stack additions: []
Exit stack: []

================================

Block 0x2e5
[0x2e5:0x2e6]
---
Predecessors: [0x2e4]
Successors: []
Has unresolved jump.
---
0x2e5 JUMPDEST
0x2e6 JUMP
---
0x2e5: JUMPDEST 
0x2e6: JUMP S0
---
Entry stack: []
Stack pops: 1
Stack additions: []
Exit stack: []

================================

Block 0x2e7
[0x2e7:0x2fe]
---
Predecessors: [0xc4]
Successors: [0x2ff, 0x338]
---
0x2e7 JUMPDEST
0x2e8 PUSH1 0x0
0x2ea SLOAD
0x2eb CALLER
0x2ec PUSH1 0x1
0x2ee PUSH1 0xa0
0x2f0 PUSH1 0x2
0x2f2 EXP
0x2f3 SUB
0x2f4 SWAP1
0x2f5 DUP2
0x2f6 AND
0x2f7 SWAP2
0x2f8 AND
0x2f9 EQ
0x2fa ISZERO
0x2fb PUSH2 0x338
0x2fe JUMPI
---
0x2e7: JUMPDEST 
0x2e8: V253 = 0x0
0x2ea: V254 = S[0x0]
0x2eb: V255 = CALLER
0x2ec: V256 = 0x1
0x2ee: V257 = 0xa0
0x2f0: V258 = 0x2
0x2f2: V259 = EXP 0x2 0xa0
0x2f3: V260 = SUB 0x10000000000000000000000000000000000000000 0x1
0x2f6: V261 = AND 0xffffffffffffffffffffffffffffffffffffffff V255
0x2f8: V262 = AND V254 0xffffffffffffffffffffffffffffffffffffffff
0x2f9: V263 = EQ V262 V261
0x2fa: V264 = ISZERO V263
0x2fb: V265 = 0x338
0x2fe: JUMPI 0x338 V264
---
Entry stack: [V10, 0x94, V59]
Stack pops: 0
Stack additions: []
Exit stack: [V10, 0x94, V59]

================================

Block 0x2ff
[0x2ff:0x30f]
---
Predecessors: [0x2e7]
Successors: [0x310, 0x338]
---
0x2ff PUSH1 0x1
0x301 PUSH1 0xa0
0x303 PUSH1 0x2
0x305 EXP
0x306 SUB
0x307 ADDRESS
0x308 AND
0x309 BALANCE
0x30a ISZERO
0x30b ISZERO
0x30c PUSH2 0x338
0x30f JUMPI
---
0x2ff: V266 = 0x1
0x301: V267 = 0xa0
0x303: V268 = 0x2
0x305: V269 = EXP 0x2 0xa0
0x306: V270 = SUB 0x10000000000000000000000000000000000000000 0x1
0x307: V271 = ADDRESS
0x308: V272 = AND V271 0xffffffffffffffffffffffffffffffffffffffff
0x309: V273 = BALANCE V272
0x30a: V274 = ISZERO V273
0x30b: V275 = ISZERO V274
0x30c: V276 = 0x338
0x30f: JUMPI 0x338 V275
---
Entry stack: [V10, 0x94, V59]
Stack pops: 0
Stack additions: []
Exit stack: [V10, 0x94, V59]

================================

Block 0x310
[0x310:0x337]
---
Predecessors: [0x2ff]
Successors: [0x338]
---
0x310 PUSH1 0x0
0x312 DUP1
0x313 SLOAD
0x314 PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x329 NOT
0x32a AND
0x32b PUSH1 0x1
0x32d PUSH1 0xa0
0x32f PUSH1 0x2
0x331 EXP
0x332 SUB
0x333 DUP4
0x334 AND
0x335 OR
0x336 SWAP1
0x337 SSTORE
---
0x310: V277 = 0x0
0x313: V278 = S[0x0]
0x314: V279 = 0xffffffffffffffffffffffffffffffffffffffff
0x329: V280 = NOT 0xffffffffffffffffffffffffffffffffffffffff
0x32a: V281 = AND 0xffffffffffffffffffffffff0000000000000000000000000000000000000000 V278
0x32b: V282 = 0x1
0x32d: V283 = 0xa0
0x32f: V284 = 0x2
0x331: V285 = EXP 0x2 0xa0
0x332: V286 = SUB 0x10000000000000000000000000000000000000000 0x1
0x334: V287 = AND V59 0xffffffffffffffffffffffffffffffffffffffff
0x335: V288 = OR V287 V281
0x337: S[0x0] = V288
---
Entry stack: [V10, 0x94, V59]
Stack pops: 1
Stack additions: [S0]
Exit stack: [V10, 0x94, V59]

================================

Block 0x338
[0x338:0x338]
---
Predecessors: [0x2e7, 0x2ff, 0x310]
Successors: [0x339]
---
0x338 JUMPDEST
---
0x338: JUMPDEST 
---
Entry stack: [V10, 0x94, V59]
Stack pops: 0
Stack additions: []
Exit stack: [V10, 0x94, V59]

================================

Block 0x339
[0x339:0x339]
---
Predecessors: [0x338]
Successors: [0x33a]
---
0x339 JUMPDEST
---
0x339: JUMPDEST 
---
Entry stack: [V10, 0x94, V59]
Stack pops: 0
Stack additions: []
Exit stack: [V10, 0x94, V59]

================================

Block 0x33a
[0x33a:0x33a]
---
Predecessors: [0x339]
Successors: [0x33b]
---
0x33a JUMPDEST
---
0x33a: JUMPDEST 
---
Entry stack: [V10, 0x94, V59]
Stack pops: 0
Stack additions: []
Exit stack: [V10, 0x94, V59]

================================

Block 0x33b
[0x33b:0x33d]
---
Predecessors: [0x33a]
Successors: [0x94]
---
0x33b JUMPDEST
0x33c POP
0x33d JUMP
---
0x33b: JUMPDEST 
0x33d: JUMP 0x94
---
Entry stack: [V10, 0x94, V59]
Stack pops: 2
Stack additions: []
Exit stack: [V10]

================================

Block 0x33e
[0x33e:0x34c]
---
Predecessors: [0xe5]
Successors: [0xed]
---
0x33e JUMPDEST
0x33f PUSH1 0x1
0x341 SLOAD
0x342 PUSH1 0x1
0x344 PUSH1 0xa0
0x346 PUSH1 0x2
0x348 EXP
0x349 SUB
0x34a AND
0x34b DUP2
0x34c JUMP
---
0x33e: JUMPDEST 
0x33f: V289 = 0x1
0x341: V290 = S[0x1]
0x342: V291 = 0x1
0x344: V292 = 0xa0
0x346: V293 = 0x2
0x348: V294 = EXP 0x2 0xa0
0x349: V295 = SUB 0x10000000000000000000000000000000000000000 0x1
0x34a: V296 = AND 0xffffffffffffffffffffffffffffffffffffffff V290
0x34c: JUMP 0xed
---
Entry stack: [V10, 0xed]
Stack pops: 1
Stack additions: [S0, V296]
Exit stack: [V10, 0xed, V296]

================================

Block 0x34d
[0x34d:0x3b5]
---
Predecessors: [0x114]
Successors: [0x3b6]
---
0x34d JUMPDEST
0x34e PUSH1 0x1
0x350 DUP1
0x351 SLOAD
0x352 PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x367 NOT
0x368 AND
0x369 CALLER
0x36a PUSH1 0x1
0x36c PUSH1 0xa0
0x36e PUSH1 0x2
0x370 EXP
0x371 SUB
0x372 SWAP1
0x373 DUP2
0x374 AND
0x375 SWAP2
0x376 SWAP1
0x377 SWAP2
0x378 OR
0x379 SWAP2
0x37a DUP3
0x37b SWAP1
0x37c SSTORE
0x37d PUSH1 0x3
0x37f DUP4
0x380 SWAP1
0x381 SSTORE
0x382 AND
0x383 PUSH32 0x25ff68dd81b34665b5ba7e553ee5511bf6812e12adb4a7e2c0d9e26b3099ce79
0x3a4 DUP3
0x3a5 PUSH1 0x40
0x3a7 MLOAD
0x3a8 SWAP1
0x3a9 DUP2
0x3aa MSTORE
0x3ab PUSH1 0x20
0x3ad ADD
0x3ae PUSH1 0x40
0x3b0 MLOAD
0x3b1 DUP1
0x3b2 SWAP2
0x3b3 SUB
0x3b4 SWAP1
0x3b5 LOG2
---
0x34d: JUMPDEST 
0x34e: V297 = 0x1
0x351: V298 = S[0x1]
0x352: V299 = 0xffffffffffffffffffffffffffffffffffffffff
0x367: V300 = NOT 0xffffffffffffffffffffffffffffffffffffffff
0x368: V301 = AND 0xffffffffffffffffffffffff0000000000000000000000000000000000000000 V298
0x369: V302 = CALLER
0x36a: V303 = 0x1
0x36c: V304 = 0xa0
0x36e: V305 = 0x2
0x370: V306 = EXP 0x2 0xa0
0x371: V307 = SUB 0x10000000000000000000000000000000000000000 0x1
0x374: V308 = AND 0xffffffffffffffffffffffffffffffffffffffff V302
0x378: V309 = OR V308 V301
0x37c: S[0x1] = V309
0x37d: V310 = 0x3
0x381: S[0x3] = V86
0x382: V311 = AND 0xffffffffffffffffffffffffffffffffffffffff V309
0x383: V312 = 0x25ff68dd81b34665b5ba7e553ee5511bf6812e12adb4a7e2c0d9e26b3099ce79
0x3a5: V313 = 0x40
0x3a7: V314 = M[0x40]
0x3aa: M[V314] = V86
0x3ab: V315 = 0x20
0x3ad: V316 = ADD 0x20 V314
0x3ae: V317 = 0x40
0x3b0: V318 = M[0x40]
0x3b3: V319 = SUB V316 V318
0x3b5: LOG V318 V319 0x25ff68dd81b34665b5ba7e553ee5511bf6812e12adb4a7e2c0d9e26b3099ce79 V311
---
Entry stack: [V10, 0x94, V86]
Stack pops: 1
Stack additions: [S0]
Exit stack: [V10, 0x94, V86]

================================

Block 0x3b6
[0x3b6:0x3b8]
---
Predecessors: [0x34d]
Successors: [0x94]
---
0x3b6 JUMPDEST
0x3b7 POP
0x3b8 JUMP
---
0x3b6: JUMPDEST 
0x3b8: JUMP 0x94
---
Entry stack: [V10, 0x94, V86]
Stack pops: 2
Stack additions: []
Exit stack: [V10]

================================

Block 0x3b9
[0x3b9:0x3be]
---
Predecessors: [0x136]
Successors: [0x13e]
---
0x3b9 JUMPDEST
0x3ba PUSH1 0x3
0x3bc SLOAD
0x3bd DUP2
0x3be JUMP
---
0x3b9: JUMPDEST 
0x3ba: V320 = 0x3
0x3bc: V321 = S[0x3]
0x3be: JUMP 0x13e
---
Entry stack: [V10, 0x13e]
Stack pops: 1
Stack additions: [S0, V321]
Exit stack: [V10, 0x13e, V321]

================================

Block 0x3bf
[0x3bf:0x3d0]
---
Predecessors: [0x15b]
Successors: [0x13e]
---
0x3bf JUMPDEST
0x3c0 PUSH1 0x2
0x3c2 PUSH1 0x20
0x3c4 MSTORE
0x3c5 PUSH1 0x0
0x3c7 SWAP1
0x3c8 DUP2
0x3c9 MSTORE
0x3ca PUSH1 0x40
0x3cc SWAP1
0x3cd SHA3
0x3ce SLOAD
0x3cf DUP2
0x3d0 JUMP
---
0x3bf: JUMPDEST 
0x3c0: V322 = 0x2
0x3c2: V323 = 0x20
0x3c4: M[0x20] = 0x2
0x3c5: V324 = 0x0
0x3c9: M[0x0] = V115
0x3ca: V325 = 0x40
0x3cd: V326 = SHA3 0x0 0x40
0x3ce: V327 = S[V326]
0x3d0: JUMP 0x13e
---
Entry stack: [V10, 0x13e, V115]
Stack pops: 2
Stack additions: [S1, V327]
Exit stack: [V10, 0x13e, V327]

================================

Block 0x3d1
[0x3d1:0x3fc]
---
Predecessors: []
Successors: []
---
0x3d1 STOP
0x3d2 LOG1
0x3d3 PUSH6 0x627a7a723058
0x3da SHA3
0x3db ADDMOD
0x3dc CALL
0x3dd CREATE2
0x3de MISSING 0xbe
0x3df SIGNEXTEND
0x3e0 MISSING 0xcb
0x3e1 DUP8
0x3e2 MISSING 0x1f
0x3e3 MISSING 0xdc
0x3e4 CODECOPY
0x3e5 MISSING 0x5f
0x3e6 MISSING 0xcd
0x3e7 MLOAD
0x3e8 DIV
0x3e9 PUSH9 0x54dd3079a99106ecf1
0x3f3 CALL
0x3f4 INVALID
0x3f5 MISSING 0xb7
0x3f6 MISSING 0xdd
0x3f7 MISSING 0x1e
0x3f8 PUSH2 0xcd18
0x3fb STOP
0x3fc MISSING 0x29
---
0x3d1: STOP 
0x3d2: LOG S0 S1 S2
0x3d3: V328 = 0x627a7a723058
0x3da: V329 = SHA3 0x627a7a723058 S3
0x3db: V330 = ADDMOD V329 S4 S5
0x3dc: V331 = CALL V330 S6 S7 S8 S9 S10 S11
0x3dd: V332 = CREATE2 V331 S12 S13 S14
0x3de: MISSING 0xbe
0x3df: V333 = SIGNEXTEND S0 S1
0x3e0: MISSING 0xcb
0x3e2: MISSING 0x1f
0x3e3: MISSING 0xdc
0x3e4: CODECOPY S0 S1 S2
0x3e5: MISSING 0x5f
0x3e6: MISSING 0xcd
0x3e7: V334 = M[S0]
0x3e8: V335 = DIV V334 S1
0x3e9: V336 = 0x54dd3079a99106ecf1
0x3f3: V337 = CALL 0x54dd3079a99106ecf1 V335 S2 S3 S4 S5 S6
0x3f4: INVALID 
0x3f5: MISSING 0xb7
0x3f6: MISSING 0xdd
0x3f7: MISSING 0x1e
0x3f8: V338 = 0xcd18
0x3fb: STOP 
0x3fc: MISSING 0x29
---
Entry stack: []
Stack pops: 0
Stack additions: [V332, V333, S7, S0, S1, S2, S3, S4, S5, S6, S7, V337, 0xcd18]
Exit stack: []

================================

Function 0:
Public function signature: 0x2e1a7d4d
Entry block: 0x97
Exit block: 0x95
Body: 0x94, 0x95, 0x97, 0x1f1, 0x20a, 0x213, 0x237, 0x23c, 0x242, 0x2a6, 0x2a7, 0x2a8, 0x2a9, 0x2aa

Function 1:
Public function signature: 0x41c0e1b5
Entry block: 0xa4
Exit block: 0x95
Body: 0x94, 0x95, 0xa4, 0xab, 0xaf, 0x2ae, 0x2c6, 0x2d7

Function 2:
Public function signature: 0x4fb2e45d
Entry block: 0xb9
Exit block: 0x95
Body: 0x94, 0x95, 0xb9, 0xc0, 0xc4, 0x2e7, 0x2ff, 0x310, 0x338, 0x339, 0x33a, 0x33b

Function 3:
Public function signature: 0xb4a99a4e
Entry block: 0xda
Exit block: 0xed
Body: 0xda, 0xe1, 0xe5, 0xed, 0x33e

Function 4:
Public function signature: 0xb7f9c4f6
Entry block: 0x109
Exit block: 0x95
Body: 0x94, 0x95, 0x109, 0x110, 0x114, 0x34d, 0x3b6

Function 5:
Public function signature: 0xd0e30db0
Entry block: 0x8b
Exit block: 0x95
Body: 0x8b, 0x8c, 0x94, 0x95

Function 6:
Public function signature: 0xec8cb281
Entry block: 0x12b
Exit block: 0x13e
Body: 0x12b, 0x132, 0x136, 0x13e, 0x3b9

Function 7:
Public function signature: 0xfc7e286d
Entry block: 0x150
Exit block: 0x13e
Body: 0x13e, 0x150, 0x157, 0x15b, 0x3bf

Function 8:
Public fallback function
Entry block: 0x8b
Exit block: 0x95
Body: 0x8b, 0x8c, 0x94, 0x95

Function 9:
Private function
Entry block: 0x181
Exit block: 0x3b6
Body: 0x181, 0x191, 0x1ee, 0x1ef

