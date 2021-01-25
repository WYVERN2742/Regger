"""Configure file types and associations.

This is the standalone version, it is recommended to install
[Central](https://github.com/WYVERN2742/Central) for better console
formatting support."""
import os
import winreg
from . import fileTypes

def registerExtensions(extensions):
	for extension in extensions:
		result = os.system(f"ASSOC {extension.get('ext')}={extension.get('type')}")
		if result == 5:
			# Error code 5: Access denied
			# Commonly raised when not admin
			return False
	return True

def registerTypes(types):
	for t in types:
		if t.get('command') is None:
			# No Defined command, therefore set to default
			result = os.system(f"FTYPE {t.get('type')}=\"%1\" %*")
			continue

		result = os.system(f"FTYPE {t.get('type')}={t.get('command')}")

		if result == 5:
			# Error code 5: Access deined
			# Commonly raised when not admin
			return False

	try:
		reg = winreg.ConnectRegistry(None, winreg.HKEY_CLASSES_ROOT)
	except WindowsError as ex:
		print("? Unable to connect to registry, file icons and descriptive names will not be changed.")
		return

	for t in types:
		ty = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, t.get('type'),access=winreg.KEY_SET_VALUE)
		winreg.SetValueEx(ty, "FriendlyTypeName",0,winreg.REG_SZ,t.get('name'))
		image = t.get('image')
		if image is not None:
			winreg.SetValue(winreg.HKEY_CLASSES_ROOT, t.get('type'), winreg.REG_SZ, t.get('name'))
			winreg.SetValue(ty,"DefaultIcon", winreg.REG_SZ, image)
			winreg.CloseKey(ty)
			print(f"HKEY_CLASSES_ROOT/{t.get('type')}/DefaultIcon =>{image}")
	return True

def refreshIcons():
	os.system("refreshIcons.bat")

def main():
	print("Starting Windows File Types v1\n")
	print("Reading Config...")
	types = fileTypes.getTypes()
	extensions = fileTypes.getExtensions()

	print("\n" + "--" * 20)
	print(f"Associating {len(extensions)} file types...")

	if not registerExtensions(extensions):
		print("! Access, denied. Are you admin?")
		return

	print("\n" + "--" * 20)
	print("Linking Types...")

	registerTypes(types)

	print("\n" + "--" * 20)
	print("Refreshing icon cache...")
	refreshIcons()
	print("\n" + "--" * 20)
	print(f"Defined {len(types)} File Types with {len(extensions)} extensions.")


if __name__ == "__main__":
	main()
