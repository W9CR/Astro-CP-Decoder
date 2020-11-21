CHUNK_PARSER = {
    0x01 : "chunk_01",
}

CHUNK_TYPES = {
    0x01 : "MODEL/SERIAL/POINTER DATA",
    0x02 : "CONFIGURATION",
    0x03 : "POINTER TO HW CONFIG",
    0x04 : "CONVENTIONAL HARDWARE CONFIG",
    0x05 : "SECURE DEVIATION",
    0x06 : "POINTER TO TXDEV/SQL/BW SOFT POTS",
    0x07 : "TX POWER/DEV SOFT POT",
    0x08 : "POINTER TO SQUELCH SOFT POTS",
    0x09 : "SQUELCH SOFT POTS",
    0x0A : "POINTER TO BANDWIDTH SOFT POTS",
    0x0B : "BANDWIDTH SOFT POTS",
    0x0C : "INTERMEDIATE FREQ DATA",
    0x0D : "MDC TIMING/HW CONFIG",
    0x0E : "FREQ TUNING VALUES",
    0x0F : "FRAC-N SYNTHESIZER",
    0x11 : "BUTTON/SWITCH A/D",
    0x15 : "BBRIC",
    0x0E : "FREQ TUNING VALUES",
    0x10 : "FEATURE DESCRIPTOR",
    0x13 : "ASTRO DATA PERIPHERAL",
    0x30 : "MODEL/SERIAL/POINTER DATA",
    0x31 : "RADIO WIDE OPTIONS",
    0x33 : "KP STAT/RADIO LOCK PW/CURRENT AFFIL",
    0x34 : "POINTER TO MOBILE MORE OPTIONS",
    0x35 : "RESERVE DATA AREA (OLD)",
    0x36 : "RADIO WIDE DISP/POINTER TO PTTID/VIP",
    0x37 : "# ZONES/POINTER DATA",
    0x38 : "CHANNEL NAME TEXT PER ZONE",
    0x39 : "POINTER TO PHONE NUMBER TEXT/DATA",
    0x3A : "PHONE LIST TEXT",
    0x3B : "PHONE DTMF ACCESS/DEACCESS",
    0x3C : "BUTTON/SWITCH/KEYPAD LOGIC CONFIG",
    0x3D : "POINTER CONV/MDC/TRUNK/SEC/ASTRO/MODAT/AUX",
    0x3E : "POINTER CONV BUT/MENU CONV RADIO WIDE STAT/MSG",
    0x3F01 : "CONV BUTTON CONFIGURATION/OPTIONS",
    0x3F02 : "TRUNK BUTTON CONFIGURATION/OPTIONS",
    0x4101 : "CONV MENU OPTIONS",
    0x4102 : "TRUNK MENU OPTIONS",
    0x42 : "MPL POINTER/DATA",
    0x43 : "MPL TEXT",
    0x44 : "POINTER TO MDC SYSTEM/REPEATER ID/CALL LIST",
    0x47 : "# MDC SYSTEMS/POINTER TO SYSTEM",
    0x48 : "MDC SYSTEM DATA/POINTER TO REVERT",
    0x49 : "MDC EMERGENCY REVERT DATA",
    0x4A : "POINTER TRUNK BUT/MENU RADIO WIDE DATA/SMARTZONE",
    0x4B : "# TRUNK SYSTEMS/POINTER TO SYSTEM",
    0x4C : "POINTER TO MULTIKEY HW ENC",
    0x4D : "MULTIKEY PAR DATA/POINTER TO HW KEY DATA/INDEX",
    0x4E : "MULTIKEY # OF KEYS/POINTER TO TEXT",
    0x4F : "MULTIKEY ENCRYPTION KEY INDEX",
    0x50 : "MDC OTAR DATA",
    0x51 : "SCAN POINTER/OPTIONS",
    0x52 : "# SCAN LISTS/POINTER TO LIST",
    0x53 : "SCAN LIST CONFIG/MEMBERS",
    0x54 : "ZONE POINTER TO PERSONALITY #",
    0x55 : "# CONV/TRUNK PERSONALITIES/POINTER",
    0x56 : "CONVENTIONAL PERSONALITY DATA",
    0x56FF : "CONVENTIONAL PERSONALITY DEFAULT DATA/POINTER TO TUNING",
    0x57 : "# ZONES/TALKGROUP DATA",
    0x58 : "POINTER TO TRUNK CALL LIST TEXT/DATA",
    0x59 : "TRUNK CALL LIST TEXT",
    0x5A : "TRUNK SYSTEM DATA",
    0x5B : "TRUNK LAB DYNAMIC SYSTEM DATA",
    0x5E : "PTR TO TRNK OB CH ASSIGN/OTHERBAND CONTROL CHANNELS",
    0x5F : "TRUNK OTHERBAND CHANNEL ASSIGN",
    0x60 : "TYPE I RESERVED DATA AREA",
    0x61 : "800/900 MHZ CONTROL CHANNELS",
    0x62 : "TRUNK PERSONALITY OPTIONS",
    0x63 : "TRUNK PERSONALITY TALKGROUP DATA",
    0x64 : "TRUNK PERSONALITY SUBFLEET DATA",
    0x65 : "TRUNK PERSONALITY FAILSOFT DATA",
    0x66 : "TRUNK PERSONALITY OTHERBAND FAILSOFT DATA",
    0x67 : "TRUNK PERSONALITY EMERGENCY REVERT DATA",
    0x6C : "SMARTZONE ENABLED IN TRUNK SYSTEM",
    0x6D : "800 SMARTZONE DATA",
    0x6E : "VHF/UHF SMARTZONE DATA",
    0x6F : "SMARTZONE ENV",
    0x70 : "POINTER TO TRUNK STATUS ALIAS TEXT/DATA",
    0x71 : "POINTER TO TRUNK MESSAGE ALIAS TEXT/DATA",
    0x72 : "POINTER TO TRUNK SITE ALIAS TEXT/DATA",
    0x73 : "TRUNK STATUS ALIAS TEXT",
    0x74 : "TRUNK MESSAGE ALIAS TEXT",
    0x75 : "TRUNK SITE ALIAS TEXT",
    0x76 : "# OF TG IN TRUNK PERSONALITY",
    0x77 : "EXTENDED DEK ZONE/MODE DATA",
    0x78 : "EXTENDED DEK STATUS BUTTON INDEX",
    0x79 : "EXTENDED DEK MESSAGE BUTTON INDEX",
    0x7A : "RADIO VIP OUT CONFIG",
    0x81 : "ASTRO RADIO WIDE/CAI DATA",
    0x82 : "# ASTRO SYSTEMS/POINTER TO SYSTEM",
    0x83 : "ASTRO SYSTEMS DATA",
    0x87 : "SOFTWARE ENCRYPTION KEY DATA",
    0x88 : "ASTRO CALL LIST ID",
    0x89 : "ASTRO CALL LIST ALIAS TEXT",
    0x8A : "ASTRO EMERGENCY REVERT",
    0x8B : "OTACR DATA",
    0x8C : "PTT ID PREFIX TEXT",
    0x8D : "MODAT DATA",
    0x8E : "CONVENTIONAL STATUS ALIAS DATA",
    0x8F : "CONVENTIONAL STATUS ALIAS TEXT",
    0x90 : "CONVENTIONAL MESSAGE ALIAS DATA",
    0x91 : "CONVENTIONAL MESSAGE ALIAS TEXT",
    0x92 : "MDC CALL LIST DATA",
    0x93 : "MDC CALL LIST TEXT",
    0x94 : "SOFT ID TEXT",
    0x95 : "HARDWARE ENCRYPTION KEY TEXT",
    0x96 : "SOFTWARE ENCRYPTION KEY TEXT",
    0x97 : "PA/SIREN DATA",
    0x98 : "VRS-EP CONFIG/DATA",
    0x99 : "HHCH DATA",
    0x9B : "800 SMARTZONE DATA",
    0x9D : "REAR CONTROL HEAD OPTION",
    0x9E : "VHF/UHF SMARTZONE DATA",
    0x9F : "MDC REPEATER ID",
    0xA0 : "AUX SYSTEM POINTER",
    0xA1 : "SINGLETONE SYSTEM",
    0xA2 : "SINGLETONE TIMING DATA",
    0xA3 : "SINGLETONE TONE DATA",
    0xA4 : "QCII SYSTEM",
    0xA5 : "QCII DATA",
    0xA6 : "GE STAR SYSTEM",
    0xA7 : "GE STAR DATA",
    0xA9 : "GE STAR HW CONFIG",
    0xAB : "VRM100/VRM500 DATA",
    0xAC : "OMNILINK PREF SITE",
    0xAE : "TRC OPTION",
    0xAF : "MULTI RADIO OPTION",
    0xB0 : "POINTER TO ASTRO SYSTEM",
    0xB1 : "POINTER TO ASTRO TALKGROUP/ALIAS",
    0xB2 : "ASTRO CONV TALKGROUP ID",
    0xB3 : "ASTRO CONV TALKGROUP ALIAS TEXT",
    0xB4 : "RESERVE DATA AREA",
    0xB5 : "RESERVE DATA AREA",
    0xB6 : "RESERVE DATA AREA",
    0xB7 : "RESERVE DATA AREA",
    0xB8 : "RESERVE DATA AREA",
    0xB9 : "RESERVE DATA AREA",
    0xBA : "SMART MESSAGE",
    0xBC : "SMART MESSAGE POINTER TO TEXT/DATA",
    0xBD : "SMART MESSAGE TEXT",
    0xBE : "SMART MESSAGE OPTIONS",
    0xC1 : "APCO25 PHONE LIST TEXT",
    0xC2 : "FACTORY OVERIDE ENABLE/POINTER",
    0xC3 : "APCO25 POINTER TO PHONE NUMBER TEXT/DATA",
    0xC6 : "FACT OVER FGU SYNTH RX",
    0xC7 : "FACT OVER FGU SYNTK TX",
    0xC8 : "FACT OVER HOST CLOCK SHIFT",
    0xC9 : "FACT OVER DSP CLOCK SHIFT",
    0xCA : "FACT OVER SECURE CLOCK SHIFT",
    0xCB : "APCO25 CONTROL CHANNELS",
    0xCC : "APCO25 BASE FREQUENCY",
    0xCD : "APCO25 TRUNK CALL LIST/POINTER TO TEXT",
    0xCF : "APCO25 # TALKGROUP IN TRUNK PERSONALITY",
    0xD0 : "APCO25 TRUNK PERSONALITY TALKGROUP DATA",
    0xD8 : "CKR KEY MANAGMENT DATA",
    0xD9 : "ASTRO OTAR DATA"
}


class chunkBasecalss:
    pointers = []
    data = {}

    def getPointers(self):
        return self.pointers
