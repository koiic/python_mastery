def display_warrior_status(name, energy, strength, speed, location, direction):
	"""
	:param name:
	:param energy:
	:param strength:
	:param speed:
	:param location:
	:param direction:
	:return:
	"""
	print(f'{name}:(energy {energy}, strength {strength}, speed {speed}, direction {direction}) at location', location)


def move_warrior(speed, direction, location, other_location):
	"""
	:return: int new location
	"""
	if direction == "right":
		new_location = location + speed
	else:
		new_location = location - speed
	return new_location
