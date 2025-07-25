Block 0x0
[0x0:0xc]
---
Predecessors: []
Successors: [0xd, 0x6d]
---
0x0 PUSH1 0x60
0x2 PUSH1 0x40
0x4 MSTORE
0x5 PUSH1 0x4
0x7 CALLDATASIZE
0x8 LT
0x9 PUSH2 0x6d
0xc JUMPI
---
0x0: V0 = 0x60
0x2: V1 = 0x40
0x4: M[0x40] = 0x60
0x5: V2 = 0x4
0x7: V3 = CALLDATASIZE
0x8: V4 = LT V3 0x4
0x9: V5 = 0x6d
0xc: JUMPI 0x6d V4
---
Entry stack: []
Stack pops: 0
Stack additions: []
Exit stack: []

================================

Block 0xd
[0xd:0x40]
---
Predecessors: [0x0]
Successors: [0x41, 0x6f]
---
0xd PUSH1 0x0
0xf CALLDATALOAD
0x10 PUSH29 0x100000000000000000000000000000000000000000000000000000000
0x2e SWAP1
0x2f DIV
0x30 PUSH4 0xffffffff
0x35 AND
0x36 DUP1
0x37 PUSH4 0x1a695230
0x3c EQ
0x3d PUSH2 0x6f
0x40 JUMPI
---
0xd: V6 = 0x0
0xf: V7 = CALLDATALOAD 0x0
0x10: V8 = 0x100000000000000000000000000000000000000000000000000000000
0x2f: V9 = DIV V7 0x100000000000000000000000000000000000000000000000000000000
0x30: V10 = 0xffffffff
0x35: V11 = AND 0xffffffff V9
0x37: V12 = 0x1a695230
0x3c: V13 = EQ 0x1a695230 V11
0x3d: V14 = 0x6f
0x40: JUMPI 0x6f V13
---
Entry stack: []
Stack pops: 0
Stack additions: [V11]
Exit stack: [V11]

================================

Block 0x41
[0x41:0x4b]
---
Predecessors: [0xd]
Successors: [0x4c, 0x9d]
---
0x41 DUP1
0x42 PUSH4 0x4f057506
0x47 EQ
0x48 PUSH2 0x9d
0x4b JUMPI
---
0x42: V15 = 0x4f057506
0x47: V16 = EQ 0x4f057506 V11
0x48: V17 = 0x9d
0x4b: JUMPI 0x9d V16
---
Entry stack: [V11]
Stack pops: 1
Stack additions: [S0]
Exit stack: [V11]

================================

Block 0x4c
[0x4c:0x56]
---
Predecessors: [0x41]
Successors: [0x57, 0xc6]
---
0x4c DUP1
0x4d PUSH4 0x8caa5c91
0x52 EQ
0x53 PUSH2 0xc6
0x56 JUMPI
---
0x4d: V18 = 0x8caa5c91
0x52: V19 = EQ 0x8caa5c91 V11
0x53: V20 = 0xc6
0x56: JUMPI 0xc6 V19
---
Entry stack: [V11]
Stack pops: 1
Stack additions: [S0]
Exit stack: [V11]

================================

Block 0x57
[0x57:0x61]
---
Predecessors: [0x4c]
Successors: [0x62, 0x11b]
---
0x57 DUP1
0x58 PUSH4 0xb4a99a4e
0x5d EQ
0x5e PUSH2 0x11b
0x61 JUMPI
---
0x58: V21 = 0xb4a99a4e
0x5d: V22 = EQ 0xb4a99a4e V11
0x5e: V23 = 0x11b
0x61: JUMPI 0x11b V22
---
Entry stack: [V11]
Stack pops: 1
Stack additions: [S0]
Exit stack: [V11]

================================

Block 0x62
[0x62:0x6c]
---
Predecessors: [0x57]
Successors: [0x6d, 0x170]
---
0x62 DUP1
0x63 PUSH4 0xfd28ec3e
0x68 EQ
0x69 PUSH2 0x170
0x6c JUMPI
---
0x63: V24 = 0xfd28ec3e
0x68: V25 = EQ 0xfd28ec3e V11
0x69: V26 = 0x170
0x6c: JUMPI 0x170 V25
---
Entry stack: [V11]
Stack pops: 1
Stack additions: [S0]
Exit stack: [V11]

================================

Block 0x6d
[0x6d:0x6e]
---
Predecessors: [0x0, 0x62]
Successors: []
---
0x6d JUMPDEST
0x6e STOP
---
0x6d: JUMPDEST 
0x6e: STOP 
---
Entry stack: [V11]
Stack pops: 0
Stack additions: []
Exit stack: [V11]

================================

Block 0x6f
[0x6f:0x9a]
---
Predecessors: [0xd]
Successors: [0x1b2]
---
0x6f JUMPDEST
0x70 PUSH2 0x9b
0x73 PUSH1 0x4
0x75 DUP1
0x76 DUP1
0x77 CALLDATALOAD
0x78 PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x8d AND
0x8e SWAP1
0x8f PUSH1 0x20
0x91 ADD
0x92 SWAP1
0x93 SWAP2
0x94 SWAP1
0x95 POP
0x96 POP
0x97 PUSH2 0x1b2
0x9a JUMP
---
0x6f: JUMPDEST 
0x70: V27 = 0x9b
0x73: V28 = 0x4
0x77: V29 = CALLDATALOAD 0x4
0x78: V30 = 0xffffffffffffffffffffffffffffffffffffffff
0x8d: V31 = AND 0xffffffffffffffffffffffffffffffffffffffff V29
0x8f: V32 = 0x20
0x91: V33 = ADD 0x20 0x4
0x97: V34 = 0x1b2
0x9a: JUMP 0x1b2
---
Entry stack: [V11]
Stack pops: 0
Stack additions: [0x9b, V31]
Exit stack: [V11, 0x9b, V31]

================================

Block 0x9b
[0x9b:0x9c]
---
Predecessors: [0x31d]
Successors: []
---
0x9b JUMPDEST
0x9c STOP
---
0x9b: JUMPDEST 
0x9c: STOP 
---
Entry stack: [V11]
Stack pops: 0
Stack additions: []
Exit stack: [V11]

================================

Block 0x9d
[0x9d:0xa3]
---
Predecessors: [0x41]
Successors: [0xa4, 0xa8]
---
0x9d JUMPDEST
0x9e CALLVALUE
0x9f ISZERO
0xa0 PUSH2 0xa8
0xa3 JUMPI
---
0x9d: JUMPDEST 
0x9e: V35 = CALLVALUE
0x9f: V36 = ISZERO V35
0xa0: V37 = 0xa8
0xa3: JUMPI 0xa8 V36
---
Entry stack: [V11]
Stack pops: 0
Stack additions: []
Exit stack: [V11]

================================

Block 0xa4
[0xa4:0xa7]
---
Predecessors: [0x9d]
Successors: []
---
0xa4 PUSH1 0x0
0xa6 DUP1
0xa7 REVERT
---
0xa4: V38 = 0x0
0xa7: REVERT 0x0 0x0
---
Entry stack: [V11]
Stack pops: 0
Stack additions: []
Exit stack: [V11]

================================

Block 0xa8
[0xa8:0xaf]
---
Predecessors: [0x9d]
Successors: [0x320]
---
0xa8 JUMPDEST
0xa9 PUSH2 0xb0
0xac PUSH2 0x320
0xaf JUMP
---
0xa8: JUMPDEST 
0xa9: V39 = 0xb0
0xac: V40 = 0x320
0xaf: JUMP 0x320
---
Entry stack: [V11]
Stack pops: 0
Stack additions: [0xb0]
Exit stack: [V11, 0xb0]

================================

Block 0xb0
[0xb0:0xc5]
---
Predecessors: [0x320]
Successors: []
---
0xb0 JUMPDEST
0xb1 PUSH1 0x40
0xb3 MLOAD
0xb4 DUP1
0xb5 DUP3
0xb6 DUP2
0xb7 MSTORE
0xb8 PUSH1 0x20
0xba ADD
0xbb SWAP2
0xbc POP
0xbd POP
0xbe PUSH1 0x40
0xc0 MLOAD
0xc1 DUP1
0xc2 SWAP2
0xc3 SUB
0xc4 SWAP1
0xc5 RETURN
---
0xb0: JUMPDEST 
0xb1: V41 = 0x40
0xb3: V42 = M[0x40]
0xb7: M[V42] = V168
0xb8: V43 = 0x20
0xba: V44 = ADD 0x20 V42
0xbe: V45 = 0x40
0xc0: V46 = M[0x40]
0xc3: V47 = SUB V44 V46
0xc5: RETURN V46 V47
---
Entry stack: [V11, 0xb0, V168]
Stack pops: 1
Stack additions: []
Exit stack: [V11, 0xb0]

================================

Block 0xc6
[0xc6:0xcc]
---
Predecessors: [0x4c]
Successors: [0xcd, 0xd1]
---
0xc6 JUMPDEST
0xc7 CALLVALUE
0xc8 ISZERO
0xc9 PUSH2 0xd1
0xcc JUMPI
---
0xc6: JUMPDEST 
0xc7: V48 = CALLVALUE
0xc8: V49 = ISZERO V48
0xc9: V50 = 0xd1
0xcc: JUMPI 0xd1 V49
---
Entry stack: [V11]
Stack pops: 0
Stack additions: []
Exit stack: [V11]

================================

Block 0xcd
[0xcd:0xd0]
---
Predecessors: [0xc6]
Successors: []
---
0xcd PUSH1 0x0
0xcf DUP1
0xd0 REVERT
---
0xcd: V51 = 0x0
0xd0: REVERT 0x0 0x0
---
Entry stack: [V11]
Stack pops: 0
Stack additions: []
Exit stack: [V11]

================================

Block 0xd1
[0xd1:0xd8]
---
Predecessors: [0xc6]
Successors: [0x326]
---
0xd1 JUMPDEST
0xd2 PUSH2 0xd9
0xd5 PUSH2 0x326
0xd8 JUMP
---
0xd1: JUMPDEST 
0xd2: V52 = 0xd9
0xd5: V53 = 0x326
0xd8: JUMP 0x326
---
Entry stack: [V11]
Stack pops: 0
Stack additions: [0xd9]
Exit stack: [V11, 0xd9]

================================

Block 0xd9
[0xd9:0x11a]
---
Predecessors: [0x326]
Successors: []
---
0xd9 JUMPDEST
0xda PUSH1 0x40
0xdc MLOAD
0xdd DUP1
0xde DUP3
0xdf PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0xf4 AND
0xf5 PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x10a AND
0x10b DUP2
0x10c MSTORE
0x10d PUSH1 0x20
0x10f ADD
0x110 SWAP2
0x111 POP
0x112 POP
0x113 PUSH1 0x40
0x115 MLOAD
0x116 DUP1
0x117 SWAP2
0x118 SUB
0x119 SWAP1
0x11a RETURN
---
0xd9: JUMPDEST 
0xda: V54 = 0x40
0xdc: V55 = M[0x40]
0xdf: V56 = 0xffffffffffffffffffffffffffffffffffffffff
0xf4: V57 = AND 0xffffffffffffffffffffffffffffffffffffffff V176
0xf5: V58 = 0xffffffffffffffffffffffffffffffffffffffff
0x10a: V59 = AND 0xffffffffffffffffffffffffffffffffffffffff V57
0x10c: M[V55] = V59
0x10d: V60 = 0x20
0x10f: V61 = ADD 0x20 V55
0x113: V62 = 0x40
0x115: V63 = M[0x40]
0x118: V64 = SUB V61 V63
0x11a: RETURN V63 V64
---
Entry stack: [V11, 0xd9, V176]
Stack pops: 1
Stack additions: []
Exit stack: [V11, 0xd9]

================================

Block 0x11b
[0x11b:0x121]
---
Predecessors: [0x57]
Successors: [0x122, 0x126]
---
0x11b JUMPDEST
0x11c CALLVALUE
0x11d ISZERO
0x11e PUSH2 0x126
0x121 JUMPI
---
0x11b: JUMPDEST 
0x11c: V65 = CALLVALUE
0x11d: V66 = ISZERO V65
0x11e: V67 = 0x126
0x121: JUMPI 0x126 V66
---
Entry stack: [V11]
Stack pops: 0
Stack additions: []
Exit stack: [V11]

================================

Block 0x122
[0x122:0x125]
---
Predecessors: [0x11b]
Successors: []
---
0x122 PUSH1 0x0
0x124 DUP1
0x125 REVERT
---
0x122: V68 = 0x0
0x125: REVERT 0x0 0x0
---
Entry stack: [V11]
Stack pops: 0
Stack additions: []
Exit stack: [V11]

================================

Block 0x126
[0x126:0x12d]
---
Predecessors: [0x11b]
Successors: [0x34c]
---
0x126 JUMPDEST
0x127 PUSH2 0x12e
0x12a PUSH2 0x34c
0x12d JUMP
---
0x126: JUMPDEST 
0x127: V69 = 0x12e
0x12a: V70 = 0x34c
0x12d: JUMP 0x34c
---
Entry stack: [V11]
Stack pops: 0
Stack additions: [0x12e]
Exit stack: [V11, 0x12e]

================================

Block 0x12e
[0x12e:0x16f]
---
Predecessors: [0x34c]
Successors: []
---
0x12e JUMPDEST
0x12f PUSH1 0x40
0x131 MLOAD
0x132 DUP1
0x133 DUP3
0x134 PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x149 AND
0x14a PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x15f AND
0x160 DUP2
0x161 MSTORE
0x162 PUSH1 0x20
0x164 ADD
0x165 SWAP2
0x166 POP
0x167 POP
0x168 PUSH1 0x40
0x16a MLOAD
0x16b DUP1
0x16c SWAP2
0x16d SUB
0x16e SWAP1
0x16f RETURN
---
0x12e: JUMPDEST 
0x12f: V71 = 0x40
0x131: V72 = M[0x40]
0x134: V73 = 0xffffffffffffffffffffffffffffffffffffffff
0x149: V74 = AND 0xffffffffffffffffffffffffffffffffffffffff V183
0x14a: V75 = 0xffffffffffffffffffffffffffffffffffffffff
0x15f: V76 = AND 0xffffffffffffffffffffffffffffffffffffffff V74
0x161: M[V72] = V76
0x162: V77 = 0x20
0x164: V78 = ADD 0x20 V72
0x168: V79 = 0x40
0x16a: V80 = M[0x40]
0x16d: V81 = SUB V78 V80
0x16f: RETURN V80 V81
---
Entry stack: [V11, 0x12e, V183]
Stack pops: 1
Stack additions: []
Exit stack: [V11, 0x12e]

================================

Block 0x170
[0x170:0x176]
---
Predecessors: [0x62]
Successors: [0x177, 0x17b]
---
0x170 JUMPDEST
0x171 CALLVALUE
0x172 ISZERO
0x173 PUSH2 0x17b
0x176 JUMPI
---
0x170: JUMPDEST 
0x171: V82 = CALLVALUE
0x172: V83 = ISZERO V82
0x173: V84 = 0x17b
0x176: JUMPI 0x17b V83
---
Entry stack: [V11]
Stack pops: 0
Stack additions: []
Exit stack: [V11]

================================

Block 0x177
[0x177:0x17a]
---
Predecessors: [0x170]
Successors: []
---
0x177 PUSH1 0x0
0x179 DUP1
0x17a REVERT
---
0x177: V85 = 0x0
0x17a: REVERT 0x0 0x0
---
Entry stack: [V11]
Stack pops: 0
Stack additions: []
Exit stack: [V11]

================================

Block 0x17b
[0x17b:0x1af]
---
Predecessors: [0x170]
Successors: [0x371]
---
0x17b JUMPDEST
0x17c PUSH2 0x1b0
0x17f PUSH1 0x4
0x181 DUP1
0x182 DUP1
0x183 CALLDATALOAD
0x184 PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x199 AND
0x19a SWAP1
0x19b PUSH1 0x20
0x19d ADD
0x19e SWAP1
0x19f SWAP2
0x1a0 SWAP1
0x1a1 DUP1
0x1a2 CALLDATALOAD
0x1a3 SWAP1
0x1a4 PUSH1 0x20
0x1a6 ADD
0x1a7 SWAP1
0x1a8 SWAP2
0x1a9 SWAP1
0x1aa POP
0x1ab POP
0x1ac PUSH2 0x371
0x1af JUMP
---
0x17b: JUMPDEST 
0x17c: V86 = 0x1b0
0x17f: V87 = 0x4
0x183: V88 = CALLDATALOAD 0x4
0x184: V89 = 0xffffffffffffffffffffffffffffffffffffffff
0x199: V90 = AND 0xffffffffffffffffffffffffffffffffffffffff V88
0x19b: V91 = 0x20
0x19d: V92 = ADD 0x20 0x4
0x1a2: V93 = CALLDATALOAD 0x24
0x1a4: V94 = 0x20
0x1a6: V95 = ADD 0x20 0x24
0x1ac: V96 = 0x371
0x1af: JUMP 0x371
---
Entry stack: [V11]
Stack pops: 0
Stack additions: [0x1b0, V90, V93]
Exit stack: [V11, 0x1b0, V90, V93]

================================

Block 0x1b0
[0x1b0:0x1b1]
---
Predecessors: [0x3cc]
Successors: []
---
0x1b0 JUMPDEST
0x1b1 STOP
---
0x1b0: JUMPDEST 
0x1b1: STOP 
---
Entry stack: [V11]
Stack pops: 0
Stack additions: []
Exit stack: [V11]

================================

Block 0x1b2
[0x1b2:0x1bc]
---
Predecessors: [0x6f]
Successors: [0x1bd, 0x31d]
---
0x1b2 JUMPDEST
0x1b3 PUSH1 0x2
0x1b5 SLOAD
0x1b6 CALLVALUE
0x1b7 GT
0x1b8 ISZERO
0x1b9 PUSH2 0x31d
0x1bc JUMPI
---
0x1b2: JUMPDEST 
0x1b3: V97 = 0x2
0x1b5: V98 = S[0x2]
0x1b6: V99 = CALLVALUE
0x1b7: V100 = GT V99 V98
0x1b8: V101 = ISZERO V100
0x1b9: V102 = 0x31d
0x1bc: JUMPI 0x31d V101
---
Entry stack: [V11, 0x9b, V31]
Stack pops: 0
Stack additions: []
Exit stack: [V11, 0x9b, V31]

================================

Block 0x1bd
[0x1bd:0x317]
---
Predecessors: [0x1b2]
Successors: [0x318, 0x31c]
---
0x1bd PUSH1 0x1
0x1bf PUSH1 0x0
0x1c1 SWAP1
0x1c2 SLOAD
0x1c3 SWAP1
0x1c4 PUSH2 0x100
0x1c7 EXP
0x1c8 SWAP1
0x1c9 DIV
0x1ca PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x1df AND
0x1e0 PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x1f5 AND
0x1f6 PUSH1 0x40
0x1f8 MLOAD
0x1f9 DUP1
0x1fa DUP1
0x1fb PUSH32 0x416464546f444228616464726573732900000000000000000000000000000000
0x21c DUP2
0x21d MSTORE
0x21e POP
0x21f PUSH1 0x10
0x221 ADD
0x222 SWAP1
0x223 POP
0x224 PUSH1 0x40
0x226 MLOAD
0x227 DUP1
0x228 SWAP2
0x229 SUB
0x22a SWAP1
0x22b SHA3
0x22c PUSH29 0x100000000000000000000000000000000000000000000000000000000
0x24a SWAP1
0x24b DIV
0x24c CALLER
0x24d PUSH1 0x40
0x24f MLOAD
0x250 DUP3
0x251 PUSH4 0xffffffff
0x256 AND
0x257 PUSH29 0x100000000000000000000000000000000000000000000000000000000
0x275 MUL
0x276 DUP2
0x277 MSTORE
0x278 PUSH1 0x4
0x27a ADD
0x27b DUP1
0x27c DUP3
0x27d PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x292 AND
0x293 PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x2a8 AND
0x2a9 DUP2
0x2aa MSTORE
0x2ab PUSH1 0x20
0x2ad ADD
0x2ae SWAP2
0x2af POP
0x2b0 POP
0x2b1 PUSH1 0x0
0x2b3 PUSH1 0x40
0x2b5 MLOAD
0x2b6 DUP1
0x2b7 DUP4
0x2b8 SUB
0x2b9 DUP2
0x2ba DUP7
0x2bb PUSH2 0x646e
0x2be GAS
0x2bf SUB
0x2c0 DELEGATECALL
0x2c1 SWAP3
0x2c2 POP
0x2c3 POP
0x2c4 POP
0x2c5 POP
0x2c6 DUP1
0x2c7 PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x2dc AND
0x2dd PUSH2 0x8fc
0x2e0 ADDRESS
0x2e1 PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x2f6 AND
0x2f7 BALANCE
0x2f8 SWAP1
0x2f9 DUP2
0x2fa ISZERO
0x2fb MUL
0x2fc SWAP1
0x2fd PUSH1 0x40
0x2ff MLOAD
0x300 PUSH1 0x0
0x302 PUSH1 0x40
0x304 MLOAD
0x305 DUP1
0x306 DUP4
0x307 SUB
0x308 DUP2
0x309 DUP6
0x30a DUP9
0x30b DUP9
0x30c CALL
0x30d SWAP4
0x30e POP
0x30f POP
0x310 POP
0x311 POP
0x312 ISZERO
0x313 ISZERO
0x314 PUSH2 0x31c
0x317 JUMPI
---
0x1bd: V103 = 0x1
0x1bf: V104 = 0x0
0x1c2: V105 = S[0x1]
0x1c4: V106 = 0x100
0x1c7: V107 = EXP 0x100 0x0
0x1c9: V108 = DIV V105 0x1
0x1ca: V109 = 0xffffffffffffffffffffffffffffffffffffffff
0x1df: V110 = AND 0xffffffffffffffffffffffffffffffffffffffff V108
0x1e0: V111 = 0xffffffffffffffffffffffffffffffffffffffff
0x1f5: V112 = AND 0xffffffffffffffffffffffffffffffffffffffff V110
0x1f6: V113 = 0x40
0x1f8: V114 = M[0x40]
0x1fb: V115 = 0x416464546f444228616464726573732900000000000000000000000000000000
0x21d: M[V114] = 0x416464546f444228616464726573732900000000000000000000000000000000
0x21f: V116 = 0x10
0x221: V117 = ADD 0x10 V114
0x224: V118 = 0x40
0x226: V119 = M[0x40]
0x229: V120 = SUB V117 V119
0x22b: V121 = SHA3 V119 V120
0x22c: V122 = 0x100000000000000000000000000000000000000000000000000000000
0x24b: V123 = DIV V121 0x100000000000000000000000000000000000000000000000000000000
0x24c: V124 = CALLER
0x24d: V125 = 0x40
0x24f: V126 = M[0x40]
0x251: V127 = 0xffffffff
0x256: V128 = AND 0xffffffff V123
0x257: V129 = 0x100000000000000000000000000000000000000000000000000000000
0x275: V130 = MUL 0x100000000000000000000000000000000000000000000000000000000 V128
0x277: M[V126] = V130
0x278: V131 = 0x4
0x27a: V132 = ADD 0x4 V126
0x27d: V133 = 0xffffffffffffffffffffffffffffffffffffffff
0x292: V134 = AND 0xffffffffffffffffffffffffffffffffffffffff V124
0x293: V135 = 0xffffffffffffffffffffffffffffffffffffffff
0x2a8: V136 = AND 0xffffffffffffffffffffffffffffffffffffffff V134
0x2aa: M[V132] = V136
0x2ab: V137 = 0x20
0x2ad: V138 = ADD 0x20 V132
0x2b1: V139 = 0x0
0x2b3: V140 = 0x40
0x2b5: V141 = M[0x40]
0x2b8: V142 = SUB V138 V141
0x2bb: V143 = 0x646e
0x2be: V144 = GAS
0x2bf: V145 = SUB V144 0x646e
0x2c0: V146 = DELEGATECALL V145 V112 V141 V142 V141 0x0
0x2c7: V147 = 0xffffffffffffffffffffffffffffffffffffffff
0x2dc: V148 = AND 0xffffffffffffffffffffffffffffffffffffffff V31
0x2dd: V149 = 0x8fc
0x2e0: V150 = ADDRESS
0x2e1: V151 = 0xffffffffffffffffffffffffffffffffffffffff
0x2f6: V152 = AND 0xffffffffffffffffffffffffffffffffffffffff V150
0x2f7: V153 = BALANCE V152
0x2fa: V154 = ISZERO V153
0x2fb: V155 = MUL V154 0x8fc
0x2fd: V156 = 0x40
0x2ff: V157 = M[0x40]
0x300: V158 = 0x0
0x302: V159 = 0x40
0x304: V160 = M[0x40]
0x307: V161 = SUB V157 V160
0x30c: V162 = CALL V155 V148 V153 V160 V161 V160 0x0
0x312: V163 = ISZERO V162
0x313: V164 = ISZERO V163
0x314: V165 = 0x31c
0x317: JUMPI 0x31c V164
---
Entry stack: [V11, 0x9b, V31]
Stack pops: 1
Stack additions: [S0]
Exit stack: [V11, 0x9b, V31]

================================

Block 0x318
[0x318:0x31b]
---
Predecessors: [0x1bd]
Successors: []
---
0x318 PUSH1 0x0
0x31a DUP1
0x31b REVERT
---
0x318: V166 = 0x0
0x31b: REVERT 0x0 0x0
---
Entry stack: [V11, 0x9b, V31]
Stack pops: 0
Stack additions: []
Exit stack: [V11, 0x9b, V31]

================================

Block 0x31c
[0x31c:0x31c]
---
Predecessors: [0x1bd]
Successors: [0x31d]
---
0x31c JUMPDEST
---
0x31c: JUMPDEST 
---
Entry stack: [V11, 0x9b, V31]
Stack pops: 0
Stack additions: []
Exit stack: [V11, 0x9b, V31]

================================

Block 0x31d
[0x31d:0x31f]
---
Predecessors: [0x1b2, 0x31c]
Successors: [0x9b]
---
0x31d JUMPDEST
0x31e POP
0x31f JUMP
---
0x31d: JUMPDEST 
0x31f: JUMP 0x9b
---
Entry stack: [V11, 0x9b, V31]
Stack pops: 2
Stack additions: []
Exit stack: [V11]

================================

Block 0x320
[0x320:0x325]
---
Predecessors: [0xa8]
Successors: [0xb0]
---
0x320 JUMPDEST
0x321 PUSH1 0x2
0x323 SLOAD
0x324 DUP2
0x325 JUMP
---
0x320: JUMPDEST 
0x321: V167 = 0x2
0x323: V168 = S[0x2]
0x325: JUMP 0xb0
---
Entry stack: [V11, 0xb0]
Stack pops: 1
Stack additions: [S0, V168]
Exit stack: [V11, 0xb0, V168]

================================

Block 0x326
[0x326:0x34b]
---
Predecessors: [0xd1]
Successors: [0xd9]
---
0x326 JUMPDEST
0x327 PUSH1 0x1
0x329 PUSH1 0x0
0x32b SWAP1
0x32c SLOAD
0x32d SWAP1
0x32e PUSH2 0x100
0x331 EXP
0x332 SWAP1
0x333 DIV
0x334 PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x349 AND
0x34a DUP2
0x34b JUMP
---
0x326: JUMPDEST 
0x327: V169 = 0x1
0x329: V170 = 0x0
0x32c: V171 = S[0x1]
0x32e: V172 = 0x100
0x331: V173 = EXP 0x100 0x0
0x333: V174 = DIV V171 0x1
0x334: V175 = 0xffffffffffffffffffffffffffffffffffffffff
0x349: V176 = AND 0xffffffffffffffffffffffffffffffffffffffff V174
0x34b: JUMP 0xd9
---
Entry stack: [V11, 0xd9]
Stack pops: 1
Stack additions: [S0, V176]
Exit stack: [V11, 0xd9, V176]

================================

Block 0x34c
[0x34c:0x370]
---
Predecessors: [0x126]
Successors: [0x12e]
---
0x34c JUMPDEST
0x34d PUSH1 0x0
0x34f DUP1
0x350 SWAP1
0x351 SLOAD
0x352 SWAP1
0x353 PUSH2 0x100
0x356 EXP
0x357 SWAP1
0x358 DIV
0x359 PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x36e AND
0x36f DUP2
0x370 JUMP
---
0x34c: JUMPDEST 
0x34d: V177 = 0x0
0x351: V178 = S[0x0]
0x353: V179 = 0x100
0x356: V180 = EXP 0x100 0x0
0x358: V181 = DIV V178 0x1
0x359: V182 = 0xffffffffffffffffffffffffffffffffffffffff
0x36e: V183 = AND 0xffffffffffffffffffffffffffffffffffffffff V181
0x370: JUMP 0x12e
---
Entry stack: [V11, 0x12e]
Stack pops: 1
Stack additions: [S0, V183]
Exit stack: [V11, 0x12e, V183]

================================

Block 0x371
[0x371:0x3c7]
---
Predecessors: [0x17b]
Successors: [0x3c8, 0x3cc]
---
0x371 JUMPDEST
0x372 PUSH1 0x0
0x374 DUP1
0x375 SWAP1
0x376 SLOAD
0x377 SWAP1
0x378 PUSH2 0x100
0x37b EXP
0x37c SWAP1
0x37d DIV
0x37e PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x393 AND
0x394 PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x3a9 AND
0x3aa CALLER
0x3ab PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x3c0 AND
0x3c1 EQ
0x3c2 ISZERO
0x3c3 ISZERO
0x3c4 PUSH2 0x3cc
0x3c7 JUMPI
---
0x371: JUMPDEST 
0x372: V184 = 0x0
0x376: V185 = S[0x0]
0x378: V186 = 0x100
0x37b: V187 = EXP 0x100 0x0
0x37d: V188 = DIV V185 0x1
0x37e: V189 = 0xffffffffffffffffffffffffffffffffffffffff
0x393: V190 = AND 0xffffffffffffffffffffffffffffffffffffffff V188
0x394: V191 = 0xffffffffffffffffffffffffffffffffffffffff
0x3a9: V192 = AND 0xffffffffffffffffffffffffffffffffffffffff V190
0x3aa: V193 = CALLER
0x3ab: V194 = 0xffffffffffffffffffffffffffffffffffffffff
0x3c0: V195 = AND 0xffffffffffffffffffffffffffffffffffffffff V193
0x3c1: V196 = EQ V195 V192
0x3c2: V197 = ISZERO V196
0x3c3: V198 = ISZERO V197
0x3c4: V199 = 0x3cc
0x3c7: JUMPI 0x3cc V198
---
Entry stack: [V11, 0x1b0, V90, V93]
Stack pops: 0
Stack additions: []
Exit stack: [V11, 0x1b0, V90, V93]

================================

Block 0x3c8
[0x3c8:0x3cb]
---
Predecessors: [0x371]
Successors: []
---
0x3c8 PUSH1 0x0
0x3ca DUP1
0x3cb REVERT
---
0x3c8: V200 = 0x0
0x3cb: REVERT 0x0 0x0
---
Entry stack: [V11, 0x1b0, V90, V93]
Stack pops: 0
Stack additions: []
Exit stack: [V11, 0x1b0, V90, V93]

================================

Block 0x3cc
[0x3cc:0x417]
---
Predecessors: [0x371]
Successors: [0x1b0]
---
0x3cc JUMPDEST
0x3cd DUP1
0x3ce PUSH1 0x2
0x3d0 DUP2
0x3d1 SWAP1
0x3d2 SSTORE
0x3d3 POP
0x3d4 DUP2
0x3d5 PUSH1 0x1
0x3d7 PUSH1 0x0
0x3d9 PUSH2 0x100
0x3dc EXP
0x3dd DUP2
0x3de SLOAD
0x3df DUP2
0x3e0 PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x3f5 MUL
0x3f6 NOT
0x3f7 AND
0x3f8 SWAP1
0x3f9 DUP4
0x3fa PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x40f AND
0x410 MUL
0x411 OR
0x412 SWAP1
0x413 SSTORE
0x414 POP
0x415 POP
0x416 POP
0x417 JUMP
---
0x3cc: JUMPDEST 
0x3ce: V201 = 0x2
0x3d2: S[0x2] = V93
0x3d5: V202 = 0x1
0x3d7: V203 = 0x0
0x3d9: V204 = 0x100
0x3dc: V205 = EXP 0x100 0x0
0x3de: V206 = S[0x1]
0x3e0: V207 = 0xffffffffffffffffffffffffffffffffffffffff
0x3f5: V208 = MUL 0xffffffffffffffffffffffffffffffffffffffff 0x1
0x3f6: V209 = NOT 0xffffffffffffffffffffffffffffffffffffffff
0x3f7: V210 = AND 0xffffffffffffffffffffffff0000000000000000000000000000000000000000 V206
0x3fa: V211 = 0xffffffffffffffffffffffffffffffffffffffff
0x40f: V212 = AND 0xffffffffffffffffffffffffffffffffffffffff V90
0x410: V213 = MUL V212 0x1
0x411: V214 = OR V213 V210
0x413: S[0x1] = V214
0x417: JUMP 0x1b0
---
Entry stack: [V11, 0x1b0, V90, V93]
Stack pops: 3
Stack additions: []
Exit stack: [V11]

================================

Block 0x418
[0x418:0x443]
---
Predecessors: []
Successors: []
---
0x418 STOP
0x419 LOG1
0x41a PUSH6 0x627a7a723058
0x421 SHA3
0x422 RETURN
0x423 PUSH26 0x2f58f7c184d0b6bcbc6ef5ef79f5075611e95084c42665af1b1
0x43e LOG2
0x43f MISSING 0xb8
0x440 MISSING 0xd2
0x441 SWAP9
0x442 STOP
0x443 MISSING 0x29
---
0x418: STOP 
0x419: LOG S0 S1 S2
0x41a: V215 = 0x627a7a723058
0x421: V216 = SHA3 0x627a7a723058 S3
0x422: RETURN V216 S4
0x423: V217 = 0x2f58f7c184d0b6bcbc6ef5ef79f5075611e95084c42665af1b1
0x43e: LOG 0x2f58f7c184d0b6bcbc6ef5ef79f5075611e95084c42665af1b1 S0 S1 S2
0x43f: MISSING 0xb8
0x440: MISSING 0xd2
0x442: STOP 
0x443: MISSING 0x29
---
Entry stack: []
Stack pops: 0
Stack additions: [S9, S1, S2, S3, S4, S5, S6, S7, S8, S0]
Exit stack: []

================================

Function 0:
Public function signature: 0x1a695230
Entry block: 0x6f
Exit block: 0x318
Body: 0x6f, 0x9b, 0x1b2, 0x1bd, 0x318, 0x31c, 0x31d

Function 1:
Public function signature: 0x4f057506
Entry block: 0x9d
Exit block: 0xb0
Body: 0x9d, 0xa4, 0xa8, 0xb0, 0x320

Function 2:
Public function signature: 0x8caa5c91
Entry block: 0xc6
Exit block: 0xd9
Body: 0xc6, 0xcd, 0xd1, 0xd9, 0x326

Function 3:
Public function signature: 0xb4a99a4e
Entry block: 0x11b
Exit block: 0x12e
Body: 0x11b, 0x122, 0x126, 0x12e, 0x34c

Function 4:
Public function signature: 0xfd28ec3e
Entry block: 0x170
Exit block: 0x1b0
Body: 0x170, 0x177, 0x17b, 0x1b0, 0x371, 0x3c8, 0x3cc

Function 5:
Public fallback function
Entry block: 0x6d
Exit block: 0x6d
Body: 0x6d

