from scipy.stats import wilcoxon

def statisticalTestForIntegrals(x, y):
    w = wilcoxon(x, y)
    return "Nie ma podstaw do odrzucenia H_0" if not w.pvalue < .05 else "Są podstawy do odrzucenia H_0"