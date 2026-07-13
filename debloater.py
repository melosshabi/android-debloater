import subprocess

# ===== STANDARD DEBLOAT =====
standard_packages = [
    # Google
    "com.google.android.tts",  # TTS From Google
    "com.google.android.voicesearch",  # Voice Search From Google
    "com.google.android.speechservices",  # TTS From Google
    "com.google.android.googlequicksearchbox",  # The Google App
    "com.google.android.apps.bard",  # Gemini
    "com.google.android.feedback",  # Google's Feedback Service
    "com.google.android.adservices.api",  # Google's Ad Services
    "com.google.mainline.telemetry",  # Data Collector
    "com.google.mainline.adservices",  # Google's Ad Services
    "com.android.chrome",  # Chrome
    "com.google.android.youtube",  # YouTube
    "com.google.android.projection.gearhead",  # Android Auto
    "com.google.android.gm",  # Gmail
    "com.google.android.apps.maps",  # Google Maps
    "com.google.android.apps.credentialmanager",  # Google Password Manager
    "com.google.android.printservice.recommendation",  # Print Suggestions
    "com.google.android.apps.accessibility.voiceaccess",  # Voice Access
    "com.google.android.apps.carrier.carrierwifi",  # Carrier Wi-Fi Helper
    "com.google.android.apps.turbo",  # Google Go / Turbo
    "com.google.android.gms.supervision",  # Parental Controls
    "com.google.android.partnersetup",  # OEM Partner Setup
    "com.google.android.ar.core",  # AR Services
    "com.google.android.apps.photos",  # Google Photos
    "com.google.android.ondevicepersonalization.services",  # Google Tracking
    "com.google.android.apps.tachyon",  # Google Meet
    "com.google.android.apps.youtube.music",  # YouTube Music
    "com.google.android.youtube.tvunplugged",  # YouTube TV
    "com.google.android.apps.youtube.kids",  # YouTube Kids
    "com.google.android.videos",  # Google TV / Play Movies
    "com.google.android.music",  # Google Play Music
    "com.google.android.apps.podcasts",  # Google Podcasts
    "com.google.android.apps.googleassistant",  # Google Assistant
    "com.google.android.apps.subscriptions.red",  # YouTube Premium
    "com.google.android.keep",  # Google Keep
    "com.google.android.apps.docs",  # Google Docs
    "com.google.android.apps.sheets",  # Google Sheets
    "com.google.android.apps.slides",  # Google Slides
    "com.google.android.apps.drive",  # Google Drive
    "com.google.android.talk",  # Google Chat
    "com.google.android.apps.meetings",  # Google Meet
    "com.google.android.dialer",  # Google Phone
    "com.google.android.contacts",  # Google Contacts
    "com.google.android.apps.nbu.files",  # Google Files
    "com.google.android.apps.wallpaper",  # Wallpapers by Google
    "com.google.android.storagemanager",  # Storage Manager
    "com.google.android.play.games",  # Google Play Games
    "com.google.android.apps.enterprise.surveyor",  # Google Surveyor
    "com.google.android.gms.location.history",  # Location History
    "com.google.android.apps.fitness",  # Google Fit
    "com.google.android.apps.wellbeing",  # Digital Wellbeing
    # Samsung
    "com.samsung.android.inputshare",  # Multi Control App
    "com.samsung.android.bixbyvision.framework",  # Bixby Vision
    "com.samsung.android.ipsgeofence",  # Samsung Visit In
    "com.samsung.android.mdx",  # Link To Windows Service
    "com.samsung.android.messaging",  # Samsung Messaging
    "com.samsung.android.spayfw",  # Samsung Pay Framework
    "com.samsung.android.samsungpass",  # Samsung Pass
    "com.samsung.android.game.gamehome",  # Gaming Hub
    "com.samsung.android.calendar",  # Samsung Calendar
    "com.samsung.android.bixby.agent",  # Bixby Agent
    "com.samsung.android.bixby.wakeup",  # Bixby Wakeup
    "com.samsung.android.visionintelligence",  # Vision Intelligence
    "com.samsung.android.scloud",  # Samsung Cloud
    "com.samsung.android.kidsinstaller",  # Kids Installer
    "com.sec.android.app.kidshome",  # Kids Home
    "com.sec.android.app.billing",  # Samsung Billing
    "com.sec.android.easyMover",  # Smart Switch
    "com.sec.android.app.fm",  # Samsung Radio
    "com.samsung.android.app.tips",  # Samsung Tips
    "com.samsung.android.game.gametools",  # Game Booster
    "com.samsung.android.game.gos",  # Game Optimizing Service
    "com.samsung.android.rubin.app",  # Samsung Rubin AI
    "com.samsung.android.app.watchmanager",  # Galaxy Watch Manager
    "com.samsung.android.buds",  # Galaxy Buds App
    "com.samsung.android.ardrawing",  # AR Drawing
    "com.samsung.android.ardoodle",  # AR Doodle
    "com.samsung.android.arzone",  # AR Zone
    "com.samsung.android.app.dressroom",  # AR Emoji Studio
    "com.samsung.android.aremoji",  # AR Emoji
    "com.samsung.android.aremojieditor",  # AR Emoji Editor
    "com.samsung.android.stickercenter",  # Sticker Center
    "com.samsung.android.app.routines",  # Bixby Routines
    "com.samsung.android.app.sharelive",  # Share Live
    "com.samsung.android.shortcutbackupservice",  # Shortcut Backup
    "com.samsung.android.allshare.service.fileshare",  # AllShare File
    "com.samsung.android.allshare.service.mediashare",  # AllShare Media
    "com.samsung.android.app.personalnfc",  # Personal NFC
    "com.samsung.android.privateshare",  # Private Share
    "com.samsung.android.knox.attestation",  # Knox Attestation
    "com.samsung.android.knox.analytics.uploader",  # Knox Analytics
    "com.samsung.android.smartswitchassistant",  # Smart Switch Assistant
    "com.samsung.android.beaconmanager",  # Beacon Manager
    "com.samsung.android.samsungpay.gear",  # Samsung Pay Gear
    "com.samsung.android.health",  # Samsung Health
    "com.samsung.android.app.health",  # Samsung Health Platform
    "com.samsung.android.wellbeing",  # Digital Wellbeing Samsung
    "com.samsung.android.forest",  # Focus Mode
    "com.samsung.android.app.spage",  # Samsung Free
    "com.samsung.android.app.sbrowser",  # Samsung Internet
    "com.samsung.android.app.music",  # Samsung Music
    # "com.samsung.android.video",  # Samsung Video Player
    "com.samsung.android.smartmirroring",  # Smart View
    "com.samsung.android.app.smartswitch",  # Smart Switch
    "com.samsung.android.app.galaxystore",  # Galaxy Store
    "com.samsung.android.mobileservice",  # Samsung Mobile Services
    "com.samsung.android.app.omcagent",  # OMC Agent
    "com.samsung.android.app.flipboardbriefing",  # Flipboard Briefing
    "com.samsung.android.smartsuggestionsservice",  # Smart Suggestions
    # Samsung TTS / Language Packs
    "com.samsung.SMT",
    "com.samsung.SMT.lang_pt_br_f00",
    "com.samsung.SMT.lang_en_us_f00",
    "com.samsung.SMT.lang_es_mx_f00",
    "com.samsung.SMT.lang_hi_in_f00",
    "com.samsung.SMT.lang_en_in_f00",
    "com.samsung.android.tts.lang.pl",
    "com.samsung.SMT.lang_ar_ae_m00",
    "com.samsung.SMT.lang_es_us_f00",
    "com.samsung.SMT.lang_en_gb_f00",
    "com.samsung.SMT.lang_ru_ru_f00",
    "com.samsung.SMT.lang_fr_fr_f00",
    "com.samsung.SMT.lang_th_th_f00",
    "com.samsung.SMT.lang_id_id_f00",
    "com.samsung.SMT.lang_es_es_f00",
    "com.samsung.SMT.lang_de_de_f00",
    "com.samsung.SMT.lang_en_us_l03",
    "com.samsung.SMT.lang_vi_vn_f00",
    "com.samsung.SMT.lang_pl_pl_f00",
    "com.samsung.SMT.lang_it_it_f00",
    # Microslop
    "com.microsoft.appmanager",  # Link to Windows
    "com.microsoft.skydrive",  # OneDrive
    "com.microsoft.teams",  # Microslop Teams
    "com.microsoft.office.word",  # Word
    "com.microsoft.office.excel",  # Excel
    "com.microsoft.office.powerpoint",  # PowerPoint
    "com.microsoft.office.outlook",  # Outlook
    "com.microsoft.launcher.enterprise",  # Microslop Launcher
    # Facebook / Meta
    "com.facebook.appmanager",  # Facebook Tracking
    "com.facebook.katana",  # Facebook
    "com.facebook.orca",  # Messenger
    "com.facebook.system",  # Facebook System Service
    "com.instagram.android",  # Instagram
    # Spyware
    "com.aura.oobe.samsung",  # Israeli Spyware
    "com.android.credentialmanager",  # Credential Manager
    "com.facebook.appmanager",  # Facebook Tracking
    "com.facebook.katana",      # Facebook
    "com.facebook.orca",        # Messenger
    "com.facebook.system",      # Facebook System Service
    "com.facebook.services",    # Meta Services
    "com.instagram.android",    # Instagram
    # Bulk addition
    "com.amazon.fv",
    "com.amazon.kindle",
    "com.amazon.mp3",
    "com.amazon.mShop.android",
    "com.amazon.venezia",
    "com.android.apps.tag",
    "com.android.backupconfirm",
    "com.android.bips",
    "com.android.bookmarkprovider",
    "com.android.dreams.basic",
    "com.android.dreams.phototable",
    "com.android.email",
    "com.android.exchange",
    "com.android.hotwordenrollment.okgoogle",
    "com.android.hotwordenrollment.xgoogle",
    "com.android.internal.display.cutout.emulation.waterfall",
    "com.android.printspooler",
    "com.android.providers.calendar",
    "com.android.providers.partnerbookmarks",
    "com.android.providers.userdictionary",
    "com.android.role.notes.enabled",
    "com.android.settings.intelligence",
    "com.android.sharedstoragebackup",
    "com.android.stk",
    "com.android.wallpapercropper",
    "com.android.wallpaper.livepicker",
    "com.audible.application",
    "com.blurb.checkout",
    "com.cequint.ecid",
    "com.cnn.mobile.android.phone.edgepanel",
    "com.diotek.sec.lookup.dictionary",
    "com.dsi.ant.plugins.antplus",
    "com.dsi.ant.sample.acquirechannels",
    "com.dsi.ant.server",
    "com.dsi.ant.service.socket",
    "com.enhance.gameservice",
    "com.flipboard.app",
    "com.flipboard.boxer.app",
    "com.google.android.aicore",
    "com.google.android.apps.aiwallpapers",
    "com.google.android.apps.books",
    "com.google.android.apps.magazines",
    "com.google.android.apps.plus",
    "com.google.android.apps.restore",
    "com.google.android.healthconnect.controller",
    "com.google.android.onetimeinitializer",
    "com.google.android.safetycenter.resources",
    "com.google.android.syncadapters.calendar",
    "com.google.ar.core",
    "com.google.audio.hearing.visualization.accessibility.scribe",
    "com.google.vr.vrcore",
    "com.gotv.nflgamecenter.us.lite",
    "com.hancom.office.editor.hidden",
    "com.imdb.mobile",
    "com.infraware.polarisoffice5",
    "com.linkedin.android",
    "com.microsoft.office.officehubrow",
    "com.mobeam.barcodeService",
    "com.monotype.android.font.chococooky",
    "com.monotype.android.font.cooljazz",
    "com.monotype.android.font.foundation",
    "com.monotype.android.font.rosemary",
    "com.monotype.android.font.samsungone",
    "com.netflix.mediaclient",
    "com.nuance.swype.input",
    "com.osp.app.signin",
    "com.policydm",
    "com.samsung.aasaservice",
    "com.samsung.android.aicore",
    "com.samsung.android.aircommandmanager",
    "com.samsung.android.app.advsounddetector",
    "com.samsung.android.app.appsedge",
    "com.samsung.android.app.assistantmenu",
    "com.samsung.android.app.camera.sticker.facear3d.preload",
    "com.samsung.android.app.camera.sticker.facearavatar.preload",
    "com.samsung.android.app.camera.sticker.facearframe.preload",
    "com.samsung.android.app.camera.sticker.facear.preload",
    "com.samsung.android.app.camera.sticker.stamp.preload",
    "com.samsung.android.app.clipboardedge",
    "com.samsung.android.app.cocktailbarservice",
    "com.samsung.android.app.episodes",
    "com.samsung.android.app.filterinstaller",
    "com.samsung.android.app.find",
    "com.samsung.android.app.galaxyfinder",
    "com.samsung.android.app.interpreter",
    "com.samsung.android.app.ledbackcover",
    "com.samsung.android.app.ledcoverdream",
    "com.samsung.android.app.memo",
    "com.samsung.android.app.mirrorlink",
    "com.samsung.android.app.notes",
    "com.samsung.android.app.parentalcare",
    "com.samsung.android.app.readingglass",
    "com.samsung.android.app.reminder",
    "com.samsung.android.app.sbrowseredge",
    "com.samsung.android.app.settings.bixby",
    "com.samsung.android.app.simplesharing",
    "com.samsung.android.app.sketchbook",
    "com.samsung.android.app.soundpicker",
    "com.samsung.android.app.storyalbumwidget",
    "com.samsung.android.app.talkback",
    "com.samsung.android.app.taskedge",
    "com.samsung.android.app.updatecenter",
    "com.samsung.android.app.vrsetupwizardstub",
    "com.samsung.android.app.watchmanagerstub",
    "com.samsung.android.app.withtv",
    "com.samsung.android.authfw",
    "com.samsung.android.aware.service",
    "com.samsung.android.bbc.bbcagent",
    "com.samsung.android.bixby.agent.dummy",
    "com.samsung.android.bixby.es.globalaction",
    "com.samsung.android.bixby.ondevice.enus",
    "com.samsung.android.bixby.ondevice.esus",
    "com.samsung.android.bixby.plmsync",
    "com.samsung.android.bixby.service",
    "com.samsung.android.bixby.voiceinput",
    "com.samsung.android.carkey",
    "com.samsung.android.coldwalletservice",
    "com.samsung.android.da.daagent",
    "com.samsung.android.dbsc",
    "com.samsung.android.dkey",
    "com.samsung.android.dlp.service",
    "com.samsung.android.drivelink.stub",
    "com.samsung.android.easysetup",
    "com.samsung.android.email.provider",
    "com.samsung.android.ese",
    "com.samsung.android.fmm",
    "com.samsung.android.gametuner.thin",
    "com.samsung.android.globalpostprocmgr",
    "com.samsung.android.gru",
    "com.samsung.android.hmt.vrshell",
    "com.samsung.android.hmt.vrsvc",
    "com.samsung.android.hwresourceshare.storage",
    "com.samsung.android.intellivoiceservice",
    "com.samsung.android.keyguardwallpaperupdator",
    "com.samsung.android.knox.zt.framework",
    "com.samsung.android.liveeffectservice",
    "com.samsung.android.mapsagent",
    "com.samsung.android.mateagent",
    "com.samsung.android.mdecservice",
    "com.samsung.android.mdm",
    "com.samsung.android.mdx.kit",
    "com.samsung.android.net.wifi.wifiguider",
    "com.samsung.android.nmt.apps.t2t.languagepack.enesus",
    "com.samsung.android.offline.languagemodel",
    "com.samsung.android.oneconnect",
    "com.samsung.android.rajaampat",
    "com.samsung.android.samsungpassautofill",
    "com.samsung.android.scpm",
    "com.samsung.android.sdk.ocr",
    "com.samsung.android.sdk.professionalaudio.utility.jammonitor",
    "com.samsung.android.server.iris",
    "com.samsung.android.service.livedrawing",
    "com.samsung.android.service.peoplestripe",
    "com.samsung.android.service.stplatform",
    "com.samsung.android.service.tagservice",
    "com.samsung.android.service.travel",
    "com.samsung.android.setting.multisound",
    "com.samsung.android.smartsuggestions",
    "com.samsung.android.spay",
    "com.samsung.android.spdfnote",
    "com.samsung.android.ssco",
    "com.samsung.android.stickerplugin",
    "com.samsung.android.svoice",
    "com.samsung.android.svoiceime",
    "com.samsung.android.themecenter",
    "com.samsung.android.themestore",
    "com.samsung.android.tripwidget",
    "com.samsung.android.tvplus",
    "com.samsung.android.visionarapps",
    "com.samsung.android.visioncloudagent",
    "com.samsung.android.vision.model",
    "com.samsung.android.visual.cloudcore",
    "com.samsung.android.voc",
    "com.samsung.android.voicewakeup",
    "com.samsung.android.vtcamerasettings",
    "com.samsung.android.widgetapp.yahooedge.finance",
    "com.samsung.android.widgetapp.yahooedge.sport",
    "com.samsung.app.highlightplayer",
    "com.samsung.app.newtrim",
    "com.samsung.daydream.customization",
    "com.samsung.dcmservice",
    "com.samsung.desktopsystemui",
    "com.samsung.ecomm",
    "com.samsung.enhanceservice",
    "com.samsung.faceservice",
    "com.samsung.fresco.logging",
    "com.samsung.groupcast",
    "com.samsung.hs20provider",
    "com.samsung.ipservice",
    "com.samsung.knox.appsupdateagent",
    "com.samsung.knox.rcp.components",
    "com.samsung.knox.securefolder",
    "com.samsung.knox.securefolder.setuppage",
    "com.samsung.petservice",
    "com.samsung.safetyinformation",
    "com.samsung.sec.android.application.csc",
    "com.samsung.sree",
    "com.samsung.storyservice",
    "com.samsung.svoice.sync",
    "com.samsung.systemui.bixby",
    "com.samsung.systemui.bixby2",
    "com.samsung.ucs.agent.ese",
    "com.samsung.voiceserviceplatform",
    "com.sec.android.app.apex",
    "com.sec.android.app.applinker",
    "com.sec.android.app.bluetoothtest",
    "com.sec.android.app.chromecustomizations",
    "com.sec.android.app.clockpackage",
    "com.sec.android.app.DataCreate",
    "com.sec.android.app.desktoplauncher",
    "com.sec.android.app.dexonpc",
    "com.sec.android.app.factorykeystring",
    "com.sec.android.app.gamehub",
    "com.sec.android.app.hwmoduletest",
    "com.sec.android.app.magnifier",
    "com.sec.android.app.myfiles",
    "com.sec.android.app.ocr",
    "com.sec.android.app.parser",
    "com.sec.android.app.personalization",
    "com.sec.android.app.popupcalculator",
    "com.sec.android.app.quicktool",
    "com.sec.android.app.ringtoneBR",
    "com.sec.android.app.safetyassurance",
    "com.sec.android.app.samsungapps",
    "com.sec.android.app.sbrowser",
    "com.sec.android.app.SecSetupWizard",
    "com.sec.android.app.servicemodeapp",
    "com.sec.android.app.setupwizard",
    "com.sec.android.app.shealth",
    "com.sec.android.app.SmartClipEdgeService",
    "com.sec.android.app.soundalive",
    "com.sec.android.app.sysscope",
    "com.sec.android.app.tfunlock",
    "com.sec.android.app.tourviewer",
    "com.sec.android.app.translator",
    "com.sec.android.app.vepreload",
    "com.sec.android.app.ve.vebgm",
    "com.sec.android.app.voicenote",
    "com.sec.android.app.wfdbroker",
    "com.sec.android.app.withtv",
    "com.sec.android.app.wlantest",
    "com.sec.android.autodoodle.service",
    "com.sec.android.AutoPreconfig",
    "com.sec.android.cover.ledcover",
    "com.sec.android.desktopmode.uiservice",
    "com.sec.android.dexsystemui",
    "com.sec.android.diagmonagent",
    "com.sec.android.easyMover.Agent",
    "com.sec.android.easyonehand",
    "com.sec.android.emergencylauncher",
    "com.sec.android.mimage.avatarstickers",
    "com.sec.android.mimage.gear360editor",
    "com.sec.android.mimage.photoretouching",
    "com.sec.android.ofviewer",
    "com.sec.android.omc",
    "com.sec.android.Preconfig",
    "com.sec.android.preloadinstaller",
    "com.sec.android.provider.snote",
    "com.sec.android.providers.security",
    "com.sec.android.providers.tasks",
    "com.sec.android.RilServiceModeApp",
    "com.sec.android.sdhms",
    "com.sec.android.service.health",
    "com.sec.android.sidesync30",
    "com.sec.android.splitsound",
    "com.sec.android.uibcvirtualsoftkey",
    "com.sec.android.widgetapp.diotek.smemo",
    "com.sec.android.widgetapp.easymodecontactswidget",
    "com.sec.android.widgetapp.samsungapps",
    "com.sec.app.TransmitPowerService",
    "com.sec.automation",
    "com.sec.bcservice",
    "com.sec.downloadablekeystore",
    "com.sec.enterprise.knox.attestation",
    "com.sec.enterprise.knox.cloudmdm.smdms",
    "com.sec.enterprise.mdm.services.simpin",
    "com.sec.enterprise.mdm.vpn",
    "com.sec.epdgtestapp",
    "com.sec.everglades",
    "com.sec.everglades.update",
    "com.sec.factory",
    "com.sec.factory.camera",
    "com.sec.factory.iris.usercamera",
    "com.sec.hearingadjust",
    "com.sec.kidsplat.installer",
    "com.sec.knox.foldercontainer",
    "com.sec.knox.knoxsetupwizardclient",
    "com.sec.knox.switcher",
    "com.sec.location.nsflp2",
    "com.sec.mldapchecker",
    "com.sec.modem.settings",
    "com.sec.penup",
    "com.sec.providers.assisteddialing",
    "com.sec.readershub",
    "com.sec.smartcard.manager",
    "com.sec.spen.flashannotate",
    "com.sec.spp.push",
    "com.sec.sve",
    "com.sec.usbsettings",
    "com.sec.vowifispg",
    "com.sec.yosemite.phone",
    "com.sem.factoryapp",
    "com.singtel.mysingtel",
    "com.skms.android.agent",
    "com.skype.raider",
    "com.spotify.music",
    "com.srin.indramayu",
    "com.test.LTEfunctionality",
    "com.touchtype.swiftkey",
    "com.tripadvisor.tripadvisor",
    "com.trustonic.tuiservice",
    "com.tv.peel.samsung.app",
    "com.vlingo.midas",
    "com.wssnps",
    "com.yelp.android.samsungedge",
    "com.google.android.apps.messaging"
]

# ===== NUCLEAR LIST (everything above + core Samsung/Google apps) =====
# Only use this if you're turning the device into a headless server
nuclear_extra = [
    "com.samsung.android.dialer",  # Samsung Phone
    "com.samsung.android.contacts",  # Samsung Contacts
    "com.samsung.android.email.provider",  # Samsung Email
    "com.samsung.android.app.notes",  # Samsung Notes
    "com.samsung.android.app.reminder",  # Samsung Reminder
    "com.samsung.android.app.clockpack",  # Samsung Clock
    "com.samsung.android.app.calculator",  # Samsung Calculator
    # "com.samsung.android.app.fileoperator",  # My Files
    # "com.sec.android.app.myfiles",  # My Files Alt
    "com.samsung.android.da.daagent",  # Samsung DA Agent
    "com.samsung.android.app.taskedge",  # Tasks Edge
    "com.samsung.android.honeyboard",  # Samsung Keyboard
    "com.samsung.android.incallui",  # Samsung In Call UI
    "com.samsung.android.app.inter.proto",  # Samsung Inter Proto
    "com.samsung.android.storyservice",  # Story Album
    "com.samsung.android.app.setupwizardlegalprovider",  # Setup Wizard Legal
    "com.samsung.android.app.cocktailbarservice",  # Edge Panel
    "com.samsung.android.app.clip",  # Edge Clips
    "com.samsung.android.app.camera.sticker.facear",  # Camera AR Stickers
    "com.samsung.android.app.camera.sticker.overlay",  # Camera Stickers
    "com.samsung.android.samsungpositioning",  # Samsung Positioning
    "com.samsung.android.aware.service",  # WiFi Aware
    "com.samsung.android.app.galaxyfinder",  # Galaxy Search
    "com.samsung.android.mateagent",  # Samsung Mate Agent
    "com.google.android.setupwizard",  # Google Setup Wizard
    "com.samsung.android.weather",  # Samsung Weather
    "com.samsung.app.highlightplayer",  # Samsung Studio
    "com.samsung.android.video.editor",  # Samsung Video Editor
    "com.samsung.android.score",  # Samsung Core Services
    "com.samsung.android.services.core",  # Samsung Core Services Alt
    "com.android.vending",  # Google Play Store
    "com.google.android.apps.messaging",  # Google Messages
    "com.google.android.gms",  # Google Play Services
    "com.sec.android.app.samsungapps",  # Galaxy Store Alt
    "com.samsung.android.themestore",  # Galaxy Themes
    "com.samsung.android.autoblocker",  # Auto Blocker
    "com.sec.android.easyMover.Assistant",  # Android Switch / Smart Switch Assistant
]

nuclear_packages = standard_packages + nuclear_extra


def uninstall(packages):
    success = 0
    failed = 0
    skipped = 0
    for package in packages:
        print(f"Uninstalling: {package}")
        try:
            result = subprocess.run(
                ["adb", "shell", "pm", "uninstall", "--user", "0", package],
                capture_output=True,
                text=True,
            )
            if "Success" in result.stdout:
                print(f"  OK")
                success += 1
            else:
                print(f"  Skipped (not installed or already removed)")
                skipped += 1
        except Exception as e:
            print(f"  Error: {e}")
            failed += 1
    print(f"\nDone. Success: {success} | Skipped: {skipped} | Failed: {failed}")


def main():
    print("=============================")
    print("   Android Debloat Script    ")
    print("=============================")
    print()
    print("1. Standard debloat (safe, removes bloat but keeps core Android)")
    print("2. Nuclear (removes everything including core Samsung apps,")
    print("   only use if turning device into a headless server)")
    print()

    choice = input("Choose an option (1 or 2): ").strip()

    if choice == "1":
        print(f"\nRunning standard debloat ({len(standard_packages)} packages)...\n")
        uninstall(standard_packages)
    elif choice == "2":
        print("\nWARNING: Nuclear mode removes core system apps.")
        print("Only do this if the device will never be used as a daily driver.")
        confirm = input("Type 'yes' to confirm: ").strip().lower()
        if confirm == "yes":
            print(f"\nRunning nuclear debloat ({len(nuclear_packages)} packages)...\n")
            uninstall(nuclear_packages)
        else:
            print("Cancelled.")
    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()

# Restore command: adb shell pm install-existing --user 0 com.package.name
