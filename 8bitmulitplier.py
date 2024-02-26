# Greyson Willhite
# This program takes two 8 bit binary strings, multiplies them, and returns the product

def dec_to_bin(decNum):
    if decNum == 0:  # checks if input decimal is zero
        return '0'
    binaryString = ''  # initializes empty string
    while decNum > 0:  # loops until number becomes zero
        remDigit = decNum % 2  # computes the remainder
        binaryString = str(remDigit) + binaryString  # adds the remainder to binary string
        decNum //= 2  # divide by 2 and discard remainder
    return binaryString

def binary_mult_8bit(bin_a, bin_b):
    result = 0
    bin_a = int(bin_a, 2)   #convert the input strings into integers
    bin_b = int(bin_b, 2)

    for i in range(8):   #iterate through bits
        if bin_b & (1 << i): #if current bit of bin_b is 1, add bin_a shifted left by i positions
            result += bin_a << i
    return dec_to_bin(result)   #convert integer result back to a binary string and return it as the result


def main():
    test_cases_mult = [   #define test cases
        ('11100110', '10001101'),
        ('11110000', '10101010'),
        ('10011001', '00111011')
    ]

    for bin_a, bin_b in test_cases_mult:    #iterates through test cases and displays results
        product = binary_mult_8bit(bin_a, bin_b)
        print(f"Input: {bin_a}, {bin_b} | Product: {product}")

main()
