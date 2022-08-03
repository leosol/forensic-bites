__author__ = "leosol@gmail.com"
__copyright__ = "Copyleft (C) 2021 leosol"
__license__ = "GNU AGPLv3"

KNOWN_TRASH_PATHS = ["/data/com.shazam.android/",
     "/data/com.zhiliaoapp.musically/",
     "/data/com.tencent.mm/",
     "/data/com.facebook.katana/app_ras_blobs/FacebookEmoji.ttf/",
     "/data/com.google.android.gms/files/fonts/opentype/",
     "/data/com.android.chrome/",
     "/data/com.mi.globalbrowser/",
     "/data/com.miui.gallery/files/photo_editor/stickers/",
     "/data/data/com.google.android.youtube/",
     "/data/com.magicv.airbrush/",
     "/data/com.whatsapp.w4b/files/Stickers/",
     "/data/com.google.android.gms/files/nearby-fast-pair/",
     "/data/com.whatsapp.w4b/files/downloadable/wallpaper/",
     "/data/com.google.android.inputmethod.latin/",
     "/data/com.miui.weather2/",
     "/data/com.miui.msa.global/files/shared/preinstall_ad_info/",
     "/data/com.facebook.katana/app_feedback_reactions/",
     "/data/user_de/0/com.android.deskclock/files/com.android.deskclocklib.res20190812/assets/",
     "/data/com.miui.gallery/app_libs/",
     "/data/media/0/Android/data/com.mi.android.globalminusscreen/",
     "/data/user_de/0/com.miui.home/databases/launcher4x6.db/",
     "/data/data/com.mi.android.globalminusscreen/",
     "/data/media/0/Android/data/com.miui.cleanmaster/",
     "/data/com.sec.android.app.launcher/databases/launcher.db/",
     "/Root/media/0/c/a/t/v1leveling/",
     "/data/com.google.android.googlequicksearchbox/",
     "/data/com.google.android.gms/files/fonts/opentype/",
     "/fonts/NotoColorEmoji.ttf/",
     "/data/com.whatsapp/files/downloadable/wallpaper/",
     "/priv-app/WallpaperPicker_Zero2/",
     "/data/com.facebook.katana/app_msqrd_effect_asset_disk_cache_fixed_sessionless/",
     "/data/com.google.android.youtube/",
     "/data/com.tranzmate/",
     "/data/br.com.mobicare.minhaoi/",
     "/media/0/c/a/t/v1leveling/",
     "/media/0/Android/data/com.netflix.mediaclient/",
     "/data/br.com.clubeextra/",
     "data/com.google.android.feedback/shared_prefs/",
     "/fonts/SamsungColorEmoji.ttf/",
     "/data/com.whatsapp/files/Stickers/",
     "/media/0/WhatsApp/Media/WhatsApp Stickers/",
     "/media/0/WhatsApp/.StickerThumbs/",
     "/data/com.sec.android.app.samsungapps/files/",
     "/data/com.google.android.apps.magazines/",
     "/data/com.google.android.feedback/",
     "/data/com.instagram.android/cache/ig_mq_assets_dir/",
     "/app/Flipboard/",
     "/media/0/Android/data/flipboard.boxer.app/",
     "/data/com.google.android.gms/cache/ads_cache/",
     "/data/com.whatsapp/files/Stickers/",
     "/data/br.com.bemobi.appsclub.tim/files/",
     "/data/com.whatsapp/files/Avatars/",
     "/data/com.google.android.gms/files/",
     "/data/com.android.browser/",
     "/data/com.sec.android.app.samsungapps/files/",
     "/data/com.sec.android.daemonapp/cache/image_manager_disk_cache/",
     "/media/0/c/a/t/v1leveling/",
     "/data/com.alightcreative.motion/",
     "/data/com.kwai.video/",
     "/system/recent_images/",
     "/data/com.whatsapp/files/Avatars/",
     "/media/0/Android/data/com.fotos.makeover.makeup/",
     "/Root/app/CalendarGoogle/",
     "/Root/app/com.google.android.youtube-1/",
     "/Root/app/com.google.android.gms-1/",
     "/Root/data/com.snaptube.premium/",
     "/Root/framework/",
     "/Root/app/GoogleHome/",
     "/Root/app/LauncherConfig/",
     "/Root/app/LiveWallpapers/",
     "/Root/priv-app/Settings/",
     "/Root/priv-app/SetupWizard/",
     "/Root/etc/recovery-resource.dat/",
     "/Root/app/Translate/",
     "/Root/priv-app/Velvet/",
     "/Root/app/YouTube/",
     "/data/user/10/com.zhiliaoapp.musically/",
     "/data/data/com.rahul.videoderbeta/",
     "/data/data/com.badoo.mobile/",
     "/data/data/com.miui.player/",
     "/data/data/net.zedge.android/",
     "/data/data/com.google.android.apps.maps/",
     "/data/user/10/com.recarga.recarga/",
     "/data/data/com.taxis99/",
     "/system/etc/precust_theme/theme/",
     "/data/media/0/Android/data/net.zedge.android/",
     "/data/data/cn.wps.moffice_eng/",
     "/system/etc/recovery-resource.dat/",
     "/data/media/0/MIUI/theme/",
     "/system/media/theme/",
     "/data/user_de/10/com.mi.android.globallauncher/",
     "/data/data/com.adobe.photoshopmix/",
     "/data/data/com.android.wallpaperbackup/",
     "/data/data/com.whatsapp/cache/webp_static_cache/",
     "/data/data/com.credicard.app/",
     "/data/data/com.miui.cleanmaster/",
     "/data/data/com.miui.global.packageinstaller/",
     "/data/data/com.android.thememanager/",
     "/data/media/0/Android/data/com.pixel.art.coloring.color.number/",
     "/data/media/0/Android/data/com.miui.securitycenter/",
     "/data/miui/app/recommended/3rd-com.jewelsblast.ivygames.Adventure.free_143/",
     "/data/data/com.globo.ge.app/",
     "/data/data/br.com.bb.android/files/bundles/",
     "/data/data/br.gov.caixa.tem/cache/",
     "/data/system/theme_magic/customized_icons/",
     "/data/media/0/Android/data/com.dts.freefiremax/",
     "/data/media/0/Download/.com.google.Chrome.6ttPnY/",
     "/data/data/com.snaptube.premium/",
     "/data/media/0/GBWhatsApp/ModsBackup/com.gbwhatsapp/files/Avatars/",
     "/data/data/com.whatsapp/cache/Profile Pictures/",
     "/data/media/0/GBWhatsApp/ModsBackup/com.gbwhatsapp/cache/Profile Pictures/",
     "/data/data/com.whatsapp/cache/webp_static_cache/",
     "/data/media/0/gridplusapp/.Template/",
     "/data/media/0/.JlstickerPacks/",
     "/data/media/0/GBWhatsApp/Media/GBWhatsApp Stickers/",
     "/data/media/0/.binstickerPacks/",
     "/data/media/0/inshot/.sticker/",
     "/data/data/com.google.android.apps.wallpaper/",
     "/data/data/com.android.captiveportallogin/",
     "/data/media/0/Android/data/com.merge.cat.paradise/",
     "/data/data/com.google.android.gm/cache/WebView/",
     "/system/product/app/CalendarGoogle/",
     "/data/data/me.filmeshd.mega/",
     "/data/data/com.gbwhatsapp/files/downloadable/wallpaper/",
     "/data/data/com.gbwhatsapp/cache/webp_static_cache/",
     "/data/media/0/GBWhatsApp/.StickerThumbs/",
     "/data/data/com.facebook.katana/cache/WebView/",
     "/data/data/com.dts.freefireth/",
     "/data/data/com.google.android.apps.tachyon/cache/",
     "/data/data/com.motorola.launcher3/",
     "/data/data/com.google.android.apps.chromecast.app/",
     "/data/system_ce/0/shortcut_service/bitmaps/",
     "/product/priv-app/AMXGlobalContainer/AMXGlobalContainer.apk/",
     "/product/priv-app/GmsCore/m/independent/AndroidPlatformServices.apk/",
     "/product/app/CalendarGoogle/",
     "/Root/data/com.gbwhatsapp/files/downloadable/wallpaper/",
     "/Root/media/0/Kwai-video/.kwai_emoji_resource_addition/",
     "/Root/data/com.gbwhatsapp/files/Stickers/",
      "/Data/media/0/c/a/t/v1leveling/",
     "/Data/app/CalendarGoogle/",
     "/Data/app/com.google.android.youtube-1/",
     "/Data/app/com.google.android.gms-1/",
     "/Data/data/com.snaptube.premium/",
     "/Data/framework/",
     "/Data/app/GoogleHome/",
     "/Data/app/LauncherConfig/",
     "/Data/app/LiveWallpapers/",
     "/Data/priv-app/Settings/",
     "/Data/priv-app/SetupWizard/",
     "/Data/etc/recovery-resource.dat/",
     "/Data/app/Translate/",
     "/Data/priv-app/Velvet/",
     "/Data/app/YouTube/",
     "/Data/data/com.gbwhatsapp/files/downloadable/wallpaper/",
     "/Data/media/0/Kwai-video/.kwai_emoji_resource_addition/",
     "/Data/data/com.gbwhatsapp/files/Stickers/",
     "/root/data/com.google.android.youtube/",
     "/root/data/com.mi.android.globalminusscreen/",
     "/root/data/com.rahul.videoderbeta/",
     "/root/data/com.badoo.mobile/",
     "/root/data/com.miui.player/",
     "/root/data/net.zedge.android/",
     "/root/data/com.google.android.apps.maps/",
     "/root/data/com.taxis99/",
     "/root/data/cn.wps.moffice_eng/",
     "/root/data/com.adobe.photoshopmix/",
     "/root/data/com.android.wallpaperbackup/",
     "/root/data/com.whatsapp/cache/webp_static_cache/",
     "/root/data/com.credicard.app/",
     "/root/data/com.miui.cleanmaster/",
     "/root/data/com.miui.global.packageinstaller/",
     "/root/data/com.android.thememanager/",
     "/root/data/com.globo.ge.app/",
     "/root/data/br.com.bb.android/files/bundles/",
     "/root/data/br.gov.caixa.tem/cache/",
     "/root/data/com.snaptube.premium/",
     "/root/data/com.whatsapp/cache/Profile Pictures/",
     "/root/data/com.whatsapp/cache/webp_static_cache/",
     "/root/data/com.google.android.apps.wallpaper/",
     "/root/data/com.android.captiveportallogin/",
     "/root/data/com.google.android.gm/cache/WebView/",
     "/root/data/me.filmeshd.mega/",
     "/root/data/com.gbwhatsapp/files/downloadable/wallpaper/",
     "/root/data/com.gbwhatsapp/cache/webp_static_cache/",
     "/root/data/com.facebook.katana/cache/WebView/",
     "/root/data/com.dts.freefireth/",
     "/root/data/com.google.android.apps.tachyon/cache/",
     "/root/data/com.motorola.launcher3/",
     "/root/data/com.google.android.apps.chromecast.app/"]

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
        self.settings.pathImageSubsystem.predefinedRemove(KNOWN_TRASH_PATHS)
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
        self.settings.pathVideoSubsystem.predefinedRemove(KNOWN_TRASH_PATHS)
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
