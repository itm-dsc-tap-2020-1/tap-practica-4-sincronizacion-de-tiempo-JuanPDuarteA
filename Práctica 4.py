import datetime
from time import ctime
import ntplib
import os

servidor="time.windows.com"
t1=datetime.datetime.now()
try:
    t1=datetime.datetime.now()
    cliente_ntp=ntplib.NTPClient()
    respuesta=cliente_ntp.request(servidor)
    hora_actual = datetime.datetime.strptime(ctime(respuesta.tx_time), "%a %b %d %H:%M:%S %Y")
    t2=datetime.datetime.now()
    ajus=(t2-t1)/2
    hora_fin=hora_actual+ajus
    print("Hora inicial: "+str(t1.time())+"\nHora de recepción: "+str(t2.time()))
    print("Hora recibida: "+str(hora_actual)+"\nAjuste: "+str(ajus))
    print("Reloj: "+str(hora_fin))
    os.system('date --set "%s"' %hora_fin)
except:print("El servidor no estba disponible")