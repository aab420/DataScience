# import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt

# np.random.seed(0)
# sns.set()
# uniform_data = np.random.rand(10, 12)
# ax = sns.heatmap(uniform_data, vmin=0, vmax=1)
# plt.show()

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy
plt.figure(figsize=(12,10), dpi= 80)
df = pd.read_csv('student.csv')
sns.heatmap(df.corr(), xticklabels=df.corr().columns, yticklabels=df.corr().columns, cmap='RdYlGn', center=0, annot=True)
plt.title('Spotify & YouTube Heatmap', fontsize = 22)
plt.show()

