__author__ = "leosol@gmail.com"
__copyright__ = "Copyleft (C) 2021 leosol"
__license__ = "GNU AGPLv3"



class RefreshCommand:
    def execute(self, sender, event):
        print("RefreshCommand: execute")
        self.settings.subSystem.computeChatList(self.settings.minChatToBeLarge)
        self.formObj.updateChatListFromSubsystem()
    def setFormObject(self, formObj):
        self.formObj = formObj
    def setSettings(self, settingsObj):
        self.settings = settingsObj

class KeepOnlyTextMessagesCommand:
    def execute(self, sender, event):
        print("KeepOnlyTextMessagesCommand: execute")
        chatIds = self.formObj.getSelectedChats()
        self.settings.subSystem.removeAllAttachments(chatIds, self.settings.maxAttachmentsSize)
        self.settings.subSystem.computeChatList(self.settings.minChatToBeLarge)
        self.formObj.updateChatListFromSubsystem()
    def setFormObject(self, formObj):
        self.formObj = formObj
    def setSettings(self, settingsObj):
        self.settings = settingsObj

class AddAllAttachmentsCommand:
    def execute(self, sender, event):
        print("AddAllAttachmentsCommand: execute")
        chatIds = self.formObj.getSelectedChats()
        self.settings.subSystem.addAllAttachments(chatIds)
        self.settings.subSystem.computeChatList(self.settings.minChatToBeLarge)
        self.formObj.updateChatListFromSubsystem()
    def setFormObject(self, formObj):
        self.formObj = formObj
    def setSettings(self, settingsObj):
        self.settings = settingsObj

class RemoveVideosCommand:
    def execute(self, sender, event):
        print("RemoveVideosCommand: execute")
        chatIds = self.formObj.getSelectedChats()
        mimeTypes = self.settings.videosTypes
        self.settings.subSystem.removeVideos(chatIds, mimeTypes, self.settings.maxAttachmentsSize)
        self.settings.subSystem.computeChatList(self.settings.minChatToBeLarge)
        self.formObj.updateChatListFromSubsystem()
    def setFormObject(self, formObj):
        self.formObj = formObj
    def setSettings(self, settingsObj):
        self.settings = settingsObj

class GenerateReportCommand:
    def execute(self, sender, event):
        print("GenerateReportCommand: execute")
        self.settings.generateReport()
        self.settings.subSystem.computeChatList(self.settings.minChatToBeLarge)
        self.formObj.updateChatListFromSubsystem()
    def setFormObject(self, formObj):
        self.formObj = formObj
    def setSettings(self, settingsObj):
        self.settings = settingsObj

class ApplySettingsChangedCommand:
    def execute(self, sender, event):
        if self.formObj is not None:
            workDir = self.formObj.defaultFolder.Text
            maxAttachmentsSize = int(self.formObj.maxAttachmentSize.Text)
            minChatToBeLarge = int (self.formObj.minChatSize.Text)
            videosTypes = []
            if self.formObj.ch1.Checked:
                videosTypes.append(self.formObj.ch1.Text)
            if self.formObj.ch2.Checked:
                videosTypes.append(self.formObj.ch2.Text)
            if self.formObj.ch3.Checked:
                videosTypes.append(self.formObj.ch3.Text)
            if self.formObj.ch4.Checked:
                videosTypes.append(self.formObj.ch4.Text)
            self.settings.workDir = workDir
            self.settings.maxAttachmentsSize = maxAttachmentsSize
            self.settings.minChatToBeLarge = minChatToBeLarge
            self.settings.videosTypes = videosTypes
            self.formObj.updateViewFromSettingsObject()
    def setFormObject(self, formObj):
        self.formObj = formObj
    def setSettings(self, settingsObj):
        self.settings = settingsObj
        dir(settingsObj.workDir)

class SelectAllCheckBoxesCommand:
    def execute(self, sender, event):
        if self.formObj is not None:
            self.formObj.selectAllChatsInGrid()
            self.formObj.chkBoxSelectAll.Checked = False
    def setFormObject(self, formObj):
        self.formObj = formObj
        print(formObj)
    def setSettings(self, settingsObj):
        self.settings = settingsObj

class RestoreSettingsCommand:
    def execute(self, sender, event):
        if self.formObj is not None:
            self.settings.restoreDefaults()
            self.formObj.updateViewFromSettingsObject()
    def setFormObject(self, formObj):
        self.formObj = formObj
        print(formObj)
    def setSettings(self, settingsObj):
        self.settings = settingsObj



applySettingsCommand = ApplySettingsChangedCommand()
restoreSettingsCommand = RestoreSettingsCommand()
refreshCommand = RefreshCommand()
keepOnlyTextMessagesCommand = KeepOnlyTextMessagesCommand()
addAllAttachmentsCommand = AddAllAttachmentsCommand()
removeVideosCommand = RemoveVideosCommand()
generateReportCommand = GenerateReportCommand()
selectAllCheckBoxesCommand = SelectAllCheckBoxesCommand()