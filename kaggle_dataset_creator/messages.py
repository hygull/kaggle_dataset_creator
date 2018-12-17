from colorama import init, Fore

#  strip=False is necessary to print colorful text on GIT bash like terminals (tty)
init(autoreset=True, strip=False)

def warning(message, **kwargs):
	print(Fore.RED + '\nWARNING: %s' % message)

def success(message, **kwargs):
	print(Fore.GREEN + "\nSUCCESS: %s" % message)