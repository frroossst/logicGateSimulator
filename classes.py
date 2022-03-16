class Gate():

    def __init__(self,i1,i2):
        self.i1 = i1
        self.i2 = i2

    def output(self,gate_type):
        if gate_type == "and":
            out = self.i1 and self.i2

        elif gate_type == "or":
            out = self.i1 or self.i2

        elif gate_type == "not":

            if isinstance(self.i1,int) and isinstance(self.i2,int):
                raise ValueError ("not gate cannot have two inputs")
            else:
                if isinstance(self.i1,int):
                    out = not self.i1
                elif isinstance(self.i2,int):
                    out = not self.i2
        elif gate_type == "nor":
            pass

        elif gate_type == "nand": 
            pass

        elif game_type == "xor":
            pass

        elif game_type == "xnor":
            pass

        return out

class andGate(Gate):

    def __init__(self):
        Gate.__init__(self,i1,i2)
        print(self.i1)

a = andGate(1,1)
