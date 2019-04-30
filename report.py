import os
import re
import glob
import pandas as pd
import matplotlib.pyplot as plt


for path in glob.glob('log/*.out'):
    with open(path, 'r') as f:
        content = f.read()
    rows = []
    lines = content.split('\n')
    for line in lines:
        if 'Iteration' in line:
            items = [s.strip() for s in line.split('|')]
            iteration = re.findall(r'\d+', items[0])[0]
            losses = [s.split(':') for s in items[1:]]
            loss_dict = {k: float(v) for k, v in losses}
            loss_dict['iteration'] = iteration
            rows.append(loss_dict)
    df = pd.DataFrame(rows)
    df = df.set_index('iteration')
    df.plot(title=path)
    plt.show()
