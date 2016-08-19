Vowpal Wabbit :

Preprocessing file - split.py
Preprocessing time:
	0:55:02.711979


files:

train_split_vw.vw
test_split_vw.vw


commands :

for logistic regression:

vw train_split_vw.vw -f avazu_log.model.vw --loss_function logistic
vw test_split_vw.vw -t -i avazu_log.model.vw -p avazu_log.preds.txt

with l2 : 

vw -d train_split_vw.vw -b 22 -l 0.158789 --l2 4.7e-14 -f avazu_log.model2.vw --loss_function logistic
vw -d test_split_vw.vw -t -i avazu_log.model2.vw -p avazu_log.preds2.txt

for nn:
vw -d train_split_vw.vw --binary -f avazu_nn.model.vw --loss_function=logistic --nn 3
vw -d test_split_vw.vw -t -i avazu_nn.model.vw --link=logistic -p avazu_nn.preds.txt    [0,1]


