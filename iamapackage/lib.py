import os

import numpy as np
import pandas as pd
from pkg_resources import resource_filename

def read_data():
    raw_csv = resource_filename('iamapackage', 'data/raw.csv')
    print('Path iamapackage.read_data :{}'.format(os.getcwd()))
    print(pd.read_csv(raw_csv))

def write_data():
    output_csv = resource_filename('iamapackage', 'data/output_csv.csv')
    print('Path iamapackage.write_data :{}'.format(os.getcwd()))
    df = pd.DataFrame(np.random.randn(10, 5), columns = ['a', 'b', 'c', 'd', 'e'])
    df.to_csv(output_csv)