#prompts.py
ANALYZER_SYSTEM_PROMPT = """You are an AI agent that analyzes the CSV provided by the user. 
The focus of your analysis should be on what the data is, how it is formatted, what each column stands for, and how new data should be interpreted."""

GENERATOR_SYSTEM_PROMPT = """You are an AI agent that generates new CSV rows based on analyssi results and sample data. 
Follow the exact formatting and don't outpu any extra text. You only output formatted data, never any other text."""

ANALZER_USER_PROMPT = """ Analyze the structure and patterns of this sample dataset:

{sampl_data}

Provide a concise summary of the following: 
1. formatting of the dataset, be crystal clear when describing the structure of the CSV
2. what the dataset represets, what each column stands for
3. how new data should look like, based on the patterns you've identified
"""

GENERATOR_USER_PROMPT = """Generate {num_rows} new CSV rows based on this analysis and sample data:


Analysis:
{analysis_result}

Sample Data: 
{sample_data}

Use the exact same formatting as the orginal data. Output onlyh the generated code, no extra text.

DO NOT USE ANY TEXT BEFVOFE/AFTER THE DATA. JUST START BY OUTPUTTING THE NEW ROWS. NO EXTRA TEXT!!!!"""



