__author__ = "leosol@gmail.com"
__copyright__ = "Copyleft (C) 2021 leosol"
__license__ = "GNU AGPLv3"



class ChatRefreshCommand:
    def execute(self, sender, event):
        print("RefreshCommand: execute")
        self.settings.subSystem.computeChatList(self.settings.minChatToBeLarge)
        self.formObj.updateChatListFromSubsystem()
    def setFormObject(self, formObj):
        self.formObj = formObj
    def setSettings(self, settingsObj):
        self.settings = settingsObj

class ChatKeepOnlyTextMessagesCommand:
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

class ChatAddAllAttachmentsCommand:
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

class PathImageAddCommand:
    def execute(self, sender, event):
        print("PathImageAddCommand: execute")
        items = self.formObj.getSelectedItems()
        self.settings.pathImageSubsystem.addAllByPath(items)
        self.settings.pathImageSubsystem.computeList(self.settings.minChatToBeLarge)
        self.formObj.updatePathImageListFromSubsystem()
    def setFormObject(self, formObj):
        self.formObj = formObj
    def setSettings(self, settingsObj):
        self.settings = settingsObj

class ChatRemoveVideosCommand:
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

class PathImageRemoveCommand:
    def execute(self, sender, event):
        print("PathImageRemoveCommand: execute")
        pathsToRemove = self.formObj.getSelectedItems()
        self.settings.pathImageSubsystem.removeAllByPath(pathsToRemove)
        self.settings.pathImageSubsystem.computeList(self.settings.minChatToBeLarge)
        self.formObj.updatePathImageListFromSubsystem()
    def setFormObject(self, formObj):
        self.formObj = formObj
    def setSettings(self, settingsObj):
        self.settings = settingsObj


class PathImageAddAllCommand:
    def execute(self, sender, event):
        print("PathImageAddAllCommand: execute")
        self.settings.pathImageSubsystem.addAll()
        self.settings.pathImageSubsystem.computeList(self.settings.minChatToBeLarge)
        self.formObj.updatePathImageListFromSubsystem()
    def setFormObject(self, formObj):
        self.formObj = formObj
    def setSettings(self, settingsObj):
        self.settings = settingsObj

class PathImageAddCommand:
    def execute(self, sender, event):
        print("PathImageAddCommand: execute")
        pathsToRemove = self.formObj.getSelectedItems()
        self.settings.pathImageSubsystem.addAllByPath(pathsToRemove)
        self.settings.pathImageSubsystem.computeList(self.settings.minChatToBeLarge)
        self.formObj.updatePathImageListFromSubsystem()
    def setFormObject(self, formObj):
        self.formObj = formObj
    def setSettings(self, settingsObj):
        self.settings = settingsObj

class PathImagePredefinedRemoveCommand:
    def execute(self, sender, event):
        print("PathImagePredefinedRemoveCommand: execute")
        pathsToRemove = self.formObj.getSelectedItems()
        self.settings.pathImageSubsystem.predefinedRemove(pathsToRemove)
        self.settings.pathImageSubsystem.computeList(self.settings.minChatToBeLarge)
        self.formObj.updatePathImageListFromSubsystem()
    def setFormObject(self, formObj):
        self.formObj = formObj
    def setSettings(self, settingsObj):
        self.settings = settingsObj

class ChatGenerateReportCommand:
    def execute(self, sender, event):
        print("GenerateReportCommand: execute")
        self.settings.generateReport()
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
            self.settings.minFileDepth = int(self.formObj.minDirDepth.Text)
            self.settings.minDirSize = int(self.formObj.minDirSize.Text)
            self.settings.maxFileDepth = int(self.formObj.maxDirDepth.Text)
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

class ChatSelectAllCheckBoxesCommand:
    def execute(self, sender, event):
        if self.formObj is not None:
            self.formObj.selectAllChatsInGrid()
            self.formObj.chkBoxSelectAll.Checked = False
    def setFormObject(self, formObj):
        self.formObj = formObj
        print(formObj)
    def setSettings(self, settingsObj):
        self.settings = settingsObj

class ImagesSelectAllCheckBoxesCommand:
    def execute(self, sender, event):
        if self.formObj is not None:
            self.formObj.selectAllItemsInGrid()
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

class PathImagesRefreshCommand:
    def execute(self, sender, event):
        print("ImagesRefreshCommand: execute")
        self.settings.pathImageSubsystem.computeList(self.settings.minChatToBeLarge)
        self.formObj.updatePathImageListFromSubsystem()

    def setFormObject(self, formObj):
        self.formObj = formObj

    def setSettings(self, settingsObj):
        self.settings = settingsObj

#--------------------------- Video Commmands ----------------------

class PathVideosRefreshCommand:
    def execute(self, sender, event):
        print("VideosRefreshCommand: execute")
        self.settings.pathVideoSubsystem.computeList(self.settings.minChatToBeLarge)
        self.formObj.updatePathVideoListFromSubsystem()

    def setFormObject(self, formObj):
        self.formObj = formObj

    def setSettings(self, settingsObj):
        self.settings = settingsObj

class PathVideoAddAllCommand:
    def execute(self, sender, event):
        print("PathVideoAddAllCommand: execute")
        self.settings.pathVideoSubsystem.addAll()
        self.settings.pathVideoSubsystem.computeList(self.settings.minChatToBeLarge)
        self.formObj.updatePathVideoListFromSubsystem()
    def setFormObject(self, formObj):
        self.formObj = formObj
    def setSettings(self, settingsObj):
        self.settings = settingsObj

class PathVideoAddCommand:
    def execute(self, sender, event):
        print("PathVideoAddCommand: execute")
        pathsToRemove = self.formObj.getSelectedItems()
        self.settings.pathVideoSubsystem.addAllByPath(pathsToRemove)
        self.settings.pathVideoSubsystem.computeList(self.settings.minChatToBeLarge)
        self.formObj.updatePathVideoListFromSubsystem()
    def setFormObject(self, formObj):
        self.formObj = formObj
    def setSettings(self, settingsObj):
        self.settings = settingsObj

class PathVideoPredefinedRemoveCommand:
    def execute(self, sender, event):
        print("PathVideoPredefinedRemoveCommand: execute")
        pathsToRemove = self.formObj.getSelectedItems()
        self.settings.pathVideoSubsystem.predefinedRemove(pathsToRemove)
        self.settings.pathVideoSubsystem.computeList(self.settings.minChatToBeLarge)
        self.formObj.updatePathVideoListFromSubsystem()
    def setFormObject(self, formObj):
        self.formObj = formObj
    def setSettings(self, settingsObj):
        self.settings = settingsObj

class PathVideoRemoveCommand:
    def execute(self, sender, event):
        print("PathVideoRemoveCommand: execute")
        pathsToRemove = self.formObj.getSelectedItems()
        self.settings.pathVideoSubsystem.removeAllByPath(pathsToRemove)
        self.settings.pathVideoSubsystem.computeList(self.settings.minChatToBeLarge)
        self.formObj.updatePathVideoListFromSubsystem()
    def setFormObject(self, formObj):
        self.formObj = formObj
    def setSettings(self, settingsObj):
        self.settings = settingsObj

class VideosSelectAllCheckBoxesCommand:
    def execute(self, sender, event):
        print("VideosSelectAllCheckBoxesCommand: execute")
        if self.formObj is not None:
            self.formObj.selectAllItemsInGrid()
            self.formObj.chkBoxSelectAll.Checked = False
    def setFormObject(self, formObj):
        self.formObj = formObj
        print(formObj)
    def setSettings(self, settingsObj):
        self.settings = settingsObj

applySettingsCommand = ApplySettingsChangedCommand()
restoreSettingsCommand = RestoreSettingsCommand()
chatRefreshCommand = ChatRefreshCommand()
chatKeepOnlyTextMessagesCommand = ChatKeepOnlyTextMessagesCommand()
chatAddAllAttachmentsCommand = ChatAddAllAttachmentsCommand()
chatRemoveVideosCommand = ChatRemoveVideosCommand()
chatGenerateReportCommand = ChatGenerateReportCommand()
chatSelectAllCheckBoxesCommand = ChatSelectAllCheckBoxesCommand()

imagesSelectAllCheckBoxesCommand = ImagesSelectAllCheckBoxesCommand()
pathImageRemoveCommand = PathImageRemoveCommand()
pathImageAddCommand = PathImageAddCommand()
pathImagesRefreshCommand = PathImagesRefreshCommand()
pathImagePredefinedRemoveCommand = PathImagePredefinedRemoveCommand()
pathImageAddAllCommand = PathImageAddAllCommand()

pathVideoAddAllCommand = PathVideoAddAllCommand()
pathVideoAddCommand = PathVideoAddCommand()
pathVideoPredefinedRemoveCommand = PathVideoPredefinedRemoveCommand()
pathVideoRemoveCommand = PathVideoRemoveCommand()
videosSelectAllCheckBoxesCommand = VideosSelectAllCheckBoxesCommand()
pathVideosRefreshCommand = PathVideosRefreshCommand()
