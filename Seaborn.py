# Data Visualization Library
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Import dataset from seaborn library
tips = sns.load_dataset( "tips")
# This data will be imported in the form of panda libaray data
tips.head()
# This will import top 5 rows from tips dataset
tips.tail()
# This will import 5 ending rows from tips dataset
