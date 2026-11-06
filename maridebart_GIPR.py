# maridebart_GIPR.py

import numpy as np
import matplotlib.pyplot as plt

def Fact(L1, L2, Kd1, Kd2):
    """Fractional receptor activation with two agonists L1 and L2"""
    return (Kd2*L1) / (Kd1*Kd2 + Kd2*L1 + Kd1*L2)

# Dissociation constants [nM] for each ligand at GIPR
Kd1 = 0.2   # L1, GIP
Kd2 = 0.037 # L2, maridebart

# Ligand concentration, 0.001 to 100 [nM] (centered on the sub-nM Kd values)
L1 = 0.1 # [nM] GIP
L2 = np.logspace(-3, 2, 500) # [nM] maridebart

plt.figure()
line, = plt.semilogx(L2, Fact(L1, L2, Kd1, Kd2), lw=2,
                     label=f"GIP ({L1} nM)")
# Baseline activation from GIP alone (no maridebart), same color as its curve
plt.ylim(0, 1)
plt.xlabel("[maridebart] (nM, log scale)")
plt.ylabel("Fraction active (Fact)")
plt.title("GIPR activation by maridebart with GIP present")
plt.legend(loc="upper left")
plt.show()
