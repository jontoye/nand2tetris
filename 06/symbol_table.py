class SymbolTable:
    """Keeps a correspondence between symbolic labels and numeric addresses"""

    def __init__(self):
        self.symbols = {
            'SP': 0,
            'LCL': 1,
            'ARG': 2,
            'THIS': 3,
            'THAT': 4,
            'R0': 0,
            'R1': 1,
            'R2': 2,
            'R3': 3,
            'R4': 4,
            'R5': 5,
            'R6': 6,
            'R7': 7,
            'R8': 8,
            'R9': 9,
            'R10': 10,
            'R11': 11,
            'R12': 12,
            'R13': 13,
            'R14': 14,
            'R15': 15,
            'SCREEN': 16384,
            'KBD': 24576
        }
        self.next_RAM_address = 16

    def add_entry(self, symbol, address):
        self.symbols[symbol] = address

    def contains(self, symbol):
        if symbol in self.symbols:
            return True
        return False

    def get_address(self, symbol):
        return self.symbols[symbol]