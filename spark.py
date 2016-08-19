from pyspark import SparkConf, SparkContext
from pyspark.mllib.classification import LogisticRegressionWithSGD
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.feature import HashingTF
from numpy import array
import time

#building Spark Configuration and Getting a Spark Context and Loading Data into an RDD
conf = (SparkConf().setMaster("local[8]").setAppName("kaggle_ctr").set("spark.executor.memory", "2g").set("spark.driver.memory","4g").set("spark.driver.maxResultSize","0").set("spark.storage.memoryFraction", "0.5"))
sc = SparkContext(conf = conf)

hashingTF = HashingTF()


# Load and parse the data
def parsePoint_train(line):
    values = [str(x) for x in line.split(',')]
    fh = hashingTF.transform(values[2:])
    return LabeledPoint(float(values[1]), fh)

def parsePoint_test(line):
    values = [str(x) for x in line.split(',')]
    fh = hashingTF.transform(values[1:])
    return LabeledPoint(0.0, fh)

train = sc.textFile("../Data/trainOriginal.csv")
header1 = train.first()
train = train.filter(lambda line: line!=header1)
trainData = train.map(parsePoint_train)

# Test Data
test = sc.textFile("../Data/testOriginal.csv")
header = test.first()
test = test.filter(lambda line: line!=header)
testData = test.map(parsePoint_test)

# Build the model
train_start = time.time()
model = LogisticRegressionWithSGD.train(trainData)
train_end = time.time()
model.clearThreshold()

# Evaluating the model on training data
#labelsAndPreds = trainData.map(lambda p: (p.label, model.predict(p.features)))
pred_start = time.time()
preds = testData.map(lambda p: model.predict(p.features))
preds.saveAsTextFile("results")
#results = preds.collect()
pred_end = time.time()
#print results

"""
f = open("../Data/sampleSubmission.csv")
f.readline()
with open("../Data/spark_submission.csv","wb") as outfile:
    outfile.write("id,click\n")
    for line in results:
        row = f.readline().strip().split(",")
        try:
            outfile.write("%s,%f\n"%(row[0],float(line)))
            #print("%s,%f\n"%(row2[0],zygmoid(float(row[0]))))
        except:
            pass

f.close()
"""
train_time = train_end - train_start
pred_time = pred_end - pred_start
train_res = ("Training Time = " + str(train_time)) + '\n'
pred_res = ("Predicting Time = " + str(pred_time)) + '\n'
print train_res + pred_res