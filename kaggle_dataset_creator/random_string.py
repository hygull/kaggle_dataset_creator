import random
import base64
from datetime import datetime

def random_string(length=10, shuffle=True):
	now = str(datetime.now())
	# if shuffle:
	# 	now = now[::-1]

	enc_now_str = base64.b64encode(now.encode("utf8")).decode("utf8")
	enc_now_str2 = base64.b64encode(enc_now_str.encode("utf8")).decode("utf8")
	enc_now_str3 = base64.b64encode(enc_now_str2.encode("utf8")).decode("utf8")

	if now[-1] in ["9", "2"]:
		r_str = enc_now_str[::-1]
	elif now[-1] in ["5", "1", "8", "3"]:
		r_str = enc_now_str2[::-1]
	elif now[-1] in ["7", "4", "0"]:
		r_str = enc_now_str3[::-1]
	else:
		r_str = enc_now_str3

	return r_str[:length]

if __name__ == "__main__":
	print(random_string())
	print(random_string())
	print(random_string())

