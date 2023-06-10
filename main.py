#!/usr/bin/python
# -*- coding: utf-8

###########################################################
# Author >>> Falzy                                        #
# Telegram >>> https://t.me/balestra / https://t.me/op_v0 #
# Website >>> https://blackdata.altervista.org            #
###########################################################

import pyrogram
import time
import datetime
import pytz
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InputMediaPhoto, InputMediaVideo, InputMediaAudio
from googlesearch import search
import requests
from bs4 import BeautifulSoup
import json
from chatgpt import gpt
import urllib.parse
import tokens

app = Client(
    "ubot",
    api_id = tokens.API_ID,
    api_hash= tokens.API_HASH
)

zones = [
'Africa/Abidjan',
'Africa/Accra',
'Africa/Addis_Ababa',
'Africa/Algiers',
'Africa/Asmara',
'Africa/Asmera',
'Africa/Bamako',
'Africa/Bangui',
'Africa/Banjul',
'Africa/Bissau',
'Africa/Blantyre',
'Africa/Brazzaville',
'Africa/Bujumbura',
'Africa/Cairo',
'Africa/Casablanca',
'Africa/Ceuta',
'Africa/Conakry',
'Africa/Dakar',
'Africa/Dar_es_Salaam',
'Africa/Djibouti',
'Africa/Douala',
'Africa/El_Aaiun',
'Africa/Freetown',
'Africa/Gaborone',
'Africa/Harare',
'Africa/Johannesburg',
'Africa/Juba',
'Africa/Kampala',
'Africa/Khartoum',
'Africa/Kigali',
'Africa/Kinshasa',
'Africa/Lagos',
'Africa/Libreville',
'Africa/Lome',
'Africa/Luanda',
'Africa/Lubumbashi',
'Africa/Lusaka',
'Africa/Malabo',
'Africa/Maputo',
'Africa/Maseru',
'Africa/Mbabane',
'Africa/Mogadishu',
'Africa/Monrovia',
'Africa/Nairobi',
'Africa/Ndjamena',
'Africa/Niamey',
'Africa/Nouakchott',
'Africa/Ouagadougou',
'Africa/Porto-Novo',
'Africa/Sao_Tome',
'Africa/Timbuktu',
'Africa/Tripoli',
'Africa/Tunis',
'Africa/Windhoek',
'America/Adak',
'America/Anchorage',
'America/Anguilla',
'America/Antigua',
'America/Araguaina',
'America/Argentina/Buenos_Aires',
'America/Argentina/Catamarca',
'America/Argentina/ComodRivadavia',
'America/Argentina/Cordoba',
'America/Argentina/Jujuy',
'America/Argentina/La_Rioja',
'America/Argentina/Mendoza',
'America/Argentina/Rio_Gallegos',
'America/Argentina/Salta',
'America/Argentina/San_Juan',
'America/Argentina/San_Luis',
'America/Argentina/Tucuman',
'America/Argentina/Ushuaia',
'America/Aruba',
'America/Asuncion',
'America/Atikokan',
'America/Atka',
'America/Bahia',
'America/Bahia_Banderas',
'America/Barbados',
'America/Belem',
'America/Belize',
'America/Blanc-Sablon',
'America/Boa_Vista',
'America/Bogota',
'America/Boise',
'America/Buenos_Aires',
'America/Cambridge_Bay',
'America/Campo_Grande',
'America/Cancun',
'America/Caracas',
'America/Catamarca',
'America/Cayenne',
'America/Cayman',
'America/Chicago',
'America/Chihuahua',
'America/Coral_Harbour',
'America/Cordoba',
'America/Costa_Rica',
'America/Creston',
'America/Cuiaba',
'America/Curacao',
'America/Danmarkshavn',
'America/Dawson',
'America/Dawson_Creek',
'America/Denver',
'America/Detroit',
'America/Dominica',
'America/Edmonton',
'America/Eirunepe',
'America/El_Salvador',
'America/Ensenada',
'America/Fort_Nelson',
'America/Fort_Wayne',
'America/Fortaleza',
'America/Glace_Bay',
'America/Godthab',
'America/Goose_Bay',
'America/Grand_Turk',
'America/Grenada',
'America/Guadeloupe',
'America/Guatemala',
'America/Guayaquil',
'America/Guyana',
'America/Halifax',
'America/Havana',
'America/Hermosillo',
'America/Indiana/Indianapolis',
'America/Indiana/Knox',
'America/Indiana/Marengo',
'America/Indiana/Petersburg',
'America/Indiana/Tell_City',
'America/Indiana/Vevay',
'America/Indiana/Vincennes',
'America/Indiana/Winamac',
'America/Indianapolis',
'America/Inuvik',
'America/Iqaluit',
'America/Jamaica',
'America/Jujuy',
'America/Juneau',
'America/Kentucky/Louisville',
'America/Kentucky/Monticello',
'America/Knox_IN',
'America/Kralendijk',
'America/La_Paz',
'America/Lima',
'America/Los_Angeles',
'America/Louisville',
'America/Lower_Princes',
'America/Maceio',
'America/Managua',
'America/Manaus',
'America/Marigot',
'America/Martinique',
'America/Matamoros',
'America/Mazatlan',
'America/Mendoza',
'America/Menominee',
'America/Merida',
'America/Metlakatla',
'America/Mexico_City',
'America/Miquelon',
'America/Moncton',
'America/Monterrey',
'America/Montevideo',
'America/Montreal',
'America/Montserrat',
'America/Nassau',
'America/New_York',
'America/Nipigon',
'America/Nome',
'America/Noronha',
'America/North_Dakota/Beulah',
'America/North_Dakota/Center',
'America/North_Dakota/New_Salem',
'America/Ojinaga',
'America/Panama',
'America/Pangnirtung',
'America/Paramaribo',
'America/Phoenix',
'America/Port-au-Prince',
'America/Port_of_Spain',
'America/Porto_Acre',
'America/Porto_Velho',
'America/Puerto_Rico',
'America/Punta_Arenas',
'America/Rainy_River',
'America/Rankin_Inlet',
'America/Recife',
'America/Regina',
'America/Resolute',
'America/Rio_Branco',
'America/Rosario',
'America/Santa_Isabel',
'America/Santarem',
'America/Santiago',
'America/Santo_Domingo',
'America/Sao_Paulo',
'America/Scoresbysund',
'America/Shiprock',
'America/Sitka',
'America/St_Barthelemy',
'America/St_Johns',
'America/St_Kitts',
'America/St_Lucia',
'America/St_Thomas',
'America/St_Vincent',
'America/Swift_Current',
'America/Tegucigalpa',
'America/Thule',
'America/Thunder_Bay',
'America/Tijuana',
'America/Toronto',
'America/Tortola',
'America/Vancouver',
'America/Virgin',
'America/Whitehorse',
'America/Winnipeg',
'America/Yakutat',
'America/Yellowknife',
'Antarctica/Casey',
'Antarctica/Davis',
'Antarctica/DumontDUrville',
'Antarctica/Macquarie',
'Antarctica/Mawson',
'Antarctica/McMurdo',
'Antarctica/Palmer',
'Antarctica/Rothera',
'Antarctica/South_Pole',
'Antarctica/Syowa',
'Antarctica/Troll',
'Antarctica/Vostok',
'Arctic/Longyearbyen',
'Asia/Aden',
'Asia/Almaty',
'Asia/Amman',
'Asia/Anadyr',
'Asia/Aqtau',
'Asia/Aqtobe',
'Asia/Ashgabat',
'Asia/Ashkhabad',
'Asia/Atyrau',
'Asia/Baghdad',
'Asia/Bahrain',
'Asia/Baku',
'Asia/Bangkok',
'Asia/Barnaul',
'Asia/Beirut',
'Asia/Bishkek',
'Asia/Brunei',
'Asia/Calcutta',
'Asia/Chita',
'Asia/Choibalsan',
'Asia/Chongqing',
'Asia/Chungking',
'Asia/Colombo',
'Asia/Dacca',
'Asia/Damascus',
'Asia/Dhaka',
'Asia/Dili',
'Asia/Dubai',
'Asia/Dushanbe',
'Asia/Famagusta',
'Asia/Gaza',
'Asia/Harbin',
'Asia/Hebron',
'Asia/Ho_Chi_Minh',
'Asia/Hong_Kong',
'Asia/Hovd',
'Asia/Irkutsk',
'Asia/Istanbul',
'Asia/Jakarta',
'Asia/Jayapura',
'Asia/Jerusalem',
'Asia/Kabul',
'Asia/Kamchatka',
'Asia/Karachi',
'Asia/Kashgar',
'Asia/Kathmandu',
'Asia/Katmandu',
'Asia/Khandyga',
'Asia/Kolkata',
'Asia/Krasnoyarsk',
'Asia/Kuala_Lumpur',
'Asia/Kuching',
'Asia/Kuwait',
'Asia/Macao',
'Asia/Macau',
'Asia/Magadan',
'Asia/Makassar',
'Asia/Manila',
'Asia/Muscat',
'Asia/Nicosia',
'Asia/Novokuznetsk',
'Asia/Novosibirsk',
'Asia/Omsk',
'Asia/Oral',
'Asia/Phnom_Penh',
'Asia/Pontianak',
'Asia/Pyongyang',
'Asia/Qatar',
'Asia/Qyzylorda',
'Asia/Rangoon',
'Asia/Riyadh',
'Asia/Saigon',
'Asia/Sakhalin',
'Asia/Samarkand',
'Asia/Seoul',
'Asia/Shanghai',
'Asia/Singapore',
'Asia/Srednekolymsk',
'Asia/Taipei',
'Asia/Tashkent',
'Asia/Tbilisi',
'Asia/Tehran',
'Asia/Tel_Aviv',
'Asia/Thimbu',
'Asia/Thimphu',
'Asia/Tokyo',
'Asia/Tomsk',
'Asia/Ujung_Pandang',
'Asia/Ulaanbaatar',
'Asia/Ulan_Bator',
'Asia/Urumqi',
'Asia/Ust-Nera',
'Asia/Vientiane',
'Asia/Vladivostok',
'Asia/Yakutsk',
'Asia/Yangon',
'Asia/Yekaterinburg',
'Asia/Yerevan',
'Atlantic/Azores',
'Atlantic/Bermuda',
'Atlantic/Canary',
'Atlantic/Cape_Verde',
'Atlantic/Faeroe',
'Atlantic/Faroe',
'Atlantic/Jan_Mayen',
'Atlantic/Madeira',
'Atlantic/Reykjavik',
'Atlantic/South_Georgia',
'Atlantic/St_Helena',
'Atlantic/Stanley',
'Australia/ACT',
'Australia/Adelaide',
'Australia/Brisbane',
'Australia/Broken_Hill',
'Australia/Canberra',
'Australia/Currie',
'Australia/Darwin',
'Australia/Eucla',
'Australia/Hobart',
'Australia/LHI',
'Australia/Lindeman',
'Australia/Lord_Howe',
'Australia/Melbourne',
'Australia/NSW',
'Australia/North',
'Australia/Perth',
'Australia/Queensland',
'Australia/South',
'Australia/Sydney',
'Australia/Tasmania',
'Australia/Victoria',
'Australia/West',
'Australia/Yancowinna',
'Brazil/Acre',
'Brazil/DeNoronha',
'Brazil/East',
'Brazil/West',
'CET',
'CST6CDT',
'Canada/Atlantic',
'Canada/Central',
'Canada/Eastern',
'Canada/Mountain',
'Canada/Newfoundland',
'Canada/Pacific',
'Canada/Saskatchewan',
'Canada/Yukon',
'Chile/Continental',
'Chile/EasterIsland',
'Cuba',
'EET',
'EST',
'EST5EDT',
'Egypt',
'Eire',
'Etc/GMT',
'Etc/GMT+0',
'Etc/GMT+1',
'Etc/GMT+10',
'Etc/GMT+11',
'Etc/GMT+12',
'Etc/GMT+2',
'Etc/GMT+3',
'Etc/GMT+4',
'Etc/GMT+5',
'Etc/GMT+6',
'Etc/GMT+7',
'Etc/GMT+8',
'Etc/GMT+9',
'Etc/GMT-0',
'Etc/GMT-1',
'Etc/GMT-10',
'Etc/GMT-11',
'Etc/GMT-12',
'Etc/GMT-13',
'Etc/GMT-14',
'Etc/GMT-2',
'Etc/GMT-3',
'Etc/GMT-4',
'Etc/GMT-5',
'Etc/GMT-6',
'Etc/GMT-7',
'Etc/GMT-8',
'Etc/GMT-9',
'Etc/GMT0',
'Etc/Greenwich',
'Etc/UCT',
'Etc/UTC',
'Etc/Universal',
'Etc/Zulu',
'Europe/Amsterdam',
'Europe/Andorra',
'Europe/Astrakhan',
'Europe/Athens',
'Europe/Belfast',
'Europe/Belgrade',
'Europe/Berlin',
'Europe/Bratislava',
'Europe/Brussels',
'Europe/Bucharest',
'Europe/Budapest',
'Europe/Busingen',
'Europe/Chisinau',
'Europe/Copenhagen',
'Europe/Dublin',
'Europe/Gibraltar',
'Europe/Guernsey',
'Europe/Helsinki',
'Europe/Isle_of_Man',
'Europe/Istanbul',
'Europe/Jersey',
'Europe/Kaliningrad',
'Europe/Kiev',
'Europe/Kirov',
'Europe/Lisbon',
'Europe/Ljubljana',
'Europe/London',
'Europe/Luxembourg',
'Europe/Madrid',
'Europe/Malta',
'Europe/Mariehamn',
'Europe/Minsk',
'Europe/Monaco',
'Europe/Moscow',
'Europe/Nicosia',
'Europe/Oslo',
'Europe/Paris',
'Europe/Podgorica',
'Europe/Prague',
'Europe/Riga',
'Europe/Rome',
'Europe/Samara',
'Europe/San_Marino',
'Europe/Sarajevo',
'Europe/Saratov',
'Europe/Simferopol',
'Europe/Skopje',
'Europe/Sofia',
'Europe/Stockholm',
'Europe/Tallinn',
'Europe/Tirane',
'Europe/Tiraspol',
'Europe/Ulyanovsk',
'Europe/Uzhgorod',
'Europe/Vaduz',
'Europe/Vatican',
'Europe/Vienna',
'Europe/Vilnius',
'Europe/Volgograd',
'Europe/Warsaw',
'Europe/Zagreb',
'Europe/Zaporozhye',
'Europe/Zurich',
'GB',
'GB-Eire',
'GMT',
'GMT+0',
'GMT-0',
'GMT0',
'Greenwich',
'HST',
'Hongkong',
'Iceland',
'Indian/Antananarivo',
'Indian/Chagos',
'Indian/Christmas',
'Indian/Cocos',
'Indian/Comoro',
'Indian/Kerguelen',
'Indian/Mahe',
'Indian/Maldives',
'Indian/Mauritius',
'Indian/Mayotte',
'Indian/Reunion',
'Iran',
'Israel',
'Jamaica',
'Japan',
'Kwajalein',
'Libya',
'MET',
'MST',
'MST7MDT',
'Mexico/BajaNorte',
'Mexico/BajaSur',
'Mexico/General',
'NZ',
'NZ-CHAT',
'Navajo',
'PRC',
'PST8PDT',
'Pacific/Apia',
'Pacific/Auckland',
'Pacific/Bougainville',
'Pacific/Chatham',
'Pacific/Chuuk',
'Pacific/Easter',
'Pacific/Efate',
'Pacific/Enderbury',
'Pacific/Fakaofo',
'Pacific/Fiji',
'Pacific/Funafuti',
'Pacific/Galapagos',
'Pacific/Gambier',
'Pacific/Guadalcanal',
'Pacific/Guam',
'Pacific/Honolulu',
'Pacific/Johnston',
'Pacific/Kiritimati',
'Pacific/Kosrae',
'Pacific/Kwajalein',
'Pacific/Majuro',
'Pacific/Marquesas',
'Pacific/Midway',
'Pacific/Nauru',
'Pacific/Niue',
'Pacific/Norfolk',
'Pacific/Noumea',
'Pacific/Pago_Pago',
'Pacific/Palau',
'Pacific/Pitcairn',
'Pacific/Pohnpei',
'Pacific/Ponape',
'Pacific/Port_Moresby',
'Pacific/Rarotonga',
'Pacific/Saipan',
'Pacific/Samoa',
'Pacific/Tahiti',
'Pacific/Tarawa',
'Pacific/Tongatapu',
'Pacific/Truk',
'Pacific/Wake',
'Pacific/Wallis',
'Pacific/Yap',
'Poland',
'Portugal',
'ROC',
'ROK',
'Singapore',
'Turkey',
'UCT',
'US/Alaska',
'US/Aleutian',
'US/Arizona',
'US/Central',
'US/East-Indiana',
'US/Eastern',
'US/Hawaii',
'US/Indiana-Starke',
'US/Michigan',
'US/Mountain',
'US/Pacific',
'US/Pacific-New',
'US/Samoa',
'UTC',
'Universal',
'W-SU',
'WET',
'Zulu'
]

bio = "Dev > @balestra"
timezone = "cet"
botowner = "balestra"

@app.on_message(filters.user(botowner) & filters.command(["start","info"], [".", "-"]))
async def start(client, message):
    global bio, timezone
    me = await app.get_me()
    name = me.first_name
    id = me.id
    username = me.username
    
    timezone = pytz.timezone(str(timezone))
    now = (datetime.datetime.now(timezone))
    
    date = ""
    if(int(now.day)<10):
        date = "0"
    if(int(now.month)<10):        
        date = date+str(now.day)+"-0"+str(now.month)+"-"+str(now.year)
    else:
        date = date+str(now.day)+"-"+str(now.month)+"-"+str(now.year)
    
    h = str(now.hour)
    m = str(now.minute)
    s = str(now.second)
    if(int(now.hour)<10):
        h = "0" + str(now.hour)
    if(int(now.minute)<10):
        m = "0" + str(now.minute)
    if(int(now.second)<10):
        s = "0" + str(now.second)
    time = h+":"+m+":"+s
    
    msgid = message.chat.id
    await message.delete()
    await app.send_photo(msgid,"images/ubot.jpg",f"╭══「 ᮳ 」𝙑𝙀𝙓𝘾𝙃𝘼𝙊𝙎 㞮══ ⪩\n╰╮\n╭┤➥『𝙉𝘼𝙈𝙀』: {name}\n┃│➥『𝙄𝘿』: {id}\n┃│➥『𝙐𝙎𝙀𝙍𝙉𝘼𝙈𝙀』: @{username}\n┃│➥『𝘽𝙄𝙊』: \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n{bio}\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n┃│➥『𝘿𝘼𝙏𝙀』: {date}\n┃│➥『𝙏𝙄𝙈𝙀』: {time}\n┃╰══ ⪨\n╰══════════════ ⪨")

@app.on_message(filters.user(botowner) & filters.command(["tzone","tz","timezone"], ["/", ".", "-"]))
async def tz(client, message):
    global timezone, zones
    v = False
    tmp = message.text.split()[1:]
    if(len(tmp)==1):
        msg = tmp[0]
        print(msg)
        for x in zones:
            if(msg.lower()==x.lower()):
                timezone = str(msg)
                await message.edit("Time zone set successfully!")
                v = True
                break
    if not v:
        await message.edit("You must specify an existing time zone\n\nCommand: <code>/tz TIMEZONE_NAME</code>\n\nExample: <code>/tz cet</code>")


@app.on_message(filters.user(botowner) & filters.command(["help","aiuto","cmd","cmds","comandi","comando","commands","command"], ["/", ".", "-"]))
async def help(client, message):
    await message.edit("𝘾𝙊𝙈𝙈𝘼𝙉𝘿 𝙇𝙄𝙎𝙏\n\n<code>.start</code> / <code>.info</code> - show your basic info\n\n<code>.get</code> - show someone's info\n\n<code>.src</code> - search for something like being on Google!\n\n<code>.bio</code> - set your bio\n\n<code>.ask</code> - ask something and get an answer from ChatGPT\n\n<code>.cls</code> - clear ChatGPT chat logs\n\n<code>.map / .where</code> - search for a place like on Google Maps\n\n<code>.tz</code> - set the time zone\n\n<code>.who</code> - info about the developer\n")

@app.on_message(filters.user(botowner) & filters.command(["credits","who","creator","developer","dev","falzy"], ["/", ".", "-"]))
async def credits(client, message):
    msgid = message.chat.id
    await message.delete()
    await app.send_animation(msgid, "images/animation.gif", caption="𝘿𝙀𝙑𝙀𝙇𝙊𝙋𝙀𝙍\n\n◈ Credits: @balestra\n\n◈ Channel: @op_v0\n\n◈ Website: https://blackdata.altervista.org", unsave=True)
       
@app.on_message(filters.user(botowner) & filters.command(["ask","question","query","chatgpt"], ["/", ".", "-"]))
async def gptcall(client, message):
    tmp = message.text.split()[1:]
    if not tmp:        
        await message.edit("Per favore, inserisci una query valida.")
    msg = ""
    for x in tmp:
        msg = msg + x + " "
    print(msg)
    id = message.chat.id
    res = await gpt.get_answer(msg,tokens.POE_TOKEN, tokens.POE_BOT_NAME)
    await message.edit("<strong>Query:</strong>\n<code>" + msg + "</code>\n\n<strong>Answer:</strong>\n<code>" + res + "</code>")
    
@app.on_message(filters.user(botowner) & filters.command(["bio","setbio","bioset"], ["/", ".", "-"]))
async def setbio(client, message):
    global bio
    tmp = message.text.split()[1:]
    msg = ""
    for x in tmp:
        msg = msg + x + " "
    print(msg)
    bio = msg
    await message.edit("<strong>Bio is successfully set!</strong>")
    
@app.on_message(filters.user(botowner) & filters.command(["cls","clear","delchat"], ["/", ".", "-"]))
async def clear(client, message):
    await gpt.clear(tokens.POE_TOKEN, tokens.POE_BOT_NAME)
    await message.edit("AI chat log successfully cleared!")
    
@app.on_message(filters.user(botowner) & filters.command("src", ["/", ".", "-"]))
async def search_command(client, message):
    query = ' '.join(message.command[1:])  
    if not query:
        await message.edit("Per favore, inserisci una query valida.")
        return
    
    title = ""
    url = ""
    description = ""

    try:
        results = search(query,lang="it",num_results=5, advanced=True)
        if results:
            response = f"<b>Risultati della ricerca per '{query}':</b>\n\n"
            
            for x in results:
                title = x.title
                url = x.url
                description = x.description
                response += f"<a href='{url}'>{title}</a>\n{description}\n\n"
            message.edit(response)
        else:
            message.edit("Nessun risultato trovato.")
    except Exception as e:
        print(f"Errore durante la ricerca: {str(e)}")
        message.edit("Si è verificato un errore durante la ricerca.")
        
@app.on_message(filters.user(botowner) & filters.command("get", ["/", ".", "-"]))
async def statget(client, message):
    who = ' '.join(message.command[1:])  
    result = await app.get_users(who)
    status = str(result.status)
    if(status=="UserStatus.ONLINE"):
        status="online"
    elif(status=="UserStatus.OFFLINE"):
        status=f"offline: {result.last_online_date}"
    elif(status=="UserStatus.RECENTLY"):
        status="online recently"
    elif(status=="UserStatus.LAST_WEEK"):
        status="online last week"
    elif(status=="UserStatus.LAST_MONTH"):
        status="online last month"
    elif(status=="UserStatus.LONG_AGO"):
        status="online a long time ago"
    stats = f"╭══「 ᮳ 」𝙑𝙀𝙓𝘾𝙃𝘼𝙊𝙎 㞮══ ⪩\n╰╮\n╭┤➥『𝙁𝙄𝙍𝙎𝙏 𝙉𝘼𝙈𝙀』: {str(result.first_name)}"
    if(result.last_name):
        stats = stats+ f"\n┃│➥『𝙇𝘼𝙎𝙏 𝙉𝘼𝙈𝙀』: {str(result.last_name)}"
    stats = stats+ f"\n┃│➥『𝙄𝘿』: <code>{str(result.id)}</code>"
    if(result.username):
        stats = stats+ f"\n┃│➥『𝙐𝙎𝙀𝙍𝙉𝘼𝙈𝙀』: @{str(result.username)}"
    if(result.dc_id):
        stats = stats+ f"\n┃│➥『𝘿𝘾』: {result.dc_id}"
    if(result.phone_number):
        stats = stats+ f"\n┃│➥『𝙉𝙐𝙈𝘽𝙀𝙍』: +{str(result.phone_number)}"
    stats = stats+ f"\n┃│➥『𝙎𝙏𝘼𝙏𝙐𝙎』: {status}\n┃╰══ ⪨\n╰══════════════ ⪨"
    
    if(result.photo):
        photo = None
        async for x in app.get_chat_photos(who,1):
            photo = x
        await app.send_photo(message.chat.id,str(photo.file_id),stats)
        await message.delete()
    else:
        await message.edit(f"{stats}")

@app.on_message(filters.user(botowner) & filters.command(["map","maps","googlemaps","location","locate","where","posizione","dove"], ["/", ".", "-"]))
async def statget(client, message):
    address = ' '.join(message.command[1:])  
    
    if not address:        
        await message.edit("Per favore, inserisci una query valida.")
        return
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'

    response = requests.get(url).json()
    await app.send_location(message.chat.id,float(response[0]["lat"]),float(response[0]["lon"]))
    await message.delete()

@app.on_message(filters.user(botowner) & filters.command("mammt", ["/", ".", "-"]))
async def statget(client, message):
    await app.send_sticker(message.chat.id,"CAACAgQAAxkBAAEB15dkfM1XcNpfh0fv8WNItDrMsWzw9AAC_Q0AAtBk6VMgJdJcbHpBRy8E")
    await message.delete()
    
app.run()



