# CSE 151B Kaggle: Team 5 - Negative Brane Cells
## Setup
1. Ensure Pandas, Pytorch, and Numpy are all installed.
2. Place original dataset csv's in a data directory within the project directory.
    1. Fix `metaData_taxistandsID_name_GPSlocation.csv`'s invalid entry on line 42.
```
root
 |_ examples
 |_ report_assets
 ...
 |_ data
   |_ train.csv
   ...
```
`data_analysis` directory self explanatory

`embed` directory: neural net where everything except coordinates is embedded

`numeric` directory: same as `embed` except only origin_call, origin_stand, taxi_id are embedded

`simple` directory: only time and call_type are used, all one-hot encoded

