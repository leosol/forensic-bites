from datetime import date

__author__ = "leosol@gmail.com"
__copyright__ = "Copyleft (C) 2021 leosol"
__license__ = "GNU AGPLv3"

class Settings:
    def __init__(self, workDir = None, subSystem = None):
        print('Settings creator')
        print(workDir)
        self.workDir = workDir
        self.defaultWorkDir = workDir
        self.maxAttachmentsSize = 1024*1024*5*0
        self.minChatToBeLarge = 10
        self.videosTypes = ["video/mp4", "video/mpeg", "video/quicktime", "video/x-m4v"]
        self.subSystem = subSystem
    def printSettings(self):
        print(self.workDir)
        print(str(self.maxAttachmentsSize))
        print(str(self.minChatToBeLarge))
        print(str(self.videosTypes))
    def restoreDefaults(self):
        self.workDir = self.defaultWorkDir
        self.maxAttachmentsSize = 1024*1024*5
        self.minChatToBeLarge = 1024*1024*5*2
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