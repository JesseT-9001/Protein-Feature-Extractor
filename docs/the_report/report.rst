********************************
Protein Feature Extractor Report
********************************

Understanding Proteins:
=======================
Proteins are polymers of alpha amino acids, arranged in a linear sequence and connected by covalent bonds.
Amino acids are the major building blocks of a protein. Each amino acid contains a central C atom, an amino group
(NH2), a carboxyl group (COOH), and a specific R group. The R group determines the characteristics (size, polarity, and
pH) for each type of amino acid.

Feature Selection:
==================
Polarizability usually refers to the response of a molecule to an electric field. As molecules are made up of
elementary particles with electric charge, namely protons and electrons, when subject to an electric field, the
negatively charged electrons and positively charged atomic nuclei are subject to opposite forces and undergo charge
separation.

In our assignment we have chosen Polarizability as one of the features of proteins to be extracted.

Normalization:
==============
the goal of normalization is to change the values of numeric columns in the dataset to a common scale, without
distorting differences in the ranges of values. For machine learning, every dataset does not require normalization. So
we normalize the data to bring all the variables to the same range

The normalization we chose for this project is, for each sequence, to divided by the length of the sum of the char of
the sequence

Data Available:
===============
List of protein sequences which belong to 4 groups (4 places in the Gram-Negative Bacterial protein cells). The
proteins, their class labels, and a list of 55 physicochemical properties for amino acids (20 alphabets that build the
protein sequence) are available.

Logic Implemented:
==================
* Step 1: Read in protein data.
* Step 2: Read in protein attribute data.
* Step 3: Extract attribute headers.
* Step 4: Convert protein sequences to given properties.
* Step 5: Normalize count vector.
* Step 6: Pick attribute to extract and apply it.

For a more detail read :doc:`../the_code/main`

To see a basic summary of the data navigate to :doc:`../chosen_feature`. To see the full data extraction open
`Polarizability.csv`
