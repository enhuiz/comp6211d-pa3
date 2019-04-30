import os
import re
import glob
import pandas as pd
import matplotlib.pyplot as plt
# plt.style.use('ggplot')


def read(path):
    with open(path, 'r') as f:
        return f.read()


def plot_loss(path):
    content = read(path)
    lines = content.split('\n')

    rows = []
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
    df.plot(figsize=(10, 5))
    plt.legend(loc='upper right')
    img_path = 'report/fig/{}.png'.format(path.split('/')[-1].strip('.out'))
    plt.savefig(img_path)
    return '![title]({})'.format(img_path)


for path in glob.glob('log/*.out'):
    md = plot_loss(path)
    print(md)
