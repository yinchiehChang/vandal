Block 0x0
[0x0:0xc]
---
Predecessors: []
Successors: [0xd, 0x48]
---
0x0 PUSH1 0x60
0x2 PUSH1 0x40
0x4 MSTORE
0x5 PUSH1 0x4
0x7 CALLDATASIZE
0x8 LT
0x9 PUSH2 0x48
0xc JUMPI
---
0x0: V0 = 0x60
0x2: V1 = 0x40
0x4: M[0x40] = 0x60
0x5: V2 = 0x4
0x7: V3 = CALLDATASIZE
0x8: V4 = LT V3 0x4
0x9: V5 = 0x48
0xc: JUMPI 0x48 V4
---
Entry stack: []
Stack pops: 0
Stack additions: []
Exit stack: []

================================

Block 0xd
[0xd:0x26]
---
Predecessors: [0x0]
Successors: [0x27, 0x4d]
---
0xd PUSH4 0xffffffff
0x12 PUSH1 0xe0
0x14 PUSH1 0x2
0x16 EXP
0x17 PUSH1 0x0
0x19 CALLDATALOAD
0x1a DIV
0x1b AND
0x1c PUSH4 0x38af3eed
0x21 DUP2
0x22 EQ
0x23 PUSH2 0x4d
0x26 JUMPI
---
0xd: V6 = 0xffffffff
0x12: V7 = 0xe0
0x14: V8 = 0x2
0x16: V9 = EXP 0x2 0xe0
0x17: V10 = 0x0
0x19: V11 = CALLDATALOAD 0x0
0x1a: V12 = DIV V11 0x100000000000000000000000000000000000000000000000000000000
0x1b: V13 = AND V12 0xffffffff
0x1c: V14 = 0x38af3eed
0x22: V15 = EQ V13 0x38af3eed
0x23: V16 = 0x4d
0x26: JUMPI 0x4d V15
---
Entry stack: []
Stack pops: 0
Stack additions: [V13]
Exit stack: [V13]

================================

Block 0x27
[0x27:0x31]
---
Predecessors: [0xd]
Successors: [0x32, 0x7c]
---
0x27 DUP1
0x28 PUSH4 0x86d1a69f
0x2d EQ
0x2e PUSH2 0x7c
0x31 JUMPI
---
0x28: V17 = 0x86d1a69f
0x2d: V18 = EQ 0x86d1a69f V13
0x2e: V19 = 0x7c
0x31: JUMPI 0x7c V18
---
Entry stack: [V13]
Stack pops: 1
Stack additions: [S0]
Exit stack: [V13]

================================

Block 0x32
[0x32:0x3c]
---
Predecessors: [0x27]
Successors: [0x3d, 0x91]
---
0x32 DUP1
0x33 PUSH4 0xb91d4001
0x38 EQ
0x39 PUSH2 0x91
0x3c JUMPI
---
0x33: V20 = 0xb91d4001
0x38: V21 = EQ 0xb91d4001 V13
0x39: V22 = 0x91
0x3c: JUMPI 0x91 V21
---
Entry stack: [V13]
Stack pops: 1
Stack additions: [S0]
Exit stack: [V13]

================================

Block 0x3d
[0x3d:0x47]
---
Predecessors: [0x32]
Successors: [0x48, 0xb6]
---
0x3d DUP1
0x3e PUSH4 0xfc0c546a
0x43 EQ
0x44 PUSH2 0xb6
0x47 JUMPI
---
0x3e: V23 = 0xfc0c546a
0x43: V24 = EQ 0xfc0c546a V13
0x44: V25 = 0xb6
0x47: JUMPI 0xb6 V24
---
Entry stack: [V13]
Stack pops: 1
Stack additions: [S0]
Exit stack: [V13]

================================

Block 0x48
[0x48:0x4c]
---
Predecessors: [0x0, 0x3d]
Successors: []
---
0x48 JUMPDEST
0x49 PUSH1 0x0
0x4b DUP1
0x4c REVERT
---
0x48: JUMPDEST 
0x49: V26 = 0x0
0x4c: REVERT 0x0 0x0
---
Entry stack: [V13]
Stack pops: 0
Stack additions: []
Exit stack: [V13]

================================

Block 0x4d
[0x4d:0x53]
---
Predecessors: [0xd]
Successors: [0x54, 0x58]
---
0x4d JUMPDEST
0x4e CALLVALUE
0x4f ISZERO
0x50 PUSH2 0x58
0x53 JUMPI
---
0x4d: JUMPDEST 
0x4e: V27 = CALLVALUE
0x4f: V28 = ISZERO V27
0x50: V29 = 0x58
0x53: JUMPI 0x58 V28
---
Entry stack: [V13]
Stack pops: 0
Stack additions: []
Exit stack: [V13]

================================

Block 0x54
[0x54:0x57]
---
Predecessors: [0x4d]
Successors: []
---
0x54 PUSH1 0x0
0x56 DUP1
0x57 REVERT
---
0x54: V30 = 0x0
0x57: REVERT 0x0 0x0
---
Entry stack: [V13]
Stack pops: 0
Stack additions: []
Exit stack: [V13]

================================

Block 0x58
[0x58:0x5f]
---
Predecessors: [0x4d]
Successors: [0xc9]
---
0x58 JUMPDEST
0x59 PUSH2 0x60
0x5c PUSH2 0xc9
0x5f JUMP
---
0x58: JUMPDEST 
0x59: V31 = 0x60
0x5c: V32 = 0xc9
0x5f: JUMP 0xc9
---
Entry stack: [V13]
Stack pops: 0
Stack additions: [0x60]
Exit stack: [V13, 0x60]

================================

Block 0x60
[0x60:0x7b]
---
Predecessors: [0xc9, 0x18b]
Successors: []
---
0x60 JUMPDEST
0x61 PUSH1 0x40
0x63 MLOAD
0x64 PUSH1 0x1
0x66 PUSH1 0xa0
0x68 PUSH1 0x2
0x6a EXP
0x6b SUB
0x6c SWAP1
0x6d SWAP2
0x6e AND
0x6f DUP2
0x70 MSTORE
0x71 PUSH1 0x20
0x73 ADD
0x74 PUSH1 0x40
0x76 MLOAD
0x77 DUP1
0x78 SWAP2
0x79 SUB
0x7a SWAP1
0x7b RETURN
---
0x60: JUMPDEST 
0x61: V33 = 0x40
0x63: V34 = M[0x40]
0x64: V35 = 0x1
0x66: V36 = 0xa0
0x68: V37 = 0x2
0x6a: V38 = EXP 0x2 0xa0
0x6b: V39 = SUB 0x10000000000000000000000000000000000000000 0x1
0x6e: V40 = AND S0 0xffffffffffffffffffffffffffffffffffffffff
0x70: M[V34] = V40
0x71: V41 = 0x20
0x73: V42 = ADD 0x20 V34
0x74: V43 = 0x40
0x76: V44 = M[0x40]
0x79: V45 = SUB V42 V44
0x7b: RETURN V44 V45
---
Entry stack: [V13, 0x60, S0]
Stack pops: 1
Stack additions: []
Exit stack: [V13, 0x60]

================================

Block 0x7c
[0x7c:0x82]
---
Predecessors: [0x27]
Successors: [0x83, 0x87]
---
0x7c JUMPDEST
0x7d CALLVALUE
0x7e ISZERO
0x7f PUSH2 0x87
0x82 JUMPI
---
0x7c: JUMPDEST 
0x7d: V46 = CALLVALUE
0x7e: V47 = ISZERO V46
0x7f: V48 = 0x87
0x82: JUMPI 0x87 V47
---
Entry stack: [V13]
Stack pops: 0
Stack additions: []
Exit stack: [V13]

================================

Block 0x83
[0x83:0x86]
---
Predecessors: [0x7c]
Successors: []
---
0x83 PUSH1 0x0
0x85 DUP1
0x86 REVERT
---
0x83: V49 = 0x0
0x86: REVERT 0x0 0x0
---
Entry stack: [V13]
Stack pops: 0
Stack additions: []
Exit stack: [V13]

================================

Block 0x87
[0x87:0x8e]
---
Predecessors: [0x7c]
Successors: [0xd8]
---
0x87 JUMPDEST
0x88 PUSH2 0x8f
0x8b PUSH2 0xd8
0x8e JUMP
---
0x87: JUMPDEST 
0x88: V50 = 0x8f
0x8b: V51 = 0xd8
0x8e: JUMP 0xd8
---
Entry stack: [V13]
Stack pops: 0
Stack additions: [0x8f]
Exit stack: [V13, 0x8f]

================================

Block 0x8f
[0x8f:0x90]
---
Predecessors: [0x182]
Successors: []
---
0x8f JUMPDEST
0x90 STOP
---
0x8f: JUMPDEST 
0x90: STOP 
---
Entry stack: [V13]
Stack pops: 0
Stack additions: []
Exit stack: [V13]

================================

Block 0x91
[0x91:0x97]
---
Predecessors: [0x32]
Successors: [0x98, 0x9c]
---
0x91 JUMPDEST
0x92 CALLVALUE
0x93 ISZERO
0x94 PUSH2 0x9c
0x97 JUMPI
---
0x91: JUMPDEST 
0x92: V52 = CALLVALUE
0x93: V53 = ISZERO V52
0x94: V54 = 0x9c
0x97: JUMPI 0x9c V53
---
Entry stack: [V13]
Stack pops: 0
Stack additions: []
Exit stack: [V13]

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
0x98: V55 = 0x0
0x9b: REVERT 0x0 0x0
---
Entry stack: [V13]
Stack pops: 0
Stack additions: []
Exit stack: [V13]

================================

Block 0x9c
[0x9c:0xa3]
---
Predecessors: [0x91]
Successors: [0x185]
---
0x9c JUMPDEST
0x9d PUSH2 0xa4
0xa0 PUSH2 0x185
0xa3 JUMP
---
0x9c: JUMPDEST 
0x9d: V56 = 0xa4
0xa0: V57 = 0x185
0xa3: JUMP 0x185
---
Entry stack: [V13]
Stack pops: 0
Stack additions: [0xa4]
Exit stack: [V13, 0xa4]

================================

Block 0xa4
[0xa4:0xb5]
---
Predecessors: [0x185]
Successors: []
---
0xa4 JUMPDEST
0xa5 PUSH1 0x40
0xa7 MLOAD
0xa8 SWAP1
0xa9 DUP2
0xaa MSTORE
0xab PUSH1 0x20
0xad ADD
0xae PUSH1 0x40
0xb0 MLOAD
0xb1 DUP1
0xb2 SWAP2
0xb3 SUB
0xb4 SWAP1
0xb5 RETURN
---
0xa4: JUMPDEST 
0xa5: V58 = 0x40
0xa7: V59 = M[0x40]
0xaa: M[V59] = V154
0xab: V60 = 0x20
0xad: V61 = ADD 0x20 V59
0xae: V62 = 0x40
0xb0: V63 = M[0x40]
0xb3: V64 = SUB V61 V63
0xb5: RETURN V63 V64
---
Entry stack: [V13, 0xa4, V154]
Stack pops: 1
Stack additions: []
Exit stack: [V13, 0xa4]

================================

Block 0xb6
[0xb6:0xbc]
---
Predecessors: [0x3d]
Successors: [0xbd, 0xc1]
---
0xb6 JUMPDEST
0xb7 CALLVALUE
0xb8 ISZERO
0xb9 PUSH2 0xc1
0xbc JUMPI
---
0xb6: JUMPDEST 
0xb7: V65 = CALLVALUE
0xb8: V66 = ISZERO V65
0xb9: V67 = 0xc1
0xbc: JUMPI 0xc1 V66
---
Entry stack: [V13]
Stack pops: 0
Stack additions: []
Exit stack: [V13]

================================

Block 0xbd
[0xbd:0xc0]
---
Predecessors: [0xb6]
Successors: []
---
0xbd PUSH1 0x0
0xbf DUP1
0xc0 REVERT
---
0xbd: V68 = 0x0
0xc0: REVERT 0x0 0x0
---
Entry stack: [V13]
Stack pops: 0
Stack additions: []
Exit stack: [V13]

================================

Block 0xc1
[0xc1:0xc8]
---
Predecessors: [0xb6]
Successors: [0x18b]
---
0xc1 JUMPDEST
0xc2 PUSH2 0x60
0xc5 PUSH2 0x18b
0xc8 JUMP
---
0xc1: JUMPDEST 
0xc2: V69 = 0x60
0xc5: V70 = 0x18b
0xc8: JUMP 0x18b
---
Entry stack: [V13]
Stack pops: 0
Stack additions: [0x60]
Exit stack: [V13, 0x60]

================================

Block 0xc9
[0xc9:0xd7]
---
Predecessors: [0x58]
Successors: [0x60]
---
0xc9 JUMPDEST
0xca PUSH1 0x1
0xcc SLOAD
0xcd PUSH1 0x1
0xcf PUSH1 0xa0
0xd1 PUSH1 0x2
0xd3 EXP
0xd4 SUB
0xd5 AND
0xd6 DUP2
0xd7 JUMP
---
0xc9: JUMPDEST 
0xca: V71 = 0x1
0xcc: V72 = S[0x1]
0xcd: V73 = 0x1
0xcf: V74 = 0xa0
0xd1: V75 = 0x2
0xd3: V76 = EXP 0x2 0xa0
0xd4: V77 = SUB 0x10000000000000000000000000000000000000000 0x1
0xd5: V78 = AND 0xffffffffffffffffffffffffffffffffffffffff V72
0xd7: JUMP 0x60
---
Entry stack: [V13, 0x60]
Stack pops: 1
Stack additions: [S0, V78]
Exit stack: [V13, 0x60, V78]

================================

Block 0xd8
[0xd8:0xe5]
---
Predecessors: [0x87]
Successors: [0xe6, 0xea]
---
0xd8 JUMPDEST
0xd9 PUSH1 0x2
0xdb SLOAD
0xdc PUSH1 0x0
0xde SWAP1
0xdf TIMESTAMP
0xe0 LT
0xe1 ISZERO
0xe2 PUSH2 0xea
0xe5 JUMPI
---
0xd8: JUMPDEST 
0xd9: V79 = 0x2
0xdb: V80 = S[0x2]
0xdc: V81 = 0x0
0xdf: V82 = TIMESTAMP
0xe0: V83 = LT V82 V80
0xe1: V84 = ISZERO V83
0xe2: V85 = 0xea
0xe5: JUMPI 0xea V84
---
Entry stack: [V13, 0x8f]
Stack pops: 0
Stack additions: [0x0]
Exit stack: [V13, 0x8f, 0x0]

================================

Block 0xe6
[0xe6:0xe9]
---
Predecessors: [0xd8]
Successors: []
---
0xe6 PUSH1 0x0
0xe8 DUP1
0xe9 REVERT
---
0xe6: V86 = 0x0
0xe9: REVERT 0x0 0x0
---
Entry stack: [V13, 0x8f, 0x0]
Stack pops: 0
Stack additions: []
Exit stack: [V13, 0x8f, 0x0]

================================

Block 0xea
[0xea:0x135]
---
Predecessors: [0xd8]
Successors: [0x136, 0x13a]
---
0xea JUMPDEST
0xeb PUSH1 0x0
0xed SLOAD
0xee PUSH1 0x1
0xf0 PUSH1 0xa0
0xf2 PUSH1 0x2
0xf4 EXP
0xf5 SUB
0xf6 AND
0xf7 PUSH4 0x70a08231
0xfc ADDRESS
0xfd PUSH1 0x40
0xff MLOAD
0x100 PUSH1 0xe0
0x102 PUSH1 0x2
0x104 EXP
0x105 PUSH4 0xffffffff
0x10a DUP5
0x10b AND
0x10c MUL
0x10d DUP2
0x10e MSTORE
0x10f PUSH1 0x1
0x111 PUSH1 0xa0
0x113 PUSH1 0x2
0x115 EXP
0x116 SUB
0x117 SWAP1
0x118 SWAP2
0x119 AND
0x11a PUSH1 0x4
0x11c DUP3
0x11d ADD
0x11e MSTORE
0x11f PUSH1 0x24
0x121 ADD
0x122 PUSH1 0x20
0x124 PUSH1 0x40
0x126 MLOAD
0x127 DUP1
0x128 DUP4
0x129 SUB
0x12a DUP2
0x12b PUSH1 0x0
0x12d DUP8
0x12e DUP1
0x12f EXTCODESIZE
0x130 ISZERO
0x131 ISZERO
0x132 PUSH2 0x13a
0x135 JUMPI
---
0xea: JUMPDEST 
0xeb: V87 = 0x0
0xed: V88 = S[0x0]
0xee: V89 = 0x1
0xf0: V90 = 0xa0
0xf2: V91 = 0x2
0xf4: V92 = EXP 0x2 0xa0
0xf5: V93 = SUB 0x10000000000000000000000000000000000000000 0x1
0xf6: V94 = AND 0xffffffffffffffffffffffffffffffffffffffff V88
0xf7: V95 = 0x70a08231
0xfc: V96 = ADDRESS
0xfd: V97 = 0x40
0xff: V98 = M[0x40]
0x100: V99 = 0xe0
0x102: V100 = 0x2
0x104: V101 = EXP 0x2 0xe0
0x105: V102 = 0xffffffff
0x10b: V103 = AND 0x70a08231 0xffffffff
0x10c: V104 = MUL 0x70a08231 0x100000000000000000000000000000000000000000000000000000000
0x10e: M[V98] = 0x70a0823100000000000000000000000000000000000000000000000000000000
0x10f: V105 = 0x1
0x111: V106 = 0xa0
0x113: V107 = 0x2
0x115: V108 = EXP 0x2 0xa0
0x116: V109 = SUB 0x10000000000000000000000000000000000000000 0x1
0x119: V110 = AND V96 0xffffffffffffffffffffffffffffffffffffffff
0x11a: V111 = 0x4
0x11d: V112 = ADD V98 0x4
0x11e: M[V112] = V110
0x11f: V113 = 0x24
0x121: V114 = ADD 0x24 V98
0x122: V115 = 0x20
0x124: V116 = 0x40
0x126: V117 = M[0x40]
0x129: V118 = SUB V114 V117
0x12b: V119 = 0x0
0x12f: V120 = EXTCODESIZE V94
0x130: V121 = ISZERO V120
0x131: V122 = ISZERO V121
0x132: V123 = 0x13a
0x135: JUMPI 0x13a V122
---
Entry stack: [V13, 0x8f, 0x0]
Stack pops: 0
Stack additions: [V94, 0x70a08231, V114, 0x20, V117, V118, V117, 0x0, V94]
Exit stack: [V13, 0x8f, 0x0, V94, 0x70a08231, V114, 0x20, V117, V118, V117, 0x0, V94]

================================

Block 0x136
[0x136:0x139]
---
Predecessors: [0xea]
Successors: []
---
0x136 PUSH1 0x0
0x138 DUP1
0x139 REVERT
---
0x136: V124 = 0x0
0x139: REVERT 0x0 0x0
---
Entry stack: [V13, 0x8f, 0x0, V94, 0x70a08231, V114, 0x20, V117, V118, V117, 0x0, V94]
Stack pops: 0
Stack additions: []
Exit stack: [V13, 0x8f, 0x0, V94, 0x70a08231, V114, 0x20, V117, V118, V117, 0x0, V94]

================================

Block 0x13a
[0x13a:0x142]
---
Predecessors: [0xea]
Successors: [0x143, 0x147]
---
0x13a JUMPDEST
0x13b GAS
0x13c CALL
0x13d ISZERO
0x13e ISZERO
0x13f PUSH2 0x147
0x142 JUMPI
---
0x13a: JUMPDEST 
0x13b: V125 = GAS
0x13c: V126 = CALL V125 V94 0x0 V117 V118 V117 0x20
0x13d: V127 = ISZERO V126
0x13e: V128 = ISZERO V127
0x13f: V129 = 0x147
0x142: JUMPI 0x147 V128
---
Entry stack: [V13, 0x8f, 0x0, V94, 0x70a08231, V114, 0x20, V117, V118, V117, 0x0, V94]
Stack pops: 6
Stack additions: []
Exit stack: [V13, 0x8f, 0x0, V94, 0x70a08231, V114]

================================

Block 0x143
[0x143:0x146]
---
Predecessors: [0x13a]
Successors: []
---
0x143 PUSH1 0x0
0x145 DUP1
0x146 REVERT
---
0x143: V130 = 0x0
0x146: REVERT 0x0 0x0
---
Entry stack: [V13, 0x8f, 0x0, V94, 0x70a08231, V114]
Stack pops: 0
Stack additions: []
Exit stack: [V13, 0x8f, 0x0, V94, 0x70a08231, V114]

================================

Block 0x147
[0x147:0x15a]
---
Predecessors: [0x13a]
Successors: [0x15b, 0x15f]
---
0x147 JUMPDEST
0x148 POP
0x149 POP
0x14a POP
0x14b PUSH1 0x40
0x14d MLOAD
0x14e DUP1
0x14f MLOAD
0x150 SWAP2
0x151 POP
0x152 POP
0x153 PUSH1 0x0
0x155 DUP2
0x156 GT
0x157 PUSH2 0x15f
0x15a JUMPI
---
0x147: JUMPDEST 
0x14b: V131 = 0x40
0x14d: V132 = M[0x40]
0x14f: V133 = M[V132]
0x153: V134 = 0x0
0x156: V135 = GT V133 0x0
0x157: V136 = 0x15f
0x15a: JUMPI 0x15f V135
---
Entry stack: [V13, 0x8f, 0x0, V94, 0x70a08231, V114]
Stack pops: 4
Stack additions: [V133]
Exit stack: [V13, 0x8f, V133]

================================

Block 0x15b
[0x15b:0x15e]
---
Predecessors: [0x147]
Successors: []
---
0x15b PUSH1 0x0
0x15d DUP1
0x15e REVERT
---
0x15b: V137 = 0x0
0x15e: REVERT 0x0 0x0
---
Entry stack: [V13, 0x8f, V133]
Stack pops: 0
Stack additions: []
Exit stack: [V13, 0x8f, V133]

================================

Block 0x15f
[0x15f:0x181]
---
Predecessors: [0x147]
Successors: [0x19a]
---
0x15f JUMPDEST
0x160 PUSH1 0x1
0x162 SLOAD
0x163 PUSH1 0x0
0x165 SLOAD
0x166 PUSH2 0x182
0x169 SWAP2
0x16a PUSH1 0x1
0x16c PUSH1 0xa0
0x16e PUSH1 0x2
0x170 EXP
0x171 SUB
0x172 SWAP2
0x173 DUP3
0x174 AND
0x175 SWAP2
0x176 AND
0x177 DUP4
0x178 PUSH4 0xffffffff
0x17d PUSH2 0x19a
0x180 AND
0x181 JUMP
---
0x15f: JUMPDEST 
0x160: V138 = 0x1
0x162: V139 = S[0x1]
0x163: V140 = 0x0
0x165: V141 = S[0x0]
0x166: V142 = 0x182
0x16a: V143 = 0x1
0x16c: V144 = 0xa0
0x16e: V145 = 0x2
0x170: V146 = EXP 0x2 0xa0
0x171: V147 = SUB 0x10000000000000000000000000000000000000000 0x1
0x174: V148 = AND 0xffffffffffffffffffffffffffffffffffffffff V141
0x176: V149 = AND 0xffffffffffffffffffffffffffffffffffffffff V139
0x178: V150 = 0xffffffff
0x17d: V151 = 0x19a
0x180: V152 = AND 0x19a 0xffffffff
0x181: JUMP 0x19a
---
Entry stack: [V13, 0x8f, V133]
Stack pops: 1
Stack additions: [S0, 0x182, V148, V149, S0]
Exit stack: [V13, 0x8f, V133, 0x182, V148, V149, V133]

================================

Block 0x182
[0x182:0x184]
---
Predecessors: [0x20d]
Successors: [0x8f]
---
0x182 JUMPDEST
0x183 POP
0x184 JUMP
---
0x182: JUMPDEST 
0x184: JUMP 0x8f
---
Entry stack: [V13, 0x8f, V133]
Stack pops: 2
Stack additions: []
Exit stack: [V13]

================================

Block 0x185
[0x185:0x18a]
---
Predecessors: [0x9c]
Successors: [0xa4]
---
0x185 JUMPDEST
0x186 PUSH1 0x2
0x188 SLOAD
0x189 DUP2
0x18a JUMP
---
0x185: JUMPDEST 
0x186: V153 = 0x2
0x188: V154 = S[0x2]
0x18a: JUMP 0xa4
---
Entry stack: [V13, 0xa4]
Stack pops: 1
Stack additions: [S0, V154]
Exit stack: [V13, 0xa4, V154]

================================

Block 0x18b
[0x18b:0x199]
---
Predecessors: [0xc1]
Successors: [0x60]
---
0x18b JUMPDEST
0x18c PUSH1 0x0
0x18e SLOAD
0x18f PUSH1 0x1
0x191 PUSH1 0xa0
0x193 PUSH1 0x2
0x195 EXP
0x196 SUB
0x197 AND
0x198 DUP2
0x199 JUMP
---
0x18b: JUMPDEST 
0x18c: V155 = 0x0
0x18e: V156 = S[0x0]
0x18f: V157 = 0x1
0x191: V158 = 0xa0
0x193: V159 = 0x2
0x195: V160 = EXP 0x2 0xa0
0x196: V161 = SUB 0x10000000000000000000000000000000000000000 0x1
0x197: V162 = AND 0xffffffffffffffffffffffffffffffffffffffff V156
0x199: JUMP 0x60
---
Entry stack: [V13, 0x60]
Stack pops: 1
Stack additions: [S0, V162]
Exit stack: [V13, 0x60, V162]

================================

Block 0x19a
[0x19a:0x1e9]
---
Predecessors: [0x15f]
Successors: [0x1ea, 0x1ee]
---
0x19a JUMPDEST
0x19b DUP3
0x19c PUSH1 0x1
0x19e PUSH1 0xa0
0x1a0 PUSH1 0x2
0x1a2 EXP
0x1a3 SUB
0x1a4 AND
0x1a5 PUSH4 0xa9059cbb
0x1aa DUP4
0x1ab DUP4
0x1ac PUSH1 0x40
0x1ae MLOAD
0x1af PUSH1 0xe0
0x1b1 PUSH1 0x2
0x1b3 EXP
0x1b4 PUSH4 0xffffffff
0x1b9 DUP6
0x1ba AND
0x1bb MUL
0x1bc DUP2
0x1bd MSTORE
0x1be PUSH1 0x1
0x1c0 PUSH1 0xa0
0x1c2 PUSH1 0x2
0x1c4 EXP
0x1c5 SUB
0x1c6 SWAP1
0x1c7 SWAP3
0x1c8 AND
0x1c9 PUSH1 0x4
0x1cb DUP4
0x1cc ADD
0x1cd MSTORE
0x1ce PUSH1 0x24
0x1d0 DUP3
0x1d1 ADD
0x1d2 MSTORE
0x1d3 PUSH1 0x44
0x1d5 ADD
0x1d6 PUSH1 0x20
0x1d8 PUSH1 0x40
0x1da MLOAD
0x1db DUP1
0x1dc DUP4
0x1dd SUB
0x1de DUP2
0x1df PUSH1 0x0
0x1e1 DUP8
0x1e2 DUP1
0x1e3 EXTCODESIZE
0x1e4 ISZERO
0x1e5 ISZERO
0x1e6 PUSH2 0x1ee
0x1e9 JUMPI
---
0x19a: JUMPDEST 
0x19c: V163 = 0x1
0x19e: V164 = 0xa0
0x1a0: V165 = 0x2
0x1a2: V166 = EXP 0x2 0xa0
0x1a3: V167 = SUB 0x10000000000000000000000000000000000000000 0x1
0x1a4: V168 = AND 0xffffffffffffffffffffffffffffffffffffffff V148
0x1a5: V169 = 0xa9059cbb
0x1ac: V170 = 0x40
0x1ae: V171 = M[0x40]
0x1af: V172 = 0xe0
0x1b1: V173 = 0x2
0x1b3: V174 = EXP 0x2 0xe0
0x1b4: V175 = 0xffffffff
0x1ba: V176 = AND 0xa9059cbb 0xffffffff
0x1bb: V177 = MUL 0xa9059cbb 0x100000000000000000000000000000000000000000000000000000000
0x1bd: M[V171] = 0xa9059cbb00000000000000000000000000000000000000000000000000000000
0x1be: V178 = 0x1
0x1c0: V179 = 0xa0
0x1c2: V180 = 0x2
0x1c4: V181 = EXP 0x2 0xa0
0x1c5: V182 = SUB 0x10000000000000000000000000000000000000000 0x1
0x1c8: V183 = AND V149 0xffffffffffffffffffffffffffffffffffffffff
0x1c9: V184 = 0x4
0x1cc: V185 = ADD V171 0x4
0x1cd: M[V185] = V183
0x1ce: V186 = 0x24
0x1d1: V187 = ADD V171 0x24
0x1d2: M[V187] = V133
0x1d3: V188 = 0x44
0x1d5: V189 = ADD 0x44 V171
0x1d6: V190 = 0x20
0x1d8: V191 = 0x40
0x1da: V192 = M[0x40]
0x1dd: V193 = SUB V189 V192
0x1df: V194 = 0x0
0x1e3: V195 = EXTCODESIZE V168
0x1e4: V196 = ISZERO V195
0x1e5: V197 = ISZERO V196
0x1e6: V198 = 0x1ee
0x1e9: JUMPI 0x1ee V197
---
Entry stack: [V13, 0x8f, V133, 0x182, V148, V149, V133]
Stack pops: 3
Stack additions: [S2, S1, S0, V168, 0xa9059cbb, V189, 0x20, V192, V193, V192, 0x0, V168]
Exit stack: [V13, 0x8f, V133, 0x182, V148, V149, V133, V168, 0xa9059cbb, V189, 0x20, V192, V193, V192, 0x0, V168]

================================

Block 0x1ea
[0x1ea:0x1ed]
---
Predecessors: [0x19a]
Successors: []
---
0x1ea PUSH1 0x0
0x1ec DUP1
0x1ed REVERT
---
0x1ea: V199 = 0x0
0x1ed: REVERT 0x0 0x0
---
Entry stack: [V13, 0x8f, V133, 0x182, V148, V149, V133, V168, 0xa9059cbb, V189, 0x20, V192, V193, V192, 0x0, V168]
Stack pops: 0
Stack additions: []
Exit stack: [V13, 0x8f, V133, 0x182, V148, V149, V133, V168, 0xa9059cbb, V189, 0x20, V192, V193, V192, 0x0, V168]

================================

Block 0x1ee
[0x1ee:0x1f6]
---
Predecessors: [0x19a]
Successors: [0x1f7, 0x1fb]
---
0x1ee JUMPDEST
0x1ef GAS
0x1f0 CALL
0x1f1 ISZERO
0x1f2 ISZERO
0x1f3 PUSH2 0x1fb
0x1f6 JUMPI
---
0x1ee: JUMPDEST 
0x1ef: V200 = GAS
0x1f0: V201 = CALL V200 V168 0x0 V192 V193 V192 0x20
0x1f1: V202 = ISZERO V201
0x1f2: V203 = ISZERO V202
0x1f3: V204 = 0x1fb
0x1f6: JUMPI 0x1fb V203
---
Entry stack: [V13, 0x8f, V133, 0x182, V148, V149, V133, V168, 0xa9059cbb, V189, 0x20, V192, V193, V192, 0x0, V168]
Stack pops: 6
Stack additions: []
Exit stack: [V13, 0x8f, V133, 0x182, V148, V149, V133, V168, 0xa9059cbb, V189]

================================

Block 0x1f7
[0x1f7:0x1fa]
---
Predecessors: [0x1ee]
Successors: []
---
0x1f7 PUSH1 0x0
0x1f9 DUP1
0x1fa REVERT
---
0x1f7: V205 = 0x0
0x1fa: REVERT 0x0 0x0
---
Entry stack: [V13, 0x8f, V133, 0x182, V148, V149, V133, V168, 0xa9059cbb, V189]
Stack pops: 0
Stack additions: []
Exit stack: [V13, 0x8f, V133, 0x182, V148, V149, V133, V168, 0xa9059cbb, V189]

================================

Block 0x1fb
[0x1fb:0x20b]
---
Predecessors: [0x1ee]
Successors: [0x20c, 0x20d]
---
0x1fb JUMPDEST
0x1fc POP
0x1fd POP
0x1fe POP
0x1ff PUSH1 0x40
0x201 MLOAD
0x202 DUP1
0x203 MLOAD
0x204 SWAP1
0x205 POP
0x206 ISZERO
0x207 ISZERO
0x208 PUSH2 0x20d
0x20b JUMPI
---
0x1fb: JUMPDEST 
0x1ff: V206 = 0x40
0x201: V207 = M[0x40]
0x203: V208 = M[V207]
0x206: V209 = ISZERO V208
0x207: V210 = ISZERO V209
0x208: V211 = 0x20d
0x20b: JUMPI 0x20d V210
---
Entry stack: [V13, 0x8f, V133, 0x182, V148, V149, V133, V168, 0xa9059cbb, V189]
Stack pops: 3
Stack additions: []
Exit stack: [V13, 0x8f, V133, 0x182, V148, V149, V133]

================================

Block 0x20c
[0x20c:0x20c]
---
Predecessors: [0x1fb]
Successors: []
---
0x20c INVALID
---
0x20c: INVALID 
---
Entry stack: [V13, 0x8f, V133, 0x182, V148, V149, V133]
Stack pops: 0
Stack additions: []
Exit stack: [V13, 0x8f, V133, 0x182, V148, V149, V133]

================================

Block 0x20d
[0x20d:0x211]
---
Predecessors: [0x1fb]
Successors: [0x182]
---
0x20d JUMPDEST
0x20e POP
0x20f POP
0x210 POP
0x211 JUMP
---
0x20d: JUMPDEST 
0x211: JUMP 0x182
---
Entry stack: [V13, 0x8f, V133, 0x182, V148, V149, V133]
Stack pops: 4
Stack additions: []
Exit stack: [V13, 0x8f, V133]

================================

Block 0x212
[0x212:0x241]
---
Predecessors: []
Successors: []
---
0x212 STOP
0x213 LOG1
0x214 PUSH6 0x627a7a723058
0x21b SHA3
0x21c MISSING 0xc1
0x21d MISSING 0xda
0x21e SWAP3
0x21f MISSING 0xbf
0x220 MISSING 0xd5
0x221 MISSING 0x24
0x222 MISSING 0xc0
0x223 SWAP15
0x224 MISSING 0xe3
0x225 MISSING 0xbe
0x226 MISSING 0x2f
0x227 MISSING 0xaa
0x228 COINBASE
0x229 MISSING 0xaa
0x22a CREATE2
0x22b MISSING 0xf9
0x22c MISSING 0xf7
0x22d ISZERO
0x22e MISSING 0xca
0x22f LOG4
0x230 SDIV
0x231 MISSING 0x5e
0x232 OR
0x233 DUP15
0x234 REVERT
0x235 ISZERO
0x236 AND
0x237 PUSH10 0x5532d6bd0029
---
0x212: STOP 
0x213: LOG S0 S1 S2
0x214: V212 = 0x627a7a723058
0x21b: V213 = SHA3 0x627a7a723058 S3
0x21c: MISSING 0xc1
0x21d: MISSING 0xda
0x21f: MISSING 0xbf
0x220: MISSING 0xd5
0x221: MISSING 0x24
0x222: MISSING 0xc0
0x224: MISSING 0xe3
0x225: MISSING 0xbe
0x226: MISSING 0x2f
0x227: MISSING 0xaa
0x228: V214 = COINBASE
0x229: MISSING 0xaa
0x22a: V215 = CREATE2 S0 S1 S2 S3
0x22b: MISSING 0xf9
0x22c: MISSING 0xf7
0x22d: V216 = ISZERO S0
0x22e: MISSING 0xca
0x22f: LOG S0 S1 S2 S3 S4 S5
0x230: V217 = SDIV S6 S7
0x231: MISSING 0x5e
0x232: V218 = OR S0 S1
0x234: REVERT S15 V218
0x235: V219 = ISZERO S0
0x236: V220 = AND V219 S1
0x237: V221 = 0x5532d6bd0029
---
Entry stack: []
Stack pops: 0
Stack additions: [V213, S3, S1, S2, S0, S15, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S0, V214, V215, V216, V217, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, 0x5532d6bd0029, V220]
Exit stack: []

================================

Function 0:
Public function signature: 0x38af3eed
Entry block: 0x4d
Exit block: 0x60
Body: 0x4d, 0x54, 0x58, 0x60, 0xc9

Function 1:
Public function signature: 0x86d1a69f
Entry block: 0x7c
Exit block: 0x8f
Body: 0x7c, 0x83, 0x87, 0x8f, 0xd8, 0xe6, 0xea, 0x136, 0x13a, 0x143, 0x147, 0x15b, 0x15f, 0x182, 0x19a, 0x1ea, 0x1ee, 0x1f7, 0x1fb, 0x20c, 0x20d

Function 2:
Public function signature: 0xb91d4001
Entry block: 0x91
Exit block: 0xa4
Body: 0x91, 0x98, 0x9c, 0xa4, 0x185

Function 3:
Public function signature: 0xfc0c546a
Entry block: 0xb6
Exit block: 0x60
Body: 0x60, 0xb6, 0xbd, 0xc1, 0x18b

Function 4:
Public fallback function
Entry block: 0x48
Exit block: 0x48
Body: 0x48

