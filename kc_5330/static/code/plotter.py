# %%
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
import os

# %%
target_file='cdkn2a_2b_variant_location.txt'

# %%
counter = {}
with open(target_file, 'r') as f:
    lines = f.readlines()
for line in lines:
    tmp = counter.get(line, -1) + 1
    counter[line] = tmp
counter = dict(sorted(counter.items(), key=lambda item: item[1], reverse=False))

# %%
plt.barh(counter.keys(), counter.values())
plt.xlim(0, max(counter.values()) * 1.1)
plt.xlabel('Count')
plt.ylabel('Categories')
plt.title('Count of First Column Values')
for idx, (key, val) in enumerate(counter.items()):
    plt.text(val, key, str(val), va='center', ha='left')
plt.tight_layout()
plt.savefig('col1_graph.png')
plt.show()



