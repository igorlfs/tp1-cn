import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from config import load_config_from_args

SAVE_DIR = "./assets/plots"
PLOT_ATTRIBUTE_FILE_NAME = "repetitions"
PLOT_ATTRIBUTE = PLOT_ATTRIBUTE_FILE_NAME.capitalize()

config = load_config_from_args()

PATH = config.path
ATTRIBUTE_VALUE = config.var
ATTRIBUTE = config.name
ITERATIONS = config.iter

# Read
df_all_iters = [
    (pd.read_csv(f"{PATH}/{ATTRIBUTE_VALUE}-{j}-{ATTRIBUTE}.csv", comment="#"))
    for j in range(ITERATIONS)
]

# Drop Test Row
df_all_iters = [df.query("Generation != 'T'") for df in df_all_iters]

# Convert Generation to int
for k in range(ITERATIONS):
    df_all_iters[k][["Generation"]] = (
        df_all_iters[k][["Generation"]].apply(lambda x: [y[1:] for y in x]).astype(int)
    )

# Merge Data
all_data = pd.concat([df.assign(df_id=i) for i, df in enumerate(df_all_iters)], ignore_index=True)

# Enable Seaborn Theme
sns.set_theme()

# Plot
plt.figure(figsize=(10, 6))
sns.lineplot(data=all_data, x="Generation", y="Repetitions", color="b")


plt.title(f"{PLOT_ATTRIBUTE} for {ATTRIBUTE} = {ATTRIBUTE_VALUE} ({ITERATIONS} iterations)")
plt.xlabel("Generation")
plt.ylabel(f"{PLOT_ATTRIBUTE}")
plt.savefig(f"{SAVE_DIR}/{ATTRIBUTE_VALUE}-{ATTRIBUTE}-mean-{PLOT_ATTRIBUTE_FILE_NAME}.png")
