from physical import *
import SQLiteParser
from System.Convert import IsDBNull
from struct import *
from array import array
import time, codecs, time, sys, re, os
import json
import sys
import os
import simplejson as json
from pprint import pprint
import string
from pickle import FALSE
import datetime
import traceback

from modules.Models import (ChatItem, ChatList)
from random import randrange


__author__ = "leosol@gmail.com"
__copyright__ = "Copyleft (C) 2021 leosol"
__license__ = "GNU AGPLv3"

def support_safe_str(obj):
    if obj is None:
        return ""
    if isinstance(obj, str):
        out = obj
    else:
        out = str(obj, encoding='utf-8', errors='replace')
    return out

class Subsystem:
    def computeChatList(self, minChatSize):
        chatList = ChatList()
        chat_list = ds.Models[Chat]
        for chat in chat_list:
            chatId = chat.Id.Value
            participantsCount = 0
            chatAttachmentsCount = 0
            chatAttachmentsSize = 0
            chatSelectedAttachmentsSize = 0
            chatRemovedAttachmentsCount = 0
            if chatId is None:
                continue
            for message in chat.Messages:
                for attachment in message.Attachments:
                    chatAttachmentsSize = chatAttachmentsSize + attachment.Size
                    if message.MarkForReport:
                        chatSelectedAttachmentsSize = chatSelectedAttachmentsSize + attachment.Size
                        chatAttachmentsCount = chatAttachmentsCount + 1
                    else:
                        chatRemovedAttachmentsCount = chatRemovedAttachmentsCount+1
            for participant in chat.Participants:
                participantsCount = participantsCount+1
            oneMegaByte = 1024*1024
            chatObj = ChatItem(chatId, participantsCount, chatAttachmentsCount, chatSelectedAttachmentsSize/oneMegaByte, (chatAttachmentsSize-chatSelectedAttachmentsSize)/oneMegaByte, chatAttachmentsSize/oneMegaByte)
            chatObj.chatRemovedAttachmentsCount = chatRemovedAttachmentsCount
            if chatObj.totalSize > (minChatSize-1):
                chatList.chatItems.append(chatObj)
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
        attachmentsRemoved = 0
        attachmentsNotRemovedForSize = 0
        for chatId in chatIds:
            chat_list = ds.Models[Chat]
            for chat in chat_list:
                if chatId == chat.Id.Value:
                    for message in chat.Messages:
                        for attachment in message.Attachments:
                            if attachment.Size > maxAttachmentsSize:
                                message.MarkForReport = False
                                attachmentsRemoved = attachmentsRemoved+1
                            else:
                                if message.MarkForReport:
                                    attachmentsNotRemovedForSize = attachmentsNotRemovedForSize+1
        print(str(attachmentsRemoved)+" were removed from the report")
        print(str(attachmentsNotRemovedForSize)+" were not touched - consider changing MaxAttachmentsSize (settings tab)")
    def addAllAttachments(self, chatIds):
        attachmentsAded = 0
        for chatId in chatIds:
            chat_list = ds.Models[Chat]
            for chat in chat_list:
                if chatId == chat.Id.Value:
                    for message in chat.Messages:
                        message.MarkForReport = True
                        for attachment in message.Attachments:
                                attachmentsAded = attachmentsAded+1
        print("Attachments marked for report: "+str(attachmentsAded))
    def removeVideos(self, chatIds, mimeTypes, maxAttachmentsSize):
        attachmentsRemoved = 0
        chatsNotTouchedNotMime = 0
        for chatId in chatIds:
            chat_list = ds.Models[Chat]
            for chat in chat_list:
                if chatId == chat.Id.Value:
                    for message in chat.Messages:
                        for attachment in message.Attachments:
                            if attachment.Size > maxAttachmentsSize:
                                for mimeT in mimeTypes:
                                    if attachment.ContentType is not None and support_safe_str(attachment.ContentType.Value).find(mimeT) > -1:
                                        message.MarkForReport = False
                                        attachmentsRemoved = attachmentsRemoved+1
                                    else:
                                        if message.MarkForReport:
                                            chatsNotTouchedNotMime = chatsNotTouchedNotMime+1
        print(str(attachmentsRemoved) + " were removed from the report")
        print(str(chatsNotTouchedNotMime) + " were not touched - different mime type")
    def generateSinteticReport(self, file):
        temp = self.chatList.chatItems
        self.computeChatList(0)
        reportChatList = self.chatList.chatItems
        self.chatList.chatItems = temp
        with open(file, 'wb') as myfile:
            myfile.write("chatId, participantsCount, attachmentsCount, chatRemovedAttachmentsCount, selectedSize, unselectedSize, totalSize\n")
            for chatItem in reportChatList:
                if chatItem.chatRemovedAttachmentsCount>0:
                    myfile.write(chatItem.chatId+", "+str(chatItem.participantsCount)+", "+str(chatItem.attachmentsCount)+", "+str(chatItem.chatRemovedAttachmentsCount)+", "+str(chatItem.selectedSize)+", "+str(chatItem.unselectedSize)+", "+str(chatItem.totalSize)+"\n")
    def generateAnaliticReport(self, file):
        with open(file, 'wb') as myfile:
            chat_list = ds.Models[Chat]
            attachmentIndex = 0
            for chat in chat_list:
                chatId = chat.Id.Value
                for message in chat.Messages:
                    if not message.MarkForReport:
                        for attachment in message.Attachments:
                            myfile.flush()
                            myfile.write("Attachment "+str(attachmentIndex)+"---------------------------------------------\n")
                            myfile.write("ChatId: " + chatId+"\n")
                            try:
                                if message.From is not None:
                                    if message.From.Value.Name is not None:
                                        myfile.write("From: " + str(message.From.Value.Name.Value)+"\n")
                                if message.Source is not None:
                                    myfile.write("Source: "+str(message.Source.Value)+"\n")
                                if message.Body is not None:
                                    myfile.write("Body: " + support_safe_str(message.Body.Value)+"\n")
                                if message.TimeStamp is not None:
                                    formated = str(message.TimeStamp.Value)
                                    myfile.write("TimeStamp: " + formated+"\n")
                                myfile.write("File name: "+attachment.Filename.Value+"\n")
                                myfile.write("File size: "+str(attachment.Size)+"\n")
                                #myfile.write("UUID: "+str(attachment.Id))
                            except Exception:
                                print traceback.format_exc()
                            myfile.write("\n")
                            attachmentIndex = attachmentIndex + 1