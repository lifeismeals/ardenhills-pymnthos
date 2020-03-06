#!/usr/bin/python3
import sys
import base64

initial_str1 = '1c0111001f010100061a024b53535009181c'
initial_str2 = b'686974207468652062756c6c277320657965'
endianness = sys.byteorder

def hex_to_str(hex_str):
	split_hex_array = [ hex_str[i:i+2] for i in range(0, len(hex_str), 2) ]
	str_array = []
	for item in split_hex_array:
		item_new = bytes.fromhex(item)
		item_new = item_new.decode("ASCII") 
		str_array.append(item_new)	
	print(str_array)
	msg = "".join(str_array)	
	hex_msg = base64.b64encode(msg.encode()).decode()
	#print(msg)
	#print(hex_msg)
	return hex_msg


def xor_str(str1, str2):
	print(str1)
	int_str1 = int.from_bytes(str1.encode(), endianness)
	int_str2 = int.from_bytes(str2, endianness)
	print(int_str1)
	print(int_str2)
	int_result = int_str1 ^ int_str2
	
def main():
	dehex_str = hex_to_str(initial_str1)
	print(xor_str(dehex_str, initial_str2))

if __name__ == "__main__":
	main() 
