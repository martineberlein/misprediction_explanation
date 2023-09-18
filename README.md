# Explaining Mispredictions of Machine Learning Models with Influential Input Features
This repository contains data sets, trained black boxes, evaluation code and results for the master thesis "Explaining Mispredictions of Machine Learning Models with Influential Input Features". Because of file size, the spam data set is stored at https://drive.google.com/drive/folders/1fConM7s3NKoC2DPoEgl8Udc1Gsfr7qZW.

## Contents of Folders and Python Scripts
-blackboxes: contains trained black boxes and corresponding test sets  
-dataset: contains data sets used  
-evaluation: contains experimental results in .csv files and graphs  
-grammars: contains grammars needed for ISLearn  
-mmd: contains MMD implementation from Cito et al.  
-output: contains the raw output of all experiments
-thesis: contains digital version of the master thesis  
-tree: contains decision trees trained to extract rules  
  
-construct-grammar.py: code to construct grammars for ISLearn  
-dataload.py: code to read/prepare data sets, read saved test sets/models  
-evaluation.py: code to create evaluation check lists, execute experiments, extract results from outputs and create graphs  
-misprediction.py: code for the different approaches we evaluate  
-modelevaluation.py: code to calculate performance metrics for black box models and to label mispredictions  
-ruleset.py: code to handle rule sets and to format output from MMD and ISLearn  
-trainmodel.py: code to train black boxes from data sets and train decision trees for rule extraction  
-used_patterns.toml: patterns for ISLearn

## How to Run
The required inputs for every script can be determined by executing the script with "-h".  
When a single experiment should be run execute misprediction.py with the desired parameters.  
For multiple different runs, edit evaluation.py to create a checklist containing all the runs and then execute all of them.  
  
## How to add new data set
1) Add data set to dataset folder.  
2) Add as possible input argument in misprediciton.py.  
3) Add to dataload.py getdata() and do prepocessing if needed.  
4) Execute misprediction.py to train and save black box models and test sets.  
5) (Only needed if ISLearn will be used) Use construct-grammar.py and add import for grammar in misprediction.py. Also add grammer as else options in two places in misprediction.py (search for "set the correct grammar for islearn")  
6) Use misprediction.py or evaluation.py to do single or many experiments.  