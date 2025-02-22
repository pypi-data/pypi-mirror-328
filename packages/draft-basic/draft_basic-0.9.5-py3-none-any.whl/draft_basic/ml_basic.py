import math
import random
from . import basic_function
from tqdm import tqdm
import numpy as np

class Perceptron:
    def __init__(self, input_dimension):
        self.param = []
        for i in range(input_dimension + 1):
            self.param.append(random.random())


    def fit(self, x_train, y_train, lr=0.01, max_epochs=50):
        for i in range(len(y_train)):
            if y_train[i] == 0:
                y_train[i] = -1
        for i in tqdm(range(max_epochs)):
            cnt = 0
            for j in range(len(x_train)):
                x_sample = [x_train[j][index] for index in range(len(x_train[j]))]
                x_sample.append(1)
                output = 0
                for k in range(len(x_sample)):
                    output += self.param[k] * x_sample[k]

                if output >= 0:
                    y = 1
                else:
                    y = -1

                if y_train[j] == y:
                    cnt += 1
                else:
                    for k in range(len(x_sample)):
                        self.param[k] += lr * y_train[j] * x_sample[k]
            if len(y_train) == cnt:
                print('所有训练样本被正确分类，提前终止')
                break

    def predict(self, x_test):
        predict_list = []
        for i in range(len(x_test)):
            x_sample = [x_test[i][index] for index in range(len(x_test[i]))]
            x_sample.append(1)
            output = 0
            for k in range(len(x_sample)):
                output += self.param[k] * x_sample[k]

            if output >= 0:
                y = 1
            else:
                y = 0
            predict_list.append(y)
        return predict_list





class KNN:
    def __init__(self, k=5):
        self.k = k

    def fit(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train


    def predict(self, x_test):
        predict_list = []
        for i in range(len(x_test)):
            dist_dict = {}
            key_list = []
            judge_dict = {}
            for j in range(len(self.x_train)):
                dist_dict[j] = basic_function.o_dist(x_test[i], self.x_train[j])


            for k, v in sorted(dist_dict.items(), key=lambda item: item[1]):
                key_list.append(k)
                if len(key_list) == self.k:
                    break
            for j in key_list:
                label = self.y_train[j]
                if label in judge_dict:
                    judge_dict[label] += 1
                else:
                    judge_dict[label] = 1

            sorted_judge_list = sorted(judge_dict.items(), key=lambda item: item[1], reverse=True)
            first_key = next(iter(sorted_judge_list))
            predict_list.append(first_key[0])
        return predict_list
'''
class Decision_Tree:
    def __init__(self, type='ID3'):
        self.type = type

    def fit(self, x_train, y_train):
        if self.type == 'ID3':
            cnt_0 = 0
            cnt_1 = 0
            for i in range(len(y_train)):
                if y_train[i] == 0:
                    cnt_0 += 1
                if y_train[i] == 1:
                    cnt_1 += 1
            HD = - cnt_0 / len(y_train) * math.log2(cnt_0 / len(y_train)) - cnt_1 / len(y_train) * math.log2(cnt_1 / len(y_train))
            IG_list = []
            for i in range(len(x_train[0])):
                feature_type = []
                IG = HD
                for j in range(len(x_train)):
                    if not x_train[j][i] in feature_type:
                        feature_type.append(x_train[j][i])
                for j in range(len(feature_type)):
                    cnt_0 = 0
                    cnt_1 = 0
                    cnt = 0
                    for k in range(len(y_train)):
                        if y_train[k] == 0 and feature_type[j] == x_train[k][i]:
                            cnt_0 += 1
                            cnt += 1
                        if y_train[i] == 1 and feature_type[j] == x_train[k][i]:
                            cnt_1 += 1
                            cnt += 1
                    HDv = - cnt_0 / (cnt_0 + cnt_1) * math.log2(cnt_0 / (cnt_0 + cnt_1)) - cnt_1 / (cnt_0 + cnt_1) * math.log2(cnt_1 / (cnt_0 + cnt_1))
                    IG -= cnt / len(x_train) * HDv
                IG_list.append(IG)
                
'''





class K_means:
    def __init__(self, x, center_num):
        center = []
        indices = list(range(len(x)))
        random.shuffle(indices)

        x_random = [x[index] for index in indices]

        for i in range(center_num):
            center.append(x_random[i])
        self.center_num = center_num
        self.center = center
        self.x = x
        self.center_dimension = len(x[0])

    def train(self, epochs=100):
        for _ in tqdm(range(epochs)):
            center_list = []
            for i in range(self.center_num):
                center_list.append([])
            for i in range(len(self.x)):
                dist_arr = []
                for k in range(self.center_num):
                    dist = basic_function.o_dist(self.x[i], self.center[k])
                    dist_arr.append(dist)

                min_dist = min(dist_arr)
                min_index = dist_arr.index(min_dist)

                center_list[min_index].append(self.x[i])

            for i in range(self.center_num):
                for j in range(self.center_dimension):


                    elements = [sublist[j] for sublist in center_list[i]]
                    if len(elements) != 0:
                        self.center[i][j] = sum(elements) / len(elements)

        return self.center

    def predict(self):
        center_list = []
        for i in range(self.center_num):
            center_list.append([])
        for i in range(len(self.x)):
            dist_arr = []
            for k in range(self.center_num):
                dist = basic_function.o_dist(self.x[i], self.center[k])
                dist_arr.append(dist)

            min_dist = min(dist_arr)
            min_index = dist_arr.index(min_dist)

            center_list[min_index].append(self.x[i])

        return center_list


