import clr
clr.AddReference("System.Drawing")
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Windows")
clr.AddReference("System.Data")
clr.AddReference("PresentationFramework")
clr.AddReference("PresentationCore")
clr.AddReference("windowsbase")
clr.AddReference("System")

__author__ = "leosol@gmail.com"
__copyright__ = "Copyleft (C) 2021 leosol"
__license__ = "GNU AGPLv3"

from System import (Int64)

from System.Windows.Forms import (
    TextBox, CheckBox, ComboBox, Button, DockStyle,
    AnchorStyles, FlowLayoutPanel, TableLayoutPanelGrowStyle,
    ColumnStyle, SizeType, TableLayoutPanel, FlowDirection, BorderStyle, Padding,
    TableLayoutPanelCellPosition, DataGridView, DataGridViewColumn,
    DataGridViewTextBoxColumn, DataGridViewCheckBoxColumn)

from System.Drawing import (Image)
from System.IO import Path

from System.Drawing import Bitmap, Color, Size
from System.Windows.Forms import (Application, Form, Button, Label, DockStyle, AnchorStyles, FlowLayoutPanel, AutoSizeMode, TextBox, ComboBox, CheckBox,
                                  Appearance, TabControl, ToolStrip, ToolStripGripStyle, TabAlignment,
                                  TabPage, ScrollBars, ToolStripButton, ToolStripItemDisplayStyle,
                                  MenuStrip, ToolStripMenuItem, Keys)

from modules.Models import (Settings)
#from modules.Subsystem import (Subsystem, PathImageSubsystem, PathVideoSubsystem)
from modules.UFEDSubsystem import (Subsystem, PathImageSubsystem, PathVideoSubsystem)
from modules.Commands import (applySettingsCommand, restoreSettingsCommand, chatRefreshCommand, chatKeepOnlyTextMessagesCommand,
                              chatAddAllAttachmentsCommand, chatRemoveVideosCommand, chatGenerateReportCommand, chatSelectAllCheckBoxesCommand,
                              imagesSelectAllCheckBoxesCommand, pathImageRemoveCommand, pathImageAddCommand, pathImagesRefreshCommand, pathImagePredefinedRemoveCommand, pathImageAddAllCommand,
                              pathVideoAddAllCommand, pathVideoAddCommand, pathVideoPredefinedRemoveCommand, pathVideoRemoveCommand, videosSelectAllCheckBoxesCommand, pathVideosRefreshCommand)

executablePath = __file__
if executablePath is None:
    executablePath = Application.ExecutablePath
executableDirectory = Path.GetDirectoryName(executablePath)
globalSettings = Settings(executableDirectory, Subsystem(), PathImageSubsystem(), PathVideoSubsystem())
globalSettings.subSystem.computeChatList(globalSettings.minChatToBeLarge)


class VideosTab(TabPage):
    def __init__(self):
        self.Text = 'Videos'
        self.createContainer()
        self.createDataGrid()
        self.createGridControls()
        self.Controls.Add(self.container)
    def incCurrentRow(self):
        self.currentRow = self.currentRow + 1
    def createContainer(self):
        container = TableLayoutPanel()
        container.AutoSize = True
        container.Margin = Padding(10)
        container.Padding = Padding(10)
        container.Name = 'container name'
        container.ColumnCount = 3
        container.RowCount = 3
        container.AutoSizeMode = AutoSizeMode.GrowAndShrink
        container.GrowStyle = TableLayoutPanelGrowStyle.AddRows
        container.Dock = DockStyle.Fill
        container.ColumnStyles.Add(ColumnStyle(SizeType.Percent, 10))
        container.ColumnStyles.Add(ColumnStyle(SizeType.Percent, 70))
        container.ColumnStyles.Add(ColumnStyle(SizeType.Percent, 20))
        self.container = container
        self.currentRow = 0
    def createDataGrid(self):
        dataGridView = DataGridView()
        self.dataGridView = dataGridView
        dataGridView.Margin = Padding(10)
        dataGridView.Padding = Padding(10)
        dataGridView.Name = "Videos Data Grid View"
        dataGridView.AllowUserToAddRows = False
        dataGridView.Height = 480
        dataGridView.Width = 640

        chatPathColumn = DataGridViewTextBoxColumn()
        chatPathColumn.Name = "Path"
        dataGridView.Columns.Add(chatPathColumn)

        referencedCount = DataGridViewTextBoxColumn()
        referencedCount.Name = "Referenced Count"
        referencedCount.ValueType = Int64
        dataGridView.Columns.Add(referencedCount)

        actualSize = DataGridViewTextBoxColumn()
        actualSize.Name = "Size (MB)"
        actualSize.ValueType = Int64 #clr.GetClrType(type(123))
        dataGridView.Columns.Add(actualSize)

        originalSize = DataGridViewTextBoxColumn()
        originalSize.Name = "Initial Size (MB)"
        originalSize.ValueType = Int64
        dataGridView.Columns.Add(originalSize)

        selectItemColumn = DataGridViewCheckBoxColumn()
        selectItemColumn.Name = "Select"
        selectItemColumn.ToolTipText = "ToolTipText"
        dataGridView.Columns.Add(selectItemColumn)

        self.container.Controls.Add(dataGridView)
        self.container.SetCellPosition(dataGridView, TableLayoutPanelCellPosition(0, self.currentRow))
        self.container.SetColumnSpan(dataGridView, 2)
    def createGridControls(self):
        global globalSettings
        controlsContainer = FlowLayoutPanel()
        controlsContainer.FlowDirection = FlowDirection.TopDown
        controlsContainer.Dock = DockStyle.Fill

        chkBoxSelectAll = CheckBox()
        self.chkBoxSelectAll = chkBoxSelectAll
        chkBoxSelectAll.Text = "Select All"
        videosSelectAllCheckBoxesCommand.setSettings(globalSettings)
        videosSelectAllCheckBoxesCommand.setFormObject(self)
        chkBoxSelectAll.Click += videosSelectAllCheckBoxesCommand.execute

        btnRefresh = Button()
        # btnRemoveAttachments.Text = 'Refresh'
        btnRefresh.Image = Image.FromFile(globalSettings.defaultWorkDir+"\\icons\\refresh-btn.png");
        btnRefresh.AutoSize = True
        btnRefresh.Dock = DockStyle.Fill
        pathVideosRefreshCommand.setFormObject(self)
        pathVideosRefreshCommand.setSettings(globalSettings)
        btnRefresh.Click += pathVideosRefreshCommand.execute


        btnAddAll = Button()
        btnAddAll.Image = Image.FromFile(globalSettings.defaultWorkDir+"\\icons\\204-add-all.png");
        btnAddAll.AutoSize = True
        btnAddAll.Dock = DockStyle.Fill
        pathVideoAddAllCommand.setFormObject(self)
        pathVideoAddAllCommand.setSettings(globalSettings)
        btnAddAll.Click += pathVideoAddAllCommand.execute

        btnAddAllAttachments = Button()
        btnAddAllAttachments.Image = Image.FromFile(globalSettings.defaultWorkDir+"\\icons\\202-add-items-with-selected-paths.png");
        btnAddAllAttachments.AutoSize = True
        btnAddAllAttachments.Dock = DockStyle.Fill
        pathVideoAddCommand.setFormObject(self)
        pathVideoAddCommand.setSettings(globalSettings)
        btnAddAllAttachments.Click += pathVideoAddCommand.execute

        btnRemoveVideosAttachments = Button()
        #btnRemoveVideosAttachments.Text = 'Clear Video Attachments'
        btnRemoveVideosAttachments.Image = Image.FromFile(globalSettings.defaultWorkDir+"\\icons\\201-remove-items-with-path.png");
        btnRemoveVideosAttachments.AutoSize = True
        btnRemoveVideosAttachments.Dock = DockStyle.Fill
        pathVideoRemoveCommand.setFormObject(self)
        pathVideoRemoveCommand.setSettings(globalSettings)
        btnRemoveVideosAttachments.Click += pathVideoRemoveCommand.execute


        btnPredefinedRemoveVideosAttachments = Button()
        #btnPredefinedRemoveVideosAttachments.Text = 'Clear Video Attachments'
        btnPredefinedRemoveVideosAttachments.Image = Image.FromFile(globalSettings.defaultWorkDir+"\\icons\\203-remove-items-with-predefined-paths.png");
        btnPredefinedRemoveVideosAttachments.AutoSize = True
        btnPredefinedRemoveVideosAttachments.Dock = DockStyle.Fill
        pathVideoPredefinedRemoveCommand.setFormObject(self)
        pathVideoPredefinedRemoveCommand.setSettings(globalSettings)
        btnPredefinedRemoveVideosAttachments.Click += pathVideoPredefinedRemoveCommand.execute

        btnGenReport = Button()
        #btnGenReport.Text = 'Generate report'
        btnGenReport.Image = Image.FromFile(globalSettings.defaultWorkDir+"\\icons\\report-btn.png");
        btnGenReport.AutoSize = True
        btnGenReport.Dock = DockStyle.Fill
        chatGenerateReportCommand.setFormObject(self)
        chatGenerateReportCommand.setSettings(globalSettings)
        btnGenReport.Click += chatGenerateReportCommand.execute

        controlsContainer.Controls.Add(chkBoxSelectAll)
        controlsContainer.Controls.Add(btnRefresh)
        controlsContainer.Controls.Add(btnAddAll)
        controlsContainer.Controls.Add(btnAddAllAttachments)
        controlsContainer.Controls.Add(btnRemoveVideosAttachments)
        controlsContainer.Controls.Add(btnPredefinedRemoveVideosAttachments)
        controlsContainer.Controls.Add(btnGenReport)

        labelSelectedSizeVsTotalSize = Label()
        labelSelectedSizeVsTotalSize.Margin = Padding(10)
        labelSelectedSizeVsTotalSize.Text = "Selected / Total "
        controlsContainer.Controls.Add(labelSelectedSizeVsTotalSize)

        valueSelectedSizeVsTotalSize = Label()
        valueSelectedSizeVsTotalSize.Text = ""
        self.valueSelectedSizeVsTotalSize = valueSelectedSizeVsTotalSize
        controlsContainer.Controls.Add(valueSelectedSizeVsTotalSize)

        self.container.Controls.Add(controlsContainer)
        self.container.SetCellPosition(controlsContainer, TableLayoutPanelCellPosition(3, self.currentRow))
        self.incCurrentRow()
    def updatePathVideoListFromSubsystem(self):
        global globalSettings
        pathVideoList = globalSettings.pathVideoSubsystem.pathVideoList
        self.dataGridView.Rows.Clear()
        for item in pathVideoList.pathVideoItems:
            self.dataGridView.Rows.Add(item.ipath, int(item.refCount), int(item.actualSize), int(item.originalSize))
        selectedSize = globalSettings.pathVideoSubsystem.computeSelectedSize()
        totalSize = globalSettings.pathVideoSubsystem.computeTotalSize()
        self.valueSelectedSizeVsTotalSize.Text = str(selectedSize) + " / " + str(totalSize) + " (MB)"
    def selectAllItemsInGrid(self):
        for rowItem in self.dataGridView.Rows:
            rowItem.Cells[4].Value = True
    def getSelectedItems(self):
        selectedItems = []
        for rowItem in self.dataGridView.Rows:
                if rowItem.Cells[4].Value:
                    selectedItems.append(rowItem.Cells[0].Value)
        return selectedItems

class ImagesTab(TabPage):
    def __init__(self):
        self.Text = 'Images'
        self.createContainer()
        self.createDataGrid()
        self.createGridControls()
        self.Controls.Add(self.container)
    def incCurrentRow(self):
        self.currentRow = self.currentRow + 1
    def createContainer(self):
        container = TableLayoutPanel()
        container.AutoSize = True
        container.Margin = Padding(10)
        container.Padding = Padding(10)
        container.Name = 'container name'
        container.ColumnCount = 3
        container.RowCount = 3
        container.AutoSizeMode = AutoSizeMode.GrowAndShrink
        container.GrowStyle = TableLayoutPanelGrowStyle.AddRows
        container.Dock = DockStyle.Fill
        container.ColumnStyles.Add(ColumnStyle(SizeType.Percent, 10))
        container.ColumnStyles.Add(ColumnStyle(SizeType.Percent, 70))
        container.ColumnStyles.Add(ColumnStyle(SizeType.Percent, 20))
        self.container = container
        self.currentRow = 0
    def createDataGrid(self):
        dataGridView = DataGridView()
        self.dataGridView = dataGridView
        dataGridView.Margin = Padding(10)
        dataGridView.Padding = Padding(10)
        dataGridView.Name = "Images Data Grid View"
        dataGridView.AllowUserToAddRows = False
        dataGridView.Height = 480
        dataGridView.Width = 640

        chatPathColumn = DataGridViewTextBoxColumn()
        chatPathColumn.Name = "Path"
        dataGridView.Columns.Add(chatPathColumn)

        referencedCount = DataGridViewTextBoxColumn()
        referencedCount.Name = "Referenced Count"
        referencedCount.ValueType = Int64
        dataGridView.Columns.Add(referencedCount)

        actualSize = DataGridViewTextBoxColumn()
        actualSize.Name = "Size (MB)"
        actualSize.ValueType = Int64 #clr.GetClrType(type(123))
        dataGridView.Columns.Add(actualSize)

        originalSize = DataGridViewTextBoxColumn()
        originalSize.Name = "Initial Size (MB)"
        originalSize.ValueType = Int64
        dataGridView.Columns.Add(originalSize)

        selectItemColumn = DataGridViewCheckBoxColumn()
        selectItemColumn.Name = "Select"
        selectItemColumn.ToolTipText = "ToolTipText"
        dataGridView.Columns.Add(selectItemColumn)

        self.container.Controls.Add(dataGridView)
        self.container.SetCellPosition(dataGridView, TableLayoutPanelCellPosition(0, self.currentRow))
        self.container.SetColumnSpan(dataGridView, 2)
    def createGridControls(self):
        global globalSettings
        controlsContainer = FlowLayoutPanel()
        controlsContainer.FlowDirection = FlowDirection.TopDown
        controlsContainer.Dock = DockStyle.Fill

        chkBoxSelectAll = CheckBox()
        self.chkBoxSelectAll = chkBoxSelectAll
        chkBoxSelectAll.Text = "Select All"
        videosSelectAllCheckBoxesCommand.setSettings(globalSettings)
        videosSelectAllCheckBoxesCommand.setFormObject(self)
        chkBoxSelectAll.Click += videosSelectAllCheckBoxesCommand.execute

        btnRefresh = Button()
        # btnRemoveAttachments.Text = 'Refresh'
        btnRefresh.Image = Image.FromFile(globalSettings.defaultWorkDir+"\\icons\\refresh-btn.png");
        btnRefresh.AutoSize = True
        btnRefresh.Dock = DockStyle.Fill
        pathImagesRefreshCommand.setFormObject(self)
        pathImagesRefreshCommand.setSettings(globalSettings)
        btnRefresh.Click += pathImagesRefreshCommand.execute


        btnAddAll = Button()
        btnAddAll.Image = Image.FromFile(globalSettings.defaultWorkDir+"\\icons\\204-add-all.png");
        btnAddAll.AutoSize = True
        btnAddAll.Dock = DockStyle.Fill
        pathImageAddAllCommand.setFormObject(self)
        pathImageAddAllCommand.setSettings(globalSettings)
        btnAddAll.Click += pathImageAddAllCommand.execute

        btnAddAllAttachments = Button()
        btnAddAllAttachments.Image = Image.FromFile(globalSettings.defaultWorkDir+"\\icons\\202-add-items-with-selected-paths.png");
        btnAddAllAttachments.AutoSize = True
        btnAddAllAttachments.Dock = DockStyle.Fill
        pathImageAddCommand.setFormObject(self)
        pathImageAddCommand.setSettings(globalSettings)
        btnAddAllAttachments.Click += pathImageAddCommand.execute

        btnRemoveVideosAttachments = Button()
        #btnRemoveVideosAttachments.Text = 'Clear Video Attachments'
        btnRemoveVideosAttachments.Image = Image.FromFile(globalSettings.defaultWorkDir+"\\icons\\201-remove-items-with-path.png");
        btnRemoveVideosAttachments.AutoSize = True
        btnRemoveVideosAttachments.Dock = DockStyle.Fill
        pathImageRemoveCommand.setFormObject(self)
        pathImageRemoveCommand.setSettings(globalSettings)
        btnRemoveVideosAttachments.Click += pathImageRemoveCommand.execute


        btnPredefinedRemove = Button()
        btnPredefinedRemove.Image = Image.FromFile(globalSettings.defaultWorkDir+"\\icons\\203-remove-items-with-predefined-paths.png");
        btnPredefinedRemove.AutoSize = True
        btnPredefinedRemove.Dock = DockStyle.Fill
        pathImagePredefinedRemoveCommand.setFormObject(self)
        pathImagePredefinedRemoveCommand.setSettings(globalSettings)
        btnPredefinedRemove.Click += pathImagePredefinedRemoveCommand.execute

        btnGenReport = Button()
        #btnGenReport.Text = 'Generate report'
        btnGenReport.Image = Image.FromFile(globalSettings.defaultWorkDir+"\\icons\\report-btn.png");
        btnGenReport.AutoSize = True
        btnGenReport.Dock = DockStyle.Fill
        chatGenerateReportCommand.setFormObject(self)
        chatGenerateReportCommand.setSettings(globalSettings)
        btnGenReport.Click += chatGenerateReportCommand.execute

        controlsContainer.Controls.Add(chkBoxSelectAll)
        controlsContainer.Controls.Add(btnRefresh)
        controlsContainer.Controls.Add(btnAddAll)
        controlsContainer.Controls.Add(btnAddAllAttachments)
        controlsContainer.Controls.Add(btnRemoveVideosAttachments)
        controlsContainer.Controls.Add(btnPredefinedRemove)
        controlsContainer.Controls.Add(btnGenReport)

        labelSelectedSizeVsTotalSize = Label()
        labelSelectedSizeVsTotalSize.Margin = Padding(10)
        labelSelectedSizeVsTotalSize.Text = "Selected / Total "
        controlsContainer.Controls.Add(labelSelectedSizeVsTotalSize)

        valueSelectedSizeVsTotalSize = Label()
        valueSelectedSizeVsTotalSize.Text = ""
        self.valueSelectedSizeVsTotalSize = valueSelectedSizeVsTotalSize
        controlsContainer.Controls.Add(valueSelectedSizeVsTotalSize)

        self.container.Controls.Add(controlsContainer)
        self.container.SetCellPosition(controlsContainer, TableLayoutPanelCellPosition(3, self.currentRow))
        self.incCurrentRow()
    def updatePathImageListFromSubsystem(self):
        global globalSettings
        pathImageList = globalSettings.pathImageSubsystem.pathImageList
        self.dataGridView.Rows.Clear()
        for item in pathImageList.pathImageItems:
            self.dataGridView.Rows.Add(item.ipath, int(item.refCount), int(item.actualSize), int(item.originalSize))
        selectedSize = globalSettings.pathImageSubsystem.computeSelectedSize()
        totalSize = globalSettings.pathImageSubsystem.computeTotalSize()
        self.valueSelectedSizeVsTotalSize.Text = str(selectedSize) + " / " + str(totalSize) + " (MB)"
    def selectAllItemsInGrid(self):
        for rowItem in self.dataGridView.Rows:
            rowItem.Cells[4].Value = True
    def getSelectedItems(self):
        selectedItems = []
        for rowItem in self.dataGridView.Rows:
                if rowItem.Cells[4].Value:
                    selectedItems.append(rowItem.Cells[0].Value)
        return selectedItems

class ChatsTab(TabPage):
    def __init__(self):
        self.Text = 'Chats'
        self.createContainer()
        self.createDataGrid()
        self.createGridControls()
        self.Controls.Add(self.container)
        self.updateChatListFromSubsystem()
    def incCurrentRow(self):
        self.currentRow = self.currentRow + 1
    def createContainer(self):
        container = TableLayoutPanel()
        container.AutoSize = True
        container.Margin = Padding(10)
        container.Padding = Padding(10)
        container.Name = 'container name'
        container.ColumnCount = 3
        container.RowCount = 3
        container.AutoSizeMode = AutoSizeMode.GrowAndShrink
        container.GrowStyle = TableLayoutPanelGrowStyle.AddRows
        container.Dock = DockStyle.Fill
        container.ColumnStyles.Add(ColumnStyle(SizeType.Percent, 10))
        container.ColumnStyles.Add(ColumnStyle(SizeType.Percent, 70))
        container.ColumnStyles.Add(ColumnStyle(SizeType.Percent, 20))
        self.container = container
        self.currentRow = 0
    def selectChatClick(self, sender, eventArgs):
        print("Clicked at ")
    def createDataGrid(self):
        dataGridView = DataGridView()
        self.dataGridView = dataGridView
        dataGridView.Margin = Padding(10)
        dataGridView.Padding = Padding(10)
        dataGridView.Name = "Chats Data Grid View"
        dataGridView.AllowUserToAddRows = False
        dataGridView.Height = 480
        dataGridView.Width = 640

        chatIdColumn = DataGridViewTextBoxColumn()
        chatIdColumn.Name = "Chat ID"
        dataGridView.Columns.Add(chatIdColumn)

        chatParticipantsColumn = DataGridViewTextBoxColumn()
        chatParticipantsColumn.Name = "Participants"
        chatParticipantsColumn.ValueType = Int64
        dataGridView.Columns.Add(chatParticipantsColumn)

        attachmentsCount = DataGridViewTextBoxColumn()
        attachmentsCount.Name = "Attachments"
        attachmentsCount.ValueType = Int64
        dataGridView.Columns.Add(attachmentsCount)

        chatSize = DataGridViewTextBoxColumn()
        chatSize.Name = "Size (MB)"
        chatSize.ValueType = Int64 #clr.GetClrType(type(123))
        dataGridView.Columns.Add(chatSize)

        chatSizeOriginal = DataGridViewTextBoxColumn()
        chatSizeOriginal.Name = "Initial Size (MB)"
        chatSizeOriginal.ValueType = Int64
        dataGridView.Columns.Add(chatSizeOriginal)

        selectChatColumn = DataGridViewCheckBoxColumn()
        selectChatColumn.Name = "Select"
        selectChatColumn.ToolTipText = "ToolTipText"
        dataGridView.Columns.Add(selectChatColumn)

        self.container.Controls.Add(dataGridView)
        self.container.SetCellPosition(dataGridView, TableLayoutPanelCellPosition(0, self.currentRow))
        self.container.SetColumnSpan(dataGridView, 2)
    def createGridControls(self):
        global globalSettings
        controlsContainer = FlowLayoutPanel()
        controlsContainer.FlowDirection = FlowDirection.TopDown
        controlsContainer.Dock = DockStyle.Fill

        chkBoxSelectAll = CheckBox()
        self.chkBoxSelectAll = chkBoxSelectAll
        chkBoxSelectAll.Text = "Select All"
        chatSelectAllCheckBoxesCommand.setSettings(globalSettings)
        chatSelectAllCheckBoxesCommand.setFormObject(self)
        chkBoxSelectAll.Click += chatSelectAllCheckBoxesCommand.execute

        btnRefresh = Button()
        # btnRemoveAttachments.Text = 'Refresh'
        btnRefresh.Image = Image.FromFile(globalSettings.defaultWorkDir+"\\icons\\refresh-btn.png");
        btnRefresh.AutoSize = True
        btnRefresh.Dock = DockStyle.Fill
        chatRefreshCommand.setFormObject(self)
        chatRefreshCommand.setSettings(globalSettings)
        btnRefresh.Click += chatRefreshCommand.execute

        btnRemoveAttachments = Button()
        #btnRemoveAttachments.Text = 'Clear All Attachments'
        btnRemoveAttachments.Image = Image.FromFile(globalSettings.defaultWorkDir+"\\icons\\remove-non-text-btn.png");
        btnRemoveAttachments.AutoSize = True
        btnRemoveAttachments.Dock = DockStyle.Fill
        chatKeepOnlyTextMessagesCommand.setFormObject(self)
        chatKeepOnlyTextMessagesCommand.setSettings(globalSettings)
        btnRemoveAttachments.Click += chatKeepOnlyTextMessagesCommand.execute

        btnAddAllAttachments = Button()
        btnAddAllAttachments.Image = Image.FromFile(globalSettings.defaultWorkDir+"\\icons\\all-attachs-btn.png");
        btnAddAllAttachments.AutoSize = True
        btnAddAllAttachments.Dock = DockStyle.Fill
        chatAddAllAttachmentsCommand.setFormObject(self)
        chatAddAllAttachmentsCommand.setSettings(globalSettings)
        btnAddAllAttachments.Click += chatAddAllAttachmentsCommand.execute

        btnRemoveVideosAttachments = Button()
        #btnRemoveVideosAttachments.Text = 'Clear Video Attachments'
        btnRemoveVideosAttachments.Image = Image.FromFile(globalSettings.defaultWorkDir+"\\icons\\remove-videos-btn.png");
        btnRemoveVideosAttachments.AutoSize = True
        btnRemoveVideosAttachments.Dock = DockStyle.Fill
        chatRemoveVideosCommand.setFormObject(self)
        chatRemoveVideosCommand.setSettings(globalSettings)
        btnRemoveVideosAttachments.Click += chatRemoveVideosCommand.execute

        btnGenReport = Button()
        #btnGenReport.Text = 'Generate report'
        btnGenReport.Image = Image.FromFile(globalSettings.defaultWorkDir+"\\icons\\report-btn.png");
        btnGenReport.AutoSize = True
        btnGenReport.Dock = DockStyle.Fill
        chatGenerateReportCommand.setFormObject(self)
        chatGenerateReportCommand.setSettings(globalSettings)
        btnGenReport.Click += chatGenerateReportCommand.execute

        controlsContainer.Controls.Add(chkBoxSelectAll)
        controlsContainer.Controls.Add(btnRefresh)
        controlsContainer.Controls.Add(btnRemoveAttachments)
        controlsContainer.Controls.Add(btnAddAllAttachments)
        controlsContainer.Controls.Add(btnRemoveVideosAttachments)
        controlsContainer.Controls.Add(btnGenReport)

        labelSelectedSizeVsTotalSize = Label()
        labelSelectedSizeVsTotalSize.Margin = Padding(10)
        labelSelectedSizeVsTotalSize.Text = "Selected / Total "
        controlsContainer.Controls.Add(labelSelectedSizeVsTotalSize)

        valueSelectedSizeVsTotalSize = Label()
        valueSelectedSizeVsTotalSize.Text = ""
        self.valueSelectedSizeVsTotalSize = valueSelectedSizeVsTotalSize
        controlsContainer.Controls.Add(valueSelectedSizeVsTotalSize)

        self.container.Controls.Add(controlsContainer)
        self.container.SetCellPosition(controlsContainer, TableLayoutPanelCellPosition(3, self.currentRow))
        self.incCurrentRow()
    def updateChatListFromSubsystem(self):
        global globalSettings
        chatList = globalSettings.subSystem.chatList
        self.dataGridView.Rows.Clear()
        for chatItem in chatList.chatItems:
            self.dataGridView.Rows.Add(chatItem.chatId, int(chatItem.participantsCount), int(chatItem.attachmentsCount), int(chatItem.selectedSize), int(chatItem.totalSize))
        selectedSize = globalSettings.subSystem.computeSelectedSize()
        totalSize = globalSettings.subSystem.computeTotalSize()
        self.valueSelectedSizeVsTotalSize.Text = str(selectedSize)+" / "+str(totalSize)+" (MB)"
    def getSelectedChats(self):
        selectedItems = []
        for rowItem in self.dataGridView.Rows:
                if rowItem.Cells[5].Value:
                    selectedItems.append(rowItem.Cells[0].Value)
        return selectedItems
    def selectAllChatsInGrid(self):
        for rowItem in self.dataGridView.Rows:
            rowItem.Cells[5].Value = True

class SettingsTab(TabPage):
    def __init__(self):
        self.Text = 'Settings'
        container = self.createContainer()
        currentRow = 0
        self.createDefaultFolderSettings(container, currentRow)
        currentRow += 1
        self.createMaxAttachmentSettings(container, currentRow)
        currentRow += 1
        self.createMinChatSettings(container, currentRow)
        currentRow += 1
        self.createMinDirDepth(container, currentRow)
        currentRow += 1
        self.createMaxDirDepth(container, currentRow)
        currentRow += 1
        self.createMinDirSize(container, currentRow)
        currentRow += 1
        self.createVideoMimeTypes(container, currentRow)
        currentRow += 1
        self.createActionButtons(container, currentRow)
        currentRow += 1
        self.Controls.Add(container)
        self.updateViewFromSettingsObject()
    def createContainer(self):
        container = TableLayoutPanel()
        container.AutoSize = True
        container.Margin = Padding(10)
        container.Padding = Padding(10)
        container.Name = 'container name'
        container.ColumnCount = 3
        container.RowCount = 3
        container.AutoSizeMode = AutoSizeMode.GrowAndShrink
        container.GrowStyle = TableLayoutPanelGrowStyle.AddRows
        container.Dock = DockStyle.Fill
        container.ColumnStyles.Add(ColumnStyle(SizeType.Percent, 40))
        container.ColumnStyles.Add(ColumnStyle(SizeType.Percent, 50))
        container.ColumnStyles.Add(ColumnStyle(SizeType.Percent, 10))
        return container
    def createDefaultFolderSettings(self, container, currentRow):
        labelDefaultFolder = Label()
        labelDefaultFolder.Text = "Work dir:"
        container.Controls.Add(labelDefaultFolder, 0, currentRow)
        self.defaultFolder = TextBox()
        self.defaultFolder.Dock = DockStyle.Fill
        container.Controls.Add(self.defaultFolder, 1, currentRow)
    def createMaxAttachmentSettings(self, container, currentRow):
        labelMaxAttachmentSize = Label()
        labelMaxAttachmentSize.Text = "Max Attachment Size (bytes)"
        labelMaxAttachmentSize.Dock = DockStyle.Fill
        container.Controls.Add(labelMaxAttachmentSize, 0, currentRow)
        twoInARow = FlowLayoutPanel()
        twoInARow.AutoSize = True
        twoInARow.Dock = DockStyle.Fill
        twoInARow.BorderStyle = BorderStyle.None #FixedSingle
        twoInARow.Margin = Padding(0)
        twoInARow.Padding = Padding(0)
        twoInARow.AutoSizeMode = AutoSizeMode.GrowAndShrink
        twoInARow.FlowDirection = FlowDirection.LeftToRight
        self.maxAttachmentSize = TextBox()
        twoInARow.Controls.Add(self.maxAttachmentSize)
        #container.Controls.Add(maxAttachmentSize, 1, currentRow)
        hintMaxAttachmentSize = Label()
        hintMaxAttachmentSize.Text = "" #no hint
        twoInARow.Controls.Add(hintMaxAttachmentSize)
        #container.Controls.Add(hintMaxAttachmentSize, 2, currentRow)
        container.Controls.Add(twoInARow, 1, currentRow)
    def createMinDirDepth(self, container, currentRow):
        labelMinDirDepth = Label()
        labelMinDirDepth.Text = "Min Dir Depth"
        labelMinDirDepth.Dock = DockStyle.Fill
        container.Controls.Add(labelMinDirDepth, 0, currentRow)
        twoInARow = FlowLayoutPanel()
        twoInARow.AutoSize = True
        twoInARow.Dock = DockStyle.Fill
        twoInARow.BorderStyle = BorderStyle.None #FixedSingle
        twoInARow.Margin = Padding(0)
        twoInARow.Padding = Padding(0)
        twoInARow.AutoSizeMode = AutoSizeMode.GrowAndShrink
        twoInARow.FlowDirection = FlowDirection.LeftToRight
        self.minDirDepth = TextBox()
        twoInARow.Controls.Add(self.minDirDepth)
        container.Controls.Add(twoInARow, 1, currentRow)
    def createMaxDirDepth(self, container, currentRow):
        labelMaxDirDepth = Label()
        labelMaxDirDepth.Text = "Max Dir Depth"
        labelMaxDirDepth.Dock = DockStyle.Fill
        container.Controls.Add(labelMaxDirDepth, 0, currentRow)
        twoInARow = FlowLayoutPanel()
        twoInARow.AutoSize = True
        twoInARow.Dock = DockStyle.Fill
        twoInARow.BorderStyle = BorderStyle.None #FixedSingle
        twoInARow.Margin = Padding(0)
        twoInARow.Padding = Padding(0)
        twoInARow.AutoSizeMode = AutoSizeMode.GrowAndShrink
        twoInARow.FlowDirection = FlowDirection.LeftToRight
        self.maxDirDepth = TextBox()
        twoInARow.Controls.Add(self.maxDirDepth)
        container.Controls.Add(twoInARow, 1, currentRow)
    def createMinDirSize(self, container, currentRow):
        labelMinDirSize = Label()
        labelMinDirSize.Text = "Min Dir Size (MB)"
        labelMinDirSize.Dock = DockStyle.Fill
        container.Controls.Add(labelMinDirSize, 0, currentRow)
        twoInARow = FlowLayoutPanel()
        twoInARow.AutoSize = True
        twoInARow.Dock = DockStyle.Fill
        twoInARow.BorderStyle = BorderStyle.None #FixedSingle
        twoInARow.Margin = Padding(0)
        twoInARow.Padding = Padding(0)
        twoInARow.AutoSizeMode = AutoSizeMode.GrowAndShrink
        twoInARow.FlowDirection = FlowDirection.LeftToRight
        self.minDirSize = TextBox()
        twoInARow.Controls.Add(self.minDirSize)
        container.Controls.Add(twoInARow, 1, currentRow)
    def createMinChatSettings(self, container, currentRow):
        labelMinChatSize = Label()
        labelMinChatSize.Text = "Min chat size"
        labelMinChatSize.Dock = DockStyle.Fill
        labelMinChatSize.AutoSize = True
        container.Controls.Add(labelMinChatSize, 0, currentRow)
        twoInARow = FlowLayoutPanel()
        twoInARow.AutoSize = True
        twoInARow.Dock = DockStyle.Fill
        twoInARow.BorderStyle = BorderStyle.None #FixedSingle
        twoInARow.Margin = Padding(0)
        twoInARow.Padding = Padding(0)
        twoInARow.AutoSizeMode = AutoSizeMode.GrowAndShrink
        twoInARow.FlowDirection = FlowDirection.LeftToRight
        self.minChatSize = TextBox()
        twoInARow.Controls.Add(self.minChatSize)
        hintMinChatSize = Label()
        hintMinChatSize.Text = " to be considered large" #no hint
        twoInARow.Controls.Add(hintMinChatSize)
        container.Controls.Add(twoInARow, 1, currentRow)
    def updateViewFromSettingsObject(self):
        global globalSettings
        self.defaultFolder.Text = globalSettings.workDir
        self.maxAttachmentSize.Text = str(globalSettings.maxAttachmentsSize)
        self.minChatSize.Text = str(globalSettings.minChatToBeLarge)
        self.minDirDepth.Text = str(globalSettings.minFileDepth)
        self.minDirSize.Text = str(globalSettings.minDirSize)
        self.maxDirDepth.Text = str(globalSettings.maxFileDepth)
        if "video/mp4" in globalSettings.videosTypes:
            self.ch1.Checked = True
        if "video/mpeg" in globalSettings.videosTypes:
            self.ch2.Checked = True
        if "video/quicktime" in globalSettings.videosTypes:
            self.ch3.Checked = True
        if "video/x-m4v" in globalSettings.videosTypes:
            self.ch4.Checked = True
        globalSettings.printSettings()
    def createVideoMimeTypes(self, container, currentRow):
        checkBoxContainer = TableLayoutPanel()
        checkBoxContainer.AutoSize = True
        checkBoxContainer.Margin = Padding(10)
        checkBoxContainer.Padding = Padding(10)
        checkBoxContainer.Name = 'Checkbox Container'
        checkBoxContainer.ColumnCount = 4
        checkBoxContainer.RowCount = 4
        checkBoxContainer.AutoSize = True
        checkBoxContainer.AutoSizeMode = AutoSizeMode.GrowAndShrink
        checkBoxContainer.GrowStyle = TableLayoutPanelGrowStyle.AddRows
        checkBoxContainer.Dock = DockStyle.Fill
        checkBoxContainer.ColumnStyles.Add(ColumnStyle(SizeType.Percent, 25))
        checkBoxContainer.ColumnStyles.Add(ColumnStyle(SizeType.Percent, 25))
        checkBoxContainer.ColumnStyles.Add(ColumnStyle(SizeType.Percent, 25))
        checkBoxContainer.ColumnStyles.Add(ColumnStyle(SizeType.Percent, 25))

        labelMimetypes = Label()
        labelMimetypes.Text = "Videos"
        labelMimetypes.AutoSize = True
        checkBoxContainer.Controls.Add(labelMimetypes, 0, 0)

        self.ch1 = CheckBox()
        self.ch1.Text = "video/mp4"
        self.ch1.AutoSize = True

        checkBoxContainer.Controls.Add(self.ch1, 0, 1)
        self.ch2 = CheckBox()
        self.ch2.Text = "video/mpeg"

        self.ch2.AutoSize = True
        checkBoxContainer.Controls.Add(self.ch2, 1, 1)
        self.ch3 = CheckBox()
        self.ch3.Text = "video/quicktime"

        self.ch3.AutoSize = True
        checkBoxContainer.Controls.Add(self.ch3, 2, 1)
        self.ch4 = CheckBox()
        self.ch4.Text = "video/x-m4v"

        self.ch4.AutoSize = True
        checkBoxContainer.Controls.Add(self.ch4, 3, 1)

        container.Controls.Add(checkBoxContainer)
        container.SetCellPosition(checkBoxContainer, TableLayoutPanelCellPosition(0, currentRow))
        container.SetColumnSpan(checkBoxContainer, 2);
    def createActionButtons(self, container, currentRow):
        global globalSettings
        objectsInCenter = FlowLayoutPanel()
        restoreDefaults = Button()
        restoreDefaults.Text = 'Restore defaults'
        restoreSettingsCommand.setFormObject(self)
        restoreSettingsCommand.setSettings(globalSettings)
        restoreDefaults.Click += restoreSettingsCommand.execute
        restoreDefaults.AutoSize = True
        objectsInCenter.Controls.Add(restoreDefaults)
        applyBtn = Button()
        applyBtn.Text = "Apply changes"
        applyBtn.AutoSize = True
        applySettingsCommand.setFormObject(self)
        applySettingsCommand.setSettings(globalSettings)
        applyBtn.Click += applySettingsCommand.execute
        objectsInCenter.Controls.Add(applyBtn)
        objectsInCenter.Dock = DockStyle.Fill
        objectsInCenter.AutoSize = True
        objectsInCenter.AutoSizeMode = AutoSizeMode.GrowAndShrink
        objectsInCenter.BorderStyle = BorderStyle.None
        objectsInCenter.FlowDirection = FlowDirection.RightToLeft
        container.Controls.Add(objectsInCenter)
        container.SetCellPosition(objectsInCenter, TableLayoutPanelCellPosition(0,currentRow))
        container.SetColumnSpan(objectsInCenter, 2)

class AboutTab(TabPage):
    def __init__(self):
        self.Text = 'About'
        container = self.createContainer()
        self.addCredits(container)
        self.Controls.Add(container)
    def createContainer(self):
        container = FlowLayoutPanel()
        container.AutoSize = True
        container.Dock = DockStyle.Fill
        container.BorderStyle = BorderStyle.None  # FixedSingle
        container.Margin = Padding(0)
        container.Padding = Padding(0)
        container.AutoSizeMode = AutoSizeMode.GrowAndShrink
        container.FlowDirection = FlowDirection.TopDown
        return container
    def addCredits(self, container):
        authorLabel = Label()
        authorLabel.Text = "Author: leosol@gmail.com\n\nhttps://github.com/leosol\n\nLicensed under GNU AGPLv3"
        authorLabel.MinimumSize = Size(200, 200)
        authorLabel.Margin = Padding(400, 200, 0, 0)
        authorLabel.Padding = Padding(0)
        authorLabel.BorderStyle = BorderStyle.None
        container.Controls.Add(authorLabel)

class MainForm(Form):
    def __init__(self, workDir):
        global globalSettings
        Form.__init__(self)
        globalSettings.workDir = workDir
        globalSettings.defaultWorkDir = workDir
    def initializeTabs(self):
        self.Text = 'Chat Cleaner'
        self.MinimumSize = Size(996, 660)
        tab = self.tabControl = TabControl()
        imagesTab = ImagesTab()
        tab.TabPages.Add(imagesTab)
        videosTab = VideosTab()
        tab.TabPages.Add(videosTab)
        chatsTab = ChatsTab()
        tab.TabPages.Add(chatsTab)
        settingsTab = SettingsTab()
        tab.TabPages.Add(settingsTab)
        aboutTab = AboutTab()
        tab.TabPages.Add(aboutTab)
        self.tabControl.Dock = DockStyle.Fill
        self.tabControl.Alignment = TabAlignment.Top
        self.Controls.Add(self.tabControl)
        #self.initializeToolbar()
        #self.initializeMenus()
    def initializeToolbar(self):
        global globalSettings
        self.iconPath = Path.Combine(globalSettings.defaultWorkDir, 'icons')
        self.toolBar = ToolStrip()
        self.toolBar.Dock = DockStyle.Top
        self.toolBar.GripStyle = ToolStripGripStyle.Hidden
        self.addToolbarItem('Refresh', lambda sender, event: chatRefreshCommand.execute(None, None), '001-refresh-arrow.png')
        self.addToolbarItem('Report', lambda sender, event: chatGenerateReportCommand.execute(None, None), '002-report.png')
        self.Controls.Add(self.toolBar)
    def addToolbarItem(self, name, clickHandler, iconFile):
        button = ToolStripButton()
        button.Image = Bitmap(Path.Combine(self.iconPath, iconFile))
        button.ImageTransparentColor = Color.Magenta
        button.ToolTipText = name
        button.DisplayStyle = ToolStripItemDisplayStyle.Image
        button.Click += clickHandler
        self.toolBar.Items.Add(button)
    def initializeMenus(self):
        menuStrip = MenuStrip()
        menuStrip.Dock = DockStyle.Top
        fileMenu = self.createMenuItem('&File')
        saveKeys = Keys.Control | Keys.D
        #saveLogsMenuItem = self.createMenuItem(
        #    '&Save debug info',
        #    handler=self.saveLogsCommand.execute,
        #    keys=saveKeys
        #)

        saveKeys = Keys.Control | Keys.S
        #saveMenuItem = self.createMenuItem(
        #    '&Save...',
        #    handler=lambda sender, event: self.saveCommand.execute(),
        #    keys=saveKeys
        #)
        saveAsKeys = Keys.Control | Keys.Shift | Keys.S
        #saveAsMenuItem = self.createMenuItem(
        #    'S&ave As...',
        #    lambda sender, event: self.saveAsCommand.execute(),
        #    keys=saveAsKeys
        #)
        #fileMenu.DropDownItems.Add(saveLogsMenuItem)
        #fileMenu.DropDownItems.Add(saveMenuItem)
        #fileMenu.DropDownItems.Add(saveAsMenuItem)
        menuStrip.Items.Add(fileMenu)
        self.Controls.Add(menuStrip)
    def createMenuItem(self, text, handler=None, keys=None):
        menuItem = ToolStripMenuItem()
        menuItem.Text = text
        if keys:
            menuItem.ShortcutKeys = keys
        if handler:
            menuItem.Click += handler
        return menuItem