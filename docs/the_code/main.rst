*******
Main.py
*******

The file named main is the application driver.

Logic Implementation
====================

Step 1: Read in protein data.
-----------------------------

We read in protein data held in a csv file using the python module Pandas and a custom wrapper class called
:doc:`proteindatahandler`.

Step 2: Read in protein property data.
--------------------------------------

The protein attribute data, a list of vectorized properties that a protein has, is read in from a csv file using the
python module Pandas and a custom wrapper class classed :doc:`proteinattributedatahandler`.

Step 3: Extract attribute headers.
----------------------------------

To keep the code module, we extract the headers associated with the protein property attributes, this is just in case we are
presented with an attribute list that doesn't want to take into account certain attribute values.

Step 4: Convert protein sequences to given attributes.
------------------------------------------------------

Here we count how many times an attribute appears in a sequence and place the result under it's associated name and
attribute.

Step 5: Normalize count vector.
-------------------------------

We divide each attribute count by the length of the sequence.

Step 6: Pick properties to extract and apply it.
------------------------------------------------

We take the chosen index from the protein properties csv and grab it's associated position in the dataframe. We then
multiplied each attribute with it's associated count. We also summed the result under the column with the properties
name.

