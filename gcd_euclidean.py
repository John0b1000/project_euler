# file: gcd_euclidean.py
'''
This script calculates the greatest common divisor (gcd) of two
integers using the Euclidean algorithm.
'''

# import modules
#
import sys

# class: EuclidGCD
#
class EuclidGCD:
    '''
    This class calculates the greatest common divisor (gcd) of two
    integers using the Euclidean algorithm.
    '''

    # constructor
    #
    def __init__(self) -> None:
        '''This is the constructor.'''

        self.a_in = 0
        self.b_in = 0
        self.dividend = 0
        self.divisor = 0
        self.quotient = 0
        self.remainder = 0
    #
    # end constructor

    # method: calculate
    #
    def calculate(self, a_in: int, b_in: int) -> int:
        '''This method computes the greatest common divisor.'''

        # set data
        #
        self.a_in = abs(int(a_in))
        self.b_in = abs(int(b_in))
        counter = 1

        # check for the zero case
        #
        if (self.a_in == 0) or (self.b_in == 0):
            return max(self.a_in, self.b_in)

        # initialize the algorithm
        #
        self.data_init()

        # perform the Euclidean algorithm to compute the gcd
        #
        self.quotient, self.remainder = self.divide(self.dividend, self.divisor)
        print(f"Line {counter}: {self.dividend} = {self.divisor}({self.quotient}) + {self.remainder}")
        self.dividend = self.divisor
        self.divisor = self.remainder
        while self.remainder != 0:
            self.quotient, self.remainder = self.divide(self.dividend, self.divisor)
            counter = counter + 1
            print(f"Line {counter}: {self.dividend} = {self.divisor}({self.quotient}) + {self.remainder}")
            self.dividend = self.divisor
            self.divisor = self.remainder

        # return the gcd
        #
        return self.dividend
    #
    # end method: calculate

    # method: data_init
    #
    def data_init(self) -> None:
        '''This method ensures all integers are positive
        and sets up the algorithm.'''

        # set data
        #
        self.dividend = max(self.a_in, self.b_in)
        self.divisor = min(self.a_in, self.b_in)
    #
    # end method: data_init

    # method: divide
    #
    def divide(self, a_arg: int, b_arg: int) -> list[int]:
        '''This method performs Euclidean division.'''

        # define variables
        #
        a_d = a_arg
        b_d = b_arg
        q_d = 0

        # perform Euclidean division
        #
        if a_d < b_d:
            return q_d, a_d
        r_d = a_d - b_d
        q_d = q_d + 1
        while r_d > b_d:
            r_d = r_d - b_d
            q_d = q_d + 1

        # return results
        #
        return q_d, r_d
    #
    # end method: divide
#
# end class: EuclidGCD

# function: main
#
def main(argv):
    '''This is the main function.'''

    # compute the gcd using Euclidean algorithm
    #
    gcd = EuclidGCD()
    gcd_result = gcd.calculate(argv[1], argv[2])
    print(f"RESULT: gcd({argv[1]},{argv[2]}) = {gcd_result}")
#
# end function: main

# begin gracefully
#
if __name__ == '__main__':
    main(sys.argv)

#
# end file: gcd_euclidean.py
