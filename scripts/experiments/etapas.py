# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 17:00:50 2021

@author: Caro
"""
import numpy as np
from src.data_manipulation.data_manager import DataManager
from matplotlib import pyplot as plt, rc

DataManager.load_dataset('owid')

lugar = 'Argentina'

inc_data = DataManager.get_raw_daily_data(lugar)

y = inc_data.copy()

# =============================================================================
# print(y)
# print(len(y))
# =============================================================================

# Defining Splits
splits = 7


  
# Finding average of semanas
Output=[sum(y[splits*i:7*(i+1)-1])/splits for i in range(int(len(y)/7))]

print('promedio semanal:',Output)
print(len(Output))

Acumulados_semanales=[sum(Output[0:i+1]) for i in range(len(Output))]

print('Acumulados_semanales: ', Acumulados_semanales)

## paso a escala log y miro los cambios en las pendientes

Acumulados_semanales_log=np.log(Acumulados_semanales)

print('Acumulados semanales escala log', Acumulados_semanales_log)


pendientes_log=[Acumulados_semanales_log[i+1]-Acumulados_semanales_log[i] for i in range (len(Acumulados_semanales_log)-1)]

cambio_pendiente_log=[(pendientes_log[i+1]-pendientes_log[i])/pendientes_log[i] for i in range(len(pendientes_log)-1)]

print('cambios de pendientes de escala log : ', cambio_pendiente_log)

semanas_cambio_log=[i for i in range(len(cambio_pendiente_log)) if abs(cambio_pendiente_log[i])> 0.35]

print('semanas en la que se producen lso cambios de pendientes en escala log: ', semanas_cambio_log)

acumulados_sem_cambios_log=[Acumulados_semanales_log[i] for i in semanas_cambio_log]


t=range(len(Acumulados_semanales))

#plt.plot(semanas_cambio_log,acumulados_sem_cambios_log,'x',t,Acumulados_semanales_log)


## En escala normal

pendientes=[Acumulados_semanales[i+1]-Acumulados_semanales[i] for i in range (len(Acumulados_semanales_log)-1)]

cambio_pendiente=[(pendientes[i+1]-pendientes[i])/pendientes[i] for i in range(len(pendientes)-1)]

print('cambios de pendientes de escala normal : ', cambio_pendiente)

semanas_cambio=[i for i in range(len(cambio_pendiente)) if abs(cambio_pendiente[i])> 0.45]

print('semanas en la que se producen los cambios de pendientes en escala normal: ', semanas_cambio)

acumulados_sem_cambios=[Acumulados_semanales[i] for i in semanas_cambio]


t=range(len(Acumulados_semanales))

#plt.plot(semanas_cambio,acumulados_sem_cambios,'x',t,Acumulados_semanales)

 ## por la naturaleza de nuetro modelo necesitamos detectar los momentos en donde la derivada segunda se anula (o es cerca de 0)
 
#derivada segunda:
 
derivada_segunda=[pendientes[i+1]-pendientes[i] for i in range(len(pendientes)-1)]

print('derivada segunda escala normal: ', derivada_segunda)


#calculo de derivadas usando splines cubicos

from scipy.interpolate import CubicSpline

cs = CubicSpline(t, Acumulados_semanales)
xs = np.arange(0.0, 70.0, 0.1)
#fig, ax = plt.subplots(figsize=(6.5, 4))
#ax.plot(t, Acumulados_semanales, 'o', label='data')
#ax.plot(xs, cs(xs), label="S")
#ax.plot(xs, cs(xs, 1), label="S'")
#ax.plot(xs, cs(xs, 2), label="S''")
#ax.plot(xs, cs(xs, 3), label="S'''")
#ax.set_xlim(0.0, 70.0)
#ax.legend(loc='lower left', ncol=2)
#plt.show()

print('derivadas segundas escala normal: ', cs(t,2))

derivadas_splines_cubic=cs(t,1)


cambio_derivadas_splines=[(derivadas_splines_cubic[i+1]-derivadas_splines_cubic[i])/derivadas_splines_cubic[i] for i in range(len(derivadas_splines_cubic)-1)]

semanas_cambio_spl=[i for i in range(len(cambio_derivadas_splines)) if abs(cambio_derivadas_splines[i])> 0.5]

print('semanas en la que se producen los cambios de pendientes en escala normal usando splines cubicos: ', semanas_cambio_spl)

acumulados_sem_cambios_spl=[Acumulados_semanales[i] for i in semanas_cambio_spl]


#Ypor la naturaleza del modelo quiero ver cuando la derivada segunda se hace 0

derivadas2_splines_cubic=cs(t,2)
semana_der2_cero=[i for i in range(len(derivadas2_splines_cubic)) if abs(derivadas2_splines_cubic[i])< 20.0]
acumulados_sem_cambios_der2_spl=[Acumulados_semanales[i] for i in semana_der2_cero]

plt.plot(semanas_cambio_spl,acumulados_sem_cambios_spl,'x',semana_der2_cero,acumulados_sem_cambios_der2_spl,'*',t,Acumulados_semanales,'y')







