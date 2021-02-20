import snap7
from snap7 import util
from firebase import firebase
from time import sleep
plc = snap7.client.Client()
plc.connect("192.168.0.1",0,1)
firebase = firebase.FirebaseApplication('https://test-3e4aa-default-rtdb.firebaseio.com/', None)

count = 0
count_2 = 0
array_old = [0]

for sets in range(10):
	array_old.insert(sets,'0')

while True:
	seft = plc.db_read(1,0,46)

	for value in range(10):
		bytearr = bytearray(2)
		count=value*2
		count_2 = (value*2)+1
		bytearr[0]=seft[count]
		bytearr[1] = seft[count_2]
		mmm = str(snap7.util.get_int(bytearr,0))
		if str(array_old[value]) == mmm:
			print('Tag_'+str(value)+ ': '+ mmm)
		else:
			array_old[value] = mmm
			#print('Tagds_'+str(value)+ ': '+ mmm)
			#print('array_old'+str(value)+ ': '+ array_old[value])
			firebase.put('/Infor/'+str(value),'Tem',str(mmm))
	sleep(1)	
plc.disconnect()