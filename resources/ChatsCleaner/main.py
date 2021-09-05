import sys
import clr
clr.AddReference("System.Drawing")
clr.AddReference("System.Windows.Forms")


__author__ = "leosol@gmail.com"
__copyright__ = "Copyleft (C) 2021 leosol"
__license__ = "GNU AGPLv3"
__version__ = "1.0"

from System.IO import Directory, File, Path

from System.Windows.Forms import ( Application, Form, Button, Label, DockStyle, AnchorStyles, Panel,
                                   Screen, FlowLayoutPanel, AutoSizeMode, TextBox, ComboBox, CheckBox,
                                   Appearance, TabControl, ToolStrip, ToolStripGripStyle, TabAlignment,
                                   TabPage, ScrollBars, SaveFileDialog, ToolStripButton, ToolStripItemDisplayStyle,
                                   MenuStrip, ToolStripMenuItem, Keys)

from modules.Gui import MainForm
print("Path: "+str(sys.path))
executablePath = __file__
if executablePath is None:
    executablePath = Application.ExecutablePath
executableDirectory = Path.GetDirectoryName(executablePath)


print("PyThon v. "+str(sys.version_info))

Application.EnableVisualStyles()
mainWindow = MainForm(executableDirectory)
mainWindow.initializeTabs()
Application.Run(mainWindow)