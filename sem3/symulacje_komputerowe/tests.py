from scipy import stats

class Tests:
    def __init__(self):
        pass

    # Normal distribution tests
    def shapiroWilk(x):
        print("Shapiro-Wilk test", end=" - ")
        testRes = stats.shapiro(x)
        return "Sa podstawy do odrzucenia H_0" if not testRes.pvalue < 0.5 else "Nie ma podstaw do odrzucenia H_0"    
    
    def wilcoxon(x1, x2):
        print("Wilcoxon test", end=" - ")
        testRes = stats.wilcoxon(x1, x2)
        return "Sa podstawy do odrzucenia H_0" if not testRes.pvalue < 0.5 else "Nie ma podstaw do odrzucenia H_0"    

    # Unfiorm distribution tests
    def kolmogorovSmirnov(x):
        print("Kolmogorov-Smirnov test", end=" - ")
        testRes = stats.ks_1samp(x, stats.uniform.cdf)
        return "Sa podstawy do odrzucenia H_0" if not testRes.pvalue < 0.5 else "Nie ma podstaw do odrzucenia H_0"        

    def chiSquare(x):
        print("Chi-square test", end=" - ")
        testRes = stats.chisquare(x)
        return "Sa podstawy do odrzucenia H_0" if not testRes.pvalue < 0.5 else "Nie ma podstaw do odrzucenia H_0"        
