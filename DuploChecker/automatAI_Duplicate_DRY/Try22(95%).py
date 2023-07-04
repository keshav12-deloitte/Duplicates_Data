import openai
import os


def get_files_contents_as_string(folder_path):
    py_contents = ""
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".py"):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "r") as file:
                py_contents += f"{file_name}\n"
                # py_contents += "---------------------------------\n"
                py_contents += file.read()
                # py_contents += "\n-------------------------------------------------------------------------------------\n"
    return py_contents



instruction_to_GPT = """Find the duplicate and similar in below code """

folder_or_dir_path = "/Users/amananand7/PycharmProjects/automatAI_Duplicate_DRY/pages2"
all_py_file_contents = get_files_contents_as_string(folder_or_dir_path)
# print(all_py_file_contents)

openai.api_key = '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'

# response = openai.Completion.create(
#     model="davinci",
#     prompt=instruction_to_GPT + all_py_file_contents,
#     temperature=0,
#     max_tokens=500,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0,
#     stop=["END"]
# )




response = openai.Completion.create(
  model="text-davinci-003",
  prompt=" ```import pandas\nimport math\nimport pandas as pd\nclass HomeScreen:\n    def sum_two_numbers(self, a, b):\n        c = a + b\n        return c\n    def subtraction_num(self, a, b):\n        c = a - b\n        return c\n    def csv_reader(self):\n        # reading the CSV file\n        csvFile = pandas.read_csv('Giants.csv')\n        # displaying the contents of the CSV file\n        print(csvFile)\n    def read_excelSheet_local(self, path):\n        dataframe1 = pd.read_excel(path)\n        print(dataframe1)\nimport math\nimport openpyxl\nclass LoginScreen:\n    def sum_two_numbers(self, a, b):\n        c = a + b\n        return c\n    def subtraction_two_num(self, a, b):\n        c = a - b\n        return c\n    def mul(self, num1, num2):\n        result = math.ceil(num1 * num2)\n        return result\n    def qweqrqerq(self):\n        num1 = int(input(\"Enter the first number: \"))\n        num2 = int(input(\"Enter the second number: \"))\n        # Sum of the two input numbers\n        spasm = num1 + num2\n        # Output the result\n        print(\"The sum of\", num1, \"and\", num2, \"is\", sum)\n        return spasm\n    def read_excel_local_sheet_TestData(self, path):\n        dataframe = openpyxl.load_workbook(path)\n        dataframe1 = dataframe.active\n        for row in range(0, dataframe1.max_row):\n            for col in dataframe1.iter_cols(1, dataframe1.max_column):\n                print(col[row].value)\nimport math\nclass paymentScreen:\n    def sum_two_numbers(self, a, b):\n        c = a + b\n        return c\n    def readAndWriteText(self):\n        file1 = open(\"myfile.txt\", \"w\")\n        L = [\"This is Delhi \\n\", \"This is Paris \\n\", \"This is London \\n\"]\n        file1.writelines(L)\n        file1.close()\n        # Append-adds at last\n        file1 = open(\"myfile.txt\", \"a\")  # append mode\n        file1.write(\"Today \\n\")\n        file1.close()\n        file1 = open(\"myfile.txt\", \"r\")\n        print(\"Output of Readlines after appending\")\n        print(file1.readlines())\n        print()\n        file1.close()\n    def sadsaf(self, a, b):\n        soo = math.ceil(a * b)\n        return soo\n    def rajajaijdaisjf(self):\n        num1 = int(input(\"Enter the first number: \"))\n        num2 = int(input(\"Enter the second number: \"))\n        # Sum of the two input numbers\n        sum = num1 + num2\n        # Output the result\n        print(\"The sum of\", num1, \"and\", num2, \"is\", sum) ``` \n\nFind the all the  duplicate and similiar in above code and \nThe  completion format looks like this:\nDuplicate methods:\n\n[Method Name] - Present in [Class Name] , [Class Name]  and [Class Name if there]with  Confidence =  [Confidence Percentage] \n[Print the Duplicate method name with className and its implementation]\nMethod Description: [Method Description]\n[Print only the duplciate methods in above mentioned format]\n\nSimilar methods:\n\n[Method Name]  & [Method Name] - Present in [Class Name] and [Class Name] with Confidence = [Confidence Percentage]\nClass = [Class Names]\n[Print the Similar method with className and implementation]\nClass = [Class Names]\n[Print the Similar method with className  and implemenatiton]\nMethod Description: [Method Description]\n[Print all only the similar method in above mentioned format]",
  temperature=0,
  max_tokens=1147,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=["END"]
)

print(response['choices'][0]['text'])
# print(response.__dict__)

############################################################################################################RRRR#######
"""/Users/amananand7/Documents/automatAI_Duplicate_DRY/bin/python /Users/amananand7/PycharmProjects/automatAI_Duplicate_DRY/Try2(95%).py
There are a few instances of duplicate code that I can see:
1. The `sum_two_numbers()` method is duplicated in all three classes.
2. The `mulwertyu()` method in `LoginScreen` and the `asfsaf()` method in `PaymentScreen` are very similar, with only the variable names being different.
3. The `prime_checker_ValidateChecker()` method in `PaymentScreen` and the `validator_prime_number()` method in `HomeScreen` are similar in that they both check for prime numbers, but there are some differences in their implementation.

To show the duplicate code, I can print the code blocks for the `sum_two_numbers()` method and the similar `mulwertyu()` and `asfsaf()` methods:

```
# Duplicate method: sum_two_numbers()

class paymentScreen:
    
    def sum_two_numbers(self, a, b):
        c = a + b
        return c


class HomeScreen:
    
    def sum_two_numbers(self, a, b):
        c = a + b
        return c


class LoginScreen:
    
    def sum_two_numbers(self, a, b):
        c = a + b
        return c


# Similar method: mulwertyu() and asfsaf()

class PaymentScreen:
    
    def asfsaf(self, a, b):
        soo = math.ceil(a * b)
        return soo
    

class LoginScreen:
    
    def mulwertyu(self, num1, num2):
        result = math.ceil(num1 * num2)
        return result
```

Process finished with exit code 0
"""


#########################################RESPONSE#######################################################################
"""/Users/amananand7/Documents/automatAI_Duplicate_DRY/bin/python /Users/amananand7/PycharmProjects/automatAI_Duplicate_DRY/Try2(95%).py
Duplicate code is present in the following methods:

- sum_two_numbers() in PaymentScreen, HomeScreen, and LoginScreen classes
- validator_prime_number() in PaymentScreen and HomeScreen classes

Similar code is present in the following methods:

- read_excelSheet_local() in HomeScreen and read_excel_local_sheet_TestData() in LoginScreen classes. Both methods read data from an Excel file.
- prime_checker_ValidateChecker() in PaymentScreen and validator_prime_number() in HomeScreen classes. Both methods check for prime numbers in a given range.

Code for duplicate methods:

```
# Duplicate method: sum_two_numbers()
class paymentScreen:
    def sum_two_numbers(self, a, b):
        c = a + b
        return c

class HomeScreen:
    def sum_two_numbers(self, a, b):
        c = a + b
        return c

class LoginScreen:
    def sum_two_numbers(self, a, b):
        c = a + b
        return c

class paymentScreen:
    def validator_prime_number(self, low, high, primes):
        for num in range(low, high + 1):
            flag = 0
            if num < 2:
                flag = 1
            if num % 2 == 0:
                continue
            if num % 3 == 0:
                continue
            iter = 3

            while iter < int(pow(num, 0.5)):
                if num % iter == 0:
                    flag = 1
                    break
                iter += 2
            if flag == 0:
                primes.append(num)

        print(primes)

class HomeScreen:
    def validator_prime_number(self, lo, hi, pe):
        for num in range(lo, hi + 1):
            flag = 0
            if num < 2:
                flag = 1
            if num % 2 == 0:
                continue
            if num % 3 == 0:
                continue
            iter = 2
            while iter < int(pow(num, 0.5)):
                if num % iter == 0:
                    flag = 1
                    break
                iter += 1
            if flag == 0:
                pe.append(num)
        print(pe)
```

Code for similar methods:

```
# Similar methods: read_excelSheet_local() and read_excel_local_sheet_TestData()
class HomeScreen:
    def read_excelSheet_local(self, path):
        dataframe1 = pd.read_excel(path)
        print(dataframe1)

class LoginScreen:
    def read_excel_local_sheet_TestData(self, path):
        dataframe = openpyxl.load_workbook(path)
        dataframe1 = dataframe.active
        for row in range(0, dataframe1.max_row):
            for col in dataframe1.iter_cols(1, dataframe1.max_column):
                print(col[row].value)

# Similar methods: prime_checker_ValidateChecker() and validator_prime_number()
class paymentScreen:
    def prime_checker_ValidateChecker(self, low, high, primes):
        for num in range(low, high + 1):
            flag = 0
            if num < 2:
                flag = 1
            if num % 2 == 0:
                continue
            if num % 3 == 0:
                continue
            iter = 3

            while iter < int(pow(num, 0.5)):
                if num % iter == 0:
                    flag = 1
                    break
                iter += 2
            if flag == 0:
                primes.append(num)

        print(primes)

class HomeScreen:
    def validator_prime_number(self, lo, hi, pe):
        for num in range(lo, hi + 1):
            flag = 0
            if num < 2:
                flag = 1
            if num % 2 == 0:
                continue
            if num % 3 == 0:
                continue
            iter = 2
            while iter < int(pow(num, 0.5)):
                if num % iter == 0:
                    flag = 1
                    break
                iter += 1
            if flag == 0:
                pe.append(num)
        print(pe)
```

Process finished with exit code 0
"""



###################ERTYUIOIUYTRTYUIUYT##################################################################################
"""/Users/amananand7/Documents/automatAI_Duplicate_DRY/bin/python /Users/amananand7/PycharmProjects/automatAI_Duplicate_DRY/Try2(95%).py
Duplicate methods:
- `sum_two_numbers` in `PaymentScreen` and `HomeScreen` classes
- `mulwertyu` in `LoginScreen` and `PaymentScreen` classes

Similar code:
- `prime_checker_ValidateChecker` in `PaymentScreen` and `HomeScreen` classes
- `read_excel_local_sheet_TestData` in `LoginScreen` and `HomeScreen` classes

Duplicate code (sum_two_numbers method):
```
class paymentScreen:
    def sum_two_numbers(self, a, b):
        c = a + b
        return c

class HomeScreen:
    def sum_two_numbers(self, a, b):
        c = a + b
        return c
```
Duplicate code (mulwertyu method):
```
class LoginScreen:
    def mulwertyu(self, num1, num2):
        result = math.ceil(num1 * num2)
        return result

class paymentScreen:
    def asfsaf(self, a, b):
        soo = math.ceil(a * b)
        return soo
```
Method description:
- `sum_two_numbers`: returns the addition of two numbers
- `prime_checker_ValidateChecker`: checks and prints prime numbers in a range
- `read_excel_local_sheet_TestData`: reads and prints data from an excel sheet
- `mulwertyu`: returns the ceiling value of multiplication of two numbers

Process finished with exit code 0
"""

############################################RESONFOSNFO ################################################################
"""/Users/amananand7/Documents/automatAI_Duplicate_DRY/bin/python /Users/amananand7/PycharmProjects/automatAI_Duplicate_DRY/Try2(95%).py
Duplicate code is present in the sum_two_numbers method of all three classes PaymentScreen, HomeScreen, and LoginScreen.

Method description: This method takes two numbers as input and returns the sum of two numbers.

Similar code is present in the prime_checker_ValidateChecker method of PaymentScreen and validator_prime_number method of HomeScreen.

Method description: This method checks for prime numbers between a given range and returns a list of prime numbers.

Process finished with exit code 0
"""

############################################RESPONSE#####################################################################
"""/Users/amananand7/Documents/automatAI_Duplicate_DRY/bin/python /Users/amananand7/PycharmProjects/automatAI_Duplicate_DRY/Try2(95%).py
Duplicate code is present in the sum_two_numbers method of all three classes PaymentScreen, HomeScreen, and LoginScreen.

Method description: This method takes two numbers as input and returns the sum of two numbers.

Similar code is present in the prime_checker_ValidateChecker method of PaymentScreen and validator_prime_number method of HomeScreen.

Method description: This method checks for prime numbers between a given range and returns a list of prime numbers.

Process finished with exit code 0
"""


#################################################RESPONSE###############################################################
"""/Users/amananand7/Documents/automatAI_Duplicate_DRY/bin/python /Users/amananand7/PycharmProjects/automatAI_Duplicate_DRY/Try2(95%).py
Duplicate code is present in the sum_two_numbers method of all three classes PaymentScreen, HomeScreen, and LoginScreen.

Method description: This method takes two numbers as input and returns the sum of two numbers.

Similar code is present in the prime_checker_ValidateChecker method of PaymentScreen and validator_prime_number method of HomeScreen.

Method description: This method checks for prime numbers between a given range and returns a list of prime numbers.

Process finished with exit code 0
"""

################################################RESPONSE################################################################
"""/Users/amananand7/Documents/automatAI_Duplicate_DRY/bin/python /Users/amananand7/PycharmProjects/automatAI_Duplicate_DRY/Try2(95%).py
Duplicate methods:

1. sum_two_numbers(a, b) in login_page.py and base_page.py.
2. validator_prime_number(lo, hi, pe) in login_page.py and base_page.py.

Similar methods:

1. read_excel_local_sheet_TestData(path) in common_methods.py and base_page.py, both methods read data from an Excel sheet.
2. subtraction_num(a, b) in base_page.py and subtraction_two_num(a, b) in common_methods.py are similar in functionality as they both subtract two numbers.
3. csv_reader() in base_page.py and readAndWriteText() in login_page.py have similar functionality as they both read and display data from files.
4. asfsaf(a, b) in login_page.py and mulwertyu(num1, num2) in common_methods.py are similar in functionality as they both perform mathematical operations. 
5. prime_checker_ValidateChecker(low, high, primes) in login_page.py is similar in functionality to validator_prime_number(lo, hi, pe) in base_page.py, as they both check for prime numbers in a given range.

Process finished with exit code 0
"""


############################################RESPNOSE####################################################################
"""/Users/amananand7/Documents/automatAI_Duplicate_DRY/bin/python /Users/amananand7/PycharmProjects/automatAI_Duplicate_DRY/Try2(95%).py
Duplicate methods:

1. sum_two_numbers(a, b) in login_page.py and base_page.py.
2. validator_prime_number(lo, hi, pe) in login_page.py and base_page.py.

Similar methods:

1. read_excel_local_sheet_TestData(path) in common_methods.py and base_page.py, both methods read data from an Excel sheet.
2. subtraction_num(a, b) in base_page.py and subtraction_two_num(a, b) in common_methods.py are similar in functionality as they both subtract two numbers.
3. csv_reader() in base_page.py and readAndWriteText() in login_page.py have similar functionality as they both read and display data from files.
4. asfsaf(a, b) in login_page.py and mulwertyu(num1, num2) in common_methods.py are similar in functionality as they both perform mathematical operations. 
5. prime_checker_ValidateChecker(low, high, primes) in login_page.py is similar in functionality to validator_prime_number(lo, hi, pe) in base_page.py, as they both check for prime numbers in a given range.

Process finished with exit code 0
"""

##################################################RESPONSE##############################################################

"""/Users/amananand7/Documents/automatAI_Duplicate_DRY/bin/python /Users/amananand7/PycharmProjects/automatAI_Duplicate_DRY/Try2(95%).py
Duplicate code is present in the following methods across different classes:
1. `sum_two_numbers` method is present in PaymentScreen, HomeScreen, and LoginScreen classes.
2. `validator_prime_number` method is present in PaymentScreen and HomeScreen classes.
3. `read_excelSheet_local` method is present in HomeScreen class and `read_excel_local_sheet_TestData` method is present in LoginScreen class.

Similar code is present in the following methods across different classes:
1. `prime_checker_ValidateChecker` method in PaymentScreen class and `validator_prime_number` method in HomeScreen class have similar implementation logic.
2. `asfsaf` method in PaymentScreen class and `mulwertyu` method in LoginScreen class have similar implementation logic.

Process finished with exit code 0
"""


################################RESPNOSE ###############################################################################

"""/Users/amananand7/Documents/automatAI_Duplicate_DRY/bin/python /Users/amananand7/PycharmProjects/automatAI_Duplicate_DRY/Try2(95%).py
Duplicate code is present in the following methods across different classes:
1. `sum_two_numbers` method is present in PaymentScreen, HomeScreen, and LoginScreen classes.
2. `validator_prime_number` method is present in PaymentScreen and HomeScreen classes.
3. `read_excelSheet_local` method is present in HomeScreen class and `read_excel_local_sheet_TestData` method is present in LoginScreen class.

Similar code is present in the following methods across different classes:
1. `prime_checker_ValidateChecker` method in PaymentScreen class and `validator_prime_number` method in HomeScreen class have similar implementation logic.
2. `asfsaf` method in PaymentScreen class and `mulwertyu` method in LoginScreen class have similar implementation logic.

Process finished with exit code 0
"""


###################################RESPONSE#############################################################################
"""/Users/amananand7/Documents/automatAI_Duplicate_DRY/bin/python /Users/amananand7/PycharmProjects/automatAI_Duplicate_DRY/Try2(95%).py
Duplicate code is present in the `sum_two_numbers` method of the `PaymentScreen`, `HomeScreen`, and `LoginScreen` classes.

Similar code is present in the `prime_checker_ValidateChecker` method of the `PaymentScreen` class and `validator_prime_number` method of the `HomeScreen` class. Both methods check for prime numbers within a given range using a similar algorithm.

Duplicate method descriptions:
1. `sum_two_numbers`: Calculates the sum of two numbers.
2. `read_excel_local_sheet_TestData`: Reads data from an Excel sheet located locally.
3. `mulwertyu`: Calculates the product of two numbers rounded up to the nearest integer.
4. `subtraction_two_num`: Calculates the difference between two numbers.
5. `prime_checker_ValidateChecker`: Checks for prime numbers within a given range.

Process finished with exit code 0
"""

#################################RESPONSE###############################################################################

"""/Users/amananand7/Documents/automatAI_Duplicate_DRY/bin/python /Users/amananand7/PycharmProjects/automatAI_Duplicate_DRY/Try2(95%).py
Duplicate code is present in the following methods:
1. sum_two_numbers(): This method is present in all three classes - paymentScreen, HomeScreen, and LoginScreen.
2. validator_prime_number(): This method is present in both paymentScreen and HomeScreen classes, with slightly different variable names.
3. read_excelSheet_local(): This method is present in HomeScreen and read_excel_local_sheet_TestData() method is present in LoginScreen. Both of these methods read from an excel sheet.

Similar code is present in the following methods:
1. asfsaf() in paymentScreen and mulwertyu() in LoginScreen have a similar implementation that uses the ceil function from the math module.
2. prime_checker_ValidateChecker() in paymentScreen and validator_prime_number() in HomeScreen have a similar implementation for finding prime numbers, with minor differences in the variable names and iterative loops.
3. sum_two_numbers() in paymentScreen and HomeScreen, although duplicates, have a similar implementation for adding two numbers.

Process finished with exit code 0
"""

##################################RESPONSE##############################################################################

"""/Users/amananand7/Documents/automatAI_Duplicate_DRY/bin/python /Users/amananand7/PycharmProjects/automatAI_Duplicate_DRY/Try2(95%).py
Duplicate code:
1. The `sum_two_numbers()` method is present in all three classes.

Similar code:
1. The `prime_checker_ValidateChecker()` method in `login_page.py` and `validator_prime_number()` method in `base_page.py` have similar logic for checking prime numbers.
2. The `read_excelSheet_local()` method in `base_page.py` and `read_excel_local_sheet_TestData()` method in `common_methods.py` have similar logic for reading data from an Excel sheet.

Duplicate methods:
1. `sum_two_numbers()` method - present in all three classes, returns the sum of two numbers.
2. `read_excel_local_sheet_TestData()` method and `read_excelSheet_local()` method - have similar logic for reading data from an Excel sheet.

Process finished with exit code 0
"""

################################### RESPONSE ###########################################################################
"""/Users/amananand7/Documents/automatAI_Duplicate_DRY/bin/python /Users/amananand7/PycharmProjects/automatAI_Duplicate_DRY/Try2(95%).py
Duplicate methods are present in the following classes:
1. PaymentScreen: 'sum_two_numbers' method is present which is also present in LoginScreen and HomeScreen classes.
2. HomeScreen: 'validator_prime_number' method is present which is also present in PaymentScreen class.

Similar code is present in the following methods:
1. PaymentScreen 'readAndWriteText' and HomeScreen 'csv_reader' are similar as they both read and display data from a file using pandas library.
2. PaymentScreen 'prime_checker_ValidateChecker' and HomeScreen 'validator_prime_number' have similar logic to check for prime numbers in a given range.

Duplicate code and method descriptions:
1. Method name: 'sum_two_numbers'
   Class name: PaymentScreen, LoginScreen, HomeScreen
   Method implementation: Adds two numbers and returns the result.

2. Method name: 'validator_prime_number'
   Class name: PaymentScreen, HomeScreen
   Method implementation: Validates prime numbers in a given range and appends them to a list.

Note: The method 'sum_two_numbers' in LoginScreen and PaymentScreen have a minor difference in their second example but they do the same operation and have the same name, hence they are considered as duplicate methods.

Process finished with exit code 0
"""

################### RESPONSE ###########################################################################################
"""/Users/amananand7/Documents/automatAI_Duplicate_DRY/bin/python /Users/amananand7/PycharmProjects/automatAI_Duplicate_DRY/Try2(95%).py
Duplicate code is present in the following methods:
1. sum_two_numbers() in login_page.py and common_methods.py
2. validator_prime_number() in login_page.py and base_page.py

Similar code is present in the following methods:
1. asfsaf() in login_page.py and mulwertyu() in common_methods.py - Both perform a mathematical operation and return the result.
2. read_excelSheet_local() in base_page.py and read_excel_local_sheet_TestData() in common_methods.py - Both read data from an Excel sheet and display the contents. 

Duplicate code:

1. sum_two_numbers() - This method takes two integer inputs and returns their sum. It is present in both login_page.py and common_methods.py. 
2. validator_prime_number() - This method takes a range of numbers as input, checks if they are prime and returns a list of prime numbers. It is present in both login_page.py and base_page.py. 

Code:

1. sum_two_numbers():
   - Class: PaymentScreen 
        def sum_two_numbers(self, a, b):
            c = a + b
            return c
        
   - Class: LoginScreen
        def sum_two_numbers(self, a, b):
            c = a + b
            return c

2. validator_prime_number():
   - Class: PaymentScreen 
        def prime_checker_ValidateChecker(self, low, high, primes):
            for num in range(low, high + 1):
                flag = 0
                if num < 2:
                    flag = 1
                if num % 2 == 0:
                    continue
                if num % 3 == 0:
                    continue
                iter = 3

                while iter < int(pow(num, 0.5)):
                    if num % iter == 0:
                        flag = 1
                        break
                    iter += 2
                if flag == 0:
                    primes.append(num)

            print(primes)

   - Class: HomeScreen
        def validator_prime_number(self, lo, hi, pe):
            for num in range(lo, hi + 1):
                flag = 0
                if num < 2:
                    flag = 1
                if num % 2 == 0:
                    continue
                if num % 3 == 0:
                    continue
                iter = 2
                while iter < int(pow(num, 0.5)):
                    if num % iter == 0:
                        flag = 1
                        break
                    iter += 1
                if flag == 0:
                    pe.append(num)
            print(pe)

Process finished with exit code 0
"""

#################################RESPONSE ##############################################################################


