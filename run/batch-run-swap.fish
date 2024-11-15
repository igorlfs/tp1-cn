#!/usr/bin/env fish

set NUMBER_OF_REPETITIONS 10

set DEFAULT_ARGS --swap-operator-probability 0.5 --leaf-probability 0.1 --crossover-probability 0.9 --mutation-probability 0.3 --tournament-size 2 --elitism-size 1 --max-generations 100 --population-size 100 --max-depth 7 --verbose breast_cancer_coimbra

set LOG_DIR "./dumps"

set BASE_NAME "swap-ter"

set SHELL_SEED 634441

random $SHELL_SEED

set SEED_MIN 100000
set SEED_MAX 999999

for i in 0.2 0.8
    for j in (seq 1 $NUMBER_OF_REPETITIONS)
        set SEED (random $SEED_MIN $SEED_MAX)
        set ARGS $DEFAULT_ARGS --swap-terminal-probability $i --seed $SEED
        uv run python -m src $ARGS > "$LOG_DIR/$i-$(math $j - 1)-$BASE_NAME.csv"
    end
    uv run python scripts/extract_statistics.py --path $LOG_DIR --name $BASE_NAME --iter $NUMBER_OF_REPETITIONS --var $i
end
