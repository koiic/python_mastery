from codementor.warrior import display_warrior_status, move_warrior

warrior1_location = int()
warrior1_speed = int()
warrior1_strength = int()
warrior1_direction = str()
warrior1_energy = int()
warrior1_name = str()

warrior2_location = int()
warrior2_speed = int()
warrior2_strength = int()
warrior2_direction = str()
warrior2_energy = int()
warrior2_name = str()

has_energy_left = True
time = 0

if __name__ == '__main__':

	try:
		file = open("warrior.txt", "r")

		warriors_attribute = file.readlines()

		warrior1_name = warriors_attribute[0]
		warrior1_energy = int(warriors_attribute[1])
		warrior1_strength = int(warriors_attribute[2])
		warrior1_speed = int(warriors_attribute[3])
		warrior1_location = int(warriors_attribute[4])
		warrior1_direction = warriors_attribute[5]

		warrior2_name = warriors_attribute[6]
		warrior2_energy = int(warriors_attribute[7])
		warrior2_strength = int(warriors_attribute[8])
		warrior2_speed = int(warriors_attribute[9])
		warrior2_location = int(warriors_attribute[10])
		warrior2_direction = warriors_attribute[11]
		file.close()

		print("time is", time)

		display_warrior_status(warrior1_name, warrior1_energy, warrior1_strength, warrior1_speed, warrior1_location,
		                       warrior1_direction)
		display_warrior_status(warrior2_name, warrior2_energy, warrior2_strength, warrior2_speed, warrior2_location,
		                       warrior2_direction)

		while has_energy_left:
			warrior1_location = move_warrior(warrior1_speed, warrior1_direction, warrior1_location, warrior2_location)
			if warrior1_location < 0:
				warrior1_location = abs(warrior1_location)
				if warrior1_direction == "left":
					warrior1_direction = "right"
				else:
					warrior1_direction = "left"

			warrior2_location = move_warrior(warrior2_speed, warrior2_direction, warrior2_location, warrior1_location)
			if warrior2_location < 0:
				warrior2_location = abs(warrior2_location)
				if warrior2_direction == "left":
					warrior2_direction = "right"
				else:
					warrior2_direction = "left"

			time += 1
			warrior1_energy = warrior1_energy - (warrior1_speed ** 2)
			warrior2_energy = warrior2_energy - (warrior2_speed ** 2)

			warrior1_strength = warrior1_strength - (2 * warrior1_speed)
			warrior2_strength = warrior1_strength - (2 * warrior2_speed)

			print('time', time)
			display_warrior_status(warrior1_name, warrior1_energy, warrior1_strength, warrior1_speed, warrior1_location,
			                       warrior1_direction)
			display_warrior_status(warrior2_name, warrior2_energy, warrior2_strength, warrior2_speed, warrior2_location,
			                       warrior2_direction)

			if warrior1_energy <= 0 or warrior2_energy <= 0:
				has_energy_left = False

		if warrior1_energy <= 0 and warrior2_energy <= 0:
			print("Both warrior died.\n")
		elif warrior1_energy <= 0:
			print(f"{warrior1_name} died \n")
		elif warrior2_energy <= 0:
			print(f"{warrior1_name} died \n")
		else:
			print("ERROR")


	except FileNotFoundError:
		print("Uploaded file not found")

