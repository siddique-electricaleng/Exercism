def check_olympiad_date (num_digits,*arg:int) -> int :
    n_zero, n_one, n_two, n_three, n_five = 0, 0, 0, 0, 0
    digits_read = 0
    req_zero, req_one, req_two, req_three, req_five = 3, 1, 2, 1, 1
    for digit in arg:
        if(digit == 0):
            n_zero +=1
        elif(digit == 1):
            n_one +=1
        elif(digit == 2):
            n_two +=1
        elif (digit == 3):
            n_three +=1
        elif (digit == 5):
            n_five += 1

        digits_read += 1
        """ 
        print("------------------------------")
        print(f"Digits Read: {digits_read}, Zeroes: {n_zero}, Ones: {n_one}, Twos:{n_two}, Threes: {n_three}, Fives: {n_five}")
        print(f"Needed, Zeroes: {req_zero}, Ones: {req_one}, Twos:{req_two}, Threes: {req_three}, Fives: {req_five}")
        """
        if req_zero <= n_zero and req_one <= n_one and req_two <= n_two and req_three <= n_three and req_five <= n_five:
            if (digits_read <= num_digits):
                return digits_read
        elif digits_read == num_digits:
            return 0
        
dig_needed = check_olympiad_date(10, 2, 0, 1, 2, 3, 2, 5, 0, 0, 1)
print(dig_needed)