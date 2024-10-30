from enum import Enum

from src.constants import DATA_PATH


class Datasets(str, Enum):
    BREAST_CANCER = "breast_cancer_coimbra"
    WINE_RED = "wine_red"

    def get_path(self) -> str:
        match self:
            case Datasets.BREAST_CANCER:
                return f"{DATA_PATH}/breast_cancer_coimbra_"
            case Datasets.WINE_RED:
                return f"{DATA_PATH}/wine_red_"
