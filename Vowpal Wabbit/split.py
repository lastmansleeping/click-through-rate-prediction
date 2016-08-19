from datetime import datetime
from csv import DictReader
from math import exp, log, sqrt
import os

def data(path):
    ''' GENERATOR: Apply hash-trick to the original csv row
                   and for simplicity, we one-hot-encode everything

        INPUT:
            path: path to training or testing file
            D: the max index that we can hash to

        YIELDS:
            ID: id of the instance, mainly useless
            x: a list of hashed and one-hot-encoded 'indices'
               we only need the index since all values are either 0 or 1
            y: y = 1 if we have a click, else we have y = 0
    '''

    for t, row in enumerate(DictReader(open(path))):
        outrow,features="",""

        click = 1
    	if 'click' in row:
    		if row['click'] == '0':
    			click=-1
        	del row['click']

        del row['id']

        # extract date
        date = int(row['hour'][4:6])

        # turn hour really into hour, it was originally YYMMDDHH
        # extract date
        row['date'] = int(row['hour'][4:6])
        row['hour'] = row['hour'][6:]

        features=features.join([" {0}_{1}".format(i+1, row[key]) for i, key in enumerate(row)])

        outrow=outrow.join([str(click), ' |catf', features])

        yield t, row['date'], outrow

# Split trainOriginal data into train and test(29,30)

dates = [29,30]

start = datetime.now()

for t, date, outrow in data('trainOriginal.csv'):  # data is a generator
    trfile = "train_split_vw.vw"

    if date in dates:
        trfile = "test_split_vw.vw"

    if not os.path.exists(trfile):
        outfile=open(trfile, 'w')

    outfile.write('%s\n' %outrow)



print("\nPreprocessing time:\n\t%s"%(str(datetime.now() - start)))