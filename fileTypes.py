def getTypes():
	texteditor = r"C:\Program Files\Microsoft VS Code\Code.exe"
	texticon = r"C:\Program Files\Microsoft VS Code\resources\app\resources\win32\default.ico"
	return [

		# 3D Graphics
		{'type':'Model.3DStudio','name':'Legacy 3D Studio File','image':None,'command':None},
		{'type':'Model.Khronos.Collada','name':'Collaborative Design Activity','image':None,'command':None},
		{'type':'Model.Khronos.GLTransmission','name':'GL Transmission File','image':None,'command':None},
		{'type':'Model.Polygon','name':'Polygon File','image':None,'command':None},
		{'type':'Model.StereoLithography','name':'Stereo Lithographic Data','image':None,'command':None},
		{'type':'Model.Wavefront.Material','name':'Wavefont Material File','image':None,'command':None},
		{'type':'Model.Wavefront','name':'Wavefont Object File','image':None,'command':None},

		# Creation Kit Engine
		{'type':'Language.Papyrus.Compiled','name':'Compiled Papyrus','image':None,'command':None},
		{'type':'Language.Papyrus.Source','name':'Papyrus Source','image':texticon,'command':f'{texteditor} "%1" "%*"'},
		{'type':'Model.NetImmerse','name':'NetImmerse Model','image':None,'command':None},
		{'type':'Package.Bethesda.Archive','name':'Bethesda Archive','image':None,'command':None},
		{'type':'Package.Bethesda.Plugin','name':'Bethesda Plugin','image':None,'command':None},
		{'type':'Package.Bethesda.Sequence','name':'Bethesda Sequence','image':None,'command':None},

		# Doom Engine
		{'type':'Package.Doom','name':'Id Software Game Package','image':None,'command':r'"E:\Games\Doom\Zandronum\zandronum.exe" "%1" "%*"'},

		# Fonts
		{'type':'Font.OpenType.Embedded','name':'Embedded OpenType Font','image':None,'command':None},
		{'type':'Font.OpenType','name':'OpenType Font','image':None,'command':None},
		{'type':'Font.Web.OpenFontFormat.Version2','name':'Web Open Font Format v2','image':None,'command':None},
		{'type':'Font.Web.OpenFontFormat','name':'Web Open Font Format','image':None,'command':None},

		# Manufacturing
		{'type':'Manufacturing.Control.Numeric','name':'Numerical Control File','image':None,'command':None},

		# Machines
		{'type':'Machine.Control.XCT','name':'CT Configuration File','image':r'%SystemRoot%\system32\imageres.dll,-69','command':f'{texteditor} "%1" "%*"'},

		# Misc
		{'type':'dat','name':'Data File','image':None,'command':None},

		# Programming Languages
		{'type':'Language.Javascript.Node.ESModule','name':'Node.js ES Module','image':texticon,'command':f'{texteditor} "%1" "%*"'},
		{'type':'Language.Javascript.Object','name':'Javascript Object','image':texticon,'command':f'{texteditor} "%1" "%*"'},
		{'type':'Language.Javascript','name':'Javascript File','image':texticon,'command':f'{texteditor} "%1" "%*"'},
		{'type':'Language.PHP7','name':'PHP7 File','image':texticon,'command':f'{texteditor} "%1" "%*"'},
		{'type':'Language.Skrypt','name':'Skrypt File','image':texticon,'command':f'{texteditor} "%1" "%*"'},
		{'type':'Language.Web.Style','name':'Cascading Style Sheet','image':texticon,'command':f'{texteditor} "%1" "%*"'},

		# Text documents
		{'type':'Document.CodeSnippets','name':'Code Snippets','image':texticon,'command':f'{texteditor} "%1" "%*"'},
		{'type':'Document.Configuration.Markup','name':'Yet Another Markup File','image':texticon,'command':f'{texteditor} "%1" "%*"'},
		{'type':'Document.Markdown','name':'Markdown File','image':texticon,'command':f'{texteditor} "%1" "%*"'},
		{'type':'Document.Todo','name':'Todo list','image':texticon,'command':f'{texteditor} "%1" "%*"'},
		{'type':'inifile','name':'Configuration Settings','image':r'%SystemRoot%\system32\imageres.dll,-69','command':f'{texteditor} "%1" "%*"'},
		{'type':'xmlfile','name':'XML File','image':r'"C:\Program Files\Microsoft VS Code\resources\app\resources\win32\xml.ico"','command':f'{texteditor} "%1" "%*"'},

		# Valve
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
		{'type':'Package.Valve.SourceEngine.GridCache','name':'Valve Grid Cache Archive','image':None,'command':r'"E:\Software\x64\GCFScrape\GCFScape.exe" "%1" "%*"'},
		{'type':'Package.Valve.SourceEngine.NoCache','name':'Valve No Cache Archive','image':None,'command':r'"E:\Software\x64\GCFScrape\GCFScape.exe" "%1" "%*"'},
		{'type':'Package.Valve.SourceEngine','name':'Valve Pak Archive','image':None,'command':r'"E:\Software\x64\GCFScrape\GCFScape.exe" "%1" "%*"'},
		{'type':'Particle.DataModelExchange','name':'DMX Particle','image':None,'command':None},
		{'type':'ResourceList.Valve.SourceEngine','name':'Valve Resource List','image':None,'command':None},
		{'type':'Script.Valve.SourceEngine.Encrypted','name':'Valve Encrypted Script','image':None,'command':None},
		{'type':'Texture.Valve.SourceEngine','name':'Valve Texture','image':None,'command':None}
	]

def getExtensions():
	return [

		# 3D Graphics
		{'ext':'.3ds','type':'Model.3DStudio'},
		{'ext':'.dae','type':'Model.Khronos.Collada'},
		{'ext':'.gltf','type':'Model.Khronos.GLTransmission'},
		{'ext':'.mtl','type':'Model.Wavefront.Material'},
		{'ext':'.obj','type':'Model.Wavefront'},
		{'ext':'.ply','type':'Model.Polygon'},
		{'ext':'.stl','type':'Model.StereoLithography'},

		# Configuration Files
		{'ext':'.cfg','type':'inifile'},
		{'ext':'.conf','type':'inifile'},
		{'ext':'.config','type':'inifile'},
		{'ext':'.ini','type':'inifile'},
		{'ext':'.properties','type':'inifile'},
		{'ext':'.yml','type':'Document.Configuration.Markup'},

		# Creation Kit Engine
		{'ext':'.bsa','type':'Package.Bethesda.Archive'},
		{'ext':'.esp','type':'Package.Bethesda.Plugin'},
		{'ext':'.nif','type':'Model.NetImmerse'},
		{'ext':'.pex','type':'Language.Papyrus.Compiled'},
		{'ext':'.psc','type':'Language.Papyrus.Source'},
		{'ext':'.seq','type':'Package.Bethesda.Sequence'},

		# Doom Engine
		{'ext':'.pk3','type':'Package.Doom'},
		{'ext':'.wad','type':'Package.Doom'},

		# Fonts
		{'ext':'.eot','type':'Font.OpenType.Embedded'},
		{'ext':'.otf','type':'Font.OpenType'},
		{'ext':'.woff','type':'Font.Web.OpenFontFormat'},
		{'ext':'.woff2','type':'Font.Web.OpenFontFormat.Version2'},

		# Manufacturing
		{'ext':'.gcode','type':'Manufacturing.Control.Numeric'},
		{'ext':'.mpf','type':'Manufacturing.Control.Numeric'},
		{'ext':'.mpt','type':'Manufacturing.Control.Numeric'},
		{'ext':'.nc','type':'Manufacturing.Control.Numeric'},

		# Machines
		{'ext':'.xtekct','type':'Machine.Control.XCT'},


		# Misc
		{'ext':'.dat','type':'dat'},

		# Programming Languages
		{'ext':'.css','type':'Language.Web.Style'},
		{'ext':'.js','type':'Language.Javascript'},
		{'ext':'.json','type':'Language.Javascript.Object'},
		{'ext':'.jsonc','type':'Language.Javascript.Object'},
		{'ext':'.mjs','type':'Language.Javascript.Node.ESModule'},
		{'ext':'.ph7','type':'Language.PHP7'},
		{'ext':'.php','type':'Language.PHP7'},
		{'ext':'.sk','type':'Language.Skrypt'},

		# Text Documents
		{'ext':'.classpath','type':'xmlfile'},
		{'ext':'.code-snippets','type':'Document.CodeSnippets'},
		{'ext':'.md','type':'Document.Markdown'},
		{'ext':'.todo','type':'Document.Todo'},
		{'ext':'.xml','type':'xmlfile'},

		# Valve / Source engine
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
		{'ext':'.xwv','type':'Audio.Valve.SourceEngine.Xbox360'}
	]
