import os
import pandas as pd

# dataFolder = 'NewData'

# paths = []
# labels = []
# for syllable in os.listdir(dataFolder):
#     syllableFolder = dataFolder + '/' + syllable
#     for file in os.listdir(syllableFolder):
#         paths.append(syllableFolder + '/' + file)
#         labels.append(syllable)

# metadata = pd.DataFrame({
#     'path': paths,
#     'label': labels
# })

# metadata.to_parquet(dataFolder + '/metadata.parquet')

# Checking
# metadata = pd.read_parquet('NewData/metadata.parquet')
# print(metadata['label'].unique())

dataset_path = "NewData"
metadata_path = dataset_path + "/metadata.parquet"
metadata_df = pd.read_parquet(metadata_path)
dataset = []

for index, row in metadata_df.iterrows():
    dataset.append([row['path'], row['label']])

vocab = metadata_df['label'].unique()
print(vocab)