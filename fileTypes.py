"""Configure file types and associations."""
import central.uux
import os
import winreg

def getTypes():
	return [
		{'type':'Package.Doom','name':'Id Software Game Package','image':None,'command':r'"E:\Games\Doom\Zandronum\zandronum.exe" "%1"'},
		{'type':'Document.Todo','name':'Todo list','image':r'"C:\Program Files\Microsoft VS Code\resources\app\resources\win32\default.ico"','command':r'"C:\Program Files\Microsoft VS Code\Code.exe" "%1"'},
		{'type':'xmlfile','name':'XML File','image':r'"C:\Program Files\Microsoft VS Code\resources\app\resources\win32\xml.ico"','command':r'"C:\Program Files\Microsoft VS Code\Code.exe" "%1"'},
		{'type':'Document.Markdown','name':'Markdown File','image':r'"C:\Program Files\Microsoft VS Code\resources\app\resources\win32\default.ico"','command':r'"C:\Program Files\Microsoft VS Code\Code.exe" "%1"'},
		{'type':'inifile','name':'Configuration Settings','image':r'%SystemRoot%\system32\imageres.dll,-69','command':r'"C:\Program Files\Microsoft VS Code\Code.exe" "%1"'},

		{'type':'Language.Papyrus.Source','name':'Papyrus Source','image':r'"C:\Program Files\Microsoft VS Code\resources\app\resources\win32\default.ico"','command':r'"C:\Program Files\Microsoft VS Code\Code.exe" "%1"'},
		{'type':'Language.Papyrus.Compiled','name':'Compiled Papyrus','image':None,'command':None},
		{'type':'Package.Bethesda.Plugin','name':'Bethesda Plugin','image':None,'command':None},
		{'type':'Package.Bethesda.Sequence','name':'Bethesda Sequence','image':None,'command':None},
		{'type':'Package.Bethesda.Archive','name':'Bethesda Archive','image':None,'command':None},
		{'type':'Model.NetImmerse','name':'NetImmerse Model','image':None,'command':None},

		{'type':'Language.PHP7','name':'PHP 7 File','image':r'"C:\Program Files\Microsoft VS Code\resources\app\resources\win32\default.ico"','command':r'"C:\Program Files\Microsoft VS Code\Code.exe" "%1"'},

		{'type':'AI.Valve.SourceEngine.NavMesh','name':'Valve AI NavMesh','image':None,'command':None},
		{'type':'AI.Valve.SourceEngine.NodeGraph','name':'Valve AI Nodegraph','image':None,'command':None},
		{'type':'Animation.Valve.SourceEngine.Face','name':'Valve Face Expression','image':None,'command':None},
		{'type':'Animation.Valve.SourceEngine.Flex','name':'Valve Flex Animation','image':None,'command':None},
		{'type':'Animation.Valve.SourceEngine','name':'Valve Animation','image':None,'command':None},
		{'type':'Audio.Valve.SourceEngine.Xbox360','name':'Valve Xbox360 Audio','image':None,'command':None},
		{'type':'Choreography.Valve.SourceEngine','name':'Valve Choreography Data','image':None,'command':None},
		{'type':'Demo.Valve.SourceEngine','name':'Valve Source Demo','image':None,'command':None},
		{'type':'Map.Valve.GoldSrc.Rich','name':'Valve GoldSrc Rich Map','image':None,'command':None},
		{'type':'Map.Valve.GoldSrc','name':'Valve GoldSrc Map','image':None,'command':None},
		{'type':'Map.Valve.Portal2','name':'Valve Portal 2 Map','image':None,'command':None},
		{'type':'Map.Valve.SourceEngine.Compiled','name':'Valve Compiled Map','image':None,'command':None},
		{'type':'Map.Valve.SourceEngine.Lump','name':'Valve Map Lump','image':None,'command':None},
		{'type':'Map.Valve.SourceEngine.Reference','name':'Valve Hammer Reference','image':None,'command':None},
		{'type':'Map.Valve.SourceEngine.Source','name':'Valve Map Source','image':None,'command':None},
		{'type':'Material.Valve.SourceEngine','name':'Valve Material','image':None,'command':None},
		{'type':'Model.DataModelExchange','name':'Data Model eXchange','image':None,'command':None},
		{'type':'Model.Valve.SourceEngine.Collision','name':'Valve Model Collision','image':None,'command':None},
		{'type':'Model.Valve.SourceEngine.Mesh','name':'Valve Mesh Strip','image':None,'command':None},
		{'type':'Model.Valve.SourceEngine.Stripped','name':'Valve Stripping Information','image':None,'command':None},
		{'type':'Model.Valve.SourceEngine.Vertex','name':'Valve Model Vertex','image':None,'command':None},
		{'type':'Model.Valve.SourceEngine','name':'Valve Model','image':None,'command':None},
		{'type':'Package.Valve.SourceEngine.GridCache','name':'Valve Grid Cache Archive','image':None,'command':r'"E:\Software\x64\GCFScrape\GCFScape.exe" "%1"'},
		{'type':'Package.Valve.SourceEngine.NoCache','name':'Valve No Cache Archive','image':None,'command':r'"E:\Software\x64\GCFScrape\GCFScape.exe" "%1"'},
		{'type':'Package.Valve.SourceEngine','name':'Valve Pak Archive','image':None,'command':r'"E:\Software\x64\GCFScrape\GCFScape.exe" "%1"'},
		{'type':'Particle.DataModelExchange','name':'DMX Particle','image':None,'command':None},
		{'type':'ResourceList.Valve.SourceEngine','name':'Valve Resource List','image':None,'command':None},
		{'type':'Script.Valve.SourceEngine.Encrypted','name':'Valve Encrypted Script','image':None,'command':None},
		{'type':'Texture.Valve.SourceEngine','name':'Valve Texture','image':None,'command':None},

	]

def getExtensions():
	return [
		{'ext':'.ain','type':'AI.Valve.SourceEngine.NodeGraph'},
		{'ext':'.ani','type':'Animation.Valve.SourceEngine'},
		{'ext':'.bsp','type':'Map.Valve.SourceEngine.Compiled'},
		{'ext':'.dem','type':'Demo.Valve.SourceEngine'},
		{'ext':'.dmx','type':'Model.DataModelExchange'},
		{'ext':'.fgd','type':'Map.Valve.SourceEngine.Reference'},
		{'ext':'.gcf','type':'Package.Valve.SourceEngine.GridCache'},
		{'ext':'.ice','type':'Script.Valve.SourceEngine.Encrypted'},
		{'ext':'.lmp','type':'Map.Valve.SourceEngine.Lump'},
		{'ext':'.map','type':'Map.Valve.GoldSrc'},
		{'ext':'.mdl','type':'Model.Valve.SourceEngine'},
		{'ext':'.nav','type':'AI.Valve.SourceEngine.NavMesh'},
		{'ext':'.ncf','type':'Package.Valve.SourceEngine.NoCache'},
		{'ext':'.p2c','type':'Map.Valve.Portal2'},
		{'ext':'.pcf','type':'Particle.DataModelExchange'},
		{'ext':'.phy','type':'Model.Valve.SourceEngine.Collision'},
		{'ext':'.res','type':'ResourceList.Valve.SourceEngine'},
		{'ext':'.rmf','type':'Map.Valve.GoldSrc.Rich'},
		{'ext':'.vcd','type':'Choreography.Valve.SourceEngine'},
		{'ext':'.vfe','type':'Animation.Valve.SourceEngine.Face'},
		{'ext':'.vmf','type':'Map.Valve.SourceEngine.Source'},
		{'ext':'.vmt','type':'Material.Valve.SourceEngine'},
		{'ext':'.vpk','type':'Package.Valve.SourceEngine'},
		{'ext':'.vsi','type':'Model.Valve.SourceEngine.Stripped'},
		{'ext':'.vta','type':'Animation.Valve.SourceEngine.Flex'},
		{'ext':'.vtf','type':'Texture.Valve.SourceEngine'},
		{'ext':'.vtx','type':'Model.Valve.SourceEngine.Mesh'},
		{'ext':'.vvd','type':'Model.Valve.SourceEngine.Vertex'},
		{'ext':'.xwv','type':'Audio.Valve.SourceEngine.Xbox360'},

		{'ext':'.pk3','type':'Package.Doom'},
		{'ext':'.wad','type':'Package.Doom'},
		{'ext':'.esp','type':'Package.Bethesda.Plugin'},
		{'ext':'.seq','type':'Package.Bethesda.Sequence'},
		{'ext':'.bsa','type':'Package.Bethesda.Archive'},
		{'ext':'.nif','type':'Model.NetImmerse'},
		{'ext':'.todo','type':'Document.Todo'},
		{'ext':'.xml','type':'xmlfile'},
		{'ext':'.classpath','type':'xmlfile'},
		{'ext':'.md','type':'Document.Markdown'},
		{'ext':'.ph7','type':'Language.PHP7'},
		{'ext':'.psc','type':'Language.Papyrus.Source'},
		{'ext':'.pex','type':'Language.Papyrus.Compiled'},

		{'ext':'.cfg','type':'inifile'},
		{'ext':'.ini','type':'inifile'},
		{'ext':'.properties','type':'inifile'},
		{'ext':'.conf','type':'inifile'},
		{'ext':'.config','type':'inifile'}
	]

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
		central.uux.show_warning("Unable to connect to registry, file icons and descriptive names will not be changed.")
		return

	for t in types:
		ty = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, t.get('type'),access=winreg.KEY_SET_VALUE)
		winreg.SetValueEx(ty, "FriendlyTypeName",0,winreg.REG_SZ,t.get('name'))
		image = t.get('image')
		if image is not None:
			winreg.SetValue(winreg.HKEY_CLASSES_ROOT, t.get('type'), winreg.REG_SZ, t.get('name'))
			winreg.SetValue(ty,"DefaultIcon", winreg.REG_SZ, image)
			winreg.CloseKey(ty)
			central.uux.show_debug(f"HKEY_CLASSES_ROOT/{t.get('type')}/DefaultIcon =>{image}")
	return True

def refreshIcons():
	os.system("refreshIcons.bat")

def main():
	central.uux.show_success("Starting Windows File Types v1")
	central.uux.show_debug("Reading Config...")
	types = getTypes()
	extensions = getExtensions()

	central.uux.show_info(f"Associating {len(extensions)} file types...")
	central.uux.show_debug("","")

	if not registerExtensions(extensions):
		central.uux.show_error("Access, denied. Are you admin?")
		exit(-1)

	central.uux.show_section()
	central.uux.show_info("Linking Types...")
	central.uux.show_debug("")

	registerTypes(types)

	central.uux.show_info("Refreshing icon cache...")
	refreshIcons()
	central.uux.show_success(f"Defined {len(types)} File Types with {len(extensions)} extensions.")


if __name__ == "__main__":
	main()
