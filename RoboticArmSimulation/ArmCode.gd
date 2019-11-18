extends CSGMesh

var grados = {}
var t1
var t2
var nombre_archivo = '/home/emaa/Escritorio/hola.txt'
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
	if t1!=t2: #archivo modificado!!! leer las ultimas 3 lineas
		var s_arr = f.get_as_text().split("\n")
		for i in range (3):
			grados[str(i)] = s_arr[s_arr.size()-4+i] #de la antepenultima linea para adelante
		rotar_art1(Vector3(0,grados["0"],0))
		rotar_art2(Vector3(grados["1"],0,0))
		rotar_art3(Vector3(0,grados["2"],0))
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
	
func rotar_efector(target):
	var t1 = get_node("Tween")
	var t2 = get_node("Tween")
	var target2 = Vector3(20,0,0)
	t1.interpolate_property($art2/largo1/art3/largo2/gear1,"rotation_degrees",$art2/largo1/art3/largo2/gear1.rotation_degrees,$art2/largo1/art3/largo2/gear1.rotation_degrees+target,3.0,Tween.TRANS_QUINT,Tween.EASE_OUT)
	t2.interpolate_property($art2/largo1/art3/largo2/gear2,"rotation_degrees",$art2/largo1/art3/largo2/gear2.rotation_degrees,$art2/largo1/art3/largo2/gear2.rotation_degrees+target2,3.0,Tween.TRANS_QUINT,Tween.EASE_OUT)
	t1.start()
