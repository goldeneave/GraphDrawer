# GraphDrawer
Several python code script to deal with csv file and draw scatter and folded line chart

## scatter.py
The file used to draw scatter, the code first transfer the date into datetime object and then draw scatter.

Besides, it set a variable to determine the time interval, the defalut value is None, which means for each datetime value, it will has a correspond point the graph, after you set the number, it will calculate the average value between the time interval.

Also, in my file, it has 2 column save different data, so I also set a number to determine the column to draw scatter.

## normalization.py
My data is not a standard file save value, it has some redundant value, so I need to clean them before use them, the script is used to execute the task.

## clean.py
For some reason, after normalize the file, it will save some rows not useful, so clean them again.

## fold_line.py
Not have big different between scatter.py, just draw folded line chart, instead of scatter.
