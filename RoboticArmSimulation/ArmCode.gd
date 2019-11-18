extends CSGMesh

export var speed=2
var rotate_left
var rotate_right
var rotate_up
var rotate_down
var rotateValue
var rotate_base_cw
var rotate_base_anticw
var grip
var ungrip

func _ready():
	pass

func _process(delta):
	rotate_left=Input.is_action_pressed("ui_left")
	rotate_right=Input.is_action_pressed("ui_right")
	rotate_up=Input.is_action_pressed("ui_up")
	rotate_down=Input.is_action_pressed("ui_down")
	rotate_base_anticw=Input.is_key_pressed(KEY_Z)
	grip=Input.is_key_pressed(KEY_X)
	ungrip=Input.is_key_pressed(KEY_C)
	rotate_base_cw=Input.is_key_pressed(KEY_V)
	
	rotateValue=speed*delta
	
	if rotate_base_cw:
		rotate_y(rotateValue)
	if rotate_base_anticw:
		rotate_y(-rotateValue)
	if rotate_left:
		$art2.rotate_x(-rotateValue)
	if rotate_right:
		$art2.rotate_x(rotateValue)
	if rotate_up:
		$art2/largo1/art3.rotate_y(rotateValue)
	if rotate_down:
		$art2/largo1/art3.rotate_y(-rotateValue)
	if grip:
		$art2/largo1/art3/largo2/gear1.rotate_z(rotateValue)
		$art2/largo1/art3/largo2/gear2.rotate_z(-rotateValue)
	if ungrip:
		$art2/largo1/art3/largo2/gear1.rotate_z(-rotateValue)
		$art2/largo1/art3/largo2/gear2.rotate_z(rotateValue)