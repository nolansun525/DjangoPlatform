# !pip install brewer2mpl
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')

large = 22; med = 16; small = 12
params = {'axes.titlesize': large,
          'legend.fontsize': med,
          'figure.figsize': (16, 10),
          'axes.labelsize': med,
          'axes.titlesize': med,
          'xtick.labelsize': med,
          'ytick.labelsize': med,
          'figure.titlesize': large}
plt.rcParams.update(params)
plt.style.use('seaborn-whitegrid')
sns.set_style("white")
# %matplotlib inline

# Version
print(mpl.__version__)  # >> 3.0.2
print(sns.__version__)  # >> 0.9.0



def draw(request):
    # Prepare Data

    df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mtcars.csv")

    x = df.loc[:, ['mpg']]

    df['mpg_z'] = (x - x.mean()) / x.std()

    df['colors'] = ['red' if x < 0 else 'green' for x in df['mpg_z']]

    df.sort_values('mpg_z', inplace=True)

    df.reset_index(inplace=True)

    # Draw plot

    plt.figure(figsize=(14, 10), dpi=80)

    plt.hlines(y=df.index, xmin=0, xmax=df.mpg_z, color=df.colors, alpha=0.4, linewidth=5)

    # Decorations

    plt.gca().set(ylabel='$Model$', xlabel='$Mileage$')

    plt.yticks(df.index, df.cars, fontsize=12)

    plt.title('Diverging Bars of Car Mileage', fontdict={'size': 20})

    plt.grid(linestyle='--', alpha=0.5)
    plt.show()
    plt.ren


