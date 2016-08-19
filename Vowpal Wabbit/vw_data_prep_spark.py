from pyspark import SparkContext
NUM_FEATURES = 13
CAT_FEATURES = 26

def csv_to_vw_map(line):
    if not line:
        return ""
    features = line.split(',')
    if features[0] == 'Id':
        return ""
    
    key = "" 
    # train
    if len(features) == 41: 
        num_start = 2
        if int(features[1]) == 0:
            features[1] = '-1'
        key += features[1] + " '" + features[0] + " |i "   
        
    # test
    else:
        num_start = 1
        key += "1 '" + features[0] + " |i "   
                
    for i in range(0, NUM_FEATURES):
        if features[num_start+i]:
            key += "I%d:%s " %(i+1, features[num_start+i])

    cat_start = num_start + NUM_FEATURES # 13 numerical, num_end excluded
    key +='|c '
    for i in range(0, CAT_FEATURES):
        if features[cat_start+i]:
            key += "%s " %(features[cat_start+i])
    
    return key

BASE_DIR = '/home/user/'
TRAIN_FILE = BASE_DIR + "data/train.csv"
TEST_FILE =  BASE_DIR + "data/test.csv"
TRAIN_VW_DIR = BASE_DIR + "data/train.vw/"
TEST_VW_DIR = BASE_DIR + "data/test.vw/"    
    
if __name__ == '__main__':
    # SPARK
    # Running from console, you don't need to create spark context
    sc = SparkContext('local[8]', "VW")
    
    train = sc.textFile(TRAIN_FILE) 
    train.map(csv_to_vw_map).saveAsTextFile(TRAIN_VW_DIR)

    test = sc.textFile(TEST_FILE) 
    test.map(csv_to_vw_map).saveAsTextFile(TEST_VW_DIR)