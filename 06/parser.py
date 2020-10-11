class Parse:
    """Reads an assembly language file, parses it, and provides access to each lines components (fields and symbols). Also removes all white space and comments """
    current_command = None
    has_more_commands = True

    def __init__(self, file):
        self.file = file
        with open(file) as f:
            lines = (remove_comments(line, '/') for line in f)
            lines = (line.rstrip().replace(' ', '') for line in lines)
            self.lines = list(line for line in lines if line)
            self.current_command = 0
            self.next_ROM_address = 0

    # reset state
    def reset(self):
        self.current_command = 0
        self.has_more_commands = True

    # advances current command to next line of code
    def advance(self):
        self.current_command += 1
        if self.current_command >= len(self.lines):
            self.has_more_commands = False

    # returns the type of the current command --> A_COMMAND, C_COMMAND, or L_COMMAND
    def command_type(self):
        if self.lines[self.current_command][0] == '@':
            return 'A_COMMAND'
        elif self.lines[self.current_command][0] == '(':
            return 'L_COMMAND'
        else:
            return 'C_COMMAND'

    # if A_COMMAND or L_COMMAND --> return the symbol or decimal of the current command
    def symbol(self):
        if self.command_type() == 'A_COMMAND':
            return self.lines[self.current_command][1:]
        elif self.command_type() == 'L_COMMAND':
            return self.lines[self.current_command][1:-1]

    # if C_COMMAND --> returns the dest mnemonic in the current C-command
    def dest(self):
        if self.command_type() == 'C_COMMAND':
            i = self.lines[self.current_command].find('=')
            if i >= 0:
                return self.lines[self.current_command][:i]

    # if C_COMMAND --> returns the comp mnemonic in the current C-command
    def comp(self):
        if self.command_type() == 'C_COMMAND':
            i = self.lines[self.current_command].find('=')
            if i >= 0:
                return self.lines[self.current_command][i+1:]
            j = self.lines[self.current_command].find(';')
            if j >= 0:
                return self.lines[self.current_command][:j]

    # if C_COMMAND --> returns the jump mnemonic in the current C-command
    def jump(self):
        if self.command_type() == 'C_COMMAND':
            i = self.lines[self.current_command].find(';')
            if i >= 0:
                return self.lines[self.current_command][i+1:]


# FUNCTION - remove comments from a line
def remove_comments(line, sep):
    i = line.find(sep)
    if i >= 0 and line[i+1] == sep:
        line = line[:i]
    return line.strip()
