import maya.cmds as mc
import maya.mel
#Junhao Fu#



class optionwindow(object):
    def __init__(self):
        self.window = 'mywindow'
        self.title = 'Tool Box'
        self.size = (300,650)
        self.supportsToolAction = False
      
        
    def commonMenu(self):
        self.editMenu = mc.menu(label='Edit')
        self.editMenuSave = mc.menuItem(label = 'Save Settings')
        self.editMenuReset = mc.menuItem(label = 'Reset Settings')
        self.editMenuDiv = mc.menuItem(d=True)
        self.editMenuRadio = mc.radioMenuItemCollection()
        self.editMenuTool = mc.menuItem(label = 'As Tool', radioButton = True, enable=self.supportsToolAction)
        self.editMenuAction = mc.menuItem(label = 'As Action', radioButton = True, enable=self.supportsToolAction)
        self.helpMenu = mc.menu(label='Help')
        self.helpMenuItem = mc.menuItem(label = 'Help on %s' %self.title, command = self.helpmenu)
        
    def helpmenu(*args):
        mc.launch(web='http://maya-python.com')
        
    def transform(self):
        self.transfromFrameLayout = mc.frameLayout(label="transform", collapsable = True,borderStyle="etchedIn") 
        self.transfromColumnLayout =  mc.columnLayout(columnAttach = ("left",0),adj=True)
        self.transformbutton()
        mc.setParent('..')
        
    def transformbutton(self):
        self.transfromMoveButton = mc.textFieldButtonGrp('move',ad3=2,cw3=(40,80,50),label='move', text='0 0 0', buttonLabel='move',buttonCommand="""translation = mc.textFieldButtonGrp(self.transfromMoveButton,text=True,query=True).split();mc.move(float(translation[0]),float(translation[1]),float(translation[2]),myobject)""")
        self.transfromRotateButton = mc.textFieldButtonGrp('rotate',ad3=2,cw3=(40,80,50),label='rotate', text='0 0 0', buttonLabel='rotate',buttonCommand="""rotation = mc.textFieldButtonGrp(self.transfromRotateButton,text=True,query=True).split();mc.rotate(float(rotation[0]),float(rotation[1]),float(rotation[2]),myobject)""")
        self.transfromScaleButton = mc.textFieldButtonGrp('scale',ad3=2,cw3=(40,80,50),label='scale', text='1 1 1', buttonLabel='scale',buttonCommand="""scale = mc.textFieldButtonGrp(self.transfromScaleButton,text=True,query=True).split();mc.scale(float(scale[0]),float(scale[1]),float(scale[2]),myobject)""")
        mc.setParent('..')
        
    def duplicatebutton(self):
        self.duplicateMoveButton = mc.textFieldButtonGrp('duplicatemove',ad3=2,cw3=(40,80,50),label='move', text='0 0 0', buttonLabel='duplicate',buttonCommand="""mc.duplicate(myobject,st=True);translation = mc.textFieldButtonGrp(self.duplicateMoveButton,text=True,query=True).split();mc.move(float(translation[0]),float(translation[1]),float(translation[2]))""")
        self.duplicateRotateButton = mc.textFieldButtonGrp('duplicaterotate',ad3=2,cw3=(40,80,50),label='rotate', text='0 0 0', buttonLabel='duplicate',buttonCommand="""mc.duplicate(myobject,st=True);rotation = mc.textFieldButtonGrp(self.duplicateRotateButton,text=True,query=True).split();mc.rotate(float(rotation[0]),float(rotation[1]),float(rotation[2]))""")
        self.duplicateScaleButton = mc.textFieldButtonGrp('duplicatescale',ad3=2,cw3=(40,80,50),label='scale', text='1 1 1', buttonLabel='duplicate',buttonCommand="""mc.duplicate(myobject,st=True);scale = mc.textFieldButtonGrp(self.duplicateScaleButton,text=True,query=True).split();mc.scale(float(scale[0]),float(scale[1]),float(scale[2]))""")
        mc.setParent('..')     
        
    def duplicatec(self):
        self.duplicatecFrameLayout = mc.frameLayout(label="duplicate", collapsable = True,borderStyle="etchedIn") 
        self.duplicatecColumnLayou = mc.columnLayout(columnAttach = ("left",5),adj=True)
        self.duplicatebutton()
        self.duplicatecColumnLayou2 = mc.columnLayout(columnAttach = ("both",5),adj=True)
        self.duplicatecText1 = mc.text(label='Only record last transform') 
        self.duplicatecText2 = mc.text(label='Type transform value') 
        self.duplicatecText3 = mc.text(label='Duplicate once and click smart') 
        self.duplicateButton = mc.button(label='smartTransfrom',command='mc.duplicate(st=True)')
        mc.setParent('..')

    def createobject(self):
        self.createFrameLayout = mc.frameLayout(label="create object", collapsable = True,borderStyle="etchedIn") 
        self.createColumnLayout = mc.columnLayout(columnAttach = ("both",5))
        self.createTextField = mc.textField('inputname',w=150,text='Type Object Name' )
        mc.setParent('..')
        self.createRowLayout = mc.rowLayout(numberOfColumns=3,adj=2,columnAlign3=("center","center","center"))
        self.createobjectbutton()
        mc.setParent('..')   
        
    def createobjectbutton(self):
        self.createSphereButton = mc.button('Sphere',w=50,command="""mytext= mc.textField(self.createTextField,text=True,query=True);myobject = mc.sphere(name=mytext)""")
        self.createCubeButton = mc.button('Cube',w=50,command="""mytext= mc.textField(self.createTextField,text=True,query=True);myobject = mc.Cube(name=mytext)""")
        self.createCylinderButton = mc.button('Cylinder',w=50,command="""mytext= mc.textField(self.createTextField,text=True,query=True);myobject = mc.cylinder(name=mytext)""")
        mc.setParent('..')
            

        
    def outliner(self):
        self.duplicatecFrameLayout = mc.frameLayout(label="duplicate", collapsable = True,borderStyle="etchedIn",w=300,h=550,en=1 ) 
        mc.frameLayout( labelVisible=False )
        panel = mc.outlinerPanel()
        outliner = mc.outlinerPanel(panel, query=True,outlinerEditor=True)
        mc.outlinerEditor( outliner, edit=True, mainListConnection='worldList', selectionConnection='modelList', showShapes=False, showAttributes=False, showConnected=False, showAnimCurvesOnly=False, autoExpand=False, showDagOnly=True, ignoreDagHierarchy=False, expandConnections=False, showNamespace=True, showCompounds=True, showNumericAttrsOnly=False, highlightActive=True, autoSelectNewObjects=False, doNotSelectNewObjects=False, transmitFilters=False, showSetMembers=True, setFilter='defaultSetFilter' )
        mc.setParent('..')
        mc.setParent('..')
        mc.setParent('..')
        
    def transformshelflayout(self):
        mc.shelfLayout('transfromshelf',h=100)
        mc.shelfButton( annotation='Create a sphere.', image1='sphere.png', command='mc.sphere()' ) 
        mc.shelfButton( annotation='Create a cube.', image1='cube.png', command='mc.nurbsCube()' )  
        mc.shelfButton( annotation='Create a cylinder.', image1='cylinder.png', command='mc.cylinder()' )  
        mc.shelfButton( annotation='Create a plane.', image1='plane.png', command='mc.plane()' ) 
        mc.shelfButton( annotation='Create a polySphere.', image1='polySphere.png', command='mc.polySphere()' )  
        mc.shelfButton( annotation='Create a polyCube.', image1='polyCube.png', command='mc.polyCube()' )   
        mc.shelfButton( annotation='Create a polyCylinder.', image1='polyCylinder.png', command='mc.polyCylinder()' )   
        mc.shelfButton( annotation='Create a polyPlane.', image1='polyPlane.png', command='mc.polyPlane()' )   
        mc.shelfButton( annotation='Freeze Transformations.', image1='fluidShape.svg', command='mc.makeIdentity(apply=True)' ,w=50,h=50)       
        mc.shelfButton( annotation='Center Pivot.', image1='buttonManip.svg', command="""object = mc.ls(sl=True); bbox = mc.exactWorldBoundingBox(object);center = [(bbox[0] + bbox[3])/2, (bbox[1]+bbox[4])/2, (bbox[2] + bbox[5])/2];mc.xform(object, piv=center, ws=True)""" ,w=50,h=50)  
        mc.shelfButton( annotation='Delete History.', image1='menuIconEdit.png', command='mc.DeleteHistory()' ,w=50,h=50)  
        mc.shelfButton( annotation='CV Curve Tool.', image1='curveCV.png', command="""maya.mel.eval("CVCurveTool();")""" ,w=50,h=50)  
        mc.shelfButton( annotation='Create a nurbsCircle.', image1='circle.png', command='mc.circle()' ,w=50,h=50)       
        mc.setParent( '..' )

        
    def animationshelflayout(self):
        mc.shelfLayout('animationshelf',h=40)
        mc.shelfButton( annotation='Create IK handle.', image1='kinHandle.png', command="""maya.mel.eval("IKHandleTool();")""" )  
        mc.shelfButton( annotation='JointTool.', image1='kinJoint.png', command="""maya.mel.eval("JointTool();")""" )
        mc.shelfButton( annotation='OrientJoint.', image1='orientJoint.png', command="""maya.mel.eval("OrientJointOptions();")""" )
        mc.shelfButton( annotation='SetKey.', image1='setKeyframe.png', command='mc.setKeyframe()')
        mc.shelfButton( annotation='directionallight.', image1='directionallight.png', command='mc.directionalLight()')
        mc.shelfButton( annotation='spotLight.', image1='spotlight.png', command='mc.spotLight()')
        mc.shelfButton( annotation='pointLight.', image1='pointlight.png', command='mc.pointLight()')
        mc.shelfButton( annotation='CreateCammera.', image1='view.png', command='mc.camera()')

        mc.setParent( '..' )
        
        
    def keytangent(self):
        mc.rowLayout('animabutton',nc=3)
        mc.button(label='GraphEditor',h=50,w=90,command="""maya.mel.eval("GraphEditor();")""" )
        mc.button(label='DopeSheet',h=50,w=90,command="""maya.mel.eval("DopeSheetEditor();")""" )
        mc.button(label='CharacterAnim',h=50,w=90,command="""maya.mel.eval("CharacterAnimationEditor();")""" )
        mc.setParent( '..' )
        mc.columnLayout(cat=('left',0),adjustableColumn=True)
        mc.radioButtonGrp( label='inTangentType ', labelArray3=['Auto', 'Linear', 'plateau'], numberOfRadioButtons=3,cw4=(90,50,50,0),on1="""maya.mel.eval('keyTangent -global -itt auto;')""",on2="""maya.mel.eval('keyTangent -global -itt linear;')""",on3="""maya.mel.eval('keyTangent -global -itt plateau;')""")
        mc.radioButtonGrp( label='outTangentType', labelArray3=['Auto', 'Linear', 'Step'], numberOfRadioButtons=3,cw4=(90,50,50,0),on1="""maya.mel.eval('keyTangent -global -ott auto;')""",on2="""maya.mel.eval('keyTangent -global -ott linear;')""",on3="""maya.mel.eval('keyTangent -global -ott step;')""")
        mc.text('no selection means default',align='center')
        mc.setParent( '..' )
        
        
        
    def blinn(self):
        global lastshadersg,lastshader
        shader = mc.shadingNode("blinn",asShader=True)
        shading_group = mc.sets(renderable=True,noSurfaceShader=True,empty=True)
        mc.connectAttr('%s.outColor' %shader ,'%s.surfaceShader' %shading_group)
        lastshadersg=shading_group
        lastshader=shader
        print lastshader
        
        
    def lambert(self):
        global lastshadersg,lastshader
        shader = mc.shadingNode("lambert",asShader=True)
        shading_group = mc.sets(renderable=True,noSurfaceShader=True,empty=True)
        mc.connectAttr('%s.outColor' %shader ,'%s.surfaceShader' %shading_group)
        lastshadersg=shading_group 
        lastshader=shader
        print lastshader
        
    def phong(self):
        global lastshader,lastshader
        shader = mc.shadingNode("phong",asShader=True)
        shading_group = mc.sets(renderable=True,noSurfaceShader=True,empty=True)
        mc.connectAttr('%s.outColor' %shader ,'%s.surfaceShader' %shading_group)
        lastshadersg=shading_group
        lastshader=shader
        print lastshader
        
    def assignshader(self):
        global lastshadersg
        object = mc.ls(sl=True)
        if lastshadersg:
            mc.sets(object, e=True, forceElement=lastshadersg)  
            
    def showeditor(self):
        global lastshader
        if lastshader:
            maya.mel.eval("showEditor %s;" %lastshader)
            
    def changecolor(self):
        global lastshader
        mc.colorEditor()
        rgb = mc.colorEditor(query=True, rgb=True)
        print 'RGB = ' + str(values)
        if rgb:
            mc.setAttr(lastshader+'.color',rgb[0],rgb[1],rgb[2])
        
        
    def createshader(self):
        mc.nodeIconButton( style='iconAndTextHorizontal', command="""maya.mel.eval("ArtPaintSkinWeightsTool();")""", image1='paintSkinWeights.png', label='PaintWeights',h=50,w=50)
        mc.nodeIconButton( style='iconAndTextHorizontal', command="""maya.mel.eval("HypershadeWindow();")""", image1='menuIconWindow.png', label='Hypershade',h=100,w=50)
        mc.rowLayout(nc=3)
        lastshader=''
        lastshadersg=''
        mc.nodeIconButton( style='iconAndTextHorizontal', command=self.blinn, image1='blinn.svg', label='blinn',h=50,w=90,ann='create a blinn shader.')
        mc.nodeIconButton( style='iconAndTextHorizontal', command=self.lambert, image1='lambert.svg', label='lambert',h=50,w=90,ann='create a lambert shader.')
        mc.nodeIconButton( style='iconAndTextHorizontal', command=self.phong, image1='phong.svg', label='phong',h=50,w=90,ann='create a phong shader.')
        mc.setParent( '..' )
        mc.nodeIconButton( style='iconAndTextHorizontal', command=self.showeditor, image1='menuIconWindow.png', label='last shader editwindow',h=50,w=90,ann='show edit window of last created shader')
        mc.nodeIconButton( style='iconAndTextHorizontal', command=self.assignshader, image1='aselect.png', label='assign last shader',h=50,w=90,ann='assign last created shader to selection.')
        mc.nodeIconButton( style='iconAndTextHorizontal', command=self.changecolor, image1='colorPresetSpectrum.png', label='chage last shader color',h=50,w=90,ann='change color last created shader.')
        mc.rowLayout(nc=3)
        mc.nodeIconButton( style='iconAndTextHorizontal', command="""maya.mel.eval("RenderIntoNewWindow();")""", image1='render.png', label='1Frame',h=90,w=90,ann='render this frame.')
        mc.nodeIconButton( style='iconAndTextHorizontal', command="""maya.mel.eval("unifiedRenderGlobalsWindow();")""", image1='renderGlobals.png', label='setting',h=90,w=90,ann='render setting window.')
        mc.nodeIconButton( style='iconAndTextHorizontal', command="""maya.mel.eval("BatchRender();")""", image1='menuIconRender.png', label='Batch',h=90,w=90,ann='BatchRender.')
        mc.setParent( '..' )        
        
        
    def tablayout(self):
        maintab = mc.tabLayout( 'mainShelfTab', image='smallTrash.png', imageVisible=True )
        tab1 = mc.columnLayout( 'Transfrom',adj=1)
        self.transformshelflayout()
        self.createobject()
        self.transform()
        self.duplicatec()
        mc.text('Final Project',h=30)
        mc.text('Junhao Fu',h=50,w=200)
        mc.setParent( '..' )
        mc.setParent( '..' )

        
        tab2 = mc.columnLayout( 'Outliner',adj=1)
        self.outliner()
        mc.setParent( '..' )
       
        
        tab3 = mc.columnLayout('Anim/Shad',adj=1)
        self.animationshelflayout()
        self.keytangent()
        self.createshader()
        mc.setParent( '..' )
        mc.setParent( '..' )




    def create(self):
        if mc.window(self.window, exists=True):
            mc.deleteUI(self.window, window=True)
        self.window = mc.window(self.title, title=self.title, widthHeight = self.size, menuBar=True)
        print(self.window)
        self.commonMenu()
        self.tablayout()
        mc.showWindow()




transformwindow = optionwindow()
transformwindow.create()
