Block 0x0
[0x0:0xc]
---
Predecessors: []
Successors: [0xd, 0x57]
---
0x0 PUSH1 0x60
0x2 PUSH1 0x40
0x4 MSTORE
0x5 PUSH1 0x4
0x7 CALLDATASIZE
0x8 LT
0x9 PUSH2 0x57
0xc JUMPI
---
0x0: V0 = 0x60
0x2: V1 = 0x40
0x4: M[0x40] = 0x60
0x5: V2 = 0x4
0x7: V3 = CALLDATASIZE
0x8: V4 = LT V3 0x4
0x9: V5 = 0x57
0xc: JUMPI 0x57 V4
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
Successors: [0x41, 0x59]
---
0xd PUSH1 0x0
0xf CALLDATALOAD
0x10 PUSH29 0x100000000000000000000000000000000000000000000000000000000
0x2e SWAP1
0x2f DIV
0x30 PUSH4 0xffffffff
0x35 AND
0x36 DUP1
0x37 PUSH4 0x1ac9f70d
0x3c EQ
0x3d PUSH2 0x59
0x40 JUMPI
---
0xd: V6 = 0x0
0xf: V7 = CALLDATALOAD 0x0
0x10: V8 = 0x100000000000000000000000000000000000000000000000000000000
0x2f: V9 = DIV V7 0x100000000000000000000000000000000000000000000000000000000
0x30: V10 = 0xffffffff
0x35: V11 = AND 0xffffffff V9
0x37: V12 = 0x1ac9f70d
0x3c: V13 = EQ 0x1ac9f70d V11
0x3d: V14 = 0x59
0x40: JUMPI 0x59 V13
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
Successors: [0x4c, 0x87]
---
0x41 DUP1
0x42 PUSH4 0x3ccfd60b
0x47 EQ
0x48 PUSH2 0x87
0x4b JUMPI
---
0x42: V15 = 0x3ccfd60b
0x47: V16 = EQ 0x3ccfd60b V11
0x48: V17 = 0x87
0x4b: JUMPI 0x87 V16
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
Successors: [0x57, 0x91]
---
0x4c DUP1
0x4d PUSH4 0xb4a99a4e
0x52 EQ
0x53 PUSH2 0x91
0x56 JUMPI
---
0x4d: V18 = 0xb4a99a4e
0x52: V19 = EQ 0xb4a99a4e V11
0x53: V20 = 0x91
0x56: JUMPI 0x91 V19
---
Entry stack: [V11]
Stack pops: 1
Stack additions: [S0]
Exit stack: [V11]

================================

Block 0x57
[0x57:0x58]
---
Predecessors: [0x0, 0x4c]
Successors: []
---
0x57 JUMPDEST
0x58 STOP
---
0x57: JUMPDEST 
0x58: STOP 
---
Entry stack: [V11]
Stack pops: 0
Stack additions: []
Exit stack: [V11]

================================

Block 0x59
[0x59:0x84]
---
Predecessors: [0xd]
Successors: [0xe6]
---
0x59 JUMPDEST
0x5a PUSH2 0x85
0x5d PUSH1 0x4
0x5f DUP1
0x60 DUP1
0x61 CALLDATALOAD
0x62 PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x77 AND
0x78 SWAP1
0x79 PUSH1 0x20
0x7b ADD
0x7c SWAP1
0x7d SWAP2
0x7e SWAP1
0x7f POP
0x80 POP
0x81 PUSH2 0xe6
0x84 JUMP
---
0x59: JUMPDEST 
0x5a: V21 = 0x85
0x5d: V22 = 0x4
0x61: V23 = CALLDATALOAD 0x4
0x62: V24 = 0xffffffffffffffffffffffffffffffffffffffff
0x77: V25 = AND 0xffffffffffffffffffffffffffffffffffffffff V23
0x79: V26 = 0x20
0x7b: V27 = ADD 0x20 0x4
0x81: V28 = 0xe6
0x84: JUMP 0xe6
---
Entry stack: [V11]
Stack pops: 0
Stack additions: [0x85, V25]
Exit stack: [V11, 0x85, V25]

================================

Block 0x85
[0x85:0x86]
---
Predecessors: [0x160]
Successors: []
---
0x85 JUMPDEST
0x86 STOP
---
0x85: JUMPDEST 
0x86: STOP 
---
Entry stack: [V11]
Stack pops: 0
Stack additions: []
Exit stack: [V11]

================================

Block 0x87
[0x87:0x8e]
---
Predecessors: [0x41]
Successors: [0x163]
---
0x87 JUMPDEST
0x88 PUSH2 0x8f
0x8b PUSH2 0x163
0x8e JUMP
---
0x87: JUMPDEST 
0x88: V29 = 0x8f
0x8b: V30 = 0x163
0x8e: JUMP 0x163
---
Entry stack: [V11]
Stack pops: 0
Stack additions: [0x8f]
Exit stack: [V11, 0x8f]

================================

Block 0x8f
[0x8f:0x90]
---
Predecessors: [0x236]
Successors: []
---
0x8f JUMPDEST
0x90 STOP
---
0x8f: JUMPDEST 
0x90: STOP 
---
Entry stack: [V11]
Stack pops: 0
Stack additions: []
Exit stack: [V11]

================================

Block 0x91
[0x91:0x97]
---
Predecessors: [0x4c]
Successors: [0x98, 0x9c]
---
0x91 JUMPDEST
0x92 CALLVALUE
0x93 ISZERO
0x94 PUSH2 0x9c
0x97 JUMPI
---
0x91: JUMPDEST 
0x92: V31 = CALLVALUE
0x93: V32 = ISZERO V31
0x94: V33 = 0x9c
0x97: JUMPI 0x9c V32
---
Entry stack: [V11]
Stack pops: 0
Stack additions: []
Exit stack: [V11]

================================

Block 0x98
[0x98:0x9b]
---
Predecessors: [0x91]
Successors: []
---
0x98 PUSH1 0x0
0x9a DUP1
0x9b REVERT
---
0x98: V34 = 0x0
0x9b: REVERT 0x0 0x0
---
Entry stack: [V11]
Stack pops: 0
Stack additions: []
Exit stack: [V11]

================================

Block 0x9c
[0x9c:0xa3]
---
Predecessors: [0x91]
Successors: [0x238]
---
0x9c JUMPDEST
0x9d PUSH2 0xa4
0xa0 PUSH2 0x238
0xa3 JUMP
---
0x9c: JUMPDEST 
0x9d: V35 = 0xa4
0xa0: V36 = 0x238
0xa3: JUMP 0x238
---
Entry stack: [V11]
Stack pops: 0
Stack additions: [0xa4]
Exit stack: [V11, 0xa4]

================================

Block 0xa4
[0xa4:0xe5]
---
Predecessors: [0x238]
Successors: []
---
0xa4 JUMPDEST
0xa5 PUSH1 0x40
0xa7 MLOAD
0xa8 DUP1
0xa9 DUP3
0xaa PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0xbf AND
0xc0 PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0xd5 AND
0xd6 DUP2
0xd7 MSTORE
0xd8 PUSH1 0x20
0xda ADD
0xdb SWAP2
0xdc POP
0xdd POP
0xde PUSH1 0x40
0xe0 MLOAD
0xe1 DUP1
0xe2 SWAP2
0xe3 SUB
0xe4 SWAP1
0xe5 RETURN
---
0xa4: JUMPDEST 
0xa5: V37 = 0x40
0xa7: V38 = M[0x40]
0xaa: V39 = 0xffffffffffffffffffffffffffffffffffffffff
0xbf: V40 = AND 0xffffffffffffffffffffffffffffffffffffffff V129
0xc0: V41 = 0xffffffffffffffffffffffffffffffffffffffff
0xd5: V42 = AND 0xffffffffffffffffffffffffffffffffffffffff V40
0xd7: M[V38] = V42
0xd8: V43 = 0x20
0xda: V44 = ADD 0x20 V38
0xde: V45 = 0x40
0xe0: V46 = M[0x40]
0xe3: V47 = SUB V44 V46
0xe5: RETURN V46 V47
---
Entry stack: [V11, 0xa4, V129]
Stack pops: 1
Stack additions: []
Exit stack: [V11, 0xa4]

================================

Block 0xe6
[0xe6:0x106]
---
Predecessors: [0x59]
Successors: [0x107, 0x160]
---
0xe6 JUMPDEST
0xe7 ADDRESS
0xe8 PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0xfd AND
0xfe BALANCE
0xff CALLVALUE
0x100 LT
0x101 ISZERO
0x102 ISZERO
0x103 PUSH2 0x160
0x106 JUMPI
---
0xe6: JUMPDEST 
0xe7: V48 = ADDRESS
0xe8: V49 = 0xffffffffffffffffffffffffffffffffffffffff
0xfd: V50 = AND 0xffffffffffffffffffffffffffffffffffffffff V48
0xfe: V51 = BALANCE V50
0xff: V52 = CALLVALUE
0x100: V53 = LT V52 V51
0x101: V54 = ISZERO V53
0x102: V55 = ISZERO V54
0x103: V56 = 0x160
0x106: JUMPI 0x160 V55
---
Entry stack: [V11, 0x85, V25]
Stack pops: 0
Stack additions: []
Exit stack: [V11, 0x85, V25]

================================

Block 0x107
[0x107:0x15a]
---
Predecessors: [0xe6]
Successors: [0x15b, 0x15f]
---
0x107 DUP1
0x108 PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x11d AND
0x11e PUSH2 0x8fc
0x121 CALLVALUE
0x122 ADDRESS
0x123 PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x138 AND
0x139 BALANCE
0x13a ADD
0x13b SWAP1
0x13c DUP2
0x13d ISZERO
0x13e MUL
0x13f SWAP1
0x140 PUSH1 0x40
0x142 MLOAD
0x143 PUSH1 0x0
0x145 PUSH1 0x40
0x147 MLOAD
0x148 DUP1
0x149 DUP4
0x14a SUB
0x14b DUP2
0x14c DUP6
0x14d DUP9
0x14e DUP9
0x14f CALL
0x150 SWAP4
0x151 POP
0x152 POP
0x153 POP
0x154 POP
0x155 ISZERO
0x156 ISZERO
0x157 PUSH2 0x15f
0x15a JUMPI
---
0x108: V57 = 0xffffffffffffffffffffffffffffffffffffffff
0x11d: V58 = AND 0xffffffffffffffffffffffffffffffffffffffff V25
0x11e: V59 = 0x8fc
0x121: V60 = CALLVALUE
0x122: V61 = ADDRESS
0x123: V62 = 0xffffffffffffffffffffffffffffffffffffffff
0x138: V63 = AND 0xffffffffffffffffffffffffffffffffffffffff V61
0x139: V64 = BALANCE V63
0x13a: V65 = ADD V64 V60
0x13d: V66 = ISZERO V65
0x13e: V67 = MUL V66 0x8fc
0x140: V68 = 0x40
0x142: V69 = M[0x40]
0x143: V70 = 0x0
0x145: V71 = 0x40
0x147: V72 = M[0x40]
0x14a: V73 = SUB V69 V72
0x14f: V74 = CALL V67 V58 V65 V72 V73 V72 0x0
0x155: V75 = ISZERO V74
0x156: V76 = ISZERO V75
0x157: V77 = 0x15f
0x15a: JUMPI 0x15f V76
---
Entry stack: [V11, 0x85, V25]
Stack pops: 1
Stack additions: [S0]
Exit stack: [V11, 0x85, V25]

================================

Block 0x15b
[0x15b:0x15e]
---
Predecessors: [0x107]
Successors: []
---
0x15b PUSH1 0x0
0x15d DUP1
0x15e REVERT
---
0x15b: V78 = 0x0
0x15e: REVERT 0x0 0x0
---
Entry stack: [V11, 0x85, V25]
Stack pops: 0
Stack additions: []
Exit stack: [V11, 0x85, V25]

================================

Block 0x15f
[0x15f:0x15f]
---
Predecessors: [0x107]
Successors: [0x160]
---
0x15f JUMPDEST
---
0x15f: JUMPDEST 
---
Entry stack: [V11, 0x85, V25]
Stack pops: 0
Stack additions: []
Exit stack: [V11, 0x85, V25]

================================

Block 0x160
[0x160:0x162]
---
Predecessors: [0xe6, 0x15f]
Successors: [0x85]
---
0x160 JUMPDEST
0x161 POP
0x162 JUMP
---
0x160: JUMPDEST 
0x162: JUMP 0x85
---
Entry stack: [V11, 0x85, V25]
Stack pops: 2
Stack additions: []
Exit stack: [V11]

================================

Block 0x163
[0x163:0x1b9]
---
Predecessors: [0x87]
Successors: [0x1ba, 0x1be]
---
0x163 JUMPDEST
0x164 PUSH1 0x0
0x166 DUP1
0x167 SWAP1
0x168 SLOAD
0x169 SWAP1
0x16a PUSH2 0x100
0x16d EXP
0x16e SWAP1
0x16f DIV
0x170 PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x185 AND
0x186 PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x19b AND
0x19c CALLER
0x19d PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x1b2 AND
0x1b3 EQ
0x1b4 ISZERO
0x1b5 ISZERO
0x1b6 PUSH2 0x1be
0x1b9 JUMPI
---
0x163: JUMPDEST 
0x164: V79 = 0x0
0x168: V80 = S[0x0]
0x16a: V81 = 0x100
0x16d: V82 = EXP 0x100 0x0
0x16f: V83 = DIV V80 0x1
0x170: V84 = 0xffffffffffffffffffffffffffffffffffffffff
0x185: V85 = AND 0xffffffffffffffffffffffffffffffffffffffff V83
0x186: V86 = 0xffffffffffffffffffffffffffffffffffffffff
0x19b: V87 = AND 0xffffffffffffffffffffffffffffffffffffffff V85
0x19c: V88 = CALLER
0x19d: V89 = 0xffffffffffffffffffffffffffffffffffffffff
0x1b2: V90 = AND 0xffffffffffffffffffffffffffffffffffffffff V88
0x1b3: V91 = EQ V90 V87
0x1b4: V92 = ISZERO V91
0x1b5: V93 = ISZERO V92
0x1b6: V94 = 0x1be
0x1b9: JUMPI 0x1be V93
---
Entry stack: [V11, 0x8f]
Stack pops: 0
Stack additions: []
Exit stack: [V11, 0x8f]

================================

Block 0x1ba
[0x1ba:0x1bd]
---
Predecessors: [0x163]
Successors: []
---
0x1ba PUSH1 0x0
0x1bc DUP1
0x1bd REVERT
---
0x1ba: V95 = 0x0
0x1bd: REVERT 0x0 0x0
---
Entry stack: [V11, 0x8f]
Stack pops: 0
Stack additions: []
Exit stack: [V11, 0x8f]

================================

Block 0x1be
[0x1be:0x231]
---
Predecessors: [0x163]
Successors: [0x232, 0x236]
---
0x1be JUMPDEST
0x1bf PUSH1 0x0
0x1c1 DUP1
0x1c2 SWAP1
0x1c3 SLOAD
0x1c4 SWAP1
0x1c5 PUSH2 0x100
0x1c8 EXP
0x1c9 SWAP1
0x1ca DIV
0x1cb PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x1e0 AND
0x1e1 PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x1f6 AND
0x1f7 PUSH2 0x8fc
0x1fa ADDRESS
0x1fb PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x210 AND
0x211 BALANCE
0x212 SWAP1
0x213 DUP2
0x214 ISZERO
0x215 MUL
0x216 SWAP1
0x217 PUSH1 0x40
0x219 MLOAD
0x21a PUSH1 0x0
0x21c PUSH1 0x40
0x21e MLOAD
0x21f DUP1
0x220 DUP4
0x221 SUB
0x222 DUP2
0x223 DUP6
0x224 DUP9
0x225 DUP9
0x226 CALL
0x227 SWAP4
0x228 POP
0x229 POP
0x22a POP
0x22b POP
0x22c ISZERO
0x22d ISZERO
0x22e PUSH2 0x236
0x231 JUMPI
---
0x1be: JUMPDEST 
0x1bf: V96 = 0x0
0x1c3: V97 = S[0x0]
0x1c5: V98 = 0x100
0x1c8: V99 = EXP 0x100 0x0
0x1ca: V100 = DIV V97 0x1
0x1cb: V101 = 0xffffffffffffffffffffffffffffffffffffffff
0x1e0: V102 = AND 0xffffffffffffffffffffffffffffffffffffffff V100
0x1e1: V103 = 0xffffffffffffffffffffffffffffffffffffffff
0x1f6: V104 = AND 0xffffffffffffffffffffffffffffffffffffffff V102
0x1f7: V105 = 0x8fc
0x1fa: V106 = ADDRESS
0x1fb: V107 = 0xffffffffffffffffffffffffffffffffffffffff
0x210: V108 = AND 0xffffffffffffffffffffffffffffffffffffffff V106
0x211: V109 = BALANCE V108
0x214: V110 = ISZERO V109
0x215: V111 = MUL V110 0x8fc
0x217: V112 = 0x40
0x219: V113 = M[0x40]
0x21a: V114 = 0x0
0x21c: V115 = 0x40
0x21e: V116 = M[0x40]
0x221: V117 = SUB V113 V116
0x226: V118 = CALL V111 V104 V109 V116 V117 V116 0x0
0x22c: V119 = ISZERO V118
0x22d: V120 = ISZERO V119
0x22e: V121 = 0x236
0x231: JUMPI 0x236 V120
---
Entry stack: [V11, 0x8f]
Stack pops: 0
Stack additions: []
Exit stack: [V11, 0x8f]

================================

Block 0x232
[0x232:0x235]
---
Predecessors: [0x1be]
Successors: []
---
0x232 PUSH1 0x0
0x234 DUP1
0x235 REVERT
---
0x232: V122 = 0x0
0x235: REVERT 0x0 0x0
---
Entry stack: [V11, 0x8f]
Stack pops: 0
Stack additions: []
Exit stack: [V11, 0x8f]

================================

Block 0x236
[0x236:0x237]
---
Predecessors: [0x1be]
Successors: [0x8f]
---
0x236 JUMPDEST
0x237 JUMP
---
0x236: JUMPDEST 
0x237: JUMP 0x8f
---
Entry stack: [V11, 0x8f]
Stack pops: 1
Stack additions: []
Exit stack: [V11]

================================

Block 0x238
[0x238:0x25c]
---
Predecessors: [0x9c]
Successors: [0xa4]
---
0x238 JUMPDEST
0x239 PUSH1 0x0
0x23b DUP1
0x23c SWAP1
0x23d SLOAD
0x23e SWAP1
0x23f PUSH2 0x100
0x242 EXP
0x243 SWAP1
0x244 DIV
0x245 PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x25a AND
0x25b DUP2
0x25c JUMP
---
0x238: JUMPDEST 
0x239: V123 = 0x0
0x23d: V124 = S[0x0]
0x23f: V125 = 0x100
0x242: V126 = EXP 0x100 0x0
0x244: V127 = DIV V124 0x1
0x245: V128 = 0xffffffffffffffffffffffffffffffffffffffff
0x25a: V129 = AND 0xffffffffffffffffffffffffffffffffffffffff V127
0x25c: JUMP 0xa4
---
Entry stack: [V11, 0xa4]
Stack pops: 1
Stack additions: [S0, V129]
Exit stack: [V11, 0xa4, V129]

================================

Block 0x25d
[0x25d:0x288]
---
Predecessors: []
Successors: []
---
0x25d STOP
0x25e LOG1
0x25f PUSH6 0x627a7a723058
0x266 SHA3
0x267 MISSING 0xa9
0x268 INVALID
0x269 MISSING 0xb2
0x26a MISSING 0xfc
0x26b MISSING 0xaa
0x26c AND
0x26d SUB
0x26e MISSING 0x24
0x26f PUSH9 0x96c98d0658fceebd51
0x279 ADD
0x27a EXTCODESIZE
0x27b MISSING 0x25
0x27c MISSING 0xd0
0x27d MISSING 0xe
0x27e MISSING 0x4c
0x27f MISSING 0x27
0x280 MISSING 0xc4
0x281 DUP12
0x282 TIMESTAMP
0x283 SWAP4
0x284 MISSING 0xf8
0x285 LT
0x286 MISSING 0xe3
0x287 STOP
0x288 MISSING 0x29
---
0x25d: STOP 
0x25e: LOG S0 S1 S2
0x25f: V130 = 0x627a7a723058
0x266: V131 = SHA3 0x627a7a723058 S3
0x267: MISSING 0xa9
0x268: INVALID 
0x269: MISSING 0xb2
0x26a: MISSING 0xfc
0x26b: MISSING 0xaa
0x26c: V132 = AND S0 S1
0x26d: V133 = SUB V132 S2
0x26e: MISSING 0x24
0x26f: V134 = 0x96c98d0658fceebd51
0x279: V135 = ADD 0x96c98d0658fceebd51 S0
0x27a: V136 = EXTCODESIZE V135
0x27b: MISSING 0x25
0x27c: MISSING 0xd0
0x27d: MISSING 0xe
0x27e: MISSING 0x4c
0x27f: MISSING 0x27
0x280: MISSING 0xc4
0x282: V137 = TIMESTAMP
0x284: MISSING 0xf8
0x285: V138 = LT S0 S1
0x286: MISSING 0xe3
0x287: STOP 
0x288: MISSING 0x29
---
Entry stack: []
Stack pops: 0
Stack additions: [V131, V133, V136, S2, S11, S0, S1, V137, S3, S4, S5, S6, S7, S8, S9, S10, S11, V138]
Exit stack: []

================================

Function 0:
Public function signature: 0x1ac9f70d
Entry block: 0x59
Exit block: 0x85
Body: 0x59, 0x85, 0xe6, 0x107, 0x15b, 0x15f, 0x160

Function 1:
Public function signature: 0x3ccfd60b
Entry block: 0x87
Exit block: 0x8f
Body: 0x87, 0x8f, 0x163, 0x1ba, 0x1be, 0x232, 0x236

Function 2:
Public function signature: 0xb4a99a4e
Entry block: 0x91
Exit block: 0xa4
Body: 0x91, 0x98, 0x9c, 0xa4, 0x238

Function 3:
Public fallback function
Entry block: 0x57
Exit block: 0x57
Body: 0x57

