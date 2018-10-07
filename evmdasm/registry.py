#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author : <github.com/tintinweb>
from .instructions import Instruction
from .instruction_registry import InstructionRegistry
from . import argtypes as T

INSTRUCTIONS = [
    # Stop and Arithmetic Operations
    Instruction(opcode=0x00, name='STOP', category="terminate", gas=0, description="Halts execution."),
    Instruction(opcode=0x01, name='ADD', category="arithmetic", gas=3, description="Addition operation.", args=[T.Value('a'), T.Value('b')], returns=[T.Value('result')]),
    Instruction(opcode=0x02, name='MUL', category="arithmetic", gas=5, description="Multiplication operation.", args=[T.Value('a'), T.Value('b')], returns=[T.Value('result')]),
    Instruction(opcode=0x03, name='SUB', category="arithmetic", gas=3, description="Subtraction operation.", args=[T.Value('a'), T.Value('b')], returns=[T.Value('result')]),
    Instruction(opcode=0x04, name='DIV', category="arithmetic", gas=5, description="Integer division operation.", args=[T.Value('a'), T.Value('b')], returns=[T.Value('result')]),
    Instruction(opcode=0x05, name='SDIV', category="arithmetic", gas=5, description="Signed integer", args=[T.Value('a'), T.Value('b')], returns=[T.Value('result')]),
    Instruction(opcode=0x06, name='MOD', category="arithmetic", gas=5, description="Modulo", args=[T.Value('a'), T.Value('b')], returns=[T.Value('result')]),
    Instruction(opcode=0x07, name='SMOD', category="arithmetic", gas=5, description="Signed modulo", args=[T.Value('a'), T.Value('b')], returns=[T.Value('result')]),
    Instruction(opcode=0x08, name='ADDMOD', category="arithmetic", gas=8, description="Modulo addition operation", args=[T.Value('a'), T.Value('b'), T.Value('mod')], returns=[T.Value('result')]),
    Instruction(opcode=0x09, name='MULMOD', category="arithmetic", gas=8, description="Modulo multiplication operation", args=[T.Value('a'), T.Value('b'), T.Value('mod')], returns=[T.Value('result')]),
    Instruction(opcode=0x0a, name='EXP', category="arithmetic", gas=10, description="Exponential operation.", args=[T.Value('base'), T.Value('exponent')], returns=['result']),
    Instruction(opcode=0x0b, name='SIGNEXTEND', category="arithmetic", gas=5, description="Extend length of two's complement signed integer.", args=[T.Value('bits'), T.Value('num')], returns=[T.Value('result')]),

    # Comparison & Bitwise Logic Operations
    Instruction(opcode=0x10, name='LT', category="comparison", gas=3, description="Lesser-than comparison", args=[T.Value('a'), T.Value('b')], returns=[T.Bool('flag')]),
    Instruction(opcode=0x11, name='GT', category="comparison", gas=3, description="Greater-than comparison", args=[T.Value('a'), T.Value('b')], returns=[T.Bool('flag')]),
    Instruction(opcode=0x12, name='SLT', category="comparison", gas=3, description="Signed less-than comparison", args=[T.Value('a'), T.Value('b')], returns=[T.Bool('flag')]),
    Instruction(opcode=0x13, name='SGT', category="comparison", gas=3, description="Signed greater-than comparison", args=[T.Value('a'), T.Value('b')], returns=[T.Bool('flag')]),
    Instruction(opcode=0x14, name='EQ', category="comparison", gas=3, description="Equality  comparison", args=[T.Value('a'), T.Value('b')], returns=[T.Bool('flag')]),
    Instruction(opcode=0x15, name='ISZERO', category="comparison",  gas=3, description="Simple not operator", args=[T.Value('a')], returns=[T.Bool('flag')]),
    Instruction(opcode=0x16, name='AND', category="bitwise-logic",  gas=3, description="Bitwise AND operation.", args=[T.Value('a'), T.Value('b')], returns=[T.Value('result')]),
    Instruction(opcode=0x17, name='OR', category="bitwise-logic",gas=3, description="Bitwise OR operation.", args=[T.Value('a'), T.Value('b')], returns=[T.Value('result')]),
    Instruction(opcode=0x18, name='XOR', category="bitwise-logic",gas=3, description="Bitwise XOR operation.", args=[T.Value('a'), T.Value('b')], returns=[T.Value('result')]),
    Instruction(opcode=0x19, name='NOT', category="bitwise-logic",gas=3, description="Bitwise NOT operation.", args=[T.Value('a'), T.Value('b')], returns=[T.Value('result')]),
    Instruction(opcode=0x1a, name='BYTE', category="bitwise-logic",gas=3, description="Retrieve single byte from word", args=[T.Index32('th'), T.Word('value')], returns=[T.Byte('byte')]),
    Instruction(opcode=0x1b, name='SHL', category="bitwise-logic", gas=3, fork="constantinople", description="<TBD> Shift left", args=[T.Index64('shift'), T.Value('value')], returns=[T.Value('result')]),
    Instruction(opcode=0x1c, name='SHR', category="bitwise-logic", gas=3, fork="constantinople", description="<TBD> Shift Right", args=[T.Index64('shift'), T.Value('value')], returns=[T.Value('result')]),
    Instruction(opcode=0x1d, name='SAR', category="bitwise-logic", gas=3, fork="constantinople", description="<TBD> Shift arithmetic right", args=[T.Index64('shift'), T.Value('value')], returns=[T.Bool('flag')]),

    # SHA3
    Instruction(opcode=0x20, name='SHA3', category="cryptographic", gas=30, description="Compute Keccak-256 hash.", args=[T.MemOffset('offset'), T.Length('size')], returns=[T.Value('sha3')]),

    # Environmental Information
    Instruction(opcode=0x30, name='ADDRESS', category="envinfo", gas=2, description="Get address of currently executing account.", returns=[T.Address('this.address')]),
    Instruction(opcode=0x31, name='BALANCE', category="envinfo", gas=20, description="Get balance of the given account.", args=[T.Address("address")], returns=[T.Value("this.balance")]),
    Instruction(opcode=0x32, name='ORIGIN', category="envinfo", gas=2, description="Get execution origination address.", returns=[T.Address("tx.origin")]),
    Instruction(opcode=0x33, name='CALLER', category="envinfo", gas=2, description="Get caller address.This is the address of the account that is directly responsible for this execution.", returns=[T.Address("msg.sender")]),
    Instruction(opcode=0x34, name='CALLVALUE', category="envinfo", gas=2, description="Get deposited value by the instruction/transaction responsible for this execution.", returns=[T.CallValue("msg.value")]),
    Instruction(opcode=0x35, name='CALLDATALOAD', category="envinfo", gas=3, description="Get input data of current environment.", args=[T.MemOffset('dataOffset')], returns=[T.Data("msg.data")]),
    Instruction(opcode=0x36, name='CALLDATASIZE', category="envinfo", gas=2, description="Get size of input data in current environment.", returns=[T.Length("msg.data.length")]),
    Instruction(opcode=0x37, name='CALLDATACOPY', category="envinfo", gas=3, description="Copy input data in current environment to memory. This pertains to the input data passed with the message call instruction or transaction.", args=[T.MemOffset("memOffset"), T.MemOffset("dataOffset"), T.Length("length")]),
    Instruction(opcode=0x38, name='CODESIZE', category="envinfo", gas=2, description="Get size of code running in current environment.", returns=[T.Length("codesize")]),
    Instruction(opcode=0x39, name='CODECOPY', category="envinfo", gas=3, description="Copy code running in current environment to memory.", args=[T.MemOffset("memOffset"), T.MemOffset("codeOffset"), T.Length("length")]),
    Instruction(opcode=0x3a, name='GASPRICE', category="envinfo", gas=2, description="Get price of gas in current environment.", returns=[T.Gas("tx.gasprice")]),
    Instruction(opcode=0x3b, name='EXTCODESIZE', category="envinfo", gas=20, description="Get size of an account's code.", args=[T.Address('address')], returns=["extcodesize"]),
    Instruction(opcode=0x3c, name='EXTCODECOPY', category="envinfo", gas=20, description="Copy an account's code to memory.", args=[T.Address("address"), T.MemOffset("memOffset"), T.MemOffset("codeOffset"), T.Length("length")]),
    Instruction(opcode=0x3d, name='RETURNDATASIZE', category="envinfo", gas=2, description="Push the size of the return data buffer onto the stack.", returns=["returndatasize"]),
    Instruction(opcode=0x3e, name='RETURNDATACOPY', category="envinfo", gas=3, description="Copy data from the return data buffer.", args=[T.MemOffset("memOffset"), T.MemOffset("dataOffset"), T.Length("length")]),
    Instruction(opcode=0x3f, name='EXTCODEHASH', category="envinfo", gas=400, fork="constantinople", description="<TBD> - Constantinople", args=[T.Address("address")]),


    # Block Information
    Instruction(opcode=0x40, name='BLOCKHASH', category="blockinfo", gas=20, description="Get the hash of one of the 256 most recent complete blocks.", args=[T.Index256("num")], returns=["block.blockhash"]),
    Instruction(opcode=0x41, name='COINBASE', category="blockinfo", gas=2, description="Get the block's beneficiary address.", returns=[T.Address("block.coinbase")]),
    Instruction(opcode=0x42, name='TIMESTAMP', category="blockinfo", gas=2, description="Get the block's timestamp.", returns=[T.Timestamp("block.timestamp")]),
    Instruction(opcode=0x43, name='NUMBER', category="blockinfo", gas=2, description="Get the block's number.", returns=[T.Value("block.number")]),
    Instruction(opcode=0x44, name='DIFFICULTY', category="blockinfo", gas=2, description="Get the block's difficulty.", returns=[T.Value("block.difficulty")]),
    Instruction(opcode=0x45, name='GASLIMIT', category="blockinfo", gas=2, description="Get the block's gas limit.", returns=[T.Gas("block.gaslimit")]),

    # Stack, Memory, Storage and Flow Operations
    Instruction(opcode=0x50, name='POP', category="stack", gas=2, description="Remove item from stack.", args=[T.Internal("#dummy")], ),
    # dummy is only there to indicate that there is a pop()
    Instruction(opcode=0x51, name='MLOAD', category="memory", gas=3, description="Load word from memory.", args=[T.MemOffset("offset")]),
    Instruction(opcode=0x52, name='MSTORE', category="memory", gas=3, description="Save word to memory.", args=[T.MemOffset("offset"),T.Word("value")]),
    Instruction(opcode=0x53, name='MSTORE8', category="memory", gas=3, description="Save byte to memory.", args=[T.MemOffset("offset"),T.Byte("value")]),
    Instruction(opcode=0x54, name='SLOAD', category="storage", gas=50, description="Load word from storage.", args=[T.MemOffset("loc")], returns=["value"]),
    Instruction(opcode=0x55, name='SSTORE', category="storage", gas=0, description="Save word to storage.", args=[T.MemOffset("loc"), T.Word("value")]),
    Instruction(opcode=0x56, name='JUMP', category="controlflow", gas=8, description="Alter the program counter.", args=[T.Label("evm.pc")]),
    Instruction(opcode=0x57, name='JUMPI', category="controlflow", gas=10, description="Conditionally alter the program counter.", args=[T.Label("evm.pc"), T.Bool("condition")]),
    Instruction(opcode=0x58, name='PC', category="info", gas=2, description="Get the value of the program counter prior to the increment.", returns=[T.Label("evm.pc")]),
    Instruction(opcode=0x59, name='MSIZE', category="memory", gas=2, description="Get the size of active memory in bytes.", returns=[T.Length("memory.length")]),
    Instruction(opcode=0x5a, name='GAS', category="info", gas=2, description="Get the amount of available gas, including the corresponding reduction", returns=[T.Gas("gasleft")]),
    Instruction(opcode=0x5b, name='JUMPDEST', category="label", gas=1, description="Mark a valid destination for jumps."),

    # Stack Push Operations
    Instruction(opcode=0x60, name='PUSH1', category="stack", gas=3, length_of_operand=0x1, description="Place 1 byte item on stack.", returns=[T.Value("item")]),
    Instruction(opcode=0x61, name='PUSH2', category="stack", gas=3, length_of_operand=0x2, description="Place 2-byte item on stack.", returns=[T.Value("item")]),
    Instruction(opcode=0x62, name='PUSH3', category="stack",  gas=3, length_of_operand=0x3, description="Place 3-byte item on stack.", returns=[T.Value("item")]),
    Instruction(opcode=0x63, name='PUSH4', category="stack", gas=3, length_of_operand=0x4, description="Place 4-byte item on stack.", returns=[T.Value("item")]),
    Instruction(opcode=0x64, name='PUSH5', category="stack", gas=3, length_of_operand=0x5, description="Place 5-byte item on stack.", returns=[T.Value("item")]),
    Instruction(opcode=0x65, name='PUSH6', category="stack", gas=3, length_of_operand=0x6, description="Place 6-byte item on stack.", returns=[T.Value("item")]),
    Instruction(opcode=0x66, name='PUSH7', category="stack", gas=3, length_of_operand=0x7, description="Place 7-byte item on stack.", returns=[T.Value("item")]),
    Instruction(opcode=0x67, name='PUSH8', category="stack", gas=3, length_of_operand=0x8, description="Place 8-byte item on stack.", returns=[T.Value("item")]),
    Instruction(opcode=0x68, name='PUSH9', category="stack", gas=3, length_of_operand=0x9, description="Place 9-byte item on stack.", returns=[T.Value("item")]),
    Instruction(opcode=0x69, name='PUSH10', category="stack", gas=3, length_of_operand=0xa, description="Place 10-byte item on stack.", returns=[T.Value("item")]),
    Instruction(opcode=0x6a, name='PUSH11', category="stack", gas=3, length_of_operand=0xb, description="Place 11-byte item on stack.", returns=[T.Value("item")]),
    Instruction(opcode=0x6b, name='PUSH12', category="stack", gas=3, length_of_operand=0xc, description="Place 12-byte item on stack.", returns=[T.Value("item")]),
    Instruction(opcode=0x6c, name='PUSH13', category="stack", gas=3, length_of_operand=0xd, description="Place 13-byte item on stack.", returns=[T.Value("item")]),
    Instruction(opcode=0x6d, name='PUSH14', category="stack", gas=3, length_of_operand=0xe, description="Place 14-byte item on stack.", returns=[T.Value("item")]),
    Instruction(opcode=0x6e, name='PUSH15', category="stack", gas=3, length_of_operand=0xf, description="Place 15-byte item on stack.", returns=[T.Value("item")]),
    Instruction(opcode=0x6f, name='PUSH16', category="stack", gas=3, length_of_operand=0x10, description="Place 16-byte item on stack.", returns=[T.Value("item")]),
    Instruction(opcode=0x70, name='PUSH17', category="stack", gas=3, length_of_operand=0x11, description="Place 17-byte item on stack.", returns=[T.Value("item")]),
    Instruction(opcode=0x71, name='PUSH18', category="stack", gas=3, length_of_operand=0x12, description="Place 18-byte item on stack.", returns=[T.Value("item")]),
    Instruction(opcode=0x72, name='PUSH19', category="stack", gas=3, length_of_operand=0x13, description="Place 19-byte item on stack.", returns=[T.Value("item")]),
    Instruction(opcode=0x73, name='PUSH20', category="stack", gas=3, length_of_operand=0x14, description="Place 20-byte item on stack.", returns=[T.Value("item")]),
    Instruction(opcode=0x74, name='PUSH21', category="stack", gas=3, length_of_operand=0x15, description="Place 21-byte item on stack.", returns=[T.Value("item")]),
    Instruction(opcode=0x75, name='PUSH22', category="stack", gas=3, length_of_operand=0x16, description="Place 22-byte item on stack.", returns=[T.Value("item")]),
    Instruction(opcode=0x76, name='PUSH23', category="stack", gas=3, length_of_operand=0x17, description="Place 23-byte item on stack.", returns=[T.Value("item")]),
    Instruction(opcode=0x77, name='PUSH24', category="stack", gas=3, length_of_operand=0x18, description="Place 24-byte item on stack.", returns=[T.Value("item")]),
    Instruction(opcode=0x78, name='PUSH25', category="stack", gas=3, length_of_operand=0x19, description="Place 25-byte item on stack.", returns=[T.Value("item")]),
    Instruction(opcode=0x79, name='PUSH26', category="stack", gas=3, length_of_operand=0x1a, description="Place 26-byte item on stack.", returns=[T.Value("item")]),
    Instruction(opcode=0x7a, name='PUSH27', category="stack", gas=3, length_of_operand=0x1b, description="Place 27-byte item on stack.", returns=[T.Value("item")]),
    Instruction(opcode=0x7b, name='PUSH28', category="stack", gas=3, length_of_operand=0x1c, description="Place 28-byte item on stack.", returns=[T.Value("item")]),
    Instruction(opcode=0x7c, name='PUSH29', category="stack", gas=3, length_of_operand=0x1d, description="Place 29-byte item on stack.", returns=[T.Value("item")]),
    Instruction(opcode=0x7d, name='PUSH30', category="stack", gas=3, length_of_operand=0x1e, description="Place 30-byte item on stack.", returns=[T.Value("item")]),
    Instruction(opcode=0x7e, name='PUSH31', category="stack", gas=3, length_of_operand=0x1f, description="Place 31-byte item on stack.", returns=[T.Value("item")]),
    Instruction(opcode=0x7f, name='PUSH32', category="stack", gas=3, length_of_operand=0x20, description="Place 32-byte (full word) item on stack.", returns=[T.Value("item")]),

    # Duplication Operations
    Instruction(opcode=0x80, name='DUP1', category="stack", gas=3, pops=1, pushes=2, description="Duplicate 1st stack item."),
    Instruction(opcode=0x81, name='DUP2', category="stack", gas=3, pops=2, pushes=3, description="Duplicate 2nd stack item."),
    Instruction(opcode=0x82, name='DUP3', category="stack", gas=3, pops=3, pushes=4, description="Duplicate 3rd stack item."),
    Instruction(opcode=0x83, name='DUP4', category="stack", gas=3, pops=4, pushes=5, description="Duplicate 4th stack item."),
    Instruction(opcode=0x84, name='DUP5', category="stack", gas=3, pops=5, pushes=6, description="Duplicate 5th stack item."),
    Instruction(opcode=0x85, name='DUP6', category="stack", gas=3, pops=6, pushes=7, description="Duplicate 6th stack item."),
    Instruction(opcode=0x86, name='DUP7', category="stack", gas=3, pops=7, pushes=8, description="Duplicate 7th stack item."),
    Instruction(opcode=0x87, name='DUP8', category="stack", gas=3, pops=8, pushes=9, description="Duplicate 8th stack item."),
    Instruction(opcode=0x88, name='DUP9', category="stack", gas=3, pops=9, pushes=10, description="Duplicate 9th stack item."),
    Instruction(opcode=0x89, name='DUP10', category="stack", gas=3, pops=10, pushes=11, description="Duplicate 10th stack item."),
    Instruction(opcode=0x8a, name='DUP11', category="stack", gas=3, pops=11, pushes=12, description="Duplicate 11th stack item."),
    Instruction(opcode=0x8b, name='DUP12', category="stack", gas=3, pops=12, pushes=13, description="Duplicate 12th stack item."),
    Instruction(opcode=0x8c, name='DUP13', category="stack", gas=3, pops=13, pushes=14, description="Duplicate 13th stack item."),
    Instruction(opcode=0x8d, name='DUP14', category="stack", gas=3, pops=14, pushes=15, description="Duplicate 14th stack item."),
    Instruction(opcode=0x8e, name='DUP15', category="stack", gas=3, pops=15, pushes=16, description="Duplicate 15th stack item."),
    Instruction(opcode=0x8f, name='DUP16', category="stack", gas=3, pops=16, pushes=17, description="Duplicate 16th stack item."),

    # Exchange Operations
    Instruction(opcode=0x90, name='SWAP1', category="stack", gas=3, pops=2, pushes=2, description="Exchange 1st and 2nd stack items."),
    Instruction(opcode=0x91, name='SWAP2', category="stack", gas=3, pops=3, pushes=3, description="Exchange 1st and 3rd stack items."),
    Instruction(opcode=0x92, name='SWAP3', category="stack", gas=3, pops=4, pushes=3, description="Exchange 1st and 4th stack items."),
    Instruction(opcode=0x93, name='SWAP4', category="stack", gas=3, pops=5, pushes=4, description="Exchange 1st and 5th stack items."),
    Instruction(opcode=0x94, name='SWAP5', category="stack", gas=3, pops=6, pushes=5, description="Exchange 1st and 6th stack items."),
    Instruction(opcode=0x95, name='SWAP6', category="stack", gas=3, pops=7, pushes=6, description="Exchange 1st and 7th stack items."),
    Instruction(opcode=0x96, name='SWAP7', category="stack", gas=3, pops=8, pushes=7, description="Exchange 1st and 8th stack items."),
    Instruction(opcode=0x97, name='SWAP8', category="stack", gas=3, pops=9, pushes=9, description="Exchange 1st and 9th stack items."),
    Instruction(opcode=0x98, name='SWAP9', category="stack", gas=3, pops=10, pushes=10, description="Exchange 1st and 10th stack items."),
    Instruction(opcode=0x99, name='SWAP10', category="stack", gas=3, pops=11, pushes=11, description="Exchange 1st and 11th stack items."),
    Instruction(opcode=0x9a, name='SWAP11', category="stack", gas=3, pops=12, pushes=12, description="Exchange 1st and 12th stack items."),
    Instruction(opcode=0x9b, name='SWAP12', category="stack", gas=3, pops=13, pushes=13, description="Exchange 1st and 13th stack items."),
    Instruction(opcode=0x9c, name='SWAP13', category="stack", gas=3, pops=14, pushes=14, description="Exchange 1st and 14th stack items."),
    Instruction(opcode=0x9d, name='SWAP14', category="stack", gas=3, pops=15, pushes=15, description="Exchange 1st and 15th stack items."),
    Instruction(opcode=0x9e, name='SWAP15', category="stack", gas=3, pops=16, pushes=16, description="Exchange 1st and 16th stack items."),
    Instruction(opcode=0x9f, name='SWAP16', category="stack", gas=3, pops=17, pushes=17, description="Exchange 1st and 17th stack items."),

    # Logging Operations
    Instruction(opcode=0xa0, name='LOG0', category="event", gas=375,  description="Append log record with no topics.", args=[T.MemOffset("start"), T.Length("size")]),
    Instruction(opcode=0xa1, name='LOG1', category="event", gas=750,  description="Append log record with one topic.", args=[T.MemOffset("start"), T.Length("size"), T.Value("topic1")]),
    Instruction(opcode=0xa2, name='LOG2', category="event", gas=1125,  description="Append log record with two topics.", args=[T.MemOffset("start"), T.Length("size"), T.Value("topic1"), T.Value("topic2")]),
    Instruction(opcode=0xa3, name='LOG3', category="event", gas=1500,  description="Append log record with three topics.", args=[T.MemOffset("start"), T.Length("size"), T.Value("topic1"), T.Value("topic2"), T.Value("topic3")]),
    Instruction(opcode=0xa4, name='LOG4', category="event", gas=1875, description="Append log record with four topics.", args=[T.MemOffset("start"), T.Length("size"), T.Value("topic1"), T.Value("topic2"), T.Value("topic3"), T.Value("topic4")]),

    # unofficial opcodes used for parsing.
    Instruction(opcode=0xb0, name='UNOFFICIAL_PUSH', category="unofficial", description="unofficial opcodes used for parsing."),
    Instruction(opcode=0xb1, name='UNOFFICIAL_DUP', category="unofficial", description="unofficial opcodes used for parsing."),
    Instruction(opcode=0xb2, name='UNOFFICIAL_SWAP', category="unofficial", description="unofficial opcodes used for parsing."),

    # System Operations
    Instruction(opcode=0xf0, name='CREATE', category="system", gas=32000, description="Create a new account with associated code.", args=[T.CallValue("value"), T.MemOffset("offset"), T.Length("size")]),
    Instruction(opcode=0xf1, name='CALL', category="system", gas=40, description="Message-call into an account.", args=[T.Gas("gas"), T.Address("address"), T.CallValue("value"), T.MemOffset("inOffset"), T.Length("inSize"), T.MemOffset("retOffset"), T.Length("retSize")]),
    Instruction(opcode=0xf2, name='CALLCODE', category="system", gas=40, description="Message-call into this account with alternative account's code.", args=[T.Gas("gas"), T.Address("address"), T.CallValue("value"), T.MemOffset("inOffset"), T.Length("inSize"), T.MemOffset("retOffset"), T.Length("retSize")]),
    Instruction(opcode=0xf3, name='RETURN', category="terminate", gas=0, description="Halt execution returning output data.", args=[T.MemOffset("offset"), T.Length("size")]),
    Instruction(opcode=0xf4, name='DELEGATECALL', category="system", gas=40, description="Similar to CALLCODE except that it propagates the sender and value from the parent scope to the child scope", args=[T.Gas("gas"), T.Address("address"), T.MemOffset("inOffset"), T.Length("inSize"), T.MemOffset("retOffset"), T.Length("retSize")]),
    Instruction(opcode=0xf5, name='CREATE2', category="system", gas=32000, fork="constantinople", description="Create a new account with associated code. (Constantinople)", args=[T.Value("endowment"), T.MemOffset("offset"), T.Length("size"), T.Value("salt")]),

    # Newer opcode
    Instruction(opcode=0xfa, name='STATICCALL', category="system", gas=40, description='Call another contract (or itself) while disallowing any modifications to the state during the call.', args=[T.Gas("gas"), T.Address("address"), T.MemOffset("inOffset"), T.Length("inSize"), T.MemOffset("retOffset"), T.Length("retSize")]),
    Instruction(opcode=0xfd, name='REVERT', category="terminate", gas=0, description='throw an error', args=[T.MemOffset("offset"), T.Length("size")]),

    # Halt Execution, Mark for deletion
    Instruction(opcode=0xff, name='SELFDESTRUCT', category="terminate", gas=0, description="Halt execution and register account for later deletion.", args=[T.Address("address")]),
]

'''
/////////////////////////////////////////////////
//
// Here be dragons. Thou art forewarned
//
//
TODO: deduplicate the interfaces
'''

# offer an InstructionRegistry using the default instructions.Instruction
registry = InstructionRegistry(instructions=INSTRUCTIONS)

# rebuild the registry with our extended Instruction class. (clone with our class as template)
INSTRUCTIONS_BY_OPCODE = registry.by_opcode
INSTRUCTIONS_BY_NAME = registry.by_name
INSTRUCTIONS_BY_CATEGORY = registry.by_category
instruction = registry.instruction
INSTRUCTION_MARKS_BASICBLOCK_END = registry.instruction_marks_basicblock_end
create_instruction = registry.create_instruction




