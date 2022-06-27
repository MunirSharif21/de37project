# de37project

# de37project

The main files have the following structure: (where the arrows show inheritence of functions, a->b means a sends functions to b)

AWS -> combine_table -> cleaning_table -> get_table -> main 

The other 3 files: 
clean_function / utility_functions / normalisation 
have functions used across the main files

AWS: 
Functions related to downloading files into a specific format. 

combine_table: 
Functions for combining all the files together, alongside any cleaning that must be done prior to combining 

cleaning_table: 
The file that runs the "cleaning_functions" code in a specific order to get the desired clean format. Edit this to change the formatting or to clean more.

get_table:
The file that finally gets an actual nice and clean table set up. Hence functions here are mainly used for normalising through the extraction of columns etc.
Edit this to get all desired ERD tables. Normalisation function is inside the normalisation_protocols file.

main:
The main file that drives everything.

clean_function:
A long list of functions that clean specific rows. To format a column, simply create a function that maps a single value in a row into another 
(e.g. function that takes d.o.b. and returns age),
then put this new function into "apply_to_each_row_in_column(df_name, column_to_change, function)" as a parameter to instantly clean a whole column.
(the cleaning call is done in the "cleaning_table" file)

utility_functions:
A small file for adding primary key to the applicants before combining the applicant files

normalisation:
Contains the normalisation *super* function that takes a dataframe, extracts the desired columns into a new table, and sets a linking ID between the two tables.
It can use an existing ID, or generate a brand new one.
If generating a new ID, the new dataframe is instead structured as a set, meaning that it is effectively a new normalised table. 
The original dataframe then maps the new set onto itself (replacing all names with the foreign key), allowing for fast normalisation.
(Further docs are inside the function)
