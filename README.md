Hello :) 

This is Maygun Chen's solution to the Story Prompt challenge from Common Paper.
This project was written in Python3 and assumes the user has Python3 installed for use on the command line.

You  will find the following files in this project:

'generator.py'

    Instructions:
        1. After pulling the repo, navigate to the /story-prompt/may-solution/ directory
        2. Type the following command:
            python3 generator.py '{*/your key-value input string here/*}'
        
     Example Input:
            python3 generator.py '{"number": 46, "unit_of_measure": "feet", "place": "work", "adjective": "fluffy", "noun": "cat"}'
     Output:
            One day Anna was walking her 46 feet commute to work and found a fluffy cat on the ground.
    

    The story prompt generator that accepts a string of key-value inputs for the provided template.

    Template: One day Anna was walking her {{NUMBER}} {{UNIT_OF_MEASURE}} commute to {{PLACE}} and found a {{ADJECTIVE}} {{NOUN}} on the ground.

    The script preforms the following steps:

    Given a string of key-value inputs... 
        1. Converts the input string to a dictionary
        2. Preforms checks for all 6 key-value inputs and requests any missing key-value inputs
        3. Another check for all str inputs to be less than 100 characters long. 
        4. Records input string to 'record.txt' file
        5. Outputs the template with corresponding key-value inputs.


'statistics.py'

    Instructions:
        1. After pulling the repo, navigate to the /story-prompt/may-solution/ directory
        2. Type the following command:
            python3 statistics.py

    The second command line appliation that outputs stats about the stored records including: 
        - The maximum, minimum, and average values for the 'NUMBER' responses.
        - The 3 most commmon recorded inputs for the 4 string inuts. These records appear in tuple form indicating (the string, # of occurences). 


'record.txt'
    
    The text file with records of input strings. Strings are recorded in Python dictionary format.


Room for Improvement:
    - Instead of taking in a CLI input, reading from JSON file
    - Turn 'record.txt' to a JSON file
    - Importing NLTK library to check inputs are actual adjectives and nouns
