# Predict Who is Alcoholic

import pandas as pd
import numpy as np

# Data loading code:
def import_eeg_file(file_obj, df_type='wide', optimize=True):
    """
    Imports a file for a single EEG file and returns a wide or long dataframe.

    Parameters
    ----------
    file_obj
        A file-like object, such as a GzipFile, or a TextIOWrapper,
        or a regular file (such as from `open(<filename>)`)

    df_type : str, opt
        'long' or 'wide'.  If you want a 'long' dataframe or a 'wide' dataframe as an output.

    optimize: bool, opt
        True if you want data types to be coerced into their minimum sizes, false if you don't.

    Returns
    -------
    pandas.DataFrame

        The data from this file in a DataFrame object.
    """

    def parse_subject(line):
        return line[2:-4]

    def parse_alcoholic(line):
        char = line.strip('# ')[3]
        return True if char == 'a' else False

    def parse_obj(line):
        char = line.strip('# ')[1]
        return True if char == '1' else False

    def parse_match(line):
        string = line.strip('# ').split(',')[0].split(' ')[1]
        if string == 'nomatch':
            return 'nomatch'
        elif string == 'obj':
            return 'obj'
        elif string == 'match':
            return 'match'

    def parse_err(line):
        strings = line.strip('# ').split(',')[0].split(' ')
        if len(strings) == 3 and strings[2] == 'err':
            return True
        else:
            return False

    from io import TextIOWrapper
    if isinstance(file_obj, TextIOWrapper):
        text_obj = file_obj
    else:
        text_obj = TextIOWrapper(file_obj)

    header = []
    loc = None
    while True:
        loc = text_obj.tell()
        newline = text_obj.readline()
        if newline[0] == "#":
            header += [newline]
        else:
            text_obj.seek(loc)
            break

    subject = parse_subject(header[0])
    alcoholic = parse_alcoholic(header[0])
    obj = parse_obj(header[3])
    match = parse_match(header[3])
    err = parse_err(header[3])

    df = pd.read_csv(text_obj, sep=' ', header=None, names=['trial', 'sensor', 'sample', 'value'],
                     comment='#')
    df['alcoholic'] = alcoholic
    df['object'] = obj
    df['match'] = match
    df['err'] = err
    df['subject'] = subject

    df = df[['subject', 'trial', 'alcoholic', 'match', 'err', 'sensor', 'sample', 'value']]

    if optimize:
        df[['trial', 'sample']] = df[['trial', 'sample']].apply(pd.to_numeric, downcast='unsigned')
        df['value'] = df['value'].astype(np.float32)
        df['sensor'] = pd.Categorical(df['sensor'])
        df['match'] = pd.Categorical(df['match'])
        df['subject'] = pd.Categorical(df['subject'])

    if df_type == 'wide':
        df = df.pivot_table(values='value', index='sample',
                            columns=['subject', 'trial', 'alcoholic', 'match', 'err', 'sensor'])

    if df_type == 'long':
        df = df.set_index(['subject', 'trial', 'alcoholic', 'match', 'err', 'sample'])

    return df





