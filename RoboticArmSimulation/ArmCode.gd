#Simulacion en 3D de brazo robotico RRR. Tiene 3 grados de libertad + efector
#Esta simulacion consiste en generar los movimientos del brazo robotico en 
#tiempo real gracias a la lectura de un archivo, el cual sera interpretado
#como los grados de rotacion de cada articulacion del brazo robotico, en el
#orden siguiente: hombro, codo, muñeca, efector. El codigo interpreta las
#ultimas 4 lineas del archivo, los primeros 3 numeros corresponden al grado
#en sexagesimal y el 4to numero debera ser: 1-para abrir efector 0-para cerrar
extends CSGMesh
var grados = {}
var t1
var t2
#Para el correcto funcionamiento del programa cambiar la siguiente ruta
#por una en la que tiene guardado el archivo de texto a leer.
var nombre_archivo = '/home/emaa/Escritorio/angulos.txt'
var f
var t = Timer.new()

func _ready():
	f = File.new()
	f.open(nombre_archivo, File.READ)
	t.set_wait_time(0.5)
	t.connect("timeout",self,"_on_timer_timeout")
	self.add_child(t)
	t.start()
	t1= _fecha_mod(f)

func _fecha_mod(archivo):
	return archivo.get_modified_time(nombre_archivo)

func _on_timer_timeout():
	t2= _fecha_mod(f)
	if t1!=t2:
		var s_arr = f.get_as_text().split("\n")
		for i in range (4):
			grados[str(i)] = s_arr[s_arr.size()-5+i] 
		rotar_art1(Vector3(0,grados["0"],0))
		rotar_art2(Vector3(grados["1"],0,0))
		rotar_art3(Vector3(0,grados["2"],0))
		rotar_efector(grados["3"])
	t1 = t2
	t.start()

func rotar_art1(target):
	var t = get_node("Tween")
	t.interpolate_property(self,"rotation_degrees",rotation_degrees,rotation_degrees+target,3.0,Tween.TRANS_QUINT,Tween.EASE_OUT)
	t.start()

func rotar_art2(target):
	var t = get_node("Tween")
	t.interpolate_property($art2,"rotation_degrees",$art2.rotation_degrees,$art2.rotation_degrees+target,3.0,Tween.TRANS_QUINT,Tween.EASE_OUT)
	t.start()

func rotar_art3(target):
	var t = get_node("Tween")
	t.interpolate_property($art2/largo1/art3,"rotation_degrees",$art2/largo1/art3.rotation_degrees,$art2/largo1/art3.rotation_degrees+target,3.0,Tween.TRANS_QUINT,Tween.EASE_OUT)
	t.start()
	
func rotar_efector(abrir):
	#solo se puede abrir el efector si estaba cerrado y cerrarlo si estaba abierto
	if(int(abrir)==1 and $art2/largo1/art3/largo2/gear1.rotation_degrees!=Vector3(90,90,90)):
		$art2/largo1/art3/largo2/gear1.rotation_degrees = Vector3(90,90,90)
		$art2/largo1/art3/largo2/gear2.rotation_degrees = Vector3(90,-90,-90)
	if(int(abrir)==0 and $art2/largo1/art3/largo2/gear1.rotation_degrees!=Vector3(75,90,90)):
		$art2/largo1/art3/largo2/gear1.rotation_degrees = Vector3(75,90,90)
		$art2/largo1/art3/largo2/gear2.rotation_degrees = Vector3(75,-90,-90)