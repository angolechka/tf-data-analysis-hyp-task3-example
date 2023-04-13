import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest as ztest

chat_id = 266642884  # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: int) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.06
    stat, pval = ztest(x, value=y, alternative='smaller')
    return pval < alpha # Ваш ответ, True или False
