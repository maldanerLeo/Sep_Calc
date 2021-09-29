import numpy as np
from Broyden import Broyden_method
from scipy.optimize import broyden1

def FUNC_TCC(X, N):
    global N_fix, Inc_index, Fix_index, X_fix

    F_val = np.zeros(N)

    Y = np.zeros(N+N_fix)

    for i in range(0, N):
        Y[Inc_index[i]] = X[i]

    for i in range(0, N_fix):
        Y[Fix_index[i]] = X_fix[i]

    F_val[0] = Y[0] * Y[1] - Y[3] * Y[4] - Y[6] * Y[7]
    F_val[1] = Y[0] * Y[2] - Y[3] * Y[5] - Y[6] * Y[8]
    F_val[2] = Y[1] + Y[2] - 1.0
    F_val[3] = Y[4] + Y[5] - 1.0
    F_val[4] = Y[7] + Y[8] - 1.0

    return F_val


N_inc = 5  # número de íncógnitas

N_fix = 4  # número de valores fixos

# Teste para manter fixo F, xf1, B e xb1 e calcular, xf2,  xb2, D, xd1 e xd2
# sendo o vetor organizado [F = Y[0], xf1=Y[1], xf2=Y[2], B=Y[3], xb1=Y[4], xb2=Y[5], D=Y[6], xd1=Y[7], xd2=Y[8]]

X0 = np.array([0.7, 0.7, 60.0, 0.3, 0.7])  # estimativa inicial para as íncógnitas, o valor da estimativa inicial é fundamental para a convergência

X_fix = np.array([100.0, 0.5, 50.0, 0.9])

Inc_index = [2, 5, 6, 7, 8]  # lista com o índice das incógnitas

Fix_index = [0, 1, 3, 4]  # lista dos índices dos valores fixos

# res = Broyden_method(FUNC_TCC, N_inc, X0, MaxIter= 7000, h = 1e-10, Tol = 1e-7)

res = broyden1(FUNC_TCC, X0)


print(res)
#print(res['X_sol'])
#print(res['FUN_sol'])
#print(res['n_iter'])