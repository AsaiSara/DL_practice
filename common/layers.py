from common.np import * #import numpy as np
from common.config import GPU
from common.functions import softmax, cross_entropy_error

class MatMul:
    def __init__(self, W):
        self.params = [W]
        self.grads = [np.zeros_like(W)]
        self.x = None

    def forward(self, x):
        W, = self.params
        out = np.dot(x,W)
        self.x = x
        return out

    def backward(self, dout):
        W, = self.params
        dx = np.dot(dout, W.T)
        print('dx : ',dx)
        dW = np.dot(self.x.T, dout) 
        print('dW : ',dW)
        self.grads[0][...] = dW
        print("grads: ",self.grads)

        return dx

class Sigmoid:
    def __init__(self):
        self.params, self.grads = [], []
        self.out = None

    def forward(self, x):
        out = 1 / (1 + np.exp(-x))
        self.out = out
        return out

    def backward(self,dout):
        dx = dout * (1.0 - self.out) * self.out
        return dx

class Affine:
    def __init__(self, W, b):
        self.params = W,b
        self.grads = [np.zeros_like(W), np.zeros_like(b)]
        self.x = None

    def forward(self,x):
        W,b = self.params
        out = np.dot(x, W) + b
        self.x = x
        return out

    def backward(self,dout):
        W,b = self.params
        dx = np.dot(dout, W.T)
        dW = np.dot(self.x.T, dout)
        db = np.sum(dout, axis=0)

        self.grads[0][...] = dW
        self.grads[1][...] = db
        return dx

class Softmax:
    def __init__(self):
        self.params, self.grads = [], []
        self.out = None

    def forward(self, x):
        self.out = softmax(x)
        return self.out

    def backward(self, dout):
        dx = self.out * dout
        sumdx = np.sum(dx, axis=1, keepdims=True)
        dx -= self.out * sumdx 
        return dx

class SigmoidWithLoss:
    def __init__(self):
        self.params, self.grads = [], []
        self.loss = None
        self.y = None #sigmoidの出力
        self.t = None #教師データ

    def forward(self, x, t):
        self.t = t
        self.y = 1 / ( 1 + np.exp(-x))

        self.loss = cross_entoropy_error(np.c_[1 - self.y, self.y], self.t)

        return self.loss
