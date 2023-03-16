import numpy as np
import matplotlib.pyplot as plt
# Constants
a = 5.132 #mm/s/MPa
n = 0.222 # - 
R_int = 12.5E-3 # 12.5 # mm
R_max = 38.4E-3 # 38.4 # mm
Len_grain = 0.107 # 107 # mm
Prop_den = 1841 # 1.841E-9 # kg/mm^3
Dt = 7.8E-3 #8.37E-3
De = 16.74E-3 
At = np.pi * (Dt/2)**2 # mm^2
Ae = np.pi * (De/2)**2
R = 206.3 # 206.3E+6 # mm^2 s^-2 K^-1 
Tc = 1558.722 # k
c = 908 # 908E+3 #911E+3 #mm/s
alp = 0.1 * 2*np.pi/360 # rads
index = 0
gam = 1.1209
Gam = np.sqrt(gam) * (2/(gam + 1)) ** ((gam + 1)/(2 * (gam - 1)))
Ae_At_giv = Ae/At

# initail values
Pc = 101325 # 101325E-6
Pa = 101325 # 101325E-6
dt = 0.001
w = 0
Vc = np.pi * (R_int**2) * Len_grain
t = 0

# Data Arrays

# Functions
def dw_dt(Pc):
    dw = r(Pc)

    return dw

def Pe_PC():
    Ae_At_cal_arr = []
    Pe_Pc_arr = []
    for Pe_Pc_cal in np.arange(0,0.1,0.00001):
        Ae_At_cal = Gam/np.sqrt((2 * gam)/(gam - 1) * (Pe_Pc_cal) ** 2/gam * (1 - Pe_Pc_cal ** ((gam - 1)/gam)))
        
        Pe_Pc_arr.append(Pe_Pc_cal)
        Ae_At_cal_arr.append(Ae_At_cal)

    for Ae_At in Ae_At_cal_arr:
        if Ae_At_giv*0.9999 < Ae_At < Ae_At_giv*1.0001:
            Ae_index = Ae_At_cal_arr.index(Ae_At)
            Pe_PC_int = Pe_Pc_arr[Ae_index]
            
        else:
            None

    return Pe_PC_int

def r(Pc):
    r_val = a * ((Pc * 1E-6) ** n)

    return r_val * 1E-3

def Ab(w):
    global state
    #if (w + R_int) < R_max:
    #    A = (2 * np.pi * (R_int + w) * Len_grain)
    #else:
    #    A = 0

    if w < Len_grain*np.tan(alp):
        A = (np.pi * (2*R_int + w) * w)/np.sin(alp)
        state = 1

    elif Len_grain*np.tan(alp) < w < R_max - R_int:
        A = (R_int + w) * (2*np.pi*Len_grain)/np.cos(alp) - np.pi * Len_grain**2 * (np.tan(alp)/np.cos(alp))
        state = 2

    elif R_max - R_int < w < R_max - R_int + Len_grain*np.tan(alp):
        x = R_int + w - Len_grain*np.tan(alp)
        A = (np.pi*(R_max + x)*(R_max - x))/np.sin(alp)
        state = 3

    else:
        A = 0
        state = 4
    
    return A

def dv_dt(Pc,w):
    dv = r(Pc) * Ab(w)

    return dv

def dPc_dt(Vc,Pc,w):
    dPc = ((R * Tc)/Vc) * (Prop_den * r(Pc) * Ab(w) - (Pc * At)/c) - (Pc/Vc)*dv_dt(Pc,w)

    return dPc

def TRP(w,Vc,Pc):
    global Time, Reg, w_value, ChamPres, Ue_values, massflow_values, Thrust, Momentum
    Time = []
    Reg = []
    w_value = []
    ChamPres = []
    Ue_values = []
    massflow_values = []
    Thrust = []
    Momentum = []

    for t in np.arange(0,6,dt):
        # do calculaations 
        #t = t + dt
        
        w = w + dw_dt(Pc)*dt

        Vc = Vc + dv_dt(Pc,w)*dt

        Pc = Pc + dPc_dt(Vc,Pc,w)*dt

        # do thrust calculation

        Ue = np.sqrt((2 * gam)/(gam - 1) * R * Tc * (1 - (Pe_Pc_val) ** ((gam - 1)/gam)))

        m = (Pc * At)/c

        Cf = Gam * np.sqrt((2 * gam)/(gam - 1) * (1 - (Pe_Pc_val) ** ((gam - 1)/gam))) + (Pe_Pc_val - Pa/Pc)*Ae_At_giv

        F =  Cf * c * m  + (Pe_Pc_val*Pc - Pa)*Ae

        # grab data
        # print(Cf)
        
        Time.append(t)
        Ue_values.append(Ue)
        Thrust.append(F)
        massflow_values.append(m)
        Reg.append(r(Pc))
        w_value.append(w)
        ChamPres.append(Pc)
        Momentum.append(m * Ue)

    index = [i for i, j in enumerate(ChamPres) if j > 1E+6]
    start_time = Time[index[0]]
    #print(start_time)
    Time = Time - start_time

def Graphs(x,y,col):
    plt.scatter(x,y,c=col,marker="+")
    

Pe_Pc_val = Pe_PC()
TRP(w,Vc,Pc)
Graphs(Time,Momentum,'r')
alp = 1 * 2*np.pi/360
TRP(w,Vc,Pc)
Graphs(Time,Momentum,'b')
alp = 3 * 2*np.pi/360
TRP(w,Vc,Pc)
Graphs(Time,Momentum,'g')

plt.show()


