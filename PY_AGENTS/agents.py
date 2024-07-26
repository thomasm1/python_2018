# agent-mapl.py

import os
import csv
import anthropic
from prompts import *

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
def analyzer_agent(sample_data):
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

# generator agent
def generator_agent(analysis_result, sample_data, num_rows=30):
  message = client.messages.create(
    model=sonnet,
    max_tokens=1500, # allow for longer response
    temperature=1, # high temp for creative, divers output
    system=GENERATOR_SYSTEM_PROMPT,
    messages=[
      {
        "role":"user",
        "content": GENERATOR_USER_PROMPT.format(
          num_rows=num_rows,
          analysis_result=analysis_result,
          sample_data=sample_data
        )
      }
    ]
  )    
  return message.content[0].text


#main fucntion to run analyzer and generator agents: CONTROL THE AGENTS!

#get input
file_path = input("\nPuh-lease enter the name of your CSV file: ")
file_path = os.path.join('/app/data', file_path)
desired_rows =  int(input("n now Enter the number of rows you want in the new dataset: "))

#read data
sample_data = read_csv(file_path)
sample_data_str  = "\n".join([",".join(row) for row in sample_data]) # convert 2d list to a single string

print("\nLaunching team of Agents")

analysis_result = analyzer_agent(sample_data_str)
print("\n### Analyzer Agent output:###\n")
print(analysis_result)
print("\n=-============\n\nGenerating new data....")

#output
output_file = "/app/data/new_dataset.csv"
headers = sample_data[0]
 
#creat output with headers
save_to_csv("", output_file, headers)


batch_size = 30  #number of rows to genrate in each batch
generated_rows = 0 # counter to keep track of rows generated

# generate data in batches until rows reached
while generated_rows < desired_rows:
  rows_to_generate = min(batch_size, desired_rows - generated rows)
  generated_data = generator_agent(analysis_result, sample_data_str, rows_to_generate)
  #append gen data to output file
  save_to_csv(generated_data, output_file)
  #update count of generated rows
  generated_rows += rows_to_generate
  #print progress update
  print(f"Generated {generated_rows} rows out of {desired_rows}")

# inform process complete
print(f"\nGenerated data has been saved to {output_file}")

# THE END
