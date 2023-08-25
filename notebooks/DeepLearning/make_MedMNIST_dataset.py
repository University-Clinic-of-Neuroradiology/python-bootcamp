import os
import medmnist
import pandas as pd

from typing import Text
from medmnist.info import INFO


DATASET = 'chestmnist'
FOLDER = 'data'
POSTFIX = 'png'
OUTPUT_CSV = 'data/dataset.csv'


def make_dataset() -> None:
    
    medmnist_csv_file = os.path.join(FOLDER, DATASET + '.csv')
    
    if not os.path.isfile(medmnist_csv_file):
        for split in ["train", "val", "test"]:
            print(f"Saving {DATASET} {split}...")
            dataset = getattr(medmnist, INFO[DATASET]['python_class'])(
                split=split, download=True)
            dataset.save(FOLDER, POSTFIX)  
            
    df = pd.read_csv('data/chestmnist.csv', header = None)
    cols = ['split', 'img'] + list(INFO['chestmnist']['label'].values())
    df = df.rename(columns={ i: col for i, col in enumerate(cols)})
    df['img'] = df['img'].apply(lambda x: os.path.join('data/chestmnist/', x))
    
    df.to_csv(OUTPUT_CSV, index = False)

if __name__ == '__main__':
    make_dataset()