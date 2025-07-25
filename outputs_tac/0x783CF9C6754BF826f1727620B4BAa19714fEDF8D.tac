Block 0x0
[0x0:0xc]
---
Predecessors: []
Successors: [0xd, 0x41]
---
0x0 PUSH1 0x60
0x2 PUSH1 0x40
0x4 MSTORE
0x5 PUSH1 0x4
0x7 CALLDATASIZE
0x8 LT
0x9 PUSH2 0x41
0xc JUMPI
---
0x0: V0 = 0x60
0x2: V1 = 0x40
0x4: M[0x40] = 0x60
0x5: V2 = 0x4
0x7: V3 = CALLDATASIZE
0x8: V4 = LT V3 0x4
0x9: V5 = 0x41
0xc: JUMPI 0x41 V4
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
Successors: [0x41, 0x43]
---
0xd PUSH1 0x0
0xf CALLDATALOAD
0x10 PUSH29 0x100000000000000000000000000000000000000000000000000000000
0x2e SWAP1
0x2f DIV
0x30 PUSH4 0xffffffff
0x35 AND
0x36 DUP1
0x37 PUSH4 0x29f0a422
0x3c EQ
0x3d PUSH2 0x43
0x40 JUMPI
---
0xd: V6 = 0x0
0xf: V7 = CALLDATALOAD 0x0
0x10: V8 = 0x100000000000000000000000000000000000000000000000000000000
0x2f: V9 = DIV V7 0x100000000000000000000000000000000000000000000000000000000
0x30: V10 = 0xffffffff
0x35: V11 = AND 0xffffffff V9
0x37: V12 = 0x29f0a422
0x3c: V13 = EQ 0x29f0a422 V11
0x3d: V14 = 0x43
0x40: JUMPI 0x43 V13
---
Entry stack: []
Stack pops: 0
Stack additions: [V11]
Exit stack: [V11]

================================

Block 0x41
[0x41:0x42]
---
Predecessors: [0x0, 0xd]
Successors: []
---
0x41 JUMPDEST
0x42 STOP
---
0x41: JUMPDEST 
0x42: STOP 
---
Entry stack: [V11]
Stack pops: 0
Stack additions: []
Exit stack: [V11]

================================

Block 0x43
[0x43:0x77]
---
Predecessors: [0xd]
Successors: [0x7a]
---
0x43 JUMPDEST
0x44 PUSH2 0x78
0x47 PUSH1 0x4
0x49 DUP1
0x4a DUP1
0x4b CALLDATALOAD
0x4c PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x61 AND
0x62 SWAP1
0x63 PUSH1 0x20
0x65 ADD
0x66 SWAP1
0x67 SWAP2
0x68 SWAP1
0x69 DUP1
0x6a CALLDATALOAD
0x6b SWAP1
0x6c PUSH1 0x20
0x6e ADD
0x6f SWAP1
0x70 SWAP2
0x71 SWAP1
0x72 POP
0x73 POP
0x74 PUSH2 0x7a
0x77 JUMP
---
0x43: JUMPDEST 
0x44: V15 = 0x78
0x47: V16 = 0x4
0x4b: V17 = CALLDATALOAD 0x4
0x4c: V18 = 0xffffffffffffffffffffffffffffffffffffffff
0x61: V19 = AND 0xffffffffffffffffffffffffffffffffffffffff V17
0x63: V20 = 0x20
0x65: V21 = ADD 0x20 0x4
0x6a: V22 = CALLDATALOAD 0x24
0x6c: V23 = 0x20
0x6e: V24 = ADD 0x20 0x24
0x74: V25 = 0x7a
0x77: JUMP 0x7a
---
Entry stack: [V11]
Stack pops: 0
Stack additions: [0x78, V19, V22]
Exit stack: [V11, 0x78, V19, V22]

================================

Block 0x78
[0x78:0x79]
---
Predecessors: [0x1f5]
Successors: []
---
0x78 JUMPDEST
0x79 STOP
---
0x78: JUMPDEST 
0x79: STOP 
---
Entry stack: [V11]
Stack pops: 0
Stack additions: []
Exit stack: [V11]

================================

Block 0x7a
[0x7a:0x8c]
---
Predecessors: [0x43]
Successors: [0x8d, 0x1f5]
---
0x7a JUMPDEST
0x7b PUSH1 0x0
0x7d PUSH8 0xde0b6b3a7640000
0x86 CALLVALUE
0x87 GT
0x88 ISZERO
0x89 PUSH2 0x1f5
0x8c JUMPI
---
0x7a: JUMPDEST 
0x7b: V26 = 0x0
0x7d: V27 = 0xde0b6b3a7640000
0x86: V28 = CALLVALUE
0x87: V29 = GT V28 0xde0b6b3a7640000
0x88: V30 = ISZERO V29
0x89: V31 = 0x1f5
0x8c: JUMPI 0x1f5 V30
---
Entry stack: [V11, 0x78, V19, V22]
Stack pops: 0
Stack additions: [0x0]
Exit stack: [V11, 0x78, V19, V22, 0x0]

================================

Block 0x8d
[0x8d:0xc1]
---
Predecessors: [0x7a]
Successors: [0xc2, 0xc6]
---
0x8d ORIGIN
0x8e PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0xa3 AND
0xa4 CALLER
0xa5 PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0xba AND
0xbb EQ
0xbc ISZERO
0xbd ISZERO
0xbe PUSH2 0xc6
0xc1 JUMPI
---
0x8d: V32 = ORIGIN
0x8e: V33 = 0xffffffffffffffffffffffffffffffffffffffff
0xa3: V34 = AND 0xffffffffffffffffffffffffffffffffffffffff V32
0xa4: V35 = CALLER
0xa5: V36 = 0xffffffffffffffffffffffffffffffffffffffff
0xba: V37 = AND 0xffffffffffffffffffffffffffffffffffffffff V35
0xbb: V38 = EQ V37 V34
0xbc: V39 = ISZERO V38
0xbd: V40 = ISZERO V39
0xbe: V41 = 0xc6
0xc1: JUMPI 0xc6 V40
---
Entry stack: [V11, 0x78, V19, V22, 0x0]
Stack pops: 0
Stack additions: []
Exit stack: [V11, 0x78, V19, V22, 0x0]

================================

Block 0xc2
[0xc2:0xc5]
---
Predecessors: [0x8d]
Successors: []
---
0xc2 PUSH1 0x0
0xc4 DUP1
0xc5 REVERT
---
0xc2: V42 = 0x0
0xc5: REVERT 0x0 0x0
---
Entry stack: [V11, 0x78, V19, V22, 0x0]
Stack pops: 0
Stack additions: []
Exit stack: [V11, 0x78, V19, V22, 0x0]

================================

Block 0xc6
[0xc6:0x10b]
---
Predecessors: [0x8d]
Successors: [0x1fa]
---
0xc6 JUMPDEST
0xc7 TIMESTAMP
0xc8 DUP2
0xc9 PUSH1 0x0
0xcb ADD
0xcc DUP2
0xcd SWAP1
0xce SSTORE
0xcf POP
0xd0 ADDRESS
0xd1 PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0xe6 AND
0xe7 BALANCE
0xe8 DUP2
0xe9 PUSH1 0x1
0xeb ADD
0xec DUP2
0xed SWAP1
0xee SSTORE
0xef POP
0xf0 DUP2
0xf1 DUP2
0xf2 PUSH1 0x2
0xf4 ADD
0xf5 DUP2
0xf6 SWAP1
0xf7 SSTORE
0xf8 POP
0xf9 PUSH1 0x3
0xfb DUP1
0xfc SLOAD
0xfd DUP1
0xfe PUSH1 0x1
0x100 ADD
0x101 DUP3
0x102 DUP2
0x103 PUSH2 0x10c
0x106 SWAP2
0x107 SWAP1
0x108 PUSH2 0x1fa
0x10b JUMP
---
0xc6: JUMPDEST 
0xc7: V43 = TIMESTAMP
0xc9: V44 = 0x0
0xcb: V45 = ADD 0x0 0x0
0xce: S[0x0] = V43
0xd0: V46 = ADDRESS
0xd1: V47 = 0xffffffffffffffffffffffffffffffffffffffff
0xe6: V48 = AND 0xffffffffffffffffffffffffffffffffffffffff V46
0xe7: V49 = BALANCE V48
0xe9: V50 = 0x1
0xeb: V51 = ADD 0x1 0x0
0xee: S[0x1] = V49
0xf2: V52 = 0x2
0xf4: V53 = ADD 0x2 0x0
0xf7: S[0x2] = V22
0xf9: V54 = 0x3
0xfc: V55 = S[0x3]
0xfe: V56 = 0x1
0x100: V57 = ADD 0x1 V55
0x103: V58 = 0x10c
0x108: V59 = 0x1fa
0x10b: JUMP 0x1fa
---
Entry stack: [V11, 0x78, V19, V22, 0x0]
Stack pops: 2
Stack additions: [S1, S0, 0x3, V55, V57, 0x10c, 0x3, V57]
Exit stack: [V11, 0x78, V19, V22, 0x0, 0x3, V55, V57, 0x10c, 0x3, V57]

================================

Block 0x10c
[0x10c:0x1f4]
---
Predecessors: [0x227]
Successors: [0x1f5]
---
0x10c JUMPDEST
0x10d SWAP2
0x10e PUSH1 0x0
0x110 MSTORE
0x111 PUSH1 0x20
0x113 PUSH1 0x0
0x115 SHA3
0x116 SWAP1
0x117 PUSH1 0x3
0x119 MUL
0x11a ADD
0x11b PUSH1 0x0
0x11d DUP4
0x11e SWAP1
0x11f SWAP2
0x120 SWAP1
0x121 SWAP2
0x122 POP
0x123 PUSH1 0x0
0x125 DUP3
0x126 ADD
0x127 SLOAD
0x128 DUP2
0x129 PUSH1 0x0
0x12b ADD
0x12c SSTORE
0x12d PUSH1 0x1
0x12f DUP3
0x130 ADD
0x131 SLOAD
0x132 DUP2
0x133 PUSH1 0x1
0x135 ADD
0x136 SSTORE
0x137 PUSH1 0x2
0x139 DUP3
0x13a ADD
0x13b SLOAD
0x13c DUP2
0x13d PUSH1 0x2
0x13f ADD
0x140 SSTORE
0x141 POP
0x142 POP
0x143 POP
0x144 PUSH1 0x4
0x146 PUSH1 0x0
0x148 SWAP1
0x149 SLOAD
0x14a SWAP1
0x14b PUSH2 0x100
0x14e EXP
0x14f SWAP1
0x150 DIV
0x151 PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x166 AND
0x167 PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x17c AND
0x17d PUSH2 0x8fc
0x180 PUSH1 0x1
0x182 SLOAD
0x183 SWAP1
0x184 DUP2
0x185 ISZERO
0x186 MUL
0x187 SWAP1
0x188 PUSH1 0x40
0x18a MLOAD
0x18b PUSH1 0x0
0x18d PUSH1 0x40
0x18f MLOAD
0x190 DUP1
0x191 DUP4
0x192 SUB
0x193 DUP2
0x194 DUP6
0x195 DUP9
0x196 DUP9
0x197 CALL
0x198 SWAP4
0x199 POP
0x19a POP
0x19b POP
0x19c POP
0x19d POP
0x19e DUP3
0x19f PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x1b4 AND
0x1b5 PUSH2 0x8fc
0x1b8 DUP4
0x1b9 SWAP1
0x1ba DUP2
0x1bb ISZERO
0x1bc MUL
0x1bd SWAP1
0x1be PUSH1 0x40
0x1c0 MLOAD
0x1c1 PUSH1 0x0
0x1c3 PUSH1 0x40
0x1c5 MLOAD
0x1c6 DUP1
0x1c7 DUP4
0x1c8 SUB
0x1c9 DUP2
0x1ca DUP6
0x1cb DUP9
0x1cc DUP9
0x1cd CALL
0x1ce SWAP4
0x1cf POP
0x1d0 POP
0x1d1 POP
0x1d2 POP
0x1d3 POP
0x1d4 PUSH1 0x1
0x1d6 SLOAD
0x1d7 PUSH1 0x0
0x1d9 DUP1
0x1da DUP3
0x1db DUP3
0x1dc SLOAD
0x1dd ADD
0x1de SWAP3
0x1df POP
0x1e0 POP
0x1e1 DUP2
0x1e2 SWAP1
0x1e3 SSTORE
0x1e4 POP
0x1e5 DUP2
0x1e6 PUSH1 0x2
0x1e8 PUSH1 0x0
0x1ea DUP3
0x1eb DUP3
0x1ec SLOAD
0x1ed ADD
0x1ee SWAP3
0x1ef POP
0x1f0 POP
0x1f1 DUP2
0x1f2 SWAP1
0x1f3 SSTORE
0x1f4 POP
---
0x10c: JUMPDEST 
0x10e: V60 = 0x0
0x110: M[0x0] = 0x3
0x111: V61 = 0x20
0x113: V62 = 0x0
0x115: V63 = SHA3 0x0 0x20
0x117: V64 = 0x3
0x119: V65 = MUL 0x3 V55
0x11a: V66 = ADD V65 V63
0x11b: V67 = 0x0
0x123: V68 = 0x0
0x126: V69 = ADD 0x0 0x0
0x127: V70 = S[0x0]
0x129: V71 = 0x0
0x12b: V72 = ADD 0x0 V66
0x12c: S[V72] = V70
0x12d: V73 = 0x1
0x130: V74 = ADD 0x0 0x1
0x131: V75 = S[0x1]
0x133: V76 = 0x1
0x135: V77 = ADD 0x1 V66
0x136: S[V77] = V75
0x137: V78 = 0x2
0x13a: V79 = ADD 0x0 0x2
0x13b: V80 = S[0x2]
0x13d: V81 = 0x2
0x13f: V82 = ADD 0x2 V66
0x140: S[V82] = V80
0x144: V83 = 0x4
0x146: V84 = 0x0
0x149: V85 = S[0x4]
0x14b: V86 = 0x100
0x14e: V87 = EXP 0x100 0x0
0x150: V88 = DIV V85 0x1
0x151: V89 = 0xffffffffffffffffffffffffffffffffffffffff
0x166: V90 = AND 0xffffffffffffffffffffffffffffffffffffffff V88
0x167: V91 = 0xffffffffffffffffffffffffffffffffffffffff
0x17c: V92 = AND 0xffffffffffffffffffffffffffffffffffffffff V90
0x17d: V93 = 0x8fc
0x180: V94 = 0x1
0x182: V95 = S[0x1]
0x185: V96 = ISZERO V95
0x186: V97 = MUL V96 0x8fc
0x188: V98 = 0x40
0x18a: V99 = M[0x40]
0x18b: V100 = 0x0
0x18d: V101 = 0x40
0x18f: V102 = M[0x40]
0x192: V103 = SUB V99 V102
0x197: V104 = CALL V97 V92 V95 V102 V103 V102 0x0
0x19f: V105 = 0xffffffffffffffffffffffffffffffffffffffff
0x1b4: V106 = AND 0xffffffffffffffffffffffffffffffffffffffff V19
0x1b5: V107 = 0x8fc
0x1bb: V108 = ISZERO V22
0x1bc: V109 = MUL V108 0x8fc
0x1be: V110 = 0x40
0x1c0: V111 = M[0x40]
0x1c1: V112 = 0x0
0x1c3: V113 = 0x40
0x1c5: V114 = M[0x40]
0x1c8: V115 = SUB V111 V114
0x1cd: V116 = CALL V109 V106 V22 V114 V115 V114 0x0
0x1d4: V117 = 0x1
0x1d6: V118 = S[0x1]
0x1d7: V119 = 0x0
0x1dc: V120 = S[0x0]
0x1dd: V121 = ADD V120 V118
0x1e3: S[0x0] = V121
0x1e6: V122 = 0x2
0x1e8: V123 = 0x0
0x1ec: V124 = S[0x2]
0x1ed: V125 = ADD V124 V22
0x1f3: S[0x2] = V125
---
Entry stack: [V11, 0x78, V19, V22, 0x0, 0x3, V55, V57]
Stack pops: 6
Stack additions: [S5, S4, S3]
Exit stack: [V11, 0x78, V19, V22, 0x0]

================================

Block 0x1f5
[0x1f5:0x1f9]
---
Predecessors: [0x7a, 0x10c]
Successors: [0x78]
---
0x1f5 JUMPDEST
0x1f6 POP
0x1f7 POP
0x1f8 POP
0x1f9 JUMP
---
0x1f5: JUMPDEST 
0x1f9: JUMP 0x78
---
Entry stack: [V11, 0x78, V19, V22, 0x0]
Stack pops: 4
Stack additions: []
Exit stack: [V11]

================================

Block 0x1fa
[0x1fa:0x207]
---
Predecessors: [0xc6]
Successors: [0x208, 0x227]
---
0x1fa JUMPDEST
0x1fb DUP2
0x1fc SLOAD
0x1fd DUP2
0x1fe DUP4
0x1ff SSTORE
0x200 DUP2
0x201 DUP2
0x202 ISZERO
0x203 GT
0x204 PUSH2 0x227
0x207 JUMPI
---
0x1fa: JUMPDEST 
0x1fc: V126 = S[0x3]
0x1ff: S[0x3] = V57
0x202: V127 = ISZERO V126
0x203: V128 = GT V127 V57
0x204: V129 = 0x227
0x207: JUMPI 0x227 V128
---
Entry stack: [V11, 0x78, V19, V22, 0x0, 0x3, V55, V57, 0x10c, 0x3, V57]
Stack pops: 2
Stack additions: [S1, S0, V126]
Exit stack: [V11, 0x78, V19, V22, 0x0, 0x3, V55, V57, 0x10c, 0x3, V57, V126]

================================

Block 0x208
[0x208:0x225]
---
Predecessors: [0x1fa]
Successors: [0x22c]
---
0x208 PUSH1 0x3
0x20a MUL
0x20b DUP2
0x20c PUSH1 0x3
0x20e MUL
0x20f DUP4
0x210 PUSH1 0x0
0x212 MSTORE
0x213 PUSH1 0x20
0x215 PUSH1 0x0
0x217 SHA3
0x218 SWAP2
0x219 DUP3
0x21a ADD
0x21b SWAP2
0x21c ADD
0x21d PUSH2 0x226
0x220 SWAP2
0x221 SWAP1
0x222 PUSH2 0x22c
0x225 JUMP
---
0x208: V130 = 0x3
0x20a: V131 = MUL 0x3 V126
0x20c: V132 = 0x3
0x20e: V133 = MUL 0x3 V57
0x210: V134 = 0x0
0x212: M[0x0] = 0x3
0x213: V135 = 0x20
0x215: V136 = 0x0
0x217: V137 = SHA3 0x0 0x20
0x21a: V138 = ADD V137 V131
0x21c: V139 = ADD V137 V133
0x21d: V140 = 0x226
0x222: V141 = 0x22c
0x225: JUMP 0x22c
---
Entry stack: [V11, 0x78, V19, V22, 0x0, 0x3, V55, V57, 0x10c, 0x3, V57, V126]
Stack pops: 3
Stack additions: [S2, S1, 0x226, V138, V139]
Exit stack: [V11, 0x78, V19, V22, 0x0, 0x3, V55, V57, 0x10c, 0x3, V57, 0x226, V138, V139]

================================

Block 0x226
[0x226:0x226]
---
Predecessors: [0x260]
Successors: [0x227]
---
0x226 JUMPDEST
---
0x226: JUMPDEST 
---
Entry stack: [V11, 0x78, V19, V22, 0x0, 0x3, V55, V57, 0x10c, 0x3, V57, V138]
Stack pops: 0
Stack additions: []
Exit stack: [V11, 0x78, V19, V22, 0x0, 0x3, V55, V57, 0x10c, 0x3, V57, V138]

================================

Block 0x227
[0x227:0x22b]
---
Predecessors: [0x1fa, 0x226]
Successors: [0x10c]
---
0x227 JUMPDEST
0x228 POP
0x229 POP
0x22a POP
0x22b JUMP
---
0x227: JUMPDEST 
0x22b: JUMP 0x10c
---
Entry stack: [V11, 0x78, V19, V22, 0x0, 0x3, V55, V57, 0x10c, 0x3, V57, S0]
Stack pops: 4
Stack additions: []
Exit stack: [V11, 0x78, V19, V22, 0x0, 0x3, V55, V57]

================================

Block 0x22c
[0x22c:0x231]
---
Predecessors: [0x208]
Successors: [0x232]
---
0x22c JUMPDEST
0x22d PUSH2 0x260
0x230 SWAP2
0x231 SWAP1
---
0x22c: JUMPDEST 
0x22d: V142 = 0x260
---
Entry stack: [V11, 0x78, V19, V22, 0x0, 0x3, V55, V57, 0x10c, 0x3, V57, 0x226, V138, V139]
Stack pops: 2
Stack additions: [0x260, S1, S0]
Exit stack: [V11, 0x78, V19, V22, 0x0, 0x3, V55, V57, 0x10c, 0x3, V57, 0x226, 0x260, V138, V139]

================================

Block 0x232
[0x232:0x23a]
---
Predecessors: [0x22c, 0x23b]
Successors: [0x23b, 0x25c]
---
0x232 JUMPDEST
0x233 DUP1
0x234 DUP3
0x235 GT
0x236 ISZERO
0x237 PUSH2 0x25c
0x23a JUMPI
---
0x232: JUMPDEST 
0x235: V143 = GT V138 S0
0x236: V144 = ISZERO V143
0x237: V145 = 0x25c
0x23a: JUMPI 0x25c V144
---
Entry stack: [V11, 0x78, V19, V22, 0x0, 0x3, V55, V57, 0x10c, 0x3, V57, 0x226, 0x260, V138, S0]
Stack pops: 2
Stack additions: [S1, S0]
Exit stack: [V11, 0x78, V19, V22, 0x0, 0x3, V55, V57, 0x10c, 0x3, V57, 0x226, 0x260, V138, S0]

================================

Block 0x23b
[0x23b:0x25b]
---
Predecessors: [0x232]
Successors: [0x232]
---
0x23b PUSH1 0x0
0x23d DUP1
0x23e DUP3
0x23f ADD
0x240 PUSH1 0x0
0x242 SWAP1
0x243 SSTORE
0x244 PUSH1 0x1
0x246 DUP3
0x247 ADD
0x248 PUSH1 0x0
0x24a SWAP1
0x24b SSTORE
0x24c PUSH1 0x2
0x24e DUP3
0x24f ADD
0x250 PUSH1 0x0
0x252 SWAP1
0x253 SSTORE
0x254 POP
0x255 PUSH1 0x3
0x257 ADD
0x258 PUSH2 0x232
0x25b JUMP
---
0x23b: V146 = 0x0
0x23f: V147 = ADD S0 0x0
0x240: V148 = 0x0
0x243: S[V147] = 0x0
0x244: V149 = 0x1
0x247: V150 = ADD S0 0x1
0x248: V151 = 0x0
0x24b: S[V150] = 0x0
0x24c: V152 = 0x2
0x24f: V153 = ADD S0 0x2
0x250: V154 = 0x0
0x253: S[V153] = 0x0
0x255: V155 = 0x3
0x257: V156 = ADD 0x3 S0
0x258: V157 = 0x232
0x25b: JUMP 0x232
---
Entry stack: [V11, 0x78, V19, V22, 0x0, 0x3, V55, V57, 0x10c, 0x3, V57, 0x226, 0x260, V138, S0]
Stack pops: 1
Stack additions: [V156]
Exit stack: [V11, 0x78, V19, V22, 0x0, 0x3, V55, V57, 0x10c, 0x3, V57, 0x226, 0x260, V138, V156]

================================

Block 0x25c
[0x25c:0x25f]
---
Predecessors: [0x232]
Successors: [0x260]
---
0x25c JUMPDEST
0x25d POP
0x25e SWAP1
0x25f JUMP
---
0x25c: JUMPDEST 
0x25f: JUMP 0x260
---
Entry stack: [V11, 0x78, V19, V22, 0x0, 0x3, V55, V57, 0x10c, 0x3, V57, 0x226, 0x260, V138, S0]
Stack pops: 3
Stack additions: [S1]
Exit stack: [V11, 0x78, V19, V22, 0x0, 0x3, V55, V57, 0x10c, 0x3, V57, 0x226, V138]

================================

Block 0x260
[0x260:0x262]
---
Predecessors: [0x25c]
Successors: [0x226]
---
0x260 JUMPDEST
0x261 SWAP1
0x262 JUMP
---
0x260: JUMPDEST 
0x262: JUMP 0x226
---
Entry stack: [V11, 0x78, V19, V22, 0x0, 0x3, V55, V57, 0x10c, 0x3, V57, 0x226, V138]
Stack pops: 2
Stack additions: [S0]
Exit stack: [V11, 0x78, V19, V22, 0x0, 0x3, V55, V57, 0x10c, 0x3, V57, V138]

================================

Block 0x263
[0x263:0x28e]
---
Predecessors: []
Successors: []
---
0x263 STOP
0x264 LOG1
0x265 PUSH6 0x627a7a723058
0x26c SHA3
0x26d MISSING 0xab
0x26e PUSH26 0x61881ee487281b633644dbb7206848a35f6dae5e18aaaf2d2060
0x289 PUSH4 0x8c546b00
0x28e MISSING 0x29
---
0x263: STOP 
0x264: LOG S0 S1 S2
0x265: V158 = 0x627a7a723058
0x26c: V159 = SHA3 0x627a7a723058 S3
0x26d: MISSING 0xab
0x26e: V160 = 0x61881ee487281b633644dbb7206848a35f6dae5e18aaaf2d2060
0x289: V161 = 0x8c546b00
0x28e: MISSING 0x29
---
Entry stack: []
Stack pops: 0
Stack additions: [V159, 0x8c546b00, 0x61881ee487281b633644dbb7206848a35f6dae5e18aaaf2d2060]
Exit stack: []

================================

Function 0:
Public function signature: 0x29f0a422
Entry block: 0x43
Exit block: 0xc2
Body: 0x43, 0x78, 0x7a, 0x8d, 0xc2, 0xc6, 0x10c, 0x1f5, 0x1fa, 0x208, 0x226, 0x227, 0x22c, 0x232, 0x23b, 0x25c, 0x260

Function 1:
Public fallback function
Entry block: 0x41
Exit block: 0x41
Body: 0x41

