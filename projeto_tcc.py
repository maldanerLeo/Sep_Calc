from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
import numpy as np
from Broyden import Broyden_method
from kivy.uix.popup import Popup


class FirstWindow(Screen):
    pass


class SecondWindow(Screen):

    def get_num(self, a):
        f = self.f.text
        t = self.t.text
        b = self.b.text
        xf1 = self.xf1.text
        xf2 = self.xf2.text
        xt1 = self.xt1.text
        xt2 = self.xt2.text
        xb1 = self.xb1.text
        xb2 = self.xb2.text

        v_val = []
        v_var = []
        index_val = []
        index_var = []
        val_0 = []

        if f == 'f' or f =='F' or f == '':
            v_var.append('F')
            index_var.append(0)
            val_0.append(1000)
        else:
            try:
                v_val.append(float(f))
                index_val.append(0)
            except:
                po = PopUp()
                po.open()
                self.t.text = 'T'
                self.b.text = 'B'
                self.f.text = 'F'
                self.xt1.text = 'xt1'
                self.xt2.text = 'xt2'
                self.xb1.text = 'xb1'
                self.xb2.text = 'xb2'
                self.xf1.text = 'xf1'
                self.xf2.text = 'xf2'

        if b == 'b' or b == 'B' or b == '':
            v_var.append('B')
            index_var.append(3)
            val_0.append(500)
        else:
            try:
                v_val.append(float(b))
                index_val.append(3)
            except:
                po = PopUp()
                po.open()
                self.t.text = 'T'
                self.b.text = 'B'
                self.f.text = 'F'
                self.xt1.text = 'xt1'
                self.xt2.text = 'xt2'
                self.xb1.text = 'xb1'
                self.xb2.text = 'xb2'
                self.xf1.text = 'xf1'
                self.xf2.text = 'xf2'

        if t == 't' or  t== 'T' or t == '':
            v_var.append('T')
            index_var.append(6)
            val_0.append(500)
        else:
            try:
                v_val.append(float(t))
                index_val.append(6)
            except:
                po = PopUp()
                po.open()
                self.t.text = 'T'
                self.b.text = 'B'
                self.f.text = 'F'
                self.xt1.text = 'xt1'
                self.xt2.text = 'xt2'
                self.xb1.text = 'xb1'
                self.xb2.text = 'xb2'
                self.xf1.text = 'xf1'
                self.xf2.text = 'xf2'

        if xf1 == 'xf1'or xf1 == 'XF1' or xf1 == '':
            v_var.append('xf1')
            index_var.append(1)
            val_0.append(0.5)
        else:
            try:
                v_val.append(float(xf1))
                index_val.append(1)
            except:
                po = PopUp()
                po.open()
                self.t.text = 'T'
                self.b.text = 'B'
                self.f.text = 'F'
                self.xt1.text = 'xt1'
                self.xt2.text = 'xt2'
                self.xb1.text = 'xb1'
                self.xb2.text = 'xb2'
                self.xf1.text = 'xf1'
                self.xf2.text = 'xf2'

        if xf2 == 'xf2' or xf2 == 'XF2' or xf2 == '':
            v_var.append('xf2')
            index_var.append(2)
            val_0.append(0.5)
        else:
            try:
                v_val.append(float(xf2))
                index_val.append(2)
            except:
                po = PopUp()
                po.open()
                self.t.text = 'T'
                self.b.text = 'B'
                self.f.text = 'F'
                self.xt1.text = 'xt1'
                self.xt2.text = 'xt2'
                self.xb1.text = 'xb1'
                self.xb2.text = 'xb2'
                self.xf1.text = 'xf1'
                self.xf2.text = 'xf2'

        if xb1 == 'xb1' or xb1 == 'XB1' or xb1 == '':
            xb1 = 'xb1'
            v_var.append(xb1)
            index_var.append(4)
            val_0.append(0.5)
        else:
            try:
                v_val.append(float(xb1))
                index_val.append(4)
            except:
                po = PopUp()
                po.open()
                self.t.text = 'T'
                self.b.text = 'B'
                self.f.text = 'F'
                self.xt1.text = 'xt1'
                self.xt2.text = 'xt2'
                self.xb1.text = 'xb1'
                self.xb2.text = 'xb2'
                self.xf1.text = 'xf1'
                self.xf2.text = 'xf2'

        if xb2 == 'xb2' or xb2 == 'XB2' or xb2 == '':
            xb2 = 'xb2'
            v_var.append(xb2)
            index_var.append(5)
            val_0.append(0.5)
        else:
            try:
                v_val.append(float(xb2))
                index_val.append(5)
            except:
                po = PopUp()
                po.open()
                self.t.text = 'T'
                self.b.text = 'B'
                self.f.text = 'F'
                self.xt1.text = 'xt1'
                self.xt2.text = 'xt2'
                self.xb1.text = 'xb1'
                self.xb2.text = 'xb2'
                self.xf1.text = 'xf1'
                self.xf2.text = 'xf2'

        if xt1 == 'xt1' or xt1 == 'XT1' or xt1 == '':
            xt1 = 'xt1'
            v_var.append(xt1)
            index_var.append(7)
            val_0.append(0.5)
        else:
            try:
                v_val.append(float(xt1))
                index_val.append(7)
            except:
                po = PopUp()
                po.open()
                self.t.text = 'T'
                self.b.text = 'B'
                self.f.text = 'F'
                self.xt1.text = 'xt1'
                self.xt2.text = 'xt2'
                self.xb1.text = 'xb1'
                self.xb2.text = 'xb2'
                self.xf1.text = 'xf1'
                self.xf2.text = 'xf2'

        if xt2 == 'xt2' or xt2 == 'XT2' or xt2 == '':
            xt2 = 'xt2'
            v_var.append(xt2)
            index_var.append(8)
            val_0.append(0.5)
        else:
            try:
                v_val.append(float(xt2))
                index_val.append(8)
            except:
                po = PopUp()
                po.open()
                self.t.text = 'T'
                self.b.text = 'B'
                self.f.text = 'F'
                self.xt1.text = 'xt1'
                self.xt2.text = 'xt2'
                self.xb1.text = 'xb1'
                self.xb2.text = 'xb2'
                self.xf1.text = 'xf1'
                self.xf2.text = 'xf2'
        i_val = 0
        i_var = 0
        for i in v_var:
            i_var += 1
        for i in v_val:
            i_val += 1

        if i_val != 4 or i_var != 5:

            po = PopUp()
            po.open()
            self.t.text = 'T'
            self.b.text = 'B'
            self.f.text = 'F'
            self.xt1.text = 'xt1'
            self.xt2.text = 'xt2'
            self.xb1.text = 'xb1'
            self.xb2.text = 'xb2'
            self.xf1.text = 'xf1'
            self.xf2.text = 'xf2'

        else:
            try:
                def FUNC_TCC(X, N):

                    global N_fix, Inc_index, Fix_index, X_fix

                    X_fix = np.array([v_val[0], v_val[1], v_val[2], v_val[3]])
                    Inc_index = index_var
                    Fix_index = index_val
                    N_fix = 4

                    F_val = np.zeros(N)

                    Y = np.zeros(N + N_fix)

                    for i in range(0, N):
                        Y[Inc_index[i]] = X[i]

                    for i in range(0, N_fix):
                        Y[Fix_index[i]] = X_fix[i]

                    F_val[0] = Y[0] * Y[1] - Y[3] * Y[4] - Y[6] * Y[7]
                    F_val[1] = Y[0] * Y[2] - Y[3] * Y[5] - Y[6] * Y[8]
                    F_val[2] = Y[1] + Y[2] - 1.0
                    F_val[3] = Y[4] + Y[5] - 1.0
                    F_val[4] = Y[7] + Y[8] - 1.0

                    np.set_printoptions(precision=2)
                    return F_val

                X0 = np.array([val_0[0], val_0[1], val_0[2], val_0[3], val_0[4]])
                N_inc = 5
                res = Broyden_method(FUNC_TCC, N_inc, X0, MaxIter=7000, h=1e-10, Tol=1e-7)

                if float(res[0]) >= 0 and float(res[1]) >=0 and float(res[2])>=0 and float(res[3])>=0 and float(res[4]) >=0:

                    if index_var[0] == 0:
                        self.f.text = str(res[0])
                        self.f.background_color = 0, 1, 1, 1
                    elif index_var[0] == 1:
                        self.xf1.text = str(res[0])
                        self.xf1.background_color = 0, 1, 1, 1
                    elif index_var[0] == 2:
                        self.xf2.text = str(res[0])
                        self.xf2.background_color = 0, 1, 1, 1
                    elif index_var[0] == 3:
                        self.b.text = str(res[0])
                        self.b.background_color = 0, 1, 1, 1
                    elif index_var[0] == 4:
                        self.xb1.text = str(res[0])
                        self.xb1.background_color = 0, 1, 1, 1
                    elif index_var[0] == 5:
                        self.xb2.text = str(res[0])
                        self.xb2.background_color = 0, 1, 1, 1
                    elif index_var[0] == 6:
                        self.t.text = str(res[0])
                        self.t.background_color = 0, 1, 1, 1
                    elif index_var[0] == 7:
                        self.xt1.text = str(res[0])
                        self.xt1.background_color = 0, 1, 1, 1
                    elif index_var[0] == 8:
                        self.xt2.text = str(res[0])
                        self.xt2.background_color = 0, 1, 1, 1

                    if index_var[1] == 0:
                        self.f.text = str(res[1])
                        self.f.background_color = 0, 1, 1, 1
                    elif index_var[1] == 1:
                        self.xf1.text = str(res[1])
                        self.xf1.background_color = 0, 1, 1, 1
                    elif index_var[1] == 2:
                        self.xf2.text = str(res[1])
                        self.xf2.background_color = 0, 1, 1, 1
                    elif index_var[1] == 3:
                        self.b.text = str(res[1])
                        self.b.background_color = 0, 1, 1, 1
                    elif index_var[1] == 4:
                        self.xb1.text = str(res[1])
                        self.xb1.background_color = 0, 1, 1, 1
                    elif index_var[1] == 5:
                        self.xb2.text = str(res[1])
                        self.xb2.background_color = 0, 1, 1, 1
                    elif index_var[1] == 6:
                        self.t.text = str(res[1])
                        self.t.background_color = 0, 1, 1, 1
                    elif index_var[1] == 7:
                        self.xt1.text = str(res[1])
                        self.xt1.background_color = 0, 1, 1, 1
                    elif index_var[1] == 8:
                        self.xt2.text = str(res[1])
                        self.xt2.background_color = 0, 1, 1, 1

                    if index_var[2] == 0:
                        self.f.text = str(res[2])
                        self.f.background_color = 0, 1, 1, 1
                    elif index_var[2] == 1:
                        self.xf1.text = str(res[2])
                        self.xf1.background_color = 0, 1, 1, 1
                    elif index_var[2] == 2:
                        self.xf2.text = str(res[2])
                        self.xf2.background_color = 0, 1, 1, 1
                    elif index_var[2] == 3:
                        self.b.text = str(res[2])
                        self.b.background_color = 0, 1, 1, 1
                    elif index_var[2] == 4:
                        self.xb1.text = str(res[2])
                        self.xb1.background_color = 0, 1, 1, 1
                    elif index_var[2] == 5:
                        self.xb2.text = str(res[2])
                        self.xb2.background_color = 0, 1, 1, 1
                    elif index_var[2] == 6:
                        self.t.text = str(res[2])
                        self.t.background_color = 0, 1, 1, 1
                    elif index_var[2] == 7:
                        self.xt1.text = str(res[2])
                        self.xt1.background_color = 0, 1, 1, 1
                    elif index_var[2] == 8:
                        self.xt2.text = str(res[2])
                        self.xt2.background_color = 0, 1, 1, 1

                    if index_var[3] == 0:
                        self.f.text = str(res[3])
                        self.f.background_color = 0, 1, 1, 1
                    elif index_var[3] == 1:
                        self.xf1.text = str(res[3])
                        self.xf1.background_color = 0, 1, 1, 1
                    elif index_var[3] == 2:
                        self.xf2.text = str(res[3])
                        self.xf2.background_color = 0, 1, 1, 1
                    elif index_var[3] == 3:
                        self.b.text = str(res[3])
                        self.b.background_color = 0, 1, 1, 1
                    elif index_var[3] == 4:
                        self.xb1.text = str(res[3])
                        self.xb1.background_color = 0, 1, 1, 1
                    elif index_var[3] == 5:
                        self.xb2.text = str(res[3])
                        self.xb2.background_color = 0, 1, 1, 1
                    elif index_var[3] == 6:
                        self.t.text = str(res[3])
                        self.t.background_color = 0, 1, 1, 1
                    elif index_var[3] == 7:
                        self.xt1.text = str(res[3])
                        self.xt1.background_color = 0, 1, 1, 1
                    elif index_var[3] == 8:
                        self.xt2.text = str(res[3])
                        self.xt2.background_color = 0, 1, 1, 1

                    if index_var[4] == 0:
                        self.f.text = str(res[4])
                        self.f.background_color = 0, 1, 1, 1
                    elif index_var[4] == 1:
                        self.xf1.text = str(res[4])
                        self.xf1.background_color = 0, 1, 1, 1
                    elif index_var[4] == 2:
                        self.xf2.text = str(res[4])
                        self.xf2.background_color = 0, 1, 1, 1
                    elif index_var[4] == 3:
                        self.b.text = str(res[4])
                        self.b.background_color = 0, 1, 1, 1
                    elif index_var[4] == 4:
                        self.xb1.text = str(res[4])
                        self.xb1.background_color = 0, 1, 1, 1
                    elif index_var[4] == 5:
                        self.xb2.text = str(res[4])
                        self.xb2.background_color = 0, 1, 1, 1
                    elif index_var[4] == 6:
                        self.t.text = str(res[4])
                        self.t.background_color = 0, 1, 1, 1
                    elif index_var[4] == 7:
                        self.xt1.text = str(res[4])
                        self.xt1.background_color = 0, 1, 1, 1
                    elif index_var[4] == 8:
                        self.xt2.text = str(res[4])
                        self.xt2.background_color = 0, 1, 1, 1
                else:
                    self.status.text = 'Problema não resolvido'
                    self.t.text = '-'
                    self.t.background_color = 1, 1, 1, 1
                    self.b.text = '-'
                    self.b.background_color = 1, 1, 1, 1
                    self.f.text = '-'
                    self.f.background_color = 1, 1, 1, 1
                    self.xt1.text = '-'
                    self.xt1.background_color = 1, 1, 1, 1
                    self.xt2.text = '-'
                    self.xt2.background_color = 1, 1, 1, 1
                    self.xb1.text = '-'
                    self.xb1.background_color = 1, 1, 1, 1
                    self.xb2.text = '-'
                    self.xb2.background_color = 1, 1, 1, 1
                    self.xf1.text = '-'
                    self.xf1.background_color = 1, 1, 1, 1
                    self.xf2.text = '-'
                    self.xf2.background_color = 1, 1, 1, 1

                if res[5] is True:
                    self.status.text = 'Problema resolvido\ncom sucesso'
                else:
                    self.status.text = 'Problema não resolvido'
                    self.t.text = '-'
                    self.t.background_color = 1, 1, 1, 1
                    self.b.text = '-'
                    self.b.background_color = 1, 1, 1, 1
                    self.f.text = '-'
                    self.f.background_color = 1, 1, 1, 1
                    self.xt1.text = '-'
                    self.xt1.background_color = 1, 1, 1, 1
                    self.xt2.text = '-'
                    self.xt2.background_color = 1, 1, 1, 1
                    self.xb1.text = '-'
                    self.xb1.background_color = 1, 1, 1, 1
                    self.xb2.text = '-'
                    self.xb2.background_color = 1, 1, 1, 1
                    self.xf1.text = '-'
                    self.xf1.background_color = 1, 1, 1, 1
                    self.xf2.text = '-'
                    self.xf2.background_color = 1, 1, 1, 1




            except:
                self.status.text = 'Problema não resolvido'
                self.t.text = '-'
                self.t.background_color = 1, 1, 1, 1
                self.b.text = '-'
                self.b.background_color = 1, 1, 1, 1
                self.f.text = '-'
                self.f.background_color = 1, 1, 1, 1
                self.xt1.text = '-'
                self.xt1.background_color = 1, 1, 1, 1
                self.xt2.text = '-'
                self.xt2.background_color = 1, 1, 1, 1
                self.xb1.text = '-'
                self.xb1.background_color = 1, 1, 1, 1
                self.xb2.text = '-'
                self.xb2.background_color = 1, 1, 1, 1
                self.xf1.text = '-'
                self.xf1.background_color = 1, 1, 1, 1
                self.xf2.text = '-'
                self.xf2.background_color = 1, 1, 1, 1

    def limpar(self, d):

        self.t.text = 'T'
        self.t.background_color = 1, 1, 1, 1
        self.b.text = 'B'
        self.b.background_color = 1, 1, 1, 1
        self.f.text = 'F'
        self.f.background_color = 1, 1, 1, 1
        self.xt1.text = 'xt1'
        self.xt1.background_color = 1, 1, 1, 1
        self.xt2.text = 'xt2'
        self.xt2.background_color = 1, 1, 1, 1
        self.xb1.text = 'xb1'
        self.xb1.background_color = 1, 1, 1, 1
        self.xb2.text = 'xb2'
        self.xb2.background_color = 1, 1, 1, 1
        self.xf1.text = 'xf1'
        self.xf1.background_color = 1, 1, 1, 1
        self.xf2.text = 'xf2'
        self.xf2.background_color = 1, 1, 1, 1
        self.status.text = ''


class WindowManagement(ScreenManager):
    pass


class PopUp(Popup):
    pass


kv = Builder.load_file("projeto.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()