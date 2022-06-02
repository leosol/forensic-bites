from datetime import date

__author__ = "leosol@gmail.com"
__copyright__ = "Copyleft (C) 2021 leosol"
__license__ = "GNU AGPLv3"

class Settings:
    def __init__(self, workDir = None, subSystem = None, pathImageSubsystem = None, pathVideoSubsystem = None):
        print('Settings creator')
        print(workDir)
        self.workDir = workDir
        self.defaultWorkDir = workDir
        self.maxAttachmentsSize = 1024*1024*5*0
        self.minChatToBeLarge = 10
        self.videosTypes = ["video/mp4", "video/mpeg", "video/quicktime", "video/x-m4v"]
        self.subSystem = subSystem
        self.subSystem.settings = self
        self.minFileDepth = 3
        self.maxFileDepth = 4
        self.minDirSize = 10
        self.pathImageSubsystem = pathImageSubsystem
        self.pathVideoSubsystem = pathVideoSubsystem
        self.pathImageSubsystem.settings = self
        self.pathVideoSubsystem.settings = self
    def printSettings(self):
        print(self.workDir)
        print(str(self.maxAttachmentsSize))
        print(str(self.minChatToBeLarge))
        print(str(self.videosTypes))
        print(str(self.minFileDepth))
        print(str(self.maxFileDepth))
        print(str(self.minDirSize))
    def restoreDefaults(self):
        self.workDir = self.defaultWorkDir
        self.maxAttachmentsSize = 1024*1024*5*0
        self.minChatToBeLarge = 10
        self.minFileDepth = 3
        self.maxFileDepth = 4
        self.minDirSize = 10
        self.videosTypes = ["video/mp4", "video/mpeg", "video/quicktime", "video/x-m4v"]
    def generateReport(self):
        file1 = self.workDir+"\Report-SUMMARY.csv";
        file2 = self.workDir+"\Report-REMOVED-attachments.csv"
        self.subSystem.generateSinteticReport(file1)
        self.subSystem.generateAnaliticReport(file2)


class ChatList:
    def __init__(self):
        self.chatItems = []

class ChatItem:
    def __init__(self, chatId, participantsCount, attachmentsCount, selectedSize, unselectedSize, totalSize):
        self.chatId = chatId
        self.participantsCount = participantsCount
        self.attachmentsCount = attachmentsCount
        self.selectedSize = selectedSize
        self.unselectedSize = unselectedSize
        self.totalSize = totalSize


class PathImageList:
    def __init__(self):
        self.pathImageItems = []

class PathImageItem:
    def __init__(self, ipath, refCount, actualSize, originalSize):
        self.ipath = ipath
        self.refCount = refCount
        self.actualSize = actualSize
        self.originalSize = originalSize

class PathVideoList:
    def __init__(self):
        self.pathVideoItems = []

class PathVideoItem:
    def __init__(self, ipath, refCount, actualSize, originalSize):
        self.ipath = ipath
        self.refCount = refCount
        self.actualSize = actualSize
        self.originalSize = originalSize