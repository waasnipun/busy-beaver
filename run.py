import sys


class BusyBeaverTuringMachine:
    def __init__(self, program, init_state, halt, blank_symbol):
        self.program = program
        self.halt = halt
        self.tape_value = blank_symbol
        self.tape = [blank_symbol]
        self.time = 0
        self.ones = 0
        self.pos = 0
        self.state = init_state
        self.move_dir = ""
        self.blank_symbol = blank_symbol

    def run_machine(self):
        while self.state != self.halt:
            self.update_state()
            self.write_tape()
            self.move_head()

    def write_tape(self):
        self.ones += (self.tape_value-self.tape[self.pos])
        self.tape[self.pos] = int(self.tape_value)

    def move_head(self):
        if self.move_dir == "R":
            self.pos += 1
        elif self.move_dir == "L":
            self.pos -= 1
        else:
            raise ("Unknown move %s " % self.move_dir)

        if self.pos < 0:
            self.tape.insert(0, self.blank_symbol)
            self.pos = 0
        if self.pos >= len(self.tape):
            self.tape.append(self.blank_symbol)

        self.time += 1

    def update_state(self):
        tape_value, self.move_dir, self.state = self.program[self.state + str(self.tape[self.pos])]
        self.tape_value = int(tape_value)



busy_beaver_programs = [{},
                        {},
                        {"A0": "1RB", "A1": "1LB", "B0": "1LA", "B1": "1RH"},
                        {"A0": "1RB", "A1": "1RH", "B0": "0RC", "B1": "1RB", "C0": "1LC", "C1": "1LA"},
                        {"A0": "1RB", "A1": "1LB", "B0": "1LA", "B1": "0LC", "C0": "1RH", "C1": "1LD", "D0": "1RD",
                         "D1": "0RA"},
                        {"A0": "1RB", "A1": "1LC", "B0": "1RC", "B1": "1RB", "C0": "1RD", "C1": "0LE", "D0": "1LA",
                         "D1": "1LD", "E0": "1RH", "E1": "0LA"}
                        ]


def busy_beaver(n):
    program = busy_beaver_programs[n]
    print("Running Busy Beaver")
    turing_machine = BusyBeaverTuringMachine(program, "A", "H", 0)
    turing_machine.run_machine()

    print("Busy Beaver finished in %d steps(s(m))", turing_machine.time)
    print("Busy Beaver has %d number of non-blank symbols(Sigma(m))", turing_machine.ones)

def usage():
    print("Running Busy beaver for 1 or 2 or 3 or 4 or 5 or 6 states.")


if __name__ == '__main__':
    if len(sys.argv[1:]) < 1:
        usage()
        sys.exit(0)
    n = int(sys.argv[1])
    if n > 6 or n < 1:
        print("Busy beaver state must be between 1 and 6 inclusive")
        sys.exit(0)
    busy_beaver(n)
