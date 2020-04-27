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

def main(args):
	packet = generate_random_packet()
	return {"packet": "0 6 71 104 48 115 116 5 "}
