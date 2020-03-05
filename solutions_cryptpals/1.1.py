#!/usr/bin/python3

import base64

hex_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

b64_str = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

def hex_to_b64(hex_str):
	split_hex_array = [ hex_str[i:i+2] for i in range(0, len(hex_str), 2) ]
	str_array = []
	for item in split_hex_array:
		item_new = bytes.fromhex(item)
		item_new = item_new.decode("ASCII") 
		str_array.append(item_new)	
	msg = "".join(str_array)	
	hex_msg = base64.b64encode(msg.encode()).decode()
	print(hex_msg)
	return hex_msg
	

def b64str_to_4int_list(base64_str):
	n = 4
	quad_int_array = [ base64_str[i:i+n] for i in range(0, len(base64_str), n) ]
	return quad_int_array

def byte_string_to_hex(byte_str):
	split_b_array = [ byte_str[i:i+1] for i in range(0, len(byte_str)) ]
	ascii_code_array = []
	for letter in split_b_array:
		ascii_code_array.append(ord(letter))
	hex_code_array = []
	for ascii in ascii_code_array:
		hex_code_array.append(hex(ascii))
	hex_str_array = []
	for hex_num in hex_code_array:
		hex_str_array.append(hex_num.lstrip("0x"))
	result = "".join(hex_str_array)
	return result 

def going_backwards():
	b64_array = b64str_to_4int_list(b64_str)
	b64_decode_array = []
	for int in b64_array:
		b64_decode_array.append(base64.b64decode(int))
	whole_array = b''.join(b64_decode_array)
	print(whole_array)
	hex_string = byte_string_to_hex(whole_array)
	print(hex_string)
	
def base64_to_4int(h_str):
	n = 4
	split_int_array = [ str.encode(h_str[i:i+n]) for i in range(0, len(h_str), n) ]
	return split_int_array

def encode_int_list(int_array):
	temp_b64_str = [] 
	for item in int_array: 
		temp_b64_str.append(base64.b64encode(item))
	return temp_b64_str

def going_forwards():
	temp_array = hex_to_b64(hex_str)
	
if __name__ == "__main__":
	going_backwards()
	going_forwards()	
