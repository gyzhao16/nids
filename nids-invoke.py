import os
import random

def generate_random_packet():
	dfa_id = 0
	len = random.randint(0, 1460)
	packet = str(dfa_id) + " " + str(len) + " "
	i = 0
	while i < len:
		packet = packet + str(random.randint(0, 255)) + " "
		i = i + 1
	return packet

def generate_json_file(str):
	json = "{\n\"packet\": \"" + str + "\"" + "\n}"
	newfile = open('param.json', 'w')
	newfile.write(json)

generate_json_file(generate_random_packet())
