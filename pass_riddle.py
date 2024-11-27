def check_guess(guess, test_code, correct_placed, correct_wrong):
    """
    Check if a guess matches the conditions for a test code
    """
    guess_str = str(guess).zfill(3)
    test_str = str(test_code).zfill(3)
    
    # Create lists to track which positions we've used
    used_guess = [False] * 3
    used_test = [False] * 3
    
    # First pass: Check correct positions
    exact_matches = 0
    for i in range(3):
        if guess_str[i] == test_str[i]:
            exact_matches += 1
            used_guess[i] = True
            used_test[i] = True
    
    # Second pass: Check wrong positions
    wrong_pos_matches = 0
    for i in range(3):
        if not used_guess[i]:
            for j in range(3):
                if not used_test[j] and i != j and guess_str[i] == test_str[j]:
                    wrong_pos_matches += 1
                    used_test[j] = True
                    break
    
    return exact_matches == correct_placed and wrong_pos_matches == correct_wrong

def find_all_passwords():
    # Store all solutions
    solutions = []
    
    # Try all possible 3-digit combinations
    for i in range(1000):
        guess = str(i).zfill(3)
        
        # Check all conditions
        if (check_guess(guess, "682", 1, 0) and    # One number correct and well placed
            check_guess(guess, "614", 0, 1) and    # One number correct but wrongly placed
            check_guess(guess, "206", 0, 2) and    # Two numbers correct but wrongly placed
            check_guess(guess, "738", 0, 0) and    # Nothing is correct
            check_guess(guess, "780", 0, 1)):      # One number correct but wrongly placed
            solutions.append(guess)
    
    return solutions if solutions else ["No solution found"]

# Run the program
solutions = find_all_passwords()
print("All possible passwords:")
for solution in solutions:
    print(solution)