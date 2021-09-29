########################################################################################################
### Autor: Vilmar Steffen                                                                            ###
### Data: 06/05/2019                                                                                 ###
### Descrição: Módulo para a execução do método de Broyden (1965) para solução de um sistema         ###
###             de equações não lineares                                                             ###
########################################################################################################
########################################################################################################

import numpy as np


def Jacobian_numeric(FUN, X, N, h):

    Jac = np.zeros((N,N))
    X_sup = np.zeros(N)
    X_inf = np.zeros(N)
    FUN_sup = np.zeros(N)
    FUN_inf = np.zeros(N)


    try:
        for j in range(0, N):
            X_sup = X[:]
            X_sup[j] = X[j] * (1.0 + h)
            FUN_sup = FUN(X_sup, N)
            X_inf = X[:]
            X_inf[j] = X[j] * (1.0 - h)
            FUN_inf = FUN(X_inf, N)

            for i in range(0, N):
                Jac[i, j] = (FUN_sup[i] - FUN_inf[i]) / (2.0 * h * X[j])
    except:
        ### Para evitar erro de execução caso alguma das raízes se aproxime de zero.

        for j in range(0, N):
            X_sup = X[:]
            X_sup[j] = X[j] + h
            FUN_sup = FUN(X_sup, N)
            X_inf = X[:]
            X_inf[j] = X[j] - h
            FUN_inf = FUN(X_inf, N)

            for i in range(0,N):
                Jac[i, j] = (FUN_sup[i] - FUN_inf[i]) / (2.0 * h)


    return Jac


def Gauss_pivo_parcial(A, B, N):


    X = np.zeros(N)

    for k in range(0, N-1):

        ### pivoteamento parcial
        for i in range(k+1, N):
            if abs(A[i,k]) > abs(A[k, k]):
                aux = B[k]
                B[k] = B[i]
                B[i] = aux

                for j in range(k, N):
                    aux = A[k, j]
                    A[k, j] = A[i, j]
                    A[i, j] = aux

        for i in range(k+1,N):
            m = A[i, k] / A[k, k]
            for j in range(k, N):
                A[i, j] = A[i, j] - m * A[k,j]
            B[i] = B[i] - m * B[k]

    for k in range (0, N):
        Sum = 0.0

        for i in range(N-k, N):
            Sum += A[N-k-1, i] * X[i]

        X[N-k-1] = (B[N-k-1] - Sum) / A[N-k-1, N-k-1]

    return X


def Broyden_method(FUN, N, Xguess, MaxIter = 100000, h = 1e-10, Tol = 1e-7):

    X = np.zeros(N)
    X_new = np.zeros(N)
    F = np.zeros(N)
    F_new = np.zeros(N)
    B = np.zeros(N)
    A = np.zeros((N, N))

    s_min = 1e-3  # passo mínimo apenas para sair da aproximação atual

    X = Xguess

    F = FUN(X, N)

    Iter = 0

    while True:

        Iter += 1

        A = Jacobian_numeric(FUN, X, N, h)

        B = - F

        DeltaX = Gauss_pivo_parcial(A, B, N)

        s = 1.0

        X_new = X + s * DeltaX

        F = FUN(X, N)

        F_new = FUN(X_new, N)

        Sum_FUN = 0.0
        Sum_FUN_new = 0.0
        for i in range(0, N):
            Sum_FUN += F[i] ** 2.0
            Sum_FUN_new += F_new[i] ** 2.0

        Sum_FUN = Sum_FUN ** 0.5
        Sum_FUN_new = Sum_FUN_new ** 0.5

        eta = Sum_FUN_new / Sum_FUN

        if eta > 1.0:
            s = ((1.0 + 6.0 * eta) ** 0.5 - 1.0 ) / (3.0 * eta)
            X_new = X + s * DeltaX
            F_new = FUN(X_new, N)

            Sum_FUN_new = 0.0
            for i in range(0, N):
                Sum_FUN_new += F_new[i] ** 2.0

            Sum_FUN_new = Sum_FUN_new ** 0.5

            eta2 = Sum_FUN_new / Sum_FUN

            ### Para o caso de mesmo com a redução do tamanho do passo o método não funcione
            ### Então, a ideia e dar apenas um passo muito pequeno.
            if eta2 > 1.0:
                s = s_min
                X_new = X + s * DeltaX
                F_new = FUN(X_new, N)

        X = X_new

        F = F_new

        if Iter >= MaxIter:
            Final_condition = False
            break
        elif Sum_FUN_new <= Tol:
            Final_condition = True
            break
    return ['{:.2f}'.format(X[0]), '{:.2f}'.format(X[1]), '{:.2f}'.format(X[2]), '{:.2f}'.format(X[3]), '{:.2f}'.format(X[4]),  Final_condition]
    #return {'X_sol': X, 'FUN_sol': F, 'n_iter': Iter, 'Message': Final_condition}