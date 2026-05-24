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
    "com.samsung.android.video",  # Samsung Video Player
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
    # Microsoft
    "com.microsoft.appmanager",  # Link to Windows
    "com.microsoft.skydrive",  # OneDrive
    "com.microsoft.teams",  # Microsoft Teams
    "com.microsoft.office.word",  # Word
    "com.microsoft.office.excel",  # Excel
    "com.microsoft.office.powerpoint",  # PowerPoint
    "com.microsoft.office.outlook",  # Outlook
    "com.microsoft.launcher.enterprise",  # Microsoft Launcher
    # Facebook / Meta
    "com.facebook.appmanager",  # Facebook Tracking
    "com.facebook.katana",  # Facebook
    "com.facebook.orca",  # Messenger
    "com.facebook.system",  # Facebook System Service
    "com.instagram.android",  # Instagram
    # Spyware
    "com.aura.oobe.samsung",  # Israeli Spyware
    "com.android.credentialmanager",  # Credential Manager
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
    "com.samsung.android.app.fileoperator",  # My Files
    "com.sec.android.app.myfiles",  # My Files Alt
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
