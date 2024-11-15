#!/usr/bin/env fish

set NUMBER_OF_REPETITIONS 10

set DEFAULT_ARGS --leaf-probability 0.1 --swap-terminal-probability 0.5 --swap-operator-probability 0.5 --tournament-size 2 --elitism-size 1 --max-generations 100 --population-size 100 --max-depth 7 --verbose breast_cancer_coimbra

set LOG_DIR "./dumps"

set BASE_NAME "operators-both-swapped"

set SHELL_SEED 634441

# Default is 0.9
set CROSSOVER_PROB 0.6

# Default is 0.05
set MUTATION_PROB 0.3

random $SHELL_SEED

set SEED_MIN 100000
set SEED_MAX 999999

for j in (seq 1 $NUMBER_OF_REPETITIONS)
    set SEED (random $SEED_MIN $SEED_MAX)
    set ARGS $DEFAULT_ARGS --crossover-probability $CROSSOVER_PROB --mutation-probability $MUTATION_PROB --seed $SEED
    uv run python -m src $ARGS > "$LOG_DIR/$BASE_NAME-$(math $j - 1).csv"
end
uv run python scripts/extract_statistics.py --path $LOG_DIR --name $BASE_NAME --iter $NUMBER_OF_REPETITIONS 
