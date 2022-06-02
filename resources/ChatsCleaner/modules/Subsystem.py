from modules.Models import (ChatItem, ChatList, PathImageList, PathImageItem, PathVideoList, PathVideoItem)
from random import randrange

__author__ = "leosol@gmail.com"
__copyright__ = "Copyleft (C) 2021 leosol"
__license__ = "GNU AGPLv3"

class Subsystem:
    def computeChatList(self, minChatSize):
        chatList = ChatList()
        ch1 = ChatItem('chatId1', 2, 10, 1024*randrange(10), 1024, 1024*2)
        ch2 = ChatItem('chatId2', 22, 11, 1023*randrange(10), 1023, 1023 * 2)
        ch3 = ChatItem('chatId3', 2002, 13, 1023*randrange(10), 1023, 1023 * 2)
        chatList.chatItems.append(ch1)
        chatList.chatItems.append(ch2)
        chatList.chatItems.append(ch3)
        self.chatList = chatList
    def computeSelectedSize(self):
        selectedSize = 0
        for chatItem in self.chatList.chatItems:
            selectedSize += chatItem.selectedSize
        return selectedSize
    def computeTotalSize(self):
        totalSize = 0
        for chatItem in self.chatList.chatItems:
            totalSize += chatItem.totalSize
        return totalSize
    def removeAllAttachments(self, chatIds, maxAttachmentsSize):
        for chatId in chatIds:
            for chatItem in self.chatList.chatItems:
                if chatId == chatItem.chatId:
                    if chatItem.attachmentsCount>0:
                        chatItem.initialAttachmentsCount = chatItem.attachmentsCount
                    chatItem.attachmentsCount = 0
    def addAllAttachments(self, chatIds):
        for chatId in chatIds:
            for chatItem in self.chatList.chatItems:
                if chatId == chatItem.chatId:
                    if chatItem.attachmentsCount == 0:
                        chatItem.attachmentsCount = chatItem.initialAttachmentsCount
    def removeVideos(self, chatIds, mimeTypes, maxAttachmentsSize):
        for chatId in chatIds:
            for chatItem in self.chatList.chatItems:
                if chatId == chatItem.chatId:
                    chatItem.selectedSize = 0
    def generateSinteticReport(self, file):
        mylist = ['value 1', 'value 2', 'value 3']
        with open(file , 'wb') as myfile:
            myfile.write(str(mylist))
    def generateAnaliticReport(self, file):
        mylist = ['value 1', 'value 2', 'value 3']
        with open(file, 'wb') as myfile:
            myfile.write(str(mylist))


class PathImageSubsystem:
    def computeList(self, minImageSize):
        listObj = PathImageList()
        item1 = PathImageItem('c:/path1', 2, 1024, 1024*2)
        item2 = PathImageItem('c:/path2', 22, 1023, 1023 * 2)
        item3 = PathImageItem('c:/path3', 2002, 1023, 1023 * 2)
        listObj.pathImageItems.append(item1)
        listObj.pathImageItems.append(item2)
        listObj.pathImageItems.append(item3)
        self.pathImageList = listObj
    def computeSelectedSize(self):
        selectedSize = 0
        for item in self.pathImageList.pathImageItems:
            selectedSize += item.actualSize
        return selectedSize
    def computeTotalSize(self):
        totalSize = 0
        for item in self.pathImageList.pathImageItems:
            totalSize += item.originalSize
        return totalSize
    def removeAllByPath(self, imageBasePath):
        print imageBasePath
    def predefinedRemove(self, imageBasePath):
        print imageBasePath
    def addAllByPath(self, imageBasePath):
        print imageBasePath
    def addAll(self):
        print 'minFileDepth: '+str(self.settings.minFileDepth)
        print 'maxFileDepth: ' + str(self.settings.maxFileDepth)
        print 'minFileSize: ' + str(self.settings.minDirSize)
        print 'AddAll'

class PathVideoSubsystem:
    def computeList(self, minImageSize):
        listObj = PathVideoList()
        item1 = PathVideoItem('c:/path1', 2, 1024, 1024*2)
        item2 = PathVideoItem('c:/path2', 22, 1023, 1023 * 2)
        item3 = PathVideoItem('c:/path3', 2002, 1023, 1023 * 2)
        listObj.pathVideoItems.append(item1)
        listObj.pathVideoItems.append(item2)
        listObj.pathVideoItems.append(item3)
        self.pathVideoList = listObj
    def computeSelectedSize(self):
        selectedSize = 0
        for item in self.pathVideoList.pathVideoItems:
            selectedSize += item.actualSize
        return selectedSize
    def computeTotalSize(self):
        totalSize = 0
        for item in self.pathVideoList.pathVideoItems:
            totalSize += item.originalSize
        return totalSize
    def removeAllByPath(self, videoBasePath):
        print videoBasePath
    def predefinedRemove(self, videoBasePath):
        print videoBasePath
    def addAllByPath(self, videoBasePath):
        print videoBasePath
    def addAll(self):
        print 'AddAll'