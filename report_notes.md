# Notes on random shit we did for the report later on

## Manual data cleaning
1. `metaData_taxistandsID_name_GPSlocation.csv`: Fixed typo on line 42: Nevogilde, latitude and longitude coordinates were combined.
![image](report_assets/1_nevogilde.png)


## Data preprocessing
1. `train.csv` Feature engineering/preprocessing
   1. Delete all rows where `MISSING_DATA` was true as the number of incorrect entries (~10) was deemed insignificant to
   the overall dataset (~1.7+ million entries).
      1. Delete column `MISSING_DATA`
   2. Delete column `DAY_TYPE`, it's `A` for every entry, what's the point in keeping it?
   3. Deleting column `TRIP_ID`, they're all unique values and we don't see how this column helps in generalization.
   4. Set `ORIGIN_STAND` and `ORIGIN_CALL` to 0 for entries where these columns are null.
      1. Convert `ORIGIN_STAND` entries to indices for embeddings.
      2. `ORIGIN_CALL` has new entries not seen in test set, leave as is and pass into neural net directly.
   5. Call type assigned to indices for embeddings
   6. Convert UNIX timestamps to day of week, month, and time of day.
      1. Delete original timestamp column
   7. Convert polylines to estimation target with entry `TARGET` in new csv: $(n - 1) * 15$, and delete `POLYLINE` column.
2. Pruning
   1. Delete rows where prediction is not within 3 standard deviations of mean
   2. Delete rows where 
3. Extra possibilities
   1. Convert elements such as `TAXI_ID` to embeddings?
      1. Neural net can learn similarities between different drivers' patterns.
   2. Add columns for longitude/latitude for type `B` entries