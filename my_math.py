# file: my_math.py
'''
This script calculates the greatest common divisor (gcd) of two
integers using the Euclidean algorithm.
'''

# import modules
#
import sys
import numpy as np

# class: MyMath
#
class MyMath:
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
        self.arr_primes = []
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

        # signal to the user that this method has been entered
        #
        print(f"OPERATION: Computing gcd({a_in},{b_in}) using the Euclidean algorithm ...")

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

    # method: find_primes
    #
    def find_primes(self, n_arg: int) -> list[int]:
        '''This method implements the Sieve of Eratosthenes to find all primes not exceeding an integer.'''

        # create an array of True boolean values
        #
        n_arg = int(n_arg)
        arr_nums = np.arange(int(n_arg)+1)
        arr_nums.fill(True)

        # signal to the user that this method has been entered
        #
        print(f"OPERATION: Computing all primes not exceeding {n_arg} ...")

        # check multiples of all integers not exceeding sqrt(n)
        #
        i = 2
        while i*i <= n_arg*n_arg:

            # determine if the current value of i is prime
            #
            if arr_nums[i]:
                for j in range(i*i, n_arg+1, i):
                    arr_nums[j] = False

            # increment the index
            #
            i += 1

        # loop over the array and find all primes less than or equal to n
        #
        count = 1
        for p in range(2, n_arg+1):
            if arr_nums[p]:
                self.arr_primes.append(p)
                print(f'prime #{count} = {p}')
                count += 1

        # return the primes in a list
        #
        return self.arr_primes
    #
    # end method: find_primes

    # method: write_primes
    #
    def write_primes(self, fname:str):
        '''This method writes all primes below a certain value to a text file.'''

        # signal to the user that this method has been entered
        #
        print(f"OPERATION: Writing computed primes list to a text file: {fname}")

        # open the file in write mode
        #
        f = open(fname, 'w', encoding='utf8')

        # write the primes line by line
        #
        for i,p in enumerate(self.arr_primes):
            f.write(f'prime #{i} = {p}\n')

        # close the file
        #
        f.close()
#
# end class: MyMath

# function: main
#
def main(argv):
    '''This is the main function.'''

    # compute the gcd using Euclidean algorithm
    #
    math = MyMath()
    gcd_result = math.calculate(argv[1], argv[2])
    print(f"RESULT: gcd({argv[1]},{argv[2]}) = {gcd_result}")

    # compute all primes less than or equal to n and write to a text file
    #
    math.find_primes(argv[3])
    math.write_primes(argv[4])
#
# end function: main

# begin gracefully
#
if __name__ == '__main__':
    main(sys.argv)

#
# end file: my_math.py
