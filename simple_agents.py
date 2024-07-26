# agent-mapl.py

import os
import csv
import anthropic

#KEY
if not os.getenv("ANTHROPIC_API_KEY"):
  os.environ["ANTHROPIC_API_KEY"] =  input("Please enter your Antrhopic API key: ") # prompt the user for anthro api key

#CLIENT
client = anthropic.Anthropic()
sonnet = "claude-3-5-sonnet-20240620"   # model name get from docs.anthropic.com/en/docs/about-claude/models

# Function to read the CSV file form the user
def read_csv(file_path):
  data = []
  with open(file_path, "r", newline="") as csvfile: #open csv in readmode
    csv_reader = csv.reader(csvfile)  # create csv reader obj
    for row in csv_reader:
      data.append(row)  # add each row to the data list
  return data

# Saving  
def save_to_csv(data, output_file, headers=None):
  mode = 'w' if headers else 'a' # set file mode: w write if headers are provide else a append
  with open(output_file, mode, newline="") as f:
    writer=csv.writer(f) # create a csv writer object
    if headers:
      writer.writerow(headers) # write the headers if provided
    for row in csv.reader(data.splitlines()): #sp;lie data stirng into rows
      writer.writerow(row)


#my personal librarian agent
def mapl_agent(sample_data):
  message = client.messages.create(
    model=sonnet,
    max_tokens=400, #limit response to 400 tokens
    temperature=0.1, # set low temp for more focused, deterministic output
    system=ANALYZER_SYSTEM_PROMPT,  # use the predefined system prompt for analyzer
    messages=[
      {
        "role":"user",
        "content": ANALYZER_USER_PROMPT.format(sample_data=sample_data)
        # format user prompt with provided smpale data
      }
    ]
  )
  return message.content[0].text # return text content of tfirst message

