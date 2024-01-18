# Test Driven Development

## Problem Statement : Sum of N numbers
This Problem provides a solution to calculate the sum of a range of numbers based on user input, using Test Driven Development methodology.

### User Stories

1. **As a user**, I want to calculate the sum of the provided numbers so that I can add a small set of numbers.
    - **Acceptance Criteria:**
        - When I input '3', I should get the output '6'.

2. **As a user**, I want to calculate the sum of a large set of numbers so that I can quickly get their sum.
    - **Acceptance Criteria:**
        - When I input the '100', the program should give the output quickly.

3. **As a user**, I want to be able to handle the case of a non-number input so that I can handle the case of a Value error.
    - **Acceptance Criteria:**
        - When I input '-1', an error message should appear, warning "Enter Positive Integer".
        - When I input 'a', an error message should appear, warning "Enter Positive Integer".
        - When I input '#', an error message should appear, warning "Enter Positive Integer".
        - When I input '1.2', an error message should appear, warning "Enter Positive Integer".

4. **As a user**, I want to be able to handle the case of input being 0 so that I can handle the case of an empty set.
    - **Acceptance Criteria:**
        - When I input '0', the output should immediately return as 0.

5. **As a user**, I want to be able to handle the case of input being empty so that I can handle the case of a Value error.
    - **Acceptance Criteria:**
        - When I don't input anything and press enter, an error message should appear, warning "Enter Positive Integer".
### Running all tests

To run all tests in the `tests` directory, execute the following command from the project directory folder:

```bash
python -m unittest discover -v
```

### Coverage Report

1. **Install coverage**
   ```bash
   pip install coverage
   ```

2. **Run tests with coverage**
   ```bash
   coverage run -m unittest discover -v
   ```

3. **View coverage report**
   ```bash
   coverage report -m
   ```

### Testcases

![testcases](https://github.com/ShrustigaSR/TDD-Sum-of-N-Numbers/assets/53357626/c935bd03-4d40-402a-a027-0b4411ec21cd)
