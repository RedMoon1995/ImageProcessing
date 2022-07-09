import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import label_binarize


if __name__ =='__main__':

    fact = [0, 0, 3, 1, 1, 3, 1, 2, 3, 1, 0, 2, 2, 0, 3, 2, 1, 2, 2, 3, 1, 0, 3, 1, 1, 1, 2, 3, 2, 0, 3, 0, 1, 3, 2, 0, 2, 3, 0, 2, 3, 1, 0, 1, 0, 1, 0, 3, 0, 0, 3, 3, 1, 0, 3, 3, 3, 2, 3, 1, 3, 1, 1, 1, 1, 0, 0, 0, 3, 3, 3, 1, 3, 3, 0, 3, 0, 1, 0, 0, 2, 0, 0, 2, 3, 3, 1, 3, 2, 3, 3, 1, 3, 0, 0, 1, 0, 1, 3, 1, 3, 0, 0, 0, 3, 3, 3, 2, 1, 3, 0, 1, 2, 2, 2, 2, 1, 3, 2, 2, 2, 2, 3, 3, 2, 0, 0, 2, 3, 2, 3, 1, 0, 0, 0, 2, 0, 1, 2, 1]

    guess = [0, 0, 3, 1, 1, 3, 1, 2, 3, 1, 0, 2, 2, 0, 3, 2, 1, 2, 2, 3, 1, 0, 3, 1, 1, 1, 2, 3, 2, 0, 3, 0, 1, 3, 2, 0, 2, 3, 0, 2, 3, 1, 0, 1, 0, 1, 0, 3, 1, 0, 3, 3, 1, 0, 3, 3, 3, 2, 3, 1, 3, 1, 1, 1, 1, 0, 0, 0, 3, 3, 3, 1, 3, 3, 0, 3, 0, 1, 0, 0, 2, 0, 0, 2, 3, 3, 1, 3, 2, 3, 3, 0, 3, 0, 0, 1, 0, 1, 3, 1, 3, 0, 0, 1, 3, 3, 3, 2, 1, 3, 0, 1, 2, 1, 2, 3, 1, 3, 2, 2, 2, 1, 3, 3, 2, 0, 0, 2, 3, 1, 3, 1, 0, 0, 2, 2, 0, 1, 2, 1]

    fact = np.array(fact)
    guess = np.array(guess)

    #diabetes = pd.read_excel('./result/pre30_person.xlsx')
    #fact = diabetes['label_gt']
    #guess = diabetes['label-pre']

    print("每个类别的精确率和召回率：\n", classification_report(fact, guess))

    # 混淆矩阵
    classes = list(set(fact))
    classes.sort()
    confusion = confusion_matrix(y_pred=guess, y_true=fact)
    plt.imshow(confusion, cmap=plt.cm.Blues)
    indices = range(len(confusion))
    plt.xticks(indices, classes)
    plt.yticks(indices, classes)
    plt.colorbar()
    plt.xlabel('Predicted label')
    plt.ylabel('True label')
    for first_index in range(len(confusion)):
        for second_index in range(len(confusion[first_index])):
            plt.text(second_index, first_index,  confusion[first_index][second_index])
    plt.show()
