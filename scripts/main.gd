extends Node2D
var thread : Thread
var DIR = OS.get_executable_path().get_base_dir()
var interpreter_path = DIR.path_join("pyscripts/venv/Scripts/python.exe")
var scritp_path = DIR.path_join("pyscripts/test.py")

var output = []
var last_emotion = ""
# Called when the node enters the scene tree for the first time.
func _ready():
	if !OS.has_feature("standalone"):
		interpreter_path = ProjectSettings.globalize_path("res://pyscripts/venv/Scripts/python.exe")
		scritp_path = ProjectSettings.globalize_path("res://pyscripts/test.py")
	thread = Thread.new()
	thread.start(info.bind())
	
func  _process(delta):
	$Emotion.text = last_emotion


# Called every frame. 'delta' is the elapsed time since the previous frame.
func info():
	while true:
		get_tree().create_timer(0.1)
		OS.execute(interpreter_path, [scritp_path], output, false)
		print(output[-1])
		last_emotion = output[-1]
		
