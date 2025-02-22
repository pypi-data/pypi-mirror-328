

def predict_accuracy(real, predict):
    if len(real) != len(predict):
        raise ValueError(f"样本真实值与预测值列表长度需相同")
    cnt = 0
    for i in range(len(real)):
        if real[i] == predict[i]:
            cnt += 1
    return cnt / len(real)
