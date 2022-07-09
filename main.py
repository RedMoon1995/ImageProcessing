import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix,roc_curve,auc
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import seaborn as sns

def svm_test():
    # 读取数据
    data = pd.read_csv("./krkopt.data")

    # 删除无效行
    data = data.dropna(axis=0)

    # 输出数据的基本信息
    # print(data.info())

    # 数据处理(使其满足特征处理的要求)
    data["draw"].replace("draw", 1, inplace=True)
    data.draw[data["draw"] != 1] = -1
    data.replace("a", 1, inplace=True)
    data.replace("b", 2, inplace=True)
    data.replace("c", 3, inplace=True)
    data.replace("d", 4, inplace=True)
    data.replace("e", 5, inplace=True)
    data.replace("f", 6, inplace=True)
    data.replace("g", 7, inplace=True)
    data.replace("h", 8, inplace=True)
    data["1"] = data["1"].astype(int)
    data["2"] = data["2"].astype(int)
    data["3"] = data["3"].astype(int)

    # 分离特征值和目标值
    x = data.iloc[:, 0:6]
    y = data["draw"]

    # 分割训练集和测试集
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.7, test_size=0.3)

    # 特征预处理-特征工程(标准化)
    std = StandardScaler()
    x_train = std.fit_transform(x_train)
    x_test = std.transform(x_test)

    # 用SVM训练数据集
    svm_svc = SVC(kernel='rbf')

    # 设置参数的取值用于网格搜索
    ga_param = [2 ** i for i in range(-5, 15)]
    c_param = [2 ** i for i in range(-15, 3)]
    # ga_param = [0.0825]
    # c_param = [16]
    param = {"gamma": ga_param, "C": c_param}

    # 设置网格搜索的参数和5折交叉验证
    gc = GridSearchCV(svm_svc, param_grid=param, cv=10)

    # 进行训练
    gc.fit(x_train, y_train)

    # 查看预测结果
    y_predict = gc.predict(x_test)

    # 准确率和召回率
    print(classification_report(y_test, y_predict))

    # 预测准确率
    print("在测试集上准确率: ", gc.score(x_test, y_test))

    print("在交叉验证当中最好的结果: ", gc.best_score_)

    print("选择最好的模型是: ", gc.best_estimator_)

    print("每个超参数每次交叉验证的结果: ", gc.cv_results_)

    cm = confusion_matrix(y_test, y_predict, labels=[-1, 1], sample_weight=None)
    fpr, tpr, threshold =roc_curve(y_test, y_predict)
    roc_auc = auc(fpr, tpr)
    sns.set()
    f, ax = plt.subplots()
    sns.heatmap(cm, annot=True, ax=ax)
    ax.set_title('confusion matrix')
    ax.set_xlabel('predict')
    ax.set_ylabel('true')
    plt.figure()
    lw = 2
    plt.figure(figsize=(10, 10))
    plt.plot(fpr, tpr, color='darkorange', lw=lw, label='ROC curve(area = %0.2f)'%roc_auc)
    plt.plot([0, 1], [1, 0], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic example')
    plt.legend(loc='lower right')
    plt.show()



    return None


if __name__ == "__main__":
    svm_test()
