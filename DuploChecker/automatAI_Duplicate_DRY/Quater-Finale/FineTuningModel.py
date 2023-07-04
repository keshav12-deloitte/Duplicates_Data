import openai
import signal
import datetime

# Set up your OpenAI API credentials
openai.api_key = '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'

# Preparing the data from jsonl to list of preparation data
training_file_name = "/Users/amananand7/PycharmProjects/automatAI_Duplicate_DRY/resources/data_prepared_train.jsonl"
validation_file_name = "/Users/amananand7/PycharmProjects/automatAI_Duplicate_DRY/resources/data_prepared_valid.jsonl"

# Uploading the file to OpenAI to fine tune  the model
purpose = 'fine-tune'
training_file_id = openai.File.create(file=open(training_file_name), purpose=purpose)
validation_file_id = openai.File.create(file=open(validation_file_name), purpose=purpose)

print(f"Training File ID: {training_file_id}")
print(training_file_id['id'])
print(f"Validate File ID: {validation_file_id}")
print(validation_file_id['id'])

# Creating a fine tune job
create_args = {
    "training_file": training_file_id['id'],
    "validation_file": validation_file_id['id'],
    "model": "davinci",
    "n_epochs": 15,
    "batch_size": 3,
    "learning_rate_multiplier": 0.3
}

response = openai.FineTune.create(**create_args)

print("Rajaji")
print(response.__dict__)
job_id = response["id"]
status = response["status"]

print(f'Fine-tunning model with jobID: {job_id}.')
print(f"Training Response: {response}")
print(f"Training Status: {status}")


# checking the fine tune job status
def signal_handler(sig, frame):
    status = openai.FineTune.retrieve(job_id).status
    print(f"Stream interrupted. Job is still {status}.")
    return


print(f'Streaming events for the fine-tuning job: {job_id}')
signal.signal(signal.SIGINT, signal_handler)

events = openai.FineTune.stream_events(job_id)
try:
    for event in events:
        print(f'{datetime.datetime.fromtimestamp(event["created_at"])} {event["message"]}')

except Exception:
    print("Stream interrupted (client disconnected).")

# TIll above codee is enough for creation of fine tune


##  Fine tune model response

# /Users/amananand7/Documents/automatAI_Duplicate_DRY/bin/python /Users/amananand7/PycharmProjects/automatAI_Duplicate_DRY/Quater-Finale/FineTuningModel.py
# Training File ID: {
#   "object": "file",
#   "id": "file-xULAMQRrr4NFgzIvOf5ICC0d",
#   "purpose": "fine-tune",
#   "filename": "file",
#   "bytes": 230504,
#   "created_at": 1687442379,
#   "status": "uploaded",
#   "status_details": null
# }
# file-xULAMQRrr4NFgzIvOf5ICC0d
# Validate File ID: {
#   "object": "file",
#   "id": "file-ww3ItZB8bcn3oURn446f6bUV",
#   "purpose": "fine-tune",
#   "filename": "file",
#   "bytes": 63092,
#   "created_at": 1687442380,
#   "status": "uploaded",
#   "status_details": null
# }
# file-ww3ItZB8bcn3oURn446f6bUV
# Rajaji
# {'_response_ms': 86, '_retrieve_params': {}, 'api_key': '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', 'api_version': None, 'api_type': None, 'organization': None, 'api_base_override': None, 'engine': None, '_previous': {'object': 'fine-tune', 'id': 'ft-gWlEy69hyyVN7dE2hzlSgGbE', 'hyperparams': {'n_epochs': 15, 'batch_size': 3, 'prompt_loss_weight': 0.01, 'learning_rate_multiplier': 0.3}, 'organization_id': 'org-AnPp4ukSu2cNBIlkLonuFUXK', 'model': 'davinci', 'training_files': [{'object': 'file', 'id': 'file-xULAMQRrr4NFgzIvOf5ICC0d', 'purpose': 'fine-tune', 'filename': 'file', 'bytes': 230504, 'created_at': 1687442379, 'status': 'processed', 'status_details': None}], 'validation_files': [{'object': 'file', 'id': 'file-ww3ItZB8bcn3oURn446f6bUV', 'purpose': 'fine-tune', 'filename': 'file', 'bytes': 63092, 'created_at': 1687442380, 'status': 'uploaded', 'status_details': None}], 'result_files': [], 'created_at': 1687442380, 'updated_at': 1687442380, 'status': 'pending', 'fine_tuned_model': None, 'events': [{'object': 'fine-tune-event', 'level': 'info', 'message': 'Created fine-tune: ft-gWlEy69hyyVN7dE2hzlSgGbE', 'created_at': 1687442380}]}}
# Fine-tunning model with jobID: ft-gWlEy69hyyVN7dE2hzlSgGbE.
# Training Response: {
#   "object": "fine-tune",
#   "id": "ft-gWlEy69hyyVN7dE2hzlSgGbE",
#   "hyperparams": {
#     "n_epochs": 15,
#     "batch_size": 3,
#     "prompt_loss_weight": 0.01,
#     "learning_rate_multiplier": 0.3
#   },
#   "organization_id": "org-AnPp4ukSu2cNBIlkLonuFUXK",
#   "model": "davinci",
#   "training_files": [
#     {
#       "object": "file",
#       "id": "file-xULAMQRrr4NFgzIvOf5ICC0d",
#       "purpose": "fine-tune",
#       "filename": "file",
#       "bytes": 230504,
#       "created_at": 1687442379,
#       "status": "processed",
#       "status_details": null
#     }
#   ],
#   "validation_files": [
#     {
#       "object": "file",
#       "id": "file-ww3ItZB8bcn3oURn446f6bUV",
#       "purpose": "fine-tune",
#       "filename": "file",
#       "bytes": 63092,
#       "created_at": 1687442380,
#       "status": "uploaded",
#       "status_details": null
#     }
#   ],
#   "result_files": [],
#   "created_at": 1687442380,
#   "updated_at": 1687442380,
#   "status": "pending",
#   "fine_tuned_model": null,
#   "events": [
#     {
#       "object": "fine-tune-event",
#       "level": "info",
#       "message": "Created fine-tune: ft-gWlEy69hyyVN7dE2hzlSgGbE",
#       "created_at": 1687442380
#     }
#   ]
# }
# Training Status: pending
# Streaming events for the fine-tuning job: ft-gWlEy69hyyVN7dE2hzlSgGbE
# 2023-06-22 19:29:40 Created fine-tune: ft-gWlEy69hyyVN7dE2hzlSgGbE
# Stream interrupted (client disconnected).
#
# Process finished with exit code 0
