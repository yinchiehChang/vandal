Block 0x0
[0x0:0xc]
---
Predecessors: []
Successors: [0xd, 0x62]
---
0x0 PUSH1 0x60
0x2 PUSH1 0x40
0x4 MSTORE
0x5 PUSH1 0x4
0x7 CALLDATASIZE
0x8 LT
0x9 PUSH2 0x62
0xc JUMPI
---
0x0: V0 = 0x60
0x2: V1 = 0x40
0x4: M[0x40] = 0x60
0x5: V2 = 0x4
0x7: V3 = CALLDATASIZE
0x8: V4 = LT V3 0x4
0x9: V5 = 0x62
0xc: JUMPI 0x62 V4
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
Successors: [0x41, 0x67]
---
0xd PUSH1 0x0
0xf CALLDATALOAD
0x10 PUSH29 0x100000000000000000000000000000000000000000000000000000000
0x2e SWAP1
0x2f DIV
0x30 PUSH4 0xffffffff
0x35 AND
0x36 DUP1
0x37 PUSH4 0x18c0e04f
0x3c EQ
0x3d PUSH2 0x67
0x40 JUMPI
---
0xd: V6 = 0x0
0xf: V7 = CALLDATALOAD 0x0
0x10: V8 = 0x100000000000000000000000000000000000000000000000000000000
0x2f: V9 = DIV V7 0x100000000000000000000000000000000000000000000000000000000
0x30: V10 = 0xffffffff
0x35: V11 = AND 0xffffffff V9
0x37: V12 = 0x18c0e04f
0x3c: V13 = EQ 0x18c0e04f V11
0x3d: V14 = 0x67
0x40: JUMPI 0x67 V13
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
Successors: [0x4c, 0x71]
---
0x41 DUP1
0x42 PUSH4 0x3ccfd60b
0x47 EQ
0x48 PUSH2 0x71
0x4b JUMPI
---
0x42: V15 = 0x3ccfd60b
0x47: V16 = EQ 0x3ccfd60b V11
0x48: V17 = 0x71
0x4b: JUMPI 0x71 V16
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
Successors: [0x57, 0x86]
---
0x4c DUP1
0x4d PUSH4 0x4c8cab79
0x52 EQ
0x53 PUSH2 0x86
0x56 JUMPI
---
0x4d: V18 = 0x4c8cab79
0x52: V19 = EQ 0x4c8cab79 V11
0x53: V20 = 0x86
0x56: JUMPI 0x86 V19
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
Successors: [0x62, 0xaf]
---
0x57 DUP1
0x58 PUSH4 0x8da5cb5b
0x5d EQ
0x5e PUSH2 0xaf
0x61 JUMPI
---
0x58: V21 = 0x8da5cb5b
0x5d: V22 = EQ 0x8da5cb5b V11
0x5e: V23 = 0xaf
0x61: JUMPI 0xaf V22
---
Entry stack: [V11]
Stack pops: 1
Stack additions: [S0]
Exit stack: [V11]

================================

Block 0x62
[0x62:0x66]
---
Predecessors: [0x0, 0x57]
Successors: []
---
0x62 JUMPDEST
0x63 PUSH1 0x0
0x65 DUP1
0x66 REVERT
---
0x62: JUMPDEST 
0x63: V24 = 0x0
0x66: REVERT 0x0 0x0
---
Entry stack: [V11]
Stack pops: 0
Stack additions: []
Exit stack: [V11]

================================

Block 0x67
[0x67:0x6e]
---
Predecessors: [0xd]
Successors: [0x104]
---
0x67 JUMPDEST
0x68 PUSH2 0x6f
0x6b PUSH2 0x104
0x6e JUMP
---
0x67: JUMPDEST 
0x68: V25 = 0x6f
0x6b: V26 = 0x104
0x6e: JUMP 0x104
---
Entry stack: [V11]
Stack pops: 0
Stack additions: [0x6f]
Exit stack: [V11, 0x6f]

================================

Block 0x6f
[0x6f:0x70]
---
Predecessors: [0x157]
Successors: []
---
0x6f JUMPDEST
0x70 STOP
---
0x6f: JUMPDEST 
0x70: STOP 
---
Entry stack: [V11]
Stack pops: 0
Stack additions: []
Exit stack: [V11]

================================

Block 0x71
[0x71:0x77]
---
Predecessors: [0x41]
Successors: [0x78, 0x7c]
---
0x71 JUMPDEST
0x72 CALLVALUE
0x73 ISZERO
0x74 PUSH2 0x7c
0x77 JUMPI
---
0x71: JUMPDEST 
0x72: V27 = CALLVALUE
0x73: V28 = ISZERO V27
0x74: V29 = 0x7c
0x77: JUMPI 0x7c V28
---
Entry stack: [V11]
Stack pops: 0
Stack additions: []
Exit stack: [V11]

================================

Block 0x78
[0x78:0x7b]
---
Predecessors: [0x71]
Successors: []
---
0x78 PUSH1 0x0
0x7a DUP1
0x7b REVERT
---
0x78: V30 = 0x0
0x7b: REVERT 0x0 0x0
---
Entry stack: [V11]
Stack pops: 0
Stack additions: []
Exit stack: [V11]

================================

Block 0x7c
[0x7c:0x83]
---
Predecessors: [0x71]
Successors: [0x159]
---
0x7c JUMPDEST
0x7d PUSH2 0x84
0x80 PUSH2 0x159
0x83 JUMP
---
0x7c: JUMPDEST 
0x7d: V31 = 0x84
0x80: V32 = 0x159
0x83: JUMP 0x159
---
Entry stack: [V11]
Stack pops: 0
Stack additions: [0x84]
Exit stack: [V11, 0x84]

================================

Block 0x84
[0x84:0x85]
---
Predecessors: [0x20b]
Successors: []
---
0x84 JUMPDEST
0x85 STOP
---
0x84: JUMPDEST 
0x85: STOP 
---
Entry stack: [V11]
Stack pops: 0
Stack additions: []
Exit stack: [V11]

================================

Block 0x86
[0x86:0x8c]
---
Predecessors: [0x4c]
Successors: [0x8d, 0x91]
---
0x86 JUMPDEST
0x87 CALLVALUE
0x88 ISZERO
0x89 PUSH2 0x91
0x8c JUMPI
---
0x86: JUMPDEST 
0x87: V33 = CALLVALUE
0x88: V34 = ISZERO V33
0x89: V35 = 0x91
0x8c: JUMPI 0x91 V34
---
Entry stack: [V11]
Stack pops: 0
Stack additions: []
Exit stack: [V11]

================================

Block 0x8d
[0x8d:0x90]
---
Predecessors: [0x86]
Successors: []
---
0x8d PUSH1 0x0
0x8f DUP1
0x90 REVERT
---
0x8d: V36 = 0x0
0x90: REVERT 0x0 0x0
---
Entry stack: [V11]
Stack pops: 0
Stack additions: []
Exit stack: [V11]

================================

Block 0x91
[0x91:0x98]
---
Predecessors: [0x86]
Successors: [0x20d]
---
0x91 JUMPDEST
0x92 PUSH2 0x99
0x95 PUSH2 0x20d
0x98 JUMP
---
0x91: JUMPDEST 
0x92: V37 = 0x99
0x95: V38 = 0x20d
0x98: JUMP 0x20d
---
Entry stack: [V11]
Stack pops: 0
Stack additions: [0x99]
Exit stack: [V11, 0x99]

================================

Block 0x99
[0x99:0xae]
---
Predecessors: [0x20d]
Successors: []
---
0x99 JUMPDEST
0x9a PUSH1 0x40
0x9c MLOAD
0x9d DUP1
0x9e DUP3
0x9f DUP2
0xa0 MSTORE
0xa1 PUSH1 0x20
0xa3 ADD
0xa4 SWAP2
0xa5 POP
0xa6 POP
0xa7 PUSH1 0x40
0xa9 MLOAD
0xaa DUP1
0xab SWAP2
0xac SUB
0xad SWAP1
0xae RETURN
---
0x99: JUMPDEST 
0x9a: V39 = 0x40
0x9c: V40 = M[0x40]
0xa0: M[V40] = V124
0xa1: V41 = 0x20
0xa3: V42 = ADD 0x20 V40
0xa7: V43 = 0x40
0xa9: V44 = M[0x40]
0xac: V45 = SUB V42 V44
0xae: RETURN V44 V45
---
Entry stack: [V11, 0x99, V124]
Stack pops: 1
Stack additions: []
Exit stack: [V11, 0x99]

================================

Block 0xaf
[0xaf:0xb5]
---
Predecessors: [0x57]
Successors: [0xb6, 0xba]
---
0xaf JUMPDEST
0xb0 CALLVALUE
0xb1 ISZERO
0xb2 PUSH2 0xba
0xb5 JUMPI
---
0xaf: JUMPDEST 
0xb0: V46 = CALLVALUE
0xb1: V47 = ISZERO V46
0xb2: V48 = 0xba
0xb5: JUMPI 0xba V47
---
Entry stack: [V11]
Stack pops: 0
Stack additions: []
Exit stack: [V11]

================================

Block 0xb6
[0xb6:0xb9]
---
Predecessors: [0xaf]
Successors: []
---
0xb6 PUSH1 0x0
0xb8 DUP1
0xb9 REVERT
---
0xb6: V49 = 0x0
0xb9: REVERT 0x0 0x0
---
Entry stack: [V11]
Stack pops: 0
Stack additions: []
Exit stack: [V11]

================================

Block 0xba
[0xba:0xc1]
---
Predecessors: [0xaf]
Successors: [0x213]
---
0xba JUMPDEST
0xbb PUSH2 0xc2
0xbe PUSH2 0x213
0xc1 JUMP
---
0xba: JUMPDEST 
0xbb: V50 = 0xc2
0xbe: V51 = 0x213
0xc1: JUMP 0x213
---
Entry stack: [V11]
Stack pops: 0
Stack additions: [0xc2]
Exit stack: [V11, 0xc2]

================================

Block 0xc2
[0xc2:0x103]
---
Predecessors: [0x213]
Successors: []
---
0xc2 JUMPDEST
0xc3 PUSH1 0x40
0xc5 MLOAD
0xc6 DUP1
0xc7 DUP3
0xc8 PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0xdd AND
0xde PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0xf3 AND
0xf4 DUP2
0xf5 MSTORE
0xf6 PUSH1 0x20
0xf8 ADD
0xf9 SWAP2
0xfa POP
0xfb POP
0xfc PUSH1 0x40
0xfe MLOAD
0xff DUP1
0x100 SWAP2
0x101 SUB
0x102 SWAP1
0x103 RETURN
---
0xc2: JUMPDEST 
0xc3: V52 = 0x40
0xc5: V53 = M[0x40]
0xc8: V54 = 0xffffffffffffffffffffffffffffffffffffffff
0xdd: V55 = AND 0xffffffffffffffffffffffffffffffffffffffff V132
0xde: V56 = 0xffffffffffffffffffffffffffffffffffffffff
0xf3: V57 = AND 0xffffffffffffffffffffffffffffffffffffffff V55
0xf5: M[V53] = V57
0xf6: V58 = 0x20
0xf8: V59 = ADD 0x20 V53
0xfc: V60 = 0x40
0xfe: V61 = M[0x40]
0x101: V62 = SUB V59 V61
0x103: RETURN V61 V62
---
Entry stack: [V11, 0xc2, V132]
Stack pops: 1
Stack additions: []
Exit stack: [V11, 0xc2]

================================

Block 0x104
[0x104:0x10e]
---
Predecessors: [0x67]
Successors: [0x10f, 0x157]
---
0x104 JUMPDEST
0x105 PUSH1 0x2
0x107 SLOAD
0x108 CALLVALUE
0x109 GT
0x10a ISZERO
0x10b PUSH2 0x157
0x10e JUMPI
---
0x104: JUMPDEST 
0x105: V63 = 0x2
0x107: V64 = S[0x2]
0x108: V65 = CALLVALUE
0x109: V66 = GT V65 V64
0x10a: V67 = ISZERO V66
0x10b: V68 = 0x157
0x10e: JUMPI 0x157 V67
---
Entry stack: [V11, 0x6f]
Stack pops: 0
Stack additions: []
Exit stack: [V11, 0x6f]

================================

Block 0x10f
[0x10f:0x156]
---
Predecessors: [0x104]
Successors: [0x157]
---
0x10f CALLER
0x110 PUSH1 0x1
0x112 PUSH1 0x0
0x114 PUSH2 0x100
0x117 EXP
0x118 DUP2
0x119 SLOAD
0x11a DUP2
0x11b PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x130 MUL
0x131 NOT
0x132 AND
0x133 SWAP1
0x134 DUP4
0x135 PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x14a AND
0x14b MUL
0x14c OR
0x14d SWAP1
0x14e SSTORE
0x14f POP
0x150 CALLVALUE
0x151 PUSH1 0x2
0x153 DUP2
0x154 SWAP1
0x155 SSTORE
0x156 POP
---
0x10f: V69 = CALLER
0x110: V70 = 0x1
0x112: V71 = 0x0
0x114: V72 = 0x100
0x117: V73 = EXP 0x100 0x0
0x119: V74 = S[0x1]
0x11b: V75 = 0xffffffffffffffffffffffffffffffffffffffff
0x130: V76 = MUL 0xffffffffffffffffffffffffffffffffffffffff 0x1
0x131: V77 = NOT 0xffffffffffffffffffffffffffffffffffffffff
0x132: V78 = AND 0xffffffffffffffffffffffff0000000000000000000000000000000000000000 V74
0x135: V79 = 0xffffffffffffffffffffffffffffffffffffffff
0x14a: V80 = AND 0xffffffffffffffffffffffffffffffffffffffff V69
0x14b: V81 = MUL V80 0x1
0x14c: V82 = OR V81 V78
0x14e: S[0x1] = V82
0x150: V83 = CALLVALUE
0x151: V84 = 0x2
0x155: S[0x2] = V83
---
Entry stack: [V11, 0x6f]
Stack pops: 0
Stack additions: []
Exit stack: [V11, 0x6f]

================================

Block 0x157
[0x157:0x158]
---
Predecessors: [0x104, 0x10f]
Successors: [0x6f]
---
0x157 JUMPDEST
0x158 JUMP
---
0x157: JUMPDEST 
0x158: JUMP 0x6f
---
Entry stack: [V11, 0x6f]
Stack pops: 1
Stack additions: []
Exit stack: [V11]

================================

Block 0x159
[0x159:0x1af]
---
Predecessors: [0x7c]
Successors: [0x1b0, 0x1b4]
---
0x159 JUMPDEST
0x15a PUSH1 0x0
0x15c DUP1
0x15d SWAP1
0x15e SLOAD
0x15f SWAP1
0x160 PUSH2 0x100
0x163 EXP
0x164 SWAP1
0x165 DIV
0x166 PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x17b AND
0x17c PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x191 AND
0x192 CALLER
0x193 PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x1a8 AND
0x1a9 EQ
0x1aa ISZERO
0x1ab ISZERO
0x1ac PUSH2 0x1b4
0x1af JUMPI
---
0x159: JUMPDEST 
0x15a: V85 = 0x0
0x15e: V86 = S[0x0]
0x160: V87 = 0x100
0x163: V88 = EXP 0x100 0x0
0x165: V89 = DIV V86 0x1
0x166: V90 = 0xffffffffffffffffffffffffffffffffffffffff
0x17b: V91 = AND 0xffffffffffffffffffffffffffffffffffffffff V89
0x17c: V92 = 0xffffffffffffffffffffffffffffffffffffffff
0x191: V93 = AND 0xffffffffffffffffffffffffffffffffffffffff V91
0x192: V94 = CALLER
0x193: V95 = 0xffffffffffffffffffffffffffffffffffffffff
0x1a8: V96 = AND 0xffffffffffffffffffffffffffffffffffffffff V94
0x1a9: V97 = EQ V96 V93
0x1aa: V98 = ISZERO V97
0x1ab: V99 = ISZERO V98
0x1ac: V100 = 0x1b4
0x1af: JUMPI 0x1b4 V99
---
Entry stack: [V11, 0x84]
Stack pops: 0
Stack additions: []
Exit stack: [V11, 0x84]

================================

Block 0x1b0
[0x1b0:0x1b3]
---
Predecessors: [0x159]
Successors: []
---
0x1b0 PUSH1 0x0
0x1b2 DUP1
0x1b3 REVERT
---
0x1b0: V101 = 0x0
0x1b3: REVERT 0x0 0x0
---
Entry stack: [V11, 0x84]
Stack pops: 0
Stack additions: []
Exit stack: [V11, 0x84]

================================

Block 0x1b4
[0x1b4:0x206]
---
Predecessors: [0x159]
Successors: [0x207, 0x20b]
---
0x1b4 JUMPDEST
0x1b5 CALLER
0x1b6 PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x1cb AND
0x1cc PUSH2 0x8fc
0x1cf ADDRESS
0x1d0 PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x1e5 AND
0x1e6 BALANCE
0x1e7 SWAP1
0x1e8 DUP2
0x1e9 ISZERO
0x1ea MUL
0x1eb SWAP1
0x1ec PUSH1 0x40
0x1ee MLOAD
0x1ef PUSH1 0x0
0x1f1 PUSH1 0x40
0x1f3 MLOAD
0x1f4 DUP1
0x1f5 DUP4
0x1f6 SUB
0x1f7 DUP2
0x1f8 DUP6
0x1f9 DUP9
0x1fa DUP9
0x1fb CALL
0x1fc SWAP4
0x1fd POP
0x1fe POP
0x1ff POP
0x200 POP
0x201 ISZERO
0x202 ISZERO
0x203 PUSH2 0x20b
0x206 JUMPI
---
0x1b4: JUMPDEST 
0x1b5: V102 = CALLER
0x1b6: V103 = 0xffffffffffffffffffffffffffffffffffffffff
0x1cb: V104 = AND 0xffffffffffffffffffffffffffffffffffffffff V102
0x1cc: V105 = 0x8fc
0x1cf: V106 = ADDRESS
0x1d0: V107 = 0xffffffffffffffffffffffffffffffffffffffff
0x1e5: V108 = AND 0xffffffffffffffffffffffffffffffffffffffff V106
0x1e6: V109 = BALANCE V108
0x1e9: V110 = ISZERO V109
0x1ea: V111 = MUL V110 0x8fc
0x1ec: V112 = 0x40
0x1ee: V113 = M[0x40]
0x1ef: V114 = 0x0
0x1f1: V115 = 0x40
0x1f3: V116 = M[0x40]
0x1f6: V117 = SUB V113 V116
0x1fb: V118 = CALL V111 V104 V109 V116 V117 V116 0x0
0x201: V119 = ISZERO V118
0x202: V120 = ISZERO V119
0x203: V121 = 0x20b
0x206: JUMPI 0x20b V120
---
Entry stack: [V11, 0x84]
Stack pops: 0
Stack additions: []
Exit stack: [V11, 0x84]

================================

Block 0x207
[0x207:0x20a]
---
Predecessors: [0x1b4]
Successors: []
---
0x207 PUSH1 0x0
0x209 DUP1
0x20a REVERT
---
0x207: V122 = 0x0
0x20a: REVERT 0x0 0x0
---
Entry stack: [V11, 0x84]
Stack pops: 0
Stack additions: []
Exit stack: [V11, 0x84]

================================

Block 0x20b
[0x20b:0x20c]
---
Predecessors: [0x1b4]
Successors: [0x84]
---
0x20b JUMPDEST
0x20c JUMP
---
0x20b: JUMPDEST 
0x20c: JUMP 0x84
---
Entry stack: [V11, 0x84]
Stack pops: 1
Stack additions: []
Exit stack: [V11]

================================

Block 0x20d
[0x20d:0x212]
---
Predecessors: [0x91]
Successors: [0x99]
---
0x20d JUMPDEST
0x20e PUSH1 0x2
0x210 SLOAD
0x211 DUP2
0x212 JUMP
---
0x20d: JUMPDEST 
0x20e: V123 = 0x2
0x210: V124 = S[0x2]
0x212: JUMP 0x99
---
Entry stack: [V11, 0x99]
Stack pops: 1
Stack additions: [S0, V124]
Exit stack: [V11, 0x99, V124]

================================

Block 0x213
[0x213:0x238]
---
Predecessors: [0xba]
Successors: [0xc2]
---
0x213 JUMPDEST
0x214 PUSH1 0x1
0x216 PUSH1 0x0
0x218 SWAP1
0x219 SLOAD
0x21a SWAP1
0x21b PUSH2 0x100
0x21e EXP
0x21f SWAP1
0x220 DIV
0x221 PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x236 AND
0x237 DUP2
0x238 JUMP
---
0x213: JUMPDEST 
0x214: V125 = 0x1
0x216: V126 = 0x0
0x219: V127 = S[0x1]
0x21b: V128 = 0x100
0x21e: V129 = EXP 0x100 0x0
0x220: V130 = DIV V127 0x1
0x221: V131 = 0xffffffffffffffffffffffffffffffffffffffff
0x236: V132 = AND 0xffffffffffffffffffffffffffffffffffffffff V130
0x238: JUMP 0xc2
---
Entry stack: [V11, 0xc2]
Stack pops: 1
Stack additions: [S0, V132]
Exit stack: [V11, 0xc2, V132]

================================

Block 0x239
[0x239:0x267]
---
Predecessors: []
Successors: []
---
0x239 STOP
0x23a LOG1
0x23b PUSH6 0x627a7a723058
0x242 SHA3
0x243 MISSING 0x27
0x244 POP
0x245 MISSING 0xb2
0x246 MISSING 0xc6
0x247 SWAP5
0x248 PUSH5 0x14c8472de5
0x24e OR
0x24f MISSING 0xc2
0x250 MISSING 0xb5
0x251 EXTCODESIZE
0x252 MISSING 0xae
0x253 BYTE
0x254 SWAP11
0x255 MISSING 0xe9
0x256 PUSH17 0x632c7017114cbca2169547350029
---
0x239: STOP 
0x23a: LOG S0 S1 S2
0x23b: V133 = 0x627a7a723058
0x242: V134 = SHA3 0x627a7a723058 S3
0x243: MISSING 0x27
0x245: MISSING 0xb2
0x246: MISSING 0xc6
0x248: V135 = 0x14c8472de5
0x24e: V136 = OR 0x14c8472de5 S5
0x24f: MISSING 0xc2
0x250: MISSING 0xb5
0x251: V137 = EXTCODESIZE S0
0x252: MISSING 0xae
0x253: V138 = BYTE S0 S1
0x255: MISSING 0xe9
0x256: V139 = 0x632c7017114cbca2169547350029
---
Entry stack: []
Stack pops: 0
Stack additions: [V134, V136, S1, S2, S3, S4, S0, V137, S12, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, V138, 0x632c7017114cbca2169547350029]
Exit stack: []

================================

Function 0:
Public function signature: 0x18c0e04f
Entry block: 0x67
Exit block: 0x6f
Body: 0x67, 0x6f, 0x104, 0x10f, 0x157

Function 1:
Public function signature: 0x3ccfd60b
Entry block: 0x71
Exit block: 0x84
Body: 0x71, 0x78, 0x7c, 0x84, 0x159, 0x1b0, 0x1b4, 0x207, 0x20b

Function 2:
Public function signature: 0x4c8cab79
Entry block: 0x86
Exit block: 0x99
Body: 0x86, 0x8d, 0x91, 0x99, 0x20d

Function 3:
Public function signature: 0x8da5cb5b
Entry block: 0xaf
Exit block: 0xc2
Body: 0xaf, 0xb6, 0xba, 0xc2, 0x213

Function 4:
Public fallback function
Entry block: 0x62
Exit block: 0x62
Body: 0x62

