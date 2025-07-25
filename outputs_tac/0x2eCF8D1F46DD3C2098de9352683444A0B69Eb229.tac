Block 0x0
[0x0:0xc]
---
Predecessors: []
Successors: [0xd, 0x4c]
---
0x0 PUSH1 0x60
0x2 PUSH1 0x40
0x4 MSTORE
0x5 PUSH1 0x4
0x7 CALLDATASIZE
0x8 LT
0x9 PUSH2 0x4c
0xc JUMPI
---
0x0: V0 = 0x60
0x2: V1 = 0x40
0x4: M[0x40] = 0x60
0x5: V2 = 0x4
0x7: V3 = CALLDATASIZE
0x8: V4 = LT V3 0x4
0x9: V5 = 0x4c
0xc: JUMPI 0x4c V4
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
Successors: [0x41, 0x4e]
---
0xd PUSH1 0x0
0xf CALLDATALOAD
0x10 PUSH29 0x100000000000000000000000000000000000000000000000000000000
0x2e SWAP1
0x2f DIV
0x30 PUSH4 0xffffffff
0x35 AND
0x36 DUP1
0x37 PUSH4 0x3ccfd60b
0x3c EQ
0x3d PUSH2 0x4e
0x40 JUMPI
---
0xd: V6 = 0x0
0xf: V7 = CALLDATALOAD 0x0
0x10: V8 = 0x100000000000000000000000000000000000000000000000000000000
0x2f: V9 = DIV V7 0x100000000000000000000000000000000000000000000000000000000
0x30: V10 = 0xffffffff
0x35: V11 = AND 0xffffffff V9
0x37: V12 = 0x3ccfd60b
0x3c: V13 = EQ 0x3ccfd60b V11
0x3d: V14 = 0x4e
0x40: JUMPI 0x4e V13
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
Successors: [0x4c, 0x58]
---
0x41 DUP1
0x42 PUSH4 0xa163a624
0x47 EQ
0x48 PUSH2 0x58
0x4b JUMPI
---
0x42: V15 = 0xa163a624
0x47: V16 = EQ 0xa163a624 V11
0x48: V17 = 0x58
0x4b: JUMPI 0x58 V16
---
Entry stack: [V11]
Stack pops: 1
Stack additions: [S0]
Exit stack: [V11]

================================

Block 0x4c
[0x4c:0x4d]
---
Predecessors: [0x0, 0x41]
Successors: []
---
0x4c JUMPDEST
0x4d STOP
---
0x4c: JUMPDEST 
0x4d: STOP 
---
Entry stack: [V11]
Stack pops: 0
Stack additions: []
Exit stack: [V11]

================================

Block 0x4e
[0x4e:0x55]
---
Predecessors: [0xd]
Successors: [0x62]
---
0x4e JUMPDEST
0x4f PUSH2 0x56
0x52 PUSH2 0x62
0x55 JUMP
---
0x4e: JUMPDEST 
0x4f: V18 = 0x56
0x52: V19 = 0x62
0x55: JUMP 0x62
---
Entry stack: [V11]
Stack pops: 0
Stack additions: [0x56]
Exit stack: [V11, 0x56]

================================

Block 0x56
[0x56:0x57]
---
Predecessors: [0x135]
Successors: []
---
0x56 JUMPDEST
0x57 STOP
---
0x56: JUMPDEST 
0x57: STOP 
---
Entry stack: [V11]
Stack pops: 0
Stack additions: []
Exit stack: [V11]

================================

Block 0x58
[0x58:0x5f]
---
Predecessors: [0x41]
Successors: [0x137]
---
0x58 JUMPDEST
0x59 PUSH2 0x60
0x5c PUSH2 0x137
0x5f JUMP
---
0x58: JUMPDEST 
0x59: V20 = 0x60
0x5c: V21 = 0x137
0x5f: JUMP 0x137
---
Entry stack: [V11]
Stack pops: 0
Stack additions: [0x60]
Exit stack: [V11, 0x60]

================================

Block 0x60
[0x60:0x61]
---
Predecessors: [0x1ce]
Successors: []
---
0x60 JUMPDEST
0x61 STOP
---
0x60: JUMPDEST 
0x61: STOP 
---
Entry stack: [V11]
Stack pops: 0
Stack additions: []
Exit stack: [V11]

================================

Block 0x62
[0x62:0xb8]
---
Predecessors: [0x4e]
Successors: [0xb9, 0xbd]
---
0x62 JUMPDEST
0x63 PUSH1 0x0
0x65 DUP1
0x66 SWAP1
0x67 SLOAD
0x68 SWAP1
0x69 PUSH2 0x100
0x6c EXP
0x6d SWAP1
0x6e DIV
0x6f PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x84 AND
0x85 PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x9a AND
0x9b CALLER
0x9c PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0xb1 AND
0xb2 EQ
0xb3 ISZERO
0xb4 ISZERO
0xb5 PUSH2 0xbd
0xb8 JUMPI
---
0x62: JUMPDEST 
0x63: V22 = 0x0
0x67: V23 = S[0x0]
0x69: V24 = 0x100
0x6c: V25 = EXP 0x100 0x0
0x6e: V26 = DIV V23 0x1
0x6f: V27 = 0xffffffffffffffffffffffffffffffffffffffff
0x84: V28 = AND 0xffffffffffffffffffffffffffffffffffffffff V26
0x85: V29 = 0xffffffffffffffffffffffffffffffffffffffff
0x9a: V30 = AND 0xffffffffffffffffffffffffffffffffffffffff V28
0x9b: V31 = CALLER
0x9c: V32 = 0xffffffffffffffffffffffffffffffffffffffff
0xb1: V33 = AND 0xffffffffffffffffffffffffffffffffffffffff V31
0xb2: V34 = EQ V33 V30
0xb3: V35 = ISZERO V34
0xb4: V36 = ISZERO V35
0xb5: V37 = 0xbd
0xb8: JUMPI 0xbd V36
---
Entry stack: [V11, 0x56]
Stack pops: 0
Stack additions: []
Exit stack: [V11, 0x56]

================================

Block 0xb9
[0xb9:0xbc]
---
Predecessors: [0x62]
Successors: []
---
0xb9 PUSH1 0x0
0xbb DUP1
0xbc REVERT
---
0xb9: V38 = 0x0
0xbc: REVERT 0x0 0x0
---
Entry stack: [V11, 0x56]
Stack pops: 0
Stack additions: []
Exit stack: [V11, 0x56]

================================

Block 0xbd
[0xbd:0x130]
---
Predecessors: [0x62]
Successors: [0x131, 0x135]
---
0xbd JUMPDEST
0xbe PUSH1 0x0
0xc0 DUP1
0xc1 SWAP1
0xc2 SLOAD
0xc3 SWAP1
0xc4 PUSH2 0x100
0xc7 EXP
0xc8 SWAP1
0xc9 DIV
0xca PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0xdf AND
0xe0 PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0xf5 AND
0xf6 PUSH2 0x8fc
0xf9 ADDRESS
0xfa PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x10f AND
0x110 BALANCE
0x111 SWAP1
0x112 DUP2
0x113 ISZERO
0x114 MUL
0x115 SWAP1
0x116 PUSH1 0x40
0x118 MLOAD
0x119 PUSH1 0x0
0x11b PUSH1 0x40
0x11d MLOAD
0x11e DUP1
0x11f DUP4
0x120 SUB
0x121 DUP2
0x122 DUP6
0x123 DUP9
0x124 DUP9
0x125 CALL
0x126 SWAP4
0x127 POP
0x128 POP
0x129 POP
0x12a POP
0x12b ISZERO
0x12c ISZERO
0x12d PUSH2 0x135
0x130 JUMPI
---
0xbd: JUMPDEST 
0xbe: V39 = 0x0
0xc2: V40 = S[0x0]
0xc4: V41 = 0x100
0xc7: V42 = EXP 0x100 0x0
0xc9: V43 = DIV V40 0x1
0xca: V44 = 0xffffffffffffffffffffffffffffffffffffffff
0xdf: V45 = AND 0xffffffffffffffffffffffffffffffffffffffff V43
0xe0: V46 = 0xffffffffffffffffffffffffffffffffffffffff
0xf5: V47 = AND 0xffffffffffffffffffffffffffffffffffffffff V45
0xf6: V48 = 0x8fc
0xf9: V49 = ADDRESS
0xfa: V50 = 0xffffffffffffffffffffffffffffffffffffffff
0x10f: V51 = AND 0xffffffffffffffffffffffffffffffffffffffff V49
0x110: V52 = BALANCE V51
0x113: V53 = ISZERO V52
0x114: V54 = MUL V53 0x8fc
0x116: V55 = 0x40
0x118: V56 = M[0x40]
0x119: V57 = 0x0
0x11b: V58 = 0x40
0x11d: V59 = M[0x40]
0x120: V60 = SUB V56 V59
0x125: V61 = CALL V54 V47 V52 V59 V60 V59 0x0
0x12b: V62 = ISZERO V61
0x12c: V63 = ISZERO V62
0x12d: V64 = 0x135
0x130: JUMPI 0x135 V63
---
Entry stack: [V11, 0x56]
Stack pops: 0
Stack additions: []
Exit stack: [V11, 0x56]

================================

Block 0x131
[0x131:0x134]
---
Predecessors: [0xbd]
Successors: []
---
0x131 PUSH1 0x0
0x133 DUP1
0x134 REVERT
---
0x131: V65 = 0x0
0x134: REVERT 0x0 0x0
---
Entry stack: [V11, 0x56]
Stack pops: 0
Stack additions: []
Exit stack: [V11, 0x56]

================================

Block 0x135
[0x135:0x136]
---
Predecessors: [0xbd]
Successors: [0x56]
---
0x135 JUMPDEST
0x136 JUMP
---
0x135: JUMPDEST 
0x136: JUMP 0x56
---
Entry stack: [V11, 0x56]
Stack pops: 1
Stack additions: []
Exit stack: [V11]

================================

Block 0x137
[0x137:0x14c]
---
Predecessors: [0x58]
Successors: [0x14d, 0x1ce]
---
0x137 JUMPDEST
0x138 PUSH1 0x0
0x13a DUP1
0x13b PUSH1 0x0
0x13d PUSH8 0x16345785d8a0000
0x146 CALLVALUE
0x147 GT
0x148 ISZERO
0x149 PUSH2 0x1ce
0x14c JUMPI
---
0x137: JUMPDEST 
0x138: V66 = 0x0
0x13b: V67 = 0x0
0x13d: V68 = 0x16345785d8a0000
0x146: V69 = CALLVALUE
0x147: V70 = GT V69 0x16345785d8a0000
0x148: V71 = ISZERO V70
0x149: V72 = 0x1ce
0x14c: JUMPI 0x1ce V71
---
Entry stack: [V11, 0x60]
Stack pops: 0
Stack additions: [0x0, 0x0, 0x0]
Exit stack: [V11, 0x60, 0x0, 0x0, 0x0]

================================

Block 0x14d
[0x14d:0x158]
---
Predecessors: [0x137]
Successors: [0x159]
---
0x14d PUSH1 0x0
0x14f SWAP3
0x150 POP
0x151 PUSH1 0x0
0x153 SWAP2
0x154 POP
0x155 PUSH1 0x0
0x157 SWAP1
0x158 POP
---
0x14d: V73 = 0x0
0x151: V74 = 0x0
0x155: V75 = 0x0
---
Entry stack: [V11, 0x60, 0x0, 0x0, 0x0]
Stack pops: 3
Stack additions: [0x0, 0x0, 0x0]
Exit stack: [V11, 0x60, 0x0, 0x0, 0x0]

================================

Block 0x159
[0x159:0x167]
---
Predecessors: [0x14d, 0x17d]
Successors: [0x168, 0x18d]
---
0x159 JUMPDEST
0x15a PUSH1 0x2
0x15c CALLVALUE
0x15d MUL
0x15e DUP2
0x15f PUSH1 0xff
0x161 AND
0x162 LT
0x163 ISZERO
0x164 PUSH2 0x18d
0x167 JUMPI
---
0x159: JUMPDEST 
0x15a: V76 = 0x2
0x15c: V77 = CALLVALUE
0x15d: V78 = MUL V77 0x2
0x15f: V79 = 0xff
0x161: V80 = AND 0xff S0
0x162: V81 = LT V80 V78
0x163: V82 = ISZERO V81
0x164: V83 = 0x18d
0x167: JUMPI 0x18d V82
---
Entry stack: [V11, 0x60, S2, S1, S0]
Stack pops: 1
Stack additions: [S0]
Exit stack: [V11, 0x60, S2, S1, S0]

================================

Block 0x168
[0x168:0x178]
---
Predecessors: [0x159]
Successors: [0x179, 0x17d]
---
0x168 PUSH1 0x2
0x16a DUP2
0x16b MUL
0x16c PUSH1 0xff
0x16e AND
0x16f SWAP3
0x170 POP
0x171 DUP2
0x172 DUP4
0x173 LT
0x174 ISZERO
0x175 PUSH2 0x17d
0x178 JUMPI
---
0x168: V84 = 0x2
0x16b: V85 = MUL S0 0x2
0x16c: V86 = 0xff
0x16e: V87 = AND 0xff V85
0x173: V88 = LT V87 S1
0x174: V89 = ISZERO V88
0x175: V90 = 0x17d
0x178: JUMPI 0x17d V89
---
Entry stack: [V11, 0x60, S2, S1, S0]
Stack pops: 3
Stack additions: [V87, S1, S0]
Exit stack: [V11, 0x60, V87, S1, S0]

================================

Block 0x179
[0x179:0x17c]
---
Predecessors: [0x168]
Successors: [0x18d]
---
0x179 PUSH2 0x18d
0x17c JUMP
---
0x179: V91 = 0x18d
0x17c: JUMP 0x18d
---
Entry stack: [V11, 0x60, V87, S1, S0]
Stack pops: 0
Stack additions: []
Exit stack: [V11, 0x60, V87, S1, S0]

================================

Block 0x17d
[0x17d:0x18c]
---
Predecessors: [0x168]
Successors: [0x159]
---
0x17d JUMPDEST
0x17e DUP3
0x17f SWAP2
0x180 POP
0x181 DUP1
0x182 DUP1
0x183 PUSH1 0x1
0x185 ADD
0x186 SWAP2
0x187 POP
0x188 POP
0x189 PUSH2 0x159
0x18c JUMP
---
0x17d: JUMPDEST 
0x183: V92 = 0x1
0x185: V93 = ADD 0x1 S0
0x189: V94 = 0x159
0x18c: JUMP 0x159
---
Entry stack: [V11, 0x60, V87, S1, S0]
Stack pops: 3
Stack additions: [S2, S2, V93]
Exit stack: [V11, 0x60, V87, V87, V93]

================================

Block 0x18d
[0x18d:0x1c8]
---
Predecessors: [0x159, 0x179]
Successors: [0x1c9, 0x1cd]
---
0x18d JUMPDEST
0x18e CALLER
0x18f PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x1a4 AND
0x1a5 PUSH2 0x8fc
0x1a8 DUP4
0x1a9 SWAP1
0x1aa DUP2
0x1ab ISZERO
0x1ac MUL
0x1ad SWAP1
0x1ae PUSH1 0x40
0x1b0 MLOAD
0x1b1 PUSH1 0x0
0x1b3 PUSH1 0x40
0x1b5 MLOAD
0x1b6 DUP1
0x1b7 DUP4
0x1b8 SUB
0x1b9 DUP2
0x1ba DUP6
0x1bb DUP9
0x1bc DUP9
0x1bd CALL
0x1be SWAP4
0x1bf POP
0x1c0 POP
0x1c1 POP
0x1c2 POP
0x1c3 ISZERO
0x1c4 ISZERO
0x1c5 PUSH2 0x1cd
0x1c8 JUMPI
---
0x18d: JUMPDEST 
0x18e: V95 = CALLER
0x18f: V96 = 0xffffffffffffffffffffffffffffffffffffffff
0x1a4: V97 = AND 0xffffffffffffffffffffffffffffffffffffffff V95
0x1a5: V98 = 0x8fc
0x1ab: V99 = ISZERO S1
0x1ac: V100 = MUL V99 0x8fc
0x1ae: V101 = 0x40
0x1b0: V102 = M[0x40]
0x1b1: V103 = 0x0
0x1b3: V104 = 0x40
0x1b5: V105 = M[0x40]
0x1b8: V106 = SUB V102 V105
0x1bd: V107 = CALL V100 V97 S1 V105 V106 V105 0x0
0x1c3: V108 = ISZERO V107
0x1c4: V109 = ISZERO V108
0x1c5: V110 = 0x1cd
0x1c8: JUMPI 0x1cd V109
---
Entry stack: [V11, 0x60, S2, S1, S0]
Stack pops: 2
Stack additions: [S1, S0]
Exit stack: [V11, 0x60, S2, S1, S0]

================================

Block 0x1c9
[0x1c9:0x1cc]
---
Predecessors: [0x18d]
Successors: []
---
0x1c9 PUSH1 0x0
0x1cb DUP1
0x1cc REVERT
---
0x1c9: V111 = 0x0
0x1cc: REVERT 0x0 0x0
---
Entry stack: [V11, 0x60, S2, S1, S0]
Stack pops: 0
Stack additions: []
Exit stack: [V11, 0x60, S2, S1, S0]

================================

Block 0x1cd
[0x1cd:0x1cd]
---
Predecessors: [0x18d]
Successors: [0x1ce]
---
0x1cd JUMPDEST
---
0x1cd: JUMPDEST 
---
Entry stack: [V11, 0x60, S2, S1, S0]
Stack pops: 0
Stack additions: []
Exit stack: [V11, 0x60, S2, S1, S0]

================================

Block 0x1ce
[0x1ce:0x1d2]
---
Predecessors: [0x137, 0x1cd]
Successors: [0x60]
---
0x1ce JUMPDEST
0x1cf POP
0x1d0 POP
0x1d1 POP
0x1d2 JUMP
---
0x1ce: JUMPDEST 
0x1d2: JUMP 0x60
---
Entry stack: [V11, 0x60, S2, S1, S0]
Stack pops: 4
Stack additions: []
Exit stack: [V11]

================================

Block 0x1d3
[0x1d3:0x20b]
---
Predecessors: []
Successors: []
---
0x1d3 STOP
0x1d4 LOG1
0x1d5 PUSH6 0x627a7a723058
0x1dc SHA3
0x1dd MISSING 0xc5
0x1de PUSH19 0x65059392e0c48c3e28b7c4348108a5c46748e9
0x1f2 CALLVALUE
0x1f3 DUP13
0x1f4 MISSING 0xf7
0x1f5 DUP12
0x1f6 TIMESTAMP
0x1f7 SIGNEXTEND
0x1f8 PUSH19 0xbda164ff0029
---
0x1d3: STOP 
0x1d4: LOG S0 S1 S2
0x1d5: V112 = 0x627a7a723058
0x1dc: V113 = SHA3 0x627a7a723058 S3
0x1dd: MISSING 0xc5
0x1de: V114 = 0x65059392e0c48c3e28b7c4348108a5c46748e9
0x1f2: V115 = CALLVALUE
0x1f4: MISSING 0xf7
0x1f6: V116 = TIMESTAMP
0x1f7: V117 = SIGNEXTEND V116 S11
0x1f8: V118 = 0xbda164ff0029
---
Entry stack: []
Stack pops: 0
Stack additions: [V113, S10, V115, 0x65059392e0c48c3e28b7c4348108a5c46748e9, S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, 0xbda164ff0029, V117, S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11]
Exit stack: []

================================

Function 0:
Public function signature: 0x3ccfd60b
Entry block: 0x4e
Exit block: 0x56
Body: 0x4e, 0x56, 0x62, 0xb9, 0xbd, 0x131, 0x135

Function 1:
Public function signature: 0xa163a624
Entry block: 0x58
Exit block: 0x1c9
Body: 0x58, 0x60, 0x137, 0x14d, 0x159, 0x168, 0x179, 0x17d, 0x18d, 0x1c9, 0x1cd, 0x1ce

Function 2:
Public fallback function
Entry block: 0x4c
Exit block: 0x4c
Body: 0x4c

