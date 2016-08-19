import math

def zygmoid(x):
    return 1 / (1 + math.exp(-x))

f = open("../../Data/sampleSubmission.csv")
f.readline()
with open("../../Data/kaggle.Submission.csv","wb") as outfile:
    outfile.write("id,click\n")
    for line in open("../../Data/click.preds.txt"):
        row = line.strip().split(" ")
        row2 = f.readline().strip().split(",")
        try:
            outfile.write("%s,%f\n"%(row2[0],zygmoid(float(row[0]))))
            #print("%s,%f\n"%(row2[0],zygmoid(float(row[0]))))
        except:
            pass
