import subprocess

packages = [
    "com.google.android.tts",  # TTS From Google
    "com.google.android.voicesearch",  # Voice Search From Google
    "com.google.android.speechservices",  # TTS From Google
    "com.google.android.googlequicksearchbox",  # The Google App
    "com.samsung.android.inputshare",  # The Multi Control App
    "com.samsung.android.bixbyvision.framework",
    "com.samsung.android.ipsgeofence",  # Samsung Visit In
    "com.google.android.apps.bard",  # Gemini
    "com.microsoft.appmanager",  # Link to Windows
    "com.samsung.android.mdx",  # Link To Windows Service
    "com.samsung.android.messaging",  # Samsung's Messaging App
    "com.google.android.apps.tachyon",  # Google Meet
    "com.samsung.android.spayfw",  # Samsung Pay Framework
    "com.samsung.android.samsungpass",  # Samsung Pass
    "com.google.android.ondevicepersonalization.services",  # Google tracking
    "com.facebook.appmanager",  # Facebook tracking
    "com.google.android.feedback",  # Google's Feedback Service
    "com.google.android.adservices.api",  # Google's Ad Services
    "com.google.mainline.telemetry",  # Data Collector
    "com.google.mainline.adservices",  # Google's Ad Services
    "com.android.chrome",  # Chrome
    "com.google.android.youtube",  # YouTube
    "com.sec.android.easyMover",  # Smart Switch
    "com.sec.android.app.fm",  # Samsung Radio
    "com.google.android.projection.gearhead",  # Android Auto
    "com.samsung.android.game.gamehome",  # Gaming Hub
    "com.google.android.gm",  # Gmail
    "com.google.android.apps.maps",  # Google Maps
    "com.microsoft.skydrive",  # OneDrive
    "com.samsung.android.calendar", # Samsung Calendar
    "com.google.android.apps.credentialmanager", # Google password manager
    "com.google.android.printservice.recommendation", # Print suggestions only
    "com.google.android.apps.accessibility.voiceaccess", # Voice Access (accessibility)
    "com.google.android.apps.carrier.carrierwifi", # Carrier Wi-Fi helper
    "com.google.android.apps.turbo", # Google Go / Turbo
    "com.google.android.gms.supervision", # Parental controls
    "com.google.android.partnersetup", # OEM partner setup
    "com.google.android.ar.core", # AR services
    "com.samsung.SMT.lang_pt_br_f00",
    "com.samsung.SMT.lang_en_us_f00",
    "com.samsung.SMT.lang_es_mx_f00",
    "com.samsung.SMT.lang_hi_in_f00",
    "com.samsung.SMT.lang_en_in_f00",
    "com.samsung.android.tts.lang.pl",
    "com.samsung.SMT",
    "com.google.android.apps.photos",
    "com.samsung.android.bixby.agent",
    "com.samsung.android.bixby.wakeup",
    "com.samsung.android.visionintelligence",
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
    "com.aura.oobe.samsung", # Israeli Spyware
    "com.sec.android.app.kidshome",
    "com.samsung.android.kidsinstaller",
    "com.samsung.android.scloud",
    "com.sec.android.app.billing",
    "com.android.credentialmanager"
]

for package in packages:
    print(f"Uninstalling: {package}")
    try:
        result = subprocess.run(
            ["adb", "uninstall", "--user", "0", package],
            capture_output=True,
            text=True,
            check=True
        )
        print("Success:", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error:", e.stderr)
