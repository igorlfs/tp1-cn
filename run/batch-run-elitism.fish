#!/usr/bin/env fish

set NUMBER_OF_REPETITIONS 10

set DEFAULT_ARGS --leaf-probability 0.1 --swap-terminal-probability 0.5 --swap-operator-probability 0.5 --crossover-probability 0.9 --mutation-probability 0.3 --max-generations 100 --tournament-size 2 --population-size 100 --max-depth 7 --verbose breast_cancer_coimbra

set LOG_DIR "./dumps"

set BASE_NAME "elitism"

set SHELL_SEED 634441

random $SHELL_SEED

set SEED_MIN 100000
set SEED_MAX 999999

set i 0

for j in (seq 1 $NUMBER_OF_REPETITIONS)
    set SEED (random $SEED_MIN $SEED_MAX)
    set ARGS $DEFAULT_ARGS --elitism-size $i --seed $SEED
    uv run python -m src $ARGS > "$LOG_DIR/$i-$(math $j - 1)-$BASE_NAME.csv"
end
uv run python scripts/extract_statistics.py --path $LOG_DIR --name $BASE_NAME --iter $NUMBER_OF_REPETITIONS --var $i
