########################################################################################################
### Autor: Vilmar Steffen                                                                            ###
### Data: 06/05/2019                                                                                 ###
### Descrição: Programa para chamar o módulo que executa o método de Broyden (1965).                 ###
########################################################################################################
########################################################################################################
import numpy as np
from math import exp, sin, cos, pi
from Broyden import Broyden_method

### primeiro teste com um problema convencional: número de incógnitas é igual ao número de equações
def FUNC_NOME(X, N):
    x1 = X[0]
    x2 = X[1]
    x3 = X[2]

    F_val = np.zeros(N)

    F_val[0] = x1 + exp(x1 - 1) + (x2 + x3) ** 2 - 27

    F_val[1] = exp(x2 - 2) / x1 + x3 ** 2 - 10

    F_val[2] = x3 + sin(x2 - 2) + x1 ** 2 - 7

    return F_val


N = 3
X0 = [5.0,5.0,5.0]



res = Broyden_method(FUNC_NOME, N, X0, MaxIter= 7000, h = 1e-10, Tol = 1e-7)

print(res)
print(res['X_sol'])
print(res['FUN_sol'])
print(res['n_iter'])


### Agora um teste para um caso similar ao que vai ser abordado no TCC no qual o número de incógnitas é maior que o
### número de equaçõe e por isso algumas destas incógnitas tem o valor fixado pelo usuário
def FUNC_NOME2(X, N):
    global N_fix, Inc_index, Fix_index, X_fix

    F_val = np.zeros(N)

    Y = np.zeros(N+N_fix)

    for i in range(0,N):
        Y[Inc_index[i]] = X[i]

    for i in range(0,N_fix):
        Y[Fix_index[i]] = X_fix[i]

    F_val[0] = Y[0] + exp(Y[0] - 1) + (Y[1] + Y[2]) ** 2.0 - 27.0 + cos(Y[3] - pi)

    F_val[1] = exp(Y[1] - 2.0) /Y[0]  + Y[2] ** 2.0 - 10.0 + 5.0 * Y[3] ** 2.0

    F_val[2] = Y[2] + sin(Y[1] - 2) + Y[0] ** 2.0 - 7.0 + exp(Y[3] ** 2.0 - 1.0)

    return F_val

N_inc = 3  # número de íncógnitas

N_fix = 1  # número de valores fixos

X0 = np.array([4.0,2.0,1.0]) # estimativa inicial para as íncógnitas, o valor da estimativa inicial é fundamental para a convergência

X_fix = np.array([2.0])

Inc_index = [1, 2, 3]  # lista com o índice das incógnitas

Fix_index = [0] # lista dos índices dos valores fixos


res = Broyden_method(FUNC_NOME2, N_inc, X0, MaxIter= 7000, h = 1e-10, Tol = 1e-7)

print(res)
print(res['X_sol'])
print(res['FUN_sol'])
print(res['n_iter'])
