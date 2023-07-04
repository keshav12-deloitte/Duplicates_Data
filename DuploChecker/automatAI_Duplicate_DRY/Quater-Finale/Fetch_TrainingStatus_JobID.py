import openai

# Set up your OpenAI API credentials
openai.api_key = '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'

job_id = "ft-gWlEy69hyyVN7dE2hzlSgGbE"
# status = openai.FineTune.retrieve(id=job_id)["status"]
# print(status)


# To get model ID
result = openai.FineTune.list()
print(f'Found {len(result.data)} finetune jobs.')

print("Rajaji")
print(result.__dict__)