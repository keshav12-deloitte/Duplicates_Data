import openai
import openpyxl

# Constants
""" All the constants required """

# Set up your OpenAI API credentials
openai.api_key = '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'
# which model to use
model_name = "text-davinci-003"
fine_tune_model_name = "davinci:ft-deloitteus-2023-06-22-14-26-18"
fine_tune_model_name1 = "davinci:ft-deloitteus-2023-06-21-16-53-53"
model_name1 = "gpt-3.5-turbo-0301"
# excel_path
excel_path = "/Users/amananand7/PycharmProjects/automatAI_Duplicate_DRY/resources/Duplicate_generator_Test_Data.xlsx"
# sheet name
sheet_name = "selenium"

new_prompt = """Find the duplicate code in the below python code:
import pandas
import math
import pandas as pd
class HomeScreen:

    def sum(self, a, b):
        c = a + b
        return c

    def subtraction(self, a, b):
        c = a - b
        return c

import math
import openpyxl

class LoginScreen:

    def sum(self, a, b):
        c = a + b
        return c

    def subtraction(self, a, b):
        c = a - b
        return c

import math


class PaymentScreen:

    def sum(self, a, b):
        c = a + b
        return c

###
"""
answer1 = openai.Completion.create(
    model=fine_tune_model_name,
    prompt=new_prompt,
    max_tokens=888
)

print(answer1['choices'][0]['text'])








