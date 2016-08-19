import math
import pandas as pd
import numpy as np
from datetime import datetime, date, time
from sklearn.metrics import roc_curve, roc_auc_score, precision_recall_curve, log_loss, average_precision_score, f1_score
import matplotlib
matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt


def zygmoid(x):
    return 1 / (1 + math.exp(-x))

# Read true labels
y_test = np.load("true_labels.npy")


# Read pred labels for logistic regression
df = pd.read_csv("avazu_log.preds3.txt",header=None)
df[0] = df[0].apply(zygmoid)
y_pred = df.values

"""
# Read pred labels for neural networks
df = pd.read_csv("avazu_nn.preds.txt",header=None)
y_pred = df.values
"""

y_pred = y_pred[:, 0]
# Compute ROC curve and ROC area
fpr, tpr, _ = roc_curve(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred)

# Plot of a ROC curve for a specific class
plt.figure()
plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Logistic Regression - VW')
#plt.title('Neural network - VW')
plt.legend(loc="lower right")
#plt.show()
#plt.savefig('roc_vw_nn.png')
plt.savefig('roc_vw_log.png')

# Compute log loss
logloss = log_loss(y_test, y_pred)

print "Log loss : %f"%logloss

# Compute precision recall curve
precision, recall, thresholds = precision_recall_curve(y_test, y_pred)
prc_auc = average_precision_score(y_test, y_pred)
# Plot of a ROC curve for a specific class
plt.figure()
plt.plot(recall, precision, label='PRC area : {0:0.2f}'.format(prc_auc))
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Logistic Regression - VW')
#plt.title('Neural network - VW')
plt.legend(loc="lower right")
#plt.show()
plt.savefig('prc_vw_log.png')

# Compute f1 score
y_pred1 = [round(x) for x in y_pred]
f1 = f1_score(y_test, y_pred1)
print "F1 Score : %f"%f1
