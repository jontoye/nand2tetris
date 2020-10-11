import sys
import parser
import code
import symbol_table


def main():
    # Get input file
    if len(sys.argv) != 2:
        print("Usage: assembler.py Prog.asm")
        sys.exit(1)
    file = sys.argv[1]

    # Create output file
    output = open(file.replace('.asm', '.hack'), 'w')

    # Parse input file, removes comments and whitespace
    parsed_code = parser.Parse(file)

    # Initialize symbol table
    lookup = symbol_table.SymbolTable()

    # 1st pass to build symbol table
    while parsed_code.has_more_commands:
        command = parsed_code.command_type()
        symbol = parsed_code.symbol()
        if command == 'L_COMMAND':
            lookup.add_entry(symbol, parsed_code.next_ROM_address)
        else:
            parsed_code.next_ROM_address += 1
        parsed_code.advance()
    parsed_code.reset()

    # 2nd pass to translate symbols
    while parsed_code.has_more_commands:
        command = parsed_code.command_type()
        symbol = parsed_code.symbol()
        if command == 'C_COMMAND':
            binary_c = code.c_to_binary(
                parsed_code.dest(), parsed_code.comp(), parsed_code.jump())
            output.write(binary_c)

        elif command == 'A_COMMAND':
            if not symbol.isnumeric():
                if not lookup.contains(symbol):
                    lookup.add_entry(symbol, lookup.next_RAM_address)
                    lookup.next_RAM_address += 1
                symbol = lookup.get_address(symbol)
            binary_a = code.a_to_binary(symbol)
            output.write(binary_a)
        parsed_code.advance()

    output.close()


if __name__ == '__main__':
    main()
