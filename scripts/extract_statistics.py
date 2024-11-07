import pandas as pd

from .config import load_config_from_args

SAVE_DIR = "./assets/statistics"

config = load_config_from_args()

df_all_iters = [
    (pd.read_csv(f"{config.path}/{config.var}-{j}-{config.name}.csv", comment="#"))
    for j in range(config.iter)
]

# Merge all DataFrames
df_concat = pd.concat(df_all_iters)

# Get test related data
df_concat_test = df_concat.query("Generation == 'T'")  # T is the Test

# Save test data
df_test = pd.DataFrame(
    data={
        "mean": [df_concat_test["BestFit"].mean()],
        "std": [df_concat_test["BestFit"].std()],
        "min": [df_concat_test["BestFit"].min()],
        "max": [df_concat_test["BestFit"].max()],
    }
)
df_test.to_csv(f"{SAVE_DIR}/{config.var}-{config.name}-test.csv", index=False)

# Remove test data and drop the non numeric column
df_concat_train = df_concat.query("Generation != 'T'").drop(columns=["Generation"])

# Aggregate train data
df_concat_train_mean = df_concat_train.groupby(by=df_concat_train.index).mean()
df_concat_train_std = df_concat_train.groupby(by=df_concat_train.index).std()

# Save train data
df_concat_train_mean.to_csv(f"{SAVE_DIR}/{config.var}-{config.name}-train-mean.csv", index=False)
df_concat_train_std.to_csv(f"{SAVE_DIR}/{config.var}-{config.name}-train-std.csv", index=False)
