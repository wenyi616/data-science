## Step 4
1. Output files to step 4 (word count) are in the folder `output-4`

## Step 5
1. Python code for step 5 is named `bigrams.py`. 
2. To run the code, type ```spark-submit path/to/wordcount.py path/to/wiki.txt```. Note that my program only accepts two parameter (path to the code and path to the text file), and both outputs (counts and distribution) are automatically saved to the same directory where my code is.
3. Output files to step 5 (count of all bigram words) are in the folder `counts-5`
4. Output files to step 5 (conditional bigram frequency distribution) are in the folder `freq-5`

## How to interpret your output for step 5
((word1, word2), x) can be interpreted as if you see a word1, there's x chance that you will see the word2 in a bigram form .
A snippet of the output is shown below:
```
(('eat', 'leafcutter'), 0.0027247956403269754)
(('eat', 'anything'), 0.005449591280653951)
(('eat', 'pasta'), 0.005449591280653951)
(('eat', 'solid'), 0.0027247956403269754)
(('eat', 'some'), 0.005449591280653951)
(('eat', 'from'), 0.01907356948228883)
(('eat', 'lemons'), 0.0027247956403269754)
(('eat', 'grains'), 0.0027247956403269754)
(('eat', 'swill'), 0.0027247956403269754)
(('eat', 'sheep'), 0.0027247956403269754)
(('eat', 'refrigeration'), 0.0027247956403269754)
(('eat', 'inceptive'), 0.0027247956403269754)
(('eat', 'droppings'), 0.0027247956403269754)
(('eat', 'litt'), 0.0027247956403269754)
(('eat', 'farm'), 0.0027247956403269754)
(('eat', 'real'), 0.0027247956403269754)
(('eat', 'fewer'), 0.0027247956403269754)
(('eat', 'feces'), 0.0027247956403269754)
(('eat', 'soiled'), 0.0027247956403269754)
(('eat', 'sausage'), 0.0027247956403269754)
...
(('eat', 'away'), 0.0027247956403269754)
(('eat', 'in'), 0.021798365122615803)
(('eat', 'people'), 0.0027247956403269754)
(('eat', 'because'), 0.005449591280653951)
(('eat', 'food'), 0.010899182561307902)
```
For example, (('eat', 'pasta'), 0.005449591280653951) means that if you see the word "eat", then you have a probability of 0.005449591280653951 to see this bigram "eat pasta". There are 176 bigrams that start with "eat", their probabilities should add up to 1. 
