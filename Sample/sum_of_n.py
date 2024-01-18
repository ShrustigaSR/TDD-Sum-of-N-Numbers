from dataclasses import dataclass
import logging

@dataclass
class SumOfNNumbers:
    N : eval

    def validate_input(self):
        if isinstance(self.N,(float,str)):
            raise ValueError("Enter Positive Integer")
        if self.N<0:
            raise ValueError("Enter Positive Integer")
    def calculate_sum(self):
        #Testcases
        '''Ensures that input N is integer'''
        try:
            self.validate_input()
            if self.N==0:
                return 0
            else:
                return self.N*(self.N+1)/2
        except ValueError as e:
            raise
        

        
