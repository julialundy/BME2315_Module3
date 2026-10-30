import numpy as np
import matplotlib.pyplot as plt

def Fact(G, S, Kd1, Kd2):
    """Fraction of Active GLP1R with GLP1 (G) and Semaglutide (S) Co-Stimulating:
       Fact = (Kd2*G + Kd1*S) / (Kd1*Kd2 + Kd2*G + Kd1*S)"""
    return (Kd2*G + Kd1*S) / (Kd1*Kd2 + Kd2*G + Kd1*S)

Kd1 = 0.17     # GLP1 dissociation constant [nM]
Kd2 = 0.38     # semaglutide dissociation constant [nM]
G_fast = 0.015 # fasting GLP1 [nM]
G_fed  = 0.040 # after-meal GLP1 [nM]
S_dose = 1.0   # typical semaglutide level [nM]

S = np.logspace(-3, 3, 500)   # semaglutide concentration with 0.001 to 1,000 [nM]

plt.figure(figsize=(7, 6))
plt.semilogx(S, Fact(G_fast, S, Kd1, Kd2), lw=2, label="GLP1 (fasting) ~ 0.0150 nM")
plt.semilogx(S, Fact(G_fed,  S, Kd1, Kd2), lw=2, ls="--", label="GLP1 (after meal) ~ 0.040 nM")
plt.axvline(S_dose, ls=":", c="gray", lw=1, label="Semaglutide ~1 nM")
plt.ylim(0, 1)
plt.xlabel("[Semaglutide] (nM, log scale)")
plt.ylabel("Fraction Active GLP1R (Fact)")
plt.title("GLP1 and Semaglutide Co-stimulation of GLP1R")
plt.legend(loc="upper left")

# Interpretation of the results
interpretation = ("The fraction of active GLP1R (Fact) is higher after a meal than when fasting (~19% vs. ~8%), unless semaglutide is present: with semaglutide ~1 nM, Fact is nearly equal for the two conditions (~74% vs. ~73%), showing how co-stimulation makes Fact similar after a meal and when fasting.")
plt.subplots_adjust(bottom=0.3)
plt.figtext(0.5, 0.02, interpretation, wrap=True, ha="center", fontsize=9)

plt.show()

# Response with no semaglutide vs. at ~1 nM semaglutide
print("No semaglutide: GLP1 (fasting):", Fact(G_fast, 0, Kd1, Kd2)) 
print("No semaglutide: GLP1 (after meal):", Fact(G_fed, 0, Kd1, Kd2))
print("1 nM semaglutide: GLP1 (fasting):", Fact(G_fast, S_dose, Kd1, Kd2))
print("1 nM semaglutide: GLP1 (after meal):", Fact(G_fed, S_dose, Kd1, Kd2))