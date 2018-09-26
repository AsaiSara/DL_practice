import sys 
sys.path.append('..')#親ディレクトリのファイルをインポートするための設定
from dataset import spiral
import matplotlib.pyplot as plt

x, t = spiral.load_data()
print('x', x.shape)
print('t', t.shape)
