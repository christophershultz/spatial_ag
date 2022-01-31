import matplotlib.pyplot as plt
import os, pdb
from matplotlib.pyplot import figure

figure(figsize=(24, 18), dpi=999)

root = os.getcwd() + "\\images\\"

dct = {'net_income': root + 'lisa_netincome.png',
       'fertilizer': root + 'lisa_fertilizer.png',
       'fuel': root + 'lisa_fuel.png',
       'labor': root + 'lisa_labor.png',
       'land': root + 'lisa_land.png',
       'machinery': root + 'lisa_machinery.png',
       'tractors': root + 'lisa_tractors.png',
       'trucks': root + 'lisa_trucks.png'}

keys = list(dct.keys())
ct = 0 

fig, axes = plt.subplots(4, 2)
for row in [0, 1, 2, 3]: 
    for col in [0, 1]: 
        key = keys[ct]
        ct += 1
        ax = axes[row, col]
        ax.set_title(key, fontsize = 6)
        ax.axis('off')
        ax.imshow(plt.imread(dct[key]))
plt.tight_layout()
plt.savefig(os.getcwd() + '\\images\\' + 'lisa_combined.pdf')