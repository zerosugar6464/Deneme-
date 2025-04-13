import asyncio
import json
from telethon import TelegramClient, events
from telethon.tl.functions.messages import SendReactionRequest
from telethon.tl.types import ReactionEmoji
from telethon.errors import FloodWaitError
from telebot.async_telebot import AsyncTeleBot
from telebot import types
import os
import random
from telethon.tl.types import ChannelParticipantsAdmins
import random
from telethon.tl.types import DocumentAttributeFilename
import sys
import subprocess
import pkg_resources
import time
import os
import asyncio
import json
from telethon import TelegramClient, events
from telethon.tl.functions.messages import SendReactionRequest
from telethon.tl.types import ReactionEmoji
from telethon.errors import FloodWaitError
from telebot.async_telebot import AsyncTeleBot
from telebot import types
import os
import random
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.tl.types import DocumentAttributeFilename
import sys
import subprocess
import pkg_resources
import time
from collections import defaultdict
from telethon import TelegramClient, events, Button
import asyncio
import time
from telethon.errors import SessionPasswordNeededError, PhoneCodeInvalidError
import asyncio
import os
import json
import datetime
import requests
import asyncio
import json
from telethon import TelegramClient, events
from telethon.tl.functions.messages import SendReactionRequest
from telethon.tl.types import ReactionEmoji
from telethon.errors import FloodWaitError
from telebot.async_telebot import AsyncTeleBot
from telebot import types
import os
import random
from telethon.tl.types import ChannelParticipantsAdmins
import random
from telethon.tl.types import DocumentAttributeFilename
import sys
import subprocess
import pkg_resources
import time
import os
import asyncio
import json
from telethon import TelegramClient, events
from telethon.tl.functions.messages import SendReactionRequest
from telethon.tl.types import ReactionEmoji
from telethon.errors import FloodWaitError
from telebot.async_telebot import AsyncTeleBot
from telebot import types
import os
import random
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.tl.types import DocumentAttributeFilename
import sys
import subprocess
import pkg_resources
import time
from youtube_dl import YoutubeDL
from googletrans import Translator
from telethon.tl.functions.users import GetFullUserRequest
from telethon.errors import MessageIdInvalidError
from collections import defaultdict
from telethon import TelegramClient, events
from yt_dlp import YoutubeDL
import os
from telethon import TelegramClient, events
from googletrans import Translator
try:
  from deep_translator import GoogleTranslator
except:
  print("Eksik Pip Bulundu. Yükleniyor...")
  os.system("pip install deep-translator --break-system-packages")
os.system('cls' if os.name == 'nt' else 'clear') 

OWNER_ID = "7525624006"
API_ID = "20824282"
API_HASH = "5c49d99b5bb9e41c9b8ada4f826989ef" 
BOT_TOKEN = "7336757348:AAGW8yt7dNW50odjiUDNhrKtQ32zSMbC2tM"
client = TelegramClient('Silataggerbot', API_ID, API_HASH)
bot = AsyncTeleBot(BOT_TOKEN)

SUBSCRIPTIONS_FILE = "subscriptions.json"
if os.path.exists(SUBSCRIPTIONS_FILE):
    with open(SUBSCRIPTIONS_FILE, 'r') as f:
        subscriptions = json.load(f)
else:
    subscriptions = {}

def save_subscriptions():
    with open(SUBSCRIPTIONS_FILE, 'w') as f:
        json.dump(subscriptions, f)

if not os.path.exists("sessions"):
    os.makedirs("sessions")

USERS_FILE = "user_states.json"
if os.path.exists(USERS_FILE):
    with open(USERS_FILE, 'r') as f:
        logged_users = json.load(f)
else:
    logged_users = {}

def save_users():
    with open(USERS_FILE, 'w') as f:
        json.dump(logged_users, f)

class UserSession:
    def __init__(self):
        self.state = None
        self.phone = None
        self.client = None
        self.code_request = None
        self.last_code = None
        self.message_id = None

user_sessions = {}
user_states = {}
user_settings = {}
tagging = {}
reaction_status = {}
reaction_emoji = {}
filters = {}
afk_users = {}
chatbot_enabled = {}
welcome_enabled = {}
welcome_messages = {}
goodbye_enabled = {}
goodbye_messages = {}
sudo_users = []
translator = Translator()
filters = {}
welcome_enabled = {}
goodbye_enabled = {}
welcome_messages = {}
goodbye_messages = {}
chatbot_enabled = {}


def check_subscription(user_id):
    str_user_id = str(user_id)
    if str_user_id not in subscriptions:
        return False
    expiry_date = datetime.datetime.strptime(subscriptions[str_user_id], "%Y-%m-%d")
    return datetime.datetime.now() <= expiry_date

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    user = await event.get_sender()
    message = await event.reply("**🧸 Lütfen Bekleyin.**")
    await asyncio.sleep(2)
    await message.edit("**🌟 Lütfen Bekleyin..**")
    await asyncio.sleep(2)
    await message.edit("**♾️ Lütfen Bekleyin...**")
    await asyncio.sleep(2)
    await main_menu(message, user)

async def main_menu(event, user):
    user_mention = f"[{user.first_name}](tg://user?id={user.id})"
    buttons = [
        [Button.inline("📘 Komutlar", f"commands_{user.id}")],
        [Button.inline("🔐 Giriş Yap", f"login_{user.id}"), Button.inline("🔑 Çıkış Yap", f"logout_{user.id}")],
        [Button.inline("❕ Uyarılar", f"warnings_{user.id}"), Button.inline("🔺 Versiyon", f"version_{user.id}")],
        [Button.url("🍂 Destek", "https://t.me/rlonch")],
        [Button.url("🎩 Gizlilik Ve Şartlar", "https://telegra.ph/Gizlilik-Politikas%C4%B1--Ko%C5%9Fullar%C4%B1-03-10")]
    ]
    await event.edit(
        f"**👋🏻 Merhaba {user_mention}\n\n"
        "🥀 Ben Çok gelişmiş + fonksiyonlu Telegram Lion User Botuyum, "
        "Benim sayemde Telegram hesabını yönetebilir gruplarını daha da aktive edebilirsin !\n\n"
        "❗ Komutlarım Ve destek için Lütfen aşşağıdakı butonları kullanın "
        "aksi takdirde size cevap vermem keyifli kullanımlar :)**",
        buttons=buttons,
        parse_mode='md'
    )

@client.on(events.CallbackQuery(pattern=r"commands_(\d+)"))
async def commands(event):
    user_id = int(event.pattern_match.group(1))
    if event.sender_id != user_id:
        return
    buttons = [
        [Button.inline("🎳 Oyun Komutları", f"game_commands_{user_id}"), Button.inline("💕 Etiket Komutları", f"tag_commands_{user_id}")],
        [Button.inline("🎨 Eğlence Komutları", f"fun_commands_{user_id}")],
        [Button.inline("🔮 Diğer Komutlar", f"other_commands_{user_id}"), Button.inline("👨‍💻 Sudo", f"sudo_commands_{user_id}")],
        [Button.inline("🔙 Geri", f"back_{user_id}")]
    ]
    await event.edit("**Lütfen Bir Buton Seçin :))**", buttons=buttons)

@client.on(events.CallbackQuery(pattern=r"warnings_(\d+)"))
async def warnings(event):
    user_id = int(event.pattern_match.group(1))
    if event.sender_id != user_id:
        return
    warning_text = (
        "📜 **Lütfen Bu Uyarıları Dikkate Alın:**\n\n"
        "• Tek cihazda bir oturum açın: Her telefon için yalnızca bir oturum açmanız önerilir.\n\n"
        "• Hesap yaşı önemli: Yeni açılmış veya sahte hesapların silinme riski bulunmaktadır. "
        "Hesabınızın en az 1 hafta önce oluşturulmuş olmasına özen gösterin.\n\n"
        "• Oturum anahtarınızı koruyun: Güvenliğiniz için oturum anahtarınızı kimseyle paylaşmayın.\n\n"
        "• Güvenlik bildirimini onaylayın: Oturum açtıktan sonra telefonunuza bir güvenlik bildirimi gelecektir. "
        "Bu bildirimi aldığınızda, \"Evet, bu benim\" seçeneğini seçerek onaylayın.\n\n"
    )
    buttons = [[Button.inline("🔙 Geri", f"back_{user_id}")]]
    await event.edit(warning_text, buttons=buttons)

@client.on(events.CallbackQuery(pattern=r"version_(\d+)"))
async def version(event):
    user_id = int(event.pattern_match.group(1))
    if event.sender_id != user_id:
        return
    version_text = "𝚅𝙴𝚁𝚂𝚈𝙾𝙽𝚂 : 01.02.01\n\n"
    buttons = [[Button.inline("🔙 Geri", f"back_{user_id}")]]
    await event.edit(version_text, buttons=buttons)

@client.on(events.CallbackQuery(pattern=r"back_(\d+)"))
async def back_to_main(event):
    user_id = int(event.pattern_match.group(1))
    if event.sender_id != user_id:
        return
    user = await event.get_sender()
    if user_id in user_sessions:
        session = user_sessions[user_id]
        if session.client:
            await session.client.disconnect()
        user_sessions[user_id] = UserSession()
    await main_menu(event, user)

@client.on(events.CallbackQuery(pattern=r"game_commands_(\d+)"))
async def game_commands(event):
    user_id = int(event.pattern_match.group(1))
    if event.sender_id != user_id:
        return
    game_text = (
        "**🎮 Oyun Komutları :**\n\n"
        "🎲 `.zarat` - Zar animasyonu atar\n"
        "🎯 `.dart` - Dart atışı yapar\n"
        "⚽️ `.futbol` - Futbol oyunu oynatır\n"
        "🏀 `.basket` - Basket atışı yaptırır\n"
        "🎳 `.bowling` - Bowling oyunu başlatır\n"
        "🎲 `.zar` - Zar atışı gerçekleştirir\n"
        "❓ `.dsoru` - Doğruluk sorusu sorar\n"
        "❗️ `.csoru` - Cesaret sorusu sorar\n"
        "💘 `.eros` - Aşk eşleştirmesi yapar\n"
        "💭 `.soz` - Rastgele güzel söz paylaşır\n"
        "👊 `.slap` - Şaka amaçlı vurma efekti\n"
        "💋 `.kiss` - Öpücük gönderme efekti\n"
        "🎰 `.slot` - Şans oyunu başlatır"
    )
    buttons = [[Button.inline("🔙 Geri", f"commands_{user_id}")]]
    await event.edit(game_text, buttons=buttons)

@client.on(events.CallbackQuery(pattern=r"tag_commands_(\d+)"))
async def tag_commands(event):
    user_id = int(event.pattern_match.group(1))
    if event.sender_id != user_id:
        return
    tag_text = (
        "**🎀 Etiket Komutları :**\n\n"
        "🎯 `.etiket` - Gruptaki tüm üyeleri sırayla etiketler\n"
        "🪅 `.setetiket` - Özel mesajla etiketleme yapar\n"
        "✨ `.tag` - İsimleri yan yana dizerek etiketler\n"
        "⚡️ `.utag` - Hızlı toplu etiketleme yapar\n"
        "🌟 `.etag` - Emojili etiketleme yapar\n"
        "👑 `.atag` - Adminleri özel şekilde etiketler\n"
        "📡 `.cagir` - Oyun çağrısı gönderir\n"
        "🎭 `.vtag` - Doğruluk Cesaret etiketlemesi yapar.\n"
        "♦ `.cancel` - Etiketleme işlemini durdurur"
    )
    buttons = [[Button.inline("🔙 Geri", f"commands_{user_id}")]]
    await event.edit(tag_text, buttons=buttons)

@client.on(events.CallbackQuery(pattern=r"fun_commands_(\d+)"))
async def fun_commands(event):
    user_id = int(event.pattern_match.group(1))
    if event.sender_id != user_id:
        return
    fun_text = (
        "**🪅 Eğlence Komutları  : **\n\n"
        "🎵 `.bul` - İstenen müziği indirir ve gönderir\n"
        "🎥 `.vbul` - İstenen videoyu indirir ve gönderir\n"
        "👮 `.admins` - Gruptaki yöneticileri listeler\n"
        "🤖 `.bots` - Gruptaki botları gösterir\n"
        "ℹ️ `.bilgi` - Grup bilgilerini gösterir\n"
        "🆔 `.id` - Kullanıcı ID'sini verir\n"
        "🔄 `.reload` - Botu yeniden başlatır\n"
        "✅ `.approve` - AFK mesajını ayarlar\n"
        "💤 `.afk on/off` - AFK modunu açar/kapatır\n"
        "⭐️ `.st on/off` - Otomatik tepkiyi açar/kapatır\n"
        "🔰 `.strove` - Tepki emojisini değiştirir\n"
        "🛠 `.alive` - Bot durumunu kontrol eder"
    )
    buttons = [[Button.inline("🔙 Geri", f"commands_{user_id}")]]
    await event.edit(fun_text, buttons=buttons)

@client.on(events.CallbackQuery(pattern=r"other_commands_(\d+)"))
async def other_commands(event):
    user_id = int(event.pattern_match.group(1))
    if event.sender_id != user_id:
        return
    other_text = (
        "**☃️ Diğer Komutlar :**\n\n"
        "📝 `.ttf` - Metni dosyaya dönüştürür\n"
        "⚠️ `.hata` - Kod hatalarını tespit eder\n"
        "🔄 `.cevir` - Metin çevirisi yapar\n"
        "📖 `.ac` - Dosya içeriğini okur\n"
        "📊 `.kurulum` - Kullanıcı bilgilerini gösterir\n"
        "🤖 `.chatbot on/off` - Yapay zeka sohbetini açar/kapatır\n"
        "⚙️ `.filter` - Otomatik cevap filtresi ekler\n"
        "🗑 `.delfilter` - Eklenen filtreyi siler\n"
        "🎯 `.wtc on/off` - Hoşgeldin mesajını açar/kapatır\n"
        "✨ `.wtcfilters` - Hoşgeldin mesajını düzenler\n"
        "🗑 `.delwtcfilters` - Hoşgeldin mesajını siler\n"
        "👋 `.hwtrx on/off` - Hoşçakal mesajını açar/kapatır\n"
        "💫 `.hwtrxfilters` - Hoşçakal mesajını düzenler\n"
        "🗑 `.delhwtrxfilters` - Hoşçakal mesajını siler"
    )
    buttons = [[Button.inline("🔙 Geri", f"commands_{user_id}")]]
    await event.edit(other_text, buttons=buttons)

@client.on(events.CallbackQuery(pattern=r"sudo_commands_(\d+)"))
async def sudo_commands(event):
    user_id = int(event.pattern_match.group(1))
    if event.sender_id != user_id:
        return
    if event.sender_id != OWNER_ID and str(event.sender_id) not in sudo_users:
        buttons = [[Button.inline("🔙 Geri", f"commands_{user_id}")]]
        await event.edit("**🔻 Üzgünüm Sudo olamadığınız için bu bölümü görüntüleyemezsiniz !**", buttons=buttons)
        return
    sudo_text = (
        "**👑 Owner Komutları:**\n\n"
        "🔰 `/duyuru` - kullaniciya / gruba duyuru yapar.\n"
        "🔰 `/sudo` - Kullanıcıya sudo yetkisi verir\n"
        "🔰 `/delsudo` - Kullanıcının sudo yetkisini alır\n"
        "🔰 `/sudolist` - Sudo kullanıcılarını listeler\n"
        "🔰 `/ban` - Kullanıcıyı bottan yasaklar\n"
        "🔰 `/unban` - Kullanıcının yasağını kaldırır\n"
        "🔰 `/mute` - Kullanıcıyı susturur\n"
        "🔰 `/unmute` - Kullanıcının susturmasını kaldırır\n"
        "🔰 `/istatik` - Bot istatistiklerini gösterir\n"
        "🔰 `/abonelik` - Kullanıcıya abonelik verir\n"
        "🔰 `/unabonelik` - Kullanıcının aboneliğini alır"
    )
    buttons = [[Button.inline("🔙 Geri", f"commands_{user_id}")]]
    await event.edit(sudo_text, buttons=buttons)

@client.on(events.CallbackQuery(pattern=r"login_(\d+)"))
async def login(event):
    user_id = int(event.pattern_match.group(1))
    if event.sender_id != user_id:
        return
    str_user_id = str(user_id)
    if not check_subscription(user_id):
        buttons = [
            [Button.url("👨‍💻 Kurucu", "t.me/rlonch")],
            [Button.inline("🔙 Geri", f"back_{user_id}")]
        ]
        await event.edit(
            "**🔻 Üzgünüm Aboneliğiniz yok. Lütfen abonelik almak için [Kurucu](t.me/rlonch)'yla iletişime geçin**",
            buttons=buttons,
            parse_mode='md',
            link_preview=False
        )
        return
    if str_user_id in logged_users:
        error_message = "**🔶 Zaten giriş yapmışsınız! Önce çıkış yapmalısınız.**"
        buttons = [[Button.inline("🔙 Geri", f"back_{user_id}")]]
        await event.edit(error_message, buttons=buttons)
        return
    login_text = (
        "**🗯 Lütfen Telefon Numaranızı +90 Şeklinde girin. Size doğrulama kodu gelecek ve bota  1 2 3 4 5 bu şekilde doğrulama kodunu gönderin.**\n\n"
        "**♦ Örnek : +90551xxxxxx**\n"
        "**ve ayrıca eğer iki adımlı doğrulamanız varsa kapatın aksi takdirde bot hesaba giremez !**"
    )
    buttons = [[Button.inline("🔙 Geri", f"back_{user_id}")]]
    await event.edit(login_text, buttons=buttons)
    if user_id not in user_sessions:
        user_sessions[user_id] = UserSession()
    user_sessions[user_id].state = "waiting_phone"
    user_sessions[user_id].message_id = event.message_id

@client.on(events.CallbackQuery(pattern=r"logout_(\d+)"))
async def logout(event):
    user_id = int(event.pattern_match.group(1))
    if event.sender_id != user_id:
        return
    str_user_id = str(user_id)
    if str_user_id in logged_users:
        session_file = os.path.join("sessions", f"user_{user_id}.session")
        try:
            if os.path.exists(session_file):
                os.remove(session_file)
            del logged_users[str_user_id]
            save_users()
            success_message = "**🔷 Başarıyla çıkış yapıldı!**"
            buttons = [[Button.inline("🔙 Geri", f"back_{user_id}")]]
            await event.edit(success_message, buttons=buttons)
        except Exception as e:
            error_message = f"**🔶 Çıkış yapılırken bir hata oluştu: {str(e)}**"
            buttons = [[Button.inline("🔙 Geri", f"back_{user_id}")]]
            await event.edit(error_message, buttons=buttons)
    else:
        error_message = "**🔶 Zaten giriş yapılmamış!**"
        buttons = [[Button.inline("🔙 Geri", f"back_{user_id}")]]
        await event.edit(error_message, buttons=buttons)

@client.on(events.NewMessage)
async def handle_messages(event):
    user_id = event.sender_id
    str_user_id = str(user_id)
    if user_id not in user_sessions or not user_sessions[user_id].state:
        return
    session = user_sessions[user_id]
    message = event.message.text.strip()
    buttons = [[Button.inline("🔙 Geri", f"back_{user_id}")]]
    if session.state == "waiting_phone":
        if not message.startswith("+"):
            await event.respond("**🔶 Lütfen telefon numaranızı +90 formatında girin!**", buttons=buttons)
            return
        try:
            session_file = os.path.join("sessions", f"user_{user_id}")
            client = TelegramClient(session_file, API_ID, API_HASH)
            await client.connect()
            code_request = await client.send_code_request(message)
            session.state = "waiting_code"
            session.phone = message
            session.client = client
            session.code_request = code_request
            session.last_code = None
            await event.respond("**🔷 Doğrulama kodu telefonunuza gönderildi.\nLütfen kodu gönderin.**", buttons=buttons)
        except Exception as e:
            await event.respond(f"**🔶 Bir hata oluştu: {str(e)}**", buttons=buttons)
            if session.client:
                await session.client.disconnect()
            user_sessions[user_id] = UserSession()
    elif session.state == "waiting_code":
        if session.last_code == message:
            return
        session.last_code = message
        try:
            try:
                await session.client.sign_in(session.phone, message)
                logged_users[str_user_id] = {
                    "phone": session.phone,
                    "login_time": str(datetime.datetime.now())
                }
                save_users()
                await event.respond("**🔷 Başarıyla giriş yapıldı!**", buttons=buttons)
                asyncio.create_task(start_client(session.client, user_id))
                user_sessions[user_id] = UserSession()
            except PhoneCodeInvalidError:
                await event.respond("**🔶 Geçersiz kod. Lütfen tekrar deneyin.**", buttons=buttons)
            except SessionPasswordNeededError:
                await event.respond("**🔶 İki faktörlü doğrulama aktif. Lütfen önce bunu devre dışı bırakın.**", buttons=buttons)
                if session.client:
                    await session.client.disconnect()
                user_sessions[user_id] = UserSession()
        except Exception as e:
            await event.respond(f"**🔶 Bir hata oluştu: {str(e)}**", buttons=buttons)
            if session.client:
                await session.client.disconnect()
            user_sessions[user_id] = UserSession()

@client.on(events.NewMessage(pattern=r'/abonelik (\d+) -(\d+) (ay|yıl|gün)$'))
async def add_subscription(event):
    if event.sender_id != OWNER_ID:
        return
    user_id, duration, period = event.pattern_match.groups()
    duration = int(duration)
    if period == "ay":
        delta = datetime.timedelta(days=30 * duration)
    elif period == "yıl":
        delta = datetime.timedelta(days=365 * duration)
    else:
        delta = datetime.timedelta(days=duration)
    expiry_date = datetime.datetime.now() + delta
    subscriptions[user_id] = expiry_date.strftime("%Y-%m-%d")
    save_subscriptions()
    await event.reply(f"**✅ {user_id} ID'li kullanıcıya {duration} {period} abonelik eklendi.\nBitiş Tarihi: {expiry_date.strftime('%Y-%m-%d')}**")

@client.on(events.NewMessage(pattern=r'/unabonelik (\d+) -(\d+) (ay|yıl|gün)$'))
async def remove_subscription(event):
    if event.sender_id != OWNER_ID:
        return
    user_id, duration, period = event.pattern_match.groups()
    duration = int(duration)
    if user_id not in subscriptions:
        await event.reply(f"**❌ {user_id} ID'li kullanıcının aktif aboneliği bulunmuyor.**")
        return
    current_expiry = datetime.datetime.strptime(subscriptions[user_id], "%Y-%m-%d")
    if period == "ay":
        delta = datetime.timedelta(days=30 * duration)
    elif period == "yıl":
        delta = datetime.timedelta(days=365 * duration)
    else:
        delta = datetime.timedelta(days=duration)
    new_expiry = current_expiry - delta
    if new_expiry <= datetime.datetime.now():
        del subscriptions[user_id]
        await event.reply(f"**❌ {user_id} ID'li kullanıcının aboneliği tamamen silindi.**")
    else:
        subscriptions[user_id] = new_expiry.strftime("%Y-%m-%d")
        await event.reply(f"**✅ {user_id} ID'li kullanıcının aboneliğinden {duration} {period} düşüldü.\nYeni Bitiş Tarihi: {new_expiry.strftime('%Y-%m-%d')}**")

async def check_and_logout_expired(user_id):
    str_user_id = str(user_id)
    if str_user_id in logged_users and not check_subscription(user_id):
        session_file = os.path.join("sessions", f"user_{user_id}.session")
        try:
            if os.path.exists(session_file):
                os.remove(session_file)
            del logged_users[str_user_id]
            save_users()
            buttons = [
                [Button.url("👨‍💻 Kurucu", "t.me/rlonch")],
                [Button.inline("🔙 Geri", f"back_{user_id}")]
            ]
            await client.send_message(user_id, 
                "**🔻 Abonelik süreniz sona erdi. Yeni abonelik almak için [Kurucu](t.me/rlonch) ile iletişime geçin.**",
                buttons=buttons,
                parse_mode='md'
            )
            if user_id in user_sessions:
                session = user_sessions[user_id]
                if session.client:
                    await session.client.disconnect()
                user_sessions[user_id] = UserSession()
            return True
        except Exception as e:
            print(f"Abonelik kontrolü hatası: {e}")
    return False

def check_subscription(user_id):
    str_user_id = str(user_id)
    if str_user_id not in subscriptions:
        return False
    expiry_date = datetime.datetime.strptime(subscriptions[str_user_id], "%Y-%m-%d")
    if datetime.datetime.now() > expiry_date:
        del subscriptions[str_user_id]
        save_subscriptions()
        return False
    return True

async def start_client(client, user_id):
    @client.on(events.NewMessage(pattern=r"\.alive"))
    async def alive_message(event):
        try:
            msg = await event.respond("**Kontrol ediliyor...**")
            await asyncio.sleep(1)
            await msg.edit("`Huh !` **LionUser** `beni çağırıyor 🌸 < Bu senin için 🥺 ...`")
            await event.delete()
        except Exception as e:
            await event.respond(f"❌ **Hata oluştu: {str(e)}**")
            await event.delete()




    @client.on(events.NewMessage(pattern=r"\.etiket(?: |$)(.*)"))
    async def tag_all(event):
        if event.is_group:
            if event.fwd_from:
                return

            chat_id = event.chat_id
            tagging[chat_id] = True
            message = event.pattern_match.group(1) if event.pattern_match.group(1) else ""
            
            try:
                await event.edit(f"**🪅 Bu Gruptaki Üyeleri Etiketlemeye Başlıyorum**")
            except:
                pass

            chat = await event.get_input_chat()
            async for user in client.iter_participants(chat):
                if not tagging.get(chat_id):
                    break
                if user.bot:
                    continue
                    
                try:
                    await event.client.send_message(event.chat_id, f"**{message}** [{user.first_name}](tg://user?id={user.id})")
                    await asyncio.sleep(3)
                except Exception as e:
                    print(f"Etiketleme hatası: {str(e)}")
                    continue

    @client.on(events.NewMessage(pattern=r"\.cancel"))
    async def cancel_tagging(event):
        chat_id = event.chat_id
        if chat_id in tagging:
            tagging[chat_id] = False
            try:
                await event.delete()
            except:
                pass

    @client.on(events.NewMessage(pattern=r"\.setetiket(?: |$)(.*)"))
    async def tag_all(event):
        if event.is_group:
            if event.fwd_from:
                return

            chat_id = event.chat_id
            message = event.pattern_match.group(1)
            
            if not message:
                try:
                    await event.edit("**⚠️ Lütfen bir mesaj belirtin!**")
                    return
                except:
                    pass
                    
            tagging[chat_id] = True
            
            try:
                await event.edit(f"**🪅 Bu Gruptaki Üyeleri Etiketlemeye Başlıyorum**")
            except:
                pass

            emojis = ["🪅","🥀","🌹","🌿","🌺","🌻","🌼","❤️‍🔥","☘️","🍃","🌾","🪻","🏵️","💮","🪷","🌷","🌟","🍂","💗","💞","💕","💟","❣️","💜","💖","💘","💜","🤍","🩵","🖤","💙","🤍","❤️","🔥","💚","🩵","🩵","💔","❤️‍🔥","💋","🫀","🫁","🗣️","🌴","🍃","🍀","🍀","🌲","🌿","🌱"]

            chat = await event.get_input_chat()
            async for user in client.iter_participants(chat):
                if not tagging.get(chat_id):
                    break
                if user.bot:
                    continue
                    
                try:
                    emoji = random.choice(emojis)
                    await event.client.send_message(event.chat_id, f"**{message}** [{emoji}](tg://user?id={user.id})")
                    await asyncio.sleep(3)
                except Exception as e:
                    print(f"Etiketleme hatası: {str(e)}")
                    continue

    @client.on(events.NewMessage(pattern=r"\.cancel"))
    async def cancel_tagging(event):
        chat_id = event.chat_id
        if chat_id in tagging:
            tagging[chat_id] = False
            try:
                await event.delete()
            except:
                pass



    @client.on(events.NewMessage(pattern=r"\.cagir(?: |$)(.*)"))
    async def call_users(event):
        if event.is_group:
            if event.fwd_from:
                return

            chat_id = event.chat_id
            message = event.pattern_match.group(1)
            
            random_calls = [
                "Oyun başlıyor oyuna gelsene ;)",
                "Oyun sensiz çekilmiyor gel artık",
                "Seni aramızda görmek istiyoruz",
                "Oyuna katılmanı bekliyoruz", 
                "Oyun başladı seni bekliyoruz",
                "Hadi gel eğlenceyi kaçırma",
                "Senin için bir sandalye ayırdık",
                "Oyunda bir kişi eksik, o da sensin",
                "Herkes hazır seni bekliyoruz",
                "Seni de oyunda görmek isteriz",
                "Oyuna katıl ve eğlenceye ortak ol",
                "Gel de biraz eğlenelim",
                "Oyun arkadaşı arıyoruz",
                "Takımımıza katılmak ister misin?",
                "Seni de aramızda görmek istiyoruz",
                "Hadi gel birlikte oynayalım",
                "Oyun daha eğlenceli olsun",
                "Seni bekliyoruz, hadi gel",
                "Biraz eğlenceye ne dersin?",
                "Oyun zamanı geldi çattı",
                "Hadi gel vakit kaybetme",
                "Eğlence başlasın",
                "Oyun arkadaşımız ol",
                "Seni de bekliyoruz",
                "Hadi katıl aramıza",
                "Oyunda yerini al",
                "Eğlenceyi kaçırma",
                "Gel de renk kat oyuna",
                "Sensiz olmaz bu oyun",
                "Hadi gel başlayalım",
                "Oyun vakti geldi",
                "Seni de oyunda görelim",
                "Katıl ve eğlenceye ortak ol",
                "Oyun seni bekliyor",
                "Hadi durma gel",
                "Eğlencenin tadı sensiz çıkmaz",
                "Oyuna renk katmaya ne dersin?",
                "Seni de aramızda görmek güzel olur",
                "Gel de şenlensin ortalık",
                "Hadi eğlenceye katıl",
                "Oyun başlıyor katılsana",
                "Seni de bekliyoruz burada",
                "Hadi gel oyuna başlayalım",
                "Eğlence sensiz olmaz",
                "Oyun arkadaşı arıyoruz hadi gel",
                "Seni de oyunda görmek isteriz",
                "Katıl ve eğlenceyi yakala",
                "Hadi gel başlayalım",
                "Oyun vakti geldi çattı",
                "Seni bekliyoruz oyunda"
            ]

            tagging[chat_id] = True
            
            try:
                await event.edit("**🎮 Aktif kullanıcıları oyuna çağırıyorum...**")
            except:
                pass

            chat = await event.get_input_chat()
            async for user in client.iter_participants(chat):
                if not tagging.get(chat_id):
                    break
                if user.bot:
                    continue
                    
                try:
                    if message:
                        await event.client.send_message(event.chat_id, f"**{message}** [{user.first_name}](tg://user?id={user.id})")
                    else:
                        random_message = random.choice(random_calls)
                        await event.client.send_message(event.chat_id, f"**{random_message}** [{user.first_name}](tg://user?id={user.id})")
                    await asyncio.sleep(3)
                except Exception as e:
                    print(f"Etiketleme hatası: {str(e)}")
                    continue

    @client.on(events.NewMessage(pattern=r"\.cancel"))
    async def cancel_tagging(event):
        chat_id = event.chat_id
        if chat_id in tagging:
            tagging[chat_id] = False
            try:
                await event.delete()
            except:
                pass



    @client.on(events.NewMessage(pattern=r"\.atag(?: |$)(.*)"))
    async def tag_admins(event):
        if event.is_group:
            if event.fwd_from:
                return

            chat_id = event.chat_id
            message = event.pattern_match.group(1)
            
            if not message:
                try:
                    await event.edit("**🪅 Lütfen Bir Mesaj belirtin !**")
                    return
                except:
                    return
            
            tagging[chat_id] = True
            
            try:
                await event.delete()
            except:
                pass

            chat = await event.get_input_chat()
            async for user in client.iter_participants(chat, filter=ChannelParticipantsAdmins):
                if not tagging.get(chat_id):
                    break
                if user.bot:
                    continue
                    
                try:
                    await event.client.send_message(event.chat_id, f"{message} [{user.first_name}](tg://user?id={user.id})")
                    await asyncio.sleep(3)
                except Exception as e:
                    print(f"Etiketleme hatası: {str(e)}")
                    continue



    @client.on(events.NewMessage(pattern=r"\.utag(?: |$)(.*)"))
    async def mass_tag(event):
        if event.is_group:
            if event.fwd_from:
                return

            chat_id = event.chat_id
            message = event.pattern_match.group(1)
            
            tagging[chat_id] = True
            
            try:
                await event.edit("**🎯 Üyeleri Toplu Etiketlemeye Başlıyorum**")
            except:
                pass

            chat = await event.get_input_chat()
            participants = []
            
            async for user in client.iter_participants(chat):
                if not user.bot and user.first_name:
                    participants.append(user)
            
            for i in range(0, len(participants), 5):
                if not tagging.get(chat_id):
                    break
                    
                group = participants[i:i+5]
                mention_text = message + " " if message else ""
                
                mentions = []
                for user in group:
                    mentions.append(f"[{user.first_name}](tg://user?id={user.id})")
                
                mention_text += " ".join(mentions)
                
                try:
                    await event.client.send_message(event.chat_id, mention_text)
                    await asyncio.sleep(2)
                except Exception as e:
                    continue

    @client.on(events.NewMessage(pattern=r"\.cancel"))
    async def cancel_tagging(event):
        chat_id = event.chat_id
        if chat_id in tagging:
            tagging[chat_id] = False
            try:
                await event.delete()
            except:
                pass



    @client.on(events.NewMessage(pattern=r"\.tag(?: |$)(.*)"))
    async def tag_all(event):
        if event.is_group:
            if event.fwd_from:
                return

            chat_id = event.chat_id
            tagging[chat_id] = True
            message = event.pattern_match.group(1) if event.pattern_match.group(1) else ""
            
            try:
                await event.edit("**🪅 Bu Gruptaki Üyeleri Etiketlemeye Başlıyorum**")
            except:
                pass

            chat = await event.get_input_chat()
            async for user in client.iter_participants(chat):
                if not tagging.get(chat_id):
                    break
                if user.bot:
                    continue
                    
                try:
                    await event.client.send_message(event.chat_id, f"**{message}** [{user.first_name}](tg://user?id={user.id})")
                    await asyncio.sleep(3)
                except Exception as e:
                    print(f"Etiketleme hatası: {str(e)}")
                    continue

    @client.on(events.NewMessage(pattern=r"\.cancel"))
    async def cancel_tagging(event):
        chat_id = event.chat_id
        if chat_id in tagging:
            tagging[chat_id] = False
            try:
                await event.delete()
            except:
                pass

    @client.on(events.NewMessage(pattern=r"\.stag"))
    async def stag(event):
        if event.is_group:
            if event.fwd_from:
                return
                
            chat_id = event.chat_id
            tagging[chat_id] = True

            poems = [
                "Gözlerinde saklı kaldı yarınlar\nYüreğimde bir sen varsın hep canlı\nSensiz geçen günler hepsi karanlık",
                
                "Ay ışığı vurunca yüzüne\nGece bile gündüz olur gözümde\nSen varsan her şey güzel özümde",
                
                "Rüzgar esse saçların dans eder\nGülüşünle dünyam renk değişir\nSensiz her yer eksik gelir bana",
                
                "Yağmur damlaları gibi temiz\nÇiçek kokusu gibi narin\nSenin varlığın öyle özel",
                
                "Denizin mavisi gözlerinde\nGüneşin sıcağı kalbinde\nBaharın tazeliği özünde",
                
                "Her sabah yeni umutlarla\nSeni düşünerek uyanırım\nGünüm seninle güzelleşir",
                
                "Gökyüzü kadar sonsuz sevgim\nDağlar kadar yüce özlemim\nSen benim en güzel şiirim",
                
                "Bulutlar gibi özgür ruhun\nKuşlar gibi neşeli sesin\nÇiçekler gibi nazlı halin",
                
                "Gecenin sessizliğinde\nYıldızlar bile seni anlatır\nAy ışığı seni hatırlatır",
                
                "Kalbin güzelliği yüzünde\nSevginin derinliği sözünde\nMutluluk var her gülüşünde",
                
                "Zaman durur seni görünce\nNefesim kesilir gülünce\nDünya güzelleşir sevince",
                
                "Bahar çiçekleri açar içimde\nKuşlar şarkı söyler dilimde\nSen varsın her anımda yine",
                
                "Deniz dalgaları gibi huzurlu\nSabah güneşi gibi umutlu\nSenin varlığın çok mutlu",
                
                "Gökkuşağı renkli hayaller\nSeninle geçen tüm günler\nKalbimde açan çiçekler",
                
                "Yıldızlar kadar parlak gözlerin\nMelekler kadar temiz özün\nŞiir gibi güzel sözlerin",
                
                "Sonbahar yaprakları gibi nazlı\nİlkbahar çiçekleri gibi tatlı\nSenin her halin ayrı anlam",
                
                "Gece karanlığında ay gibi\nSabah güneşi gibi sıcak\nSen benim en güzel şarkım",
                
                "Rüzgarın getirdiği esinti\nDenizin verdiği huzur gibi\nSenin varlığın öyle değerli",
                
                "Yağmur sonrası toprak kokusu\nBahar sabahı çiçek açışı\nSenin gülüşün öyle doğal",
                
                "Martıların özgür uçuşu\nDalgaların sahile vuruşu\nSenin ruhun öyle özgür",
                
                "Kar taneleri gibi benzersiz\nGökyüzü gibi sınırsız\nSenin sevgin öyle eşsiz",
                
                "Ormanın derinliklerinde\nKuşların şarkılarında\nSeni bulurum her anda",
                
                "Güneşin doğuşu gibi\nUmut dolu her sabah\nSeninle başlar yeni gün",
                
                "Yıldızların parıltısı\nAyın ışıltısı gibi\nSen hep ışık saçarsın",
                
                "Çiçeklerin kokusu gibi\nBaharın gelişi gibi\nSen hep yeni umut verirsin",
                
                "Nehir akışı gibi sakin\nDağ duruşu gibi heybetli\nSenin varlığın öyle güçlü",
                
                "Gökyüzünün mavisi gibi\nDenizin derinliği gibi\nSenin sevgin sonsuz",
                
                "Kuş cıvıltıları gibi neşeli\nÇiçek açışı gibi renkli\nSenin dünyam öyle güzel",
                
                "Yağmur damlaları gibi saf\nBulut beyazı gibi temiz\nSenin kalbin öyle pak",
                
                "Güneş batımı gibi huzurlu\nŞafak vakti gibi umutlu\nSeninle her an özel",
                
                "Sonbahar yaprakları gibi\nRenkli ve özgür ruhun\nHer halinle güzelsin",
                
                "Dağ zirvesi gibi yüce\nVadi yeşili gibi canlı\nSenin sevgin öyle derin",
                
                "Göl yüzeyi gibi durgun\nOrman yeşili gibi canlı\nSenin varlığın huzur verir",
                
                "Yıldız kayması gibi özel\nGece sessizliği gibi derin\nSenin her anın değerli",
                
                "Bahar yağmuru gibi bereketli\nYaz güneşi gibi sıcak\nSenin sevgin öyle zengin",
                
                "Deniz dalgası gibi özgür\nKuş kanadı gibi hafif\nSenin ruhun öyle güzel",
                
                "Gökkuşağı gibi renkli\nŞelale gibi coşkulu\nSenin varlığın öyle değerli",
                
                "Ay ışığı gibi gizemli\nGece karanlığı gibi derin\nSenin dünyam öyle anlamlı",
                
                "Sabah çiyi gibi temiz\nAkşam rüzgarı gibi serin\nSenin sevgin öyle has",
                
                "Dağ çiçeği gibi nadir\nVadi rüzgarı gibi özgür\nSenin varlığın öyle özel",
                
                "Yağmur sonrası gökkuşağı\nGüneş doğuşu gibi umutlu\nSeninle her şey güzel",
                
                "Kar tanesi gibi eşsiz\nBuz kristali gibi özel\nSenin varlığın benzersiz",
                
                "Deniz kokusu gibi ferah\nSahil kumları gibi sıcak\nSenin sevgin öyle gerçek",
                
                "Orman yolu gibi gizemli\nDağ patikası gibi zorlu\nSeninle her yol güzel",
                
                "Göl kenarı gibi huzurlu\nNehir akışı gibi dingin\nSenin varlığın öyle rahat",
                
                "Yıldızlı gece gibi büyülü\nDolunay gibi parlak\nSenin sevgin öyle ışıltılı",
                
                "Bahar rüzgarı gibi taze\nYaz yağmuru gibi bereketli\nSenin varlığın öyle değerli",
                
                "Sonbahar renkleri gibi canlı\nKış beyazı gibi temiz\nSenin dünyam öyle renkli",
                
                "Şelale sesi gibi huzurlu\nKuş sesi gibi mutlu\nSenin sesin öyle güzel",
                
                "Çiçek bahçesi gibi renkli\nGül kokusu gibi zarif\nSenin varlığın öyle narin",
                
                "Gökyüzü mavisi gibi sonsuz\nDeniz derinliği gibi sınırsız\nSenin sevgin öyle uçsuz",
                
                "Yağmur damlası gibi berrak\nKar tanesi gibi saf\nSenin kalbin öyle temiz",
                
                "Güneş ışığı gibi sıcak\nAy ışığı gibi romantik\nSenin varlığın öyle özel",
                
                "Rüzgar gibi özgür ruhlu\nToprak gibi bereketli\nSenin varlığın çok değerli",
                
                "Gün batımı gibi etkileyici\nŞafak vakti gibi umut dolu\nSenin sevgin öyle güçlü",
                
                "Gökkuşağı gibi rengarenk\nYıldızlar gibi parlak\nSenin dünyam öyle güzel",
                
                "Deniz dalgaları gibi dinamik\nSahil kumu gibi yumuşak\nSenin kalbin öyle hassas",
                
                "Bahar çiçekleri gibi taze\nYaz güneşi gibi parlak\nSenin varlığın öyle canlı",
                
                "Sonbahar yaprakları gibi zarif\nKış karı gibi beyaz\nSenin ruhun öyle temiz",
                
                "Dağ zirvesi gibi yüksek\nVadi yeşili gibi derin\nSenin sevgin öyle anlamlı",
                
                "Göl yüzeyi gibi sakin\nNehir akışı gibi kararlı\nSenin varlığın öyle huzurlu",
                
                "Yıldız ışığı gibi uzak\nAy parıltısı gibi yakın\nSenin sevgin öyle derin",
                
                "Çiçek kokusu gibi hafif\nBahar esintisi gibi taze\nSenin varlığın öyle ferah",
                
                "Kuş kanadı gibi özgür\nRüzgar gibi sınırsız\nSenin ruhun öyle engin",
                
                "Şelale gibi coşkulu\nDere gibi dingin\nSenin varlığın öyle dengeli",
                
                "Gökyüzü gibi sonsuz\nDeniz gibi derin\nSenin sevgin öyle büyük",
                
                "Yağmur gibi bereketli\nKar gibi temiz\nSenin kalbin öyle saf",
                
                "Güneş gibi parlak\nAy gibi gizemli\nSenin varlığın öyle özel",
                
                "Bulut gibi özgür\nRüzgar gibi esintili\nSenin ruhun öyle ferah",
                
                "Dağ gibi heybetli\nOva gibi geniş\nSenin sevgin öyle büyük",
                
                "Orman gibi zengin\nÇiçek gibi renkli\nSenin dünyam öyle güzel",
                
                "Deniz gibi dalgalı\nGöl gibi durgun\nSenin varlığın öyle derin",
                
                "Yıldız gibi parlak\nGece gibi gizemli\nSenin sevgin öyle özel",
                
                "Bahar gibi taze\nYaz gibi sıcak\nSenin varlığın öyle canlı",
                
                "Sonbahar gibi renkli\nKış gibi beyaz\nSenin ruhun öyle temiz",
                
                "Şafak gibi umutlu\nGün batımı gibi huzurlu\nSenin varlığın öyle değerli",
                
                "Gökkuşağı gibi renkli\nYağmur gibi berrak\nSenin kalbin öyle saf",
                
                "Rüzgar gibi özgür\nToprak gibi verimli\nSenin varlığın öyle zengin",
                
                "Deniz gibi masmavi\nGökyüzü gibi sonsuz\nSenin sevgin öyle derin",
                
                "Yağmur gibi ferah\nGüneş gibi parlak\nSenin varlığın öyle aydınlık",
                
                "Ay gibi ışıltılı\nYıldız gibi uzak\nSenin sevgin öyle derin",
                
                "Çiçek gibi zarif\nAğaç gibi güçlü\nSenin varlığın öyle özel",
                
                "Kuş gibi özgür\nBulut gibi hafif\nSenin ruhun öyle engin",
                
                "Şelale gibi güçlü\nNehir gibi akıcı\nSenin varlığın öyle etkileyici",
                
                "Gökyüzü gibi sınırsız\nDeniz gibi dalgalı\nSenin sevgin öyle büyük",
                
                "Yağmur gibi bereketli\nKar gibi saf\nSenin kalbin öyle temiz",
                
                "Güneş gibi sıcak\nAy gibi romantik\nSenin varlığın öyle özel",
                
                "Rüzgar gibi esintili\nToprak gibi cömert\nSenin varlığın öyle değerli",
                
                "Gün batımı gibi büyülü\nŞafak gibi umutlu\nSenin sevgin öyle güçlü",
                
                "Gökkuşağı gibi canlı\nYıldız gibi parlak\nSenin dünyam öyle renkli",
                
                "Deniz gibi hareketli\nKum gibi yumuşak\nSenin kalbin öyle hassas",
                
                "Çiçek gibi narin\nAğaç gibi köklü\nSenin sevgin öyle derin",
                
                "Kuş gibi neşeli\nBulut gibi özgür\nSenin ruhun öyle ferah",
                
                "Şelale gibi canlı\nGöl gibi durgun\nSenin varlığın öyle huzurlu",
                
                "Gökyüzü gibi engin\nDeniz gibi derin\nSenin sevgin öyle büyük",
                
                "Yağmur gibi hayat dolu\nKar gibi temiz\nSenin kalbin öyle saf",
                
                "Güneş gibi ısıtan\nAy gibi aydınlatan\nSenin varlığın öyle değerli",
                
                "Rüzgar gibi serinleten\nToprak gibi besleyen\nSenin sevgin öyle yaşatan",
                
                "Gün doğumu gibi umutlu\nGün batımı gibi huzurlu\nSenin varlığın öyle güzel",
                
                "Gökkuşağı gibi şaşırtan\nYıldız gibi parlayan\nSenin dünyam öyle renkli",
                
                "Deniz gibi coşkulu\nSahil gibi huzurlu\nSenin varlığın öyle dengeli",
                
                "Bahar gibi canlandıran\nYaz gibi ısıtan\nSenin sevgin öyle yaşatan",
                
                "Sonbahar gibi olgunlaştıran\nKış gibi dinlendiren\nSenin varlığın öyle öğreten",
                
                "Dağ gibi güçlendiren\nVadi gibi kucaklayan\nSenin sevgin öyle destekleyen",
                
                "Orman gibi yaşatan\nÇiçek gibi güzelleştiren\nSenin varlığın öyle zenginleştiren",
                
                "Nehir gibi akıp giden\nGöl gibi derinleşen\nSenin sevgin öyle büyüyen",
                
                "Yıldız gibi yol gösteren\nAy gibi aydınlatan\nSenin varlığın öyle yönlendiren",
                
                "Çiğ tanesi gibi yenileyen\nGüneş gibi canlandıran\nSenin sevgin öyle yaşatan",
                
                "Rüzgar gibi özgürleştiren\nYağmur gibi arındıran\nSenin varlığın öyle güzelleştiren",
                
                "Deniz gibi sonsuzlaşan\nGökyüzü gibi genişleyen\nSenin sevgin öyle büyüyen",
                
                "Yağmur gibi bereketle yağan\nKar gibi temizleyen\nSenin kalbin öyle arındıran",
                
                "Güneş gibi ısıtıp aydınlatan\nAy gibi huzur veren\nSenin varlığın öyle mutlu eden",
                
                "Rüzgar gibi ferahlatan\nToprak gibi kök salan\nSenin sevgin öyle güçlendiren",
                
                "Gün gibi umutla başlayan\nGece gibi huzurla biten\nSenin varlığın öyle anlamlı kılan",
                
                "Gökkuşağı gibi renklendiren\nYıldız gibi ışıldayan\nSenin dünyam öyle güzelleştiren",
                
                "Deniz gibi derinleşen\nKum gibi sarıp sarmalayan\nSenin kalbin öyle kucaklayan",
                
                "Bahar gibi yeşerten\nYaz gibi olgunlaştıran\nSenin sevgin öyle geliştiren"
            ]

            try:
                await event.edit("**🎯 Üyeleri Şiirlerle Etiketlemeye Başlıyorum**")
            except:
                pass

            async for user in client.iter_participants(event.chat_id):
                if not tagging.get(chat_id):
                    break
                if user.bot:
                    continue
                    
                try:
                    random_poem = random.choice(poems)
                    await event.client.send_message(event.chat_id, f"{random_poem}\n[{user.first_name}](tg://user?id={user.id})")
                    await asyncio.sleep(3)
                except Exception as e:
                    print(f"Etiketleme hatası: {str(e)}")
                    continue

    @client.on(events.NewMessage(pattern=r"\.cancel"))
    async def cancel_tagging(event):
        chat_id = event.chat_id
        if chat_id in tagging:
            tagging[chat_id] = False
            try:
                await event.delete()
            except:
                pass


    @client.on(events.NewMessage(pattern=r"\.otag(?: |$)(.*)"))
    async def military_tag(event):
        if event.is_group:
            if event.fwd_from:
                return
                
            chat_id = event.chat_id
            tagging[chat_id] = True
            message = event.pattern_match.group(1)

            military_ranks = [
                "Er", "Onbaşı", "Çavuş", "Üstçavuş", "Başçavuş", "Kıdemli Başçavuş",
                "Astsubay", "Kıdemli Astsubay", "Başastsubay", "Kıdemli Başastsubay",
                "Asteğmen", "Teğmen", "Üsteğmen", "Yüzbaşı", "Binbaşı", "Yarbay",
                "Albay", "Tuğgeneral", "Tümgeneral", "Korgeneral", "Orgeneral", "Mareşal",
                "Asker", "Komutan", "Paşa", "Başkomutan", "Kahraman", "Gazi",
                "Topçu", "Piyade", "Tankçı", "Pilot", "Denizci", "Bahriyeli",
                "Komando", "Özel Kuvvet", "SAT Komando", "Bordo Bereli", "Paraşütçü"
            ]

            try:
                await event.edit("**🎖️ Üyeleri Askeri Rütbelerle Etiketlemeye Başlıyorum**")
            except:
                pass

            async for user in client.iter_participants(event.chat_id):
                if not tagging.get(chat_id):
                    break
                if user.bot:
                    continue
                    
                try:
                    rank = random.choice(military_ranks)
                    if message:
                        await event.client.send_message(
                            event.chat_id,
                            f"**{rank}** {message} [{user.first_name}](tg://user?id={user.id})"
                        )
                    else:
                        await event.client.send_message(
                            event.chat_id,
                            f"**{rank}** [{user.first_name}](tg://user?id={user.id})"
                        )
                    await asyncio.sleep(3)
                except Exception as e:
                    print(f"Etiketleme hatası: {str(e)}")
                    continue

    @client.on(events.NewMessage(pattern=r"\.cancel"))
    async def cancel_tagging(event):
        chat_id = event.chat_id
        if chat_id in tagging:
            tagging[chat_id] = False
            try:
                await event.delete()
            except:
                pass


    @client.on(events.NewMessage(pattern=r"\.itag(?: |$)(.*)"))
    async def itag(event):
        if event.is_group:
            if event.fwd_from:
                return
                
            chat_id = event.chat_id
            tagging[chat_id] = True

            sweet_messages = [
                "Gözümün nuru {}",
                "Kalbimdeki melek {}",
                "Güzelliğin ışığı {}",
                "Gönlümün sultanı {}",
                "Nur yüzlü {}",
                "Bal gözlüm {}",
                "Güzeller güzeli {}",
                "Kalbimin sahibi {}",
                "Ruhumun yarısı {}",
                "Cennet kokulum {}",
                "Hayatımın anlamı {}",
                "Gönül bahçemin gülü {}",
                "Kalbimin meleği {}",
                "Gözbebeğim {}",
                "Can özüm {}",
                "Hayat ışığım {}",
                "Kalp tahtımın sultanı {}",
                "Gönlümün efendisi {}",
                "Huzurum {}",
                "Mutluluğum {}",
                "Yaşama sevincim {}",
                "Kalbimin neşesi {}",
                "Dünyamın güneşi {}",
                "Hayatımın yıldızı {}",
                "Gönlümün masalı {}",
                "Kalbimin şiiri {}",
                "Ruhumun ezgisi {}",
                "Hayatımın baharı {}",
                "Gözlerimin ışığı {}",
                "Kalbimin güvercini {}",
                "Huzur kaynağım {}",
                "Mutluluk pınarım {}",
                "Gönül bahçem {}",
                "Kalbimin sultanı {}",
                "Ruhumun efendisi {}",
                "Hayatımın güzelliği {}",
                "Gönlümün gülü {}",
                "Kalbimin çiçeği {}",
                "Ruhumun meltemi {}",
                "Hayatımın rengi {}",
                "Gözlerimin nuru {}",
                "Kalbimin sevinci {}",
                "Ruhumun huzuru {}",
                "Hayatımın anlamı {}",
                "Gönlümün neşesi {}",
                "Kalbimin mutluluğu {}",
                "Ruhumun sevinci {}",
                "Hayatımın güneşi {}",
                "Gönlümün yıldızı {}",
                "Kalbimin mehtabı {}",
                "Ruhumun ışığı {}",
                "Hayatımın umudu {}",
                "Gönlümün sevinci {}",
                "Kalbimin huzuru {}",
                "Ruhumun neşesi {}",
                "Hayatımın sevinci {}",
                "Gönlümün ışığı {}",
                "Kalbimin umudu {}",
                "Ruhumun güneşi {}",
                "Hayatımın mehtabı {}",
                "Gönlümün mehtabı {}",
                "Kalbimin ışığı {}",
                "Ruhumun yıldızı {}",
                "Hayatımın ışığı {}",
                "Gönlümün umudu {}",
                "Kalbimin güneşi {}",
                "Ruhumun mehtabı {}",
                "Hayatımın yıldızı {}",
                "Gönlümün güneşi {}",
                "Kalbimin yıldızı {}",
                "Ruhumun umudu {}",
                "Can parçam {}",
                "Gönül dostum {}",
                "Kalp yarım {}",
                "Ruh eşim {}",
                "Ömrümün varı {}",
                "Canımın içi {}",
                "Gönlümün varı {}",
                "Kalbimin sesi {}",
                "Ruhumun sesi {}",
                "Ömrümün neşesi {}",
                "Canımın özü {}",
                "Gönlümün özü {}",
                "Kalbimin özü {}",
                "Ruhumun özü {}",
                "Ömrümün özü {}",
                "Canımın cananı {}",
                "Gönlümün cananı {}",
                "Kalbimin cananı {}",
                "Ruhumun cananı {}",
                "Ömrümün cananı {}",
                "Canımın gülü {}",
                "Gönlümün çiçeği {}",
                "Kalbimin lalesi {}",
                "Ruhumun menekşesi {}",
                "Ömrümün papatyası {}",
                "Hayat arkadaşım {}",
                "Gönül yoldaşım {}",
                "Kalp dostum {}",
                "Ruh ikizim {}",
                "Ömür boyu dostum {}",
                "Güzel insan {}",
                "Değerli dostum {}",
                "Kıymetli arkadaşım {}",
                "Nadide çiçeğim {}",
                "Eşsiz dostum {}",
                "Biricik arkadaşım {}",
                "Güzeller güzeli {}",
                "Nur yüzlüm {}",
                "Melek yüzlüm {}",
                "Tatlı dostum {}",
                "Şeker arkadaşım {}",
                "Bal dostum {}",
                "Canım arkadaşım {}",
                "Sevgili dostum {}",
                "Değerli arkadaşım {}",
                "Güzel yürekli {}",
                "Temiz kalpli {}",
                "Nur kalpli {}",
                "Melek kalpli {}",
                "Güzel ruhlu {}",
                "Temiz ruhlu {}",
                "Nur ruhlu {}",
                "Melek ruhlu {}",
                "Güzel gönüllü {}",
                "Temiz gönüllü {}",
                "Nur gönüllü {}",
                "Melek gönüllü {}",
                "Hayatımın güzel insanı {}",
                "Gönlümün güzel insanı {}",
                "Kalbimin güzel insanı {}",
                "Ruhumun güzel insanı {}",
                "Ömrümün güzel insanı {}",
                "Hayatımın değerli insanı {}",
                "Gönlümün değerli insanı {}",
                "Kalbimin değerli insanı {}",
                "Ruhumun değerli insanı {}",
                "Ömrümün değerli insanı {}",
                "Hayatımın kıymetli insanı {}",
                "Gönlümün kıymetli insanı {}",
                "Kalbimin kıymetli insanı {}",
                "Ruhumun kıymetli insanı {}",
                "Ömrümün kıymetli insanı {}",
                "Hayatımın nadide insanı {}",
                "Gönlümün nadide insanı {}",
                "Kalbimin nadide insanı {}",
                "Ruhumun nadide insanı {}",
                "Ömrümün nadide insanı {}",
                "Hayatımın eşsiz insanı {}",
                "Gönlümün eşsiz insanı {}",
                "Kalbimin eşsiz insanı {}",
                "Ruhumun eşsiz insanı {}",
                "Ömrümün eşsiz insanı {}",
                "Hayatımın biricik insanı {}",
                "Gönlümün biricik insanı {}",
                "Kalbimin biricik insanı {}",
                "Ruhumun biricik insanı {}",
                "Ömrümün biricik insanı {}",
                "Hayatımın güzel yürekli insanı {}",
                "Gönlümün güzel yürekli insanı {}",
                "Kalbimin güzel yürekli insanı {}",
                "Ruhumun güzel yürekli insanı {}",
                "Ömrümün güzel yürekli insanı {}",
                "Hayatımın temiz kalpli insanı {}",
                "Gönlümün temiz kalpli insanı {}",
                "Kalbimin temiz kalpli insanı {}",
                "Ruhumun temiz kalpli insanı {}",
                "Ömrümün temiz kalpli insanı {}",
                "Hayatımın nur kalpli insanı {}",
                "Gönlümün nur kalpli insanı {}",
                "Kalbimin nur kalpli insanı {}",
                "Ruhumun nur kalpli insanı {}",
                "Ömrümün nur kalpli insanı {}",
                "Hayatımın melek kalpli insanı {}",
                "Gönlümün melek kalpli insanı {}",
                "Kalbimin melek kalpli insanı {}",
                "Ruhumun melek kalpli insanı {}",
                "Ömrümün melek kalpli insanı {}",
                "Sen yoksan bir yanımız eksik {}",
                "Varlığınla güzelleşen dünyamız {}",
                "Gülüşün yeter tüm dertlere {}",
                "Sohbetin şifa gibi {}",
                "Varlığın huzur veriyor {}",
                "Işık saçıyorsun etrafa {}",
                "Neşe kaynağımız {}",
                "Aramızın güzel insanı {}",
                "Kalplerin sultanı {}",
                "Gönüllerin efendisi {}",
                "Güzel dostum {}",
                "Değerli arkadaşım {}",
                "Kıymetli dostum {}",
                "Nadide insan {}",
                "Eşsiz arkadaşım {}",
                "Biricik dostum {}"
            ]

            try:
                await event.edit("**🎯 Üyeleri Güzel Sözlerle Etiketlemeye Başlıyorum**")
            except:
                pass

            async for user in client.iter_participants(event.chat_id):
                if not tagging.get(chat_id):
                    break
                if user.bot:
                    continue
                    
                try:
                    sweet_message = random.choice(sweet_messages)
                    formatted_message = sweet_message.format(f"[{user.first_name}](tg://user?id={user.id})")
                    await event.client.send_message(event.chat_id, formatted_message)
                    await asyncio.sleep(3)
                except Exception as e:
                    print(f"Etiketleme hatası: {str(e)}")
                    continue

    @client.on(events.NewMessage(pattern=r"\.cancel"))
    async def cancel_tagging(event):
        chat_id = event.chat_id
        if chat_id in tagging:
            tagging[chat_id] = False
            try:
                await event.delete()
            except:
                pass

    @client.on(events.NewMessage(pattern=r"\.slap"))
    async def slap(event):
        if event.is_group and event.reply_to_msg_id:
            reply_message = await event.get_reply_message()
            user = await reply_message.get_sender()
            sender = await event.get_sender()
            
            slap_list = [
                            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) Tüplü televizyon fırlattı 📺",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) el bombası fırlattı 💣",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) Elektrik Bombası attı ⚡",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) üzerine kahve döktü ☕",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) mikrodalga fırlattı 🔥",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) buzdolabıyla ezdi ❄️",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) çamaşır makinesi attı 🌊",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) bulaşık makinesiyle vurdu 🍽️",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) ütüyle bastı 👕",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) elektrikli süpürgeyle çarptı 🧹",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) saç kurutma makinesiyle uçurdu 💨",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) tost makinesiyle bastı 🥪",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) blender fırlattı 🌪️",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) su ısıtıcısıyla haşladı 🫖",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) vantilatörle savurdu 💨",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) klima ünitesi düşürdü ❄️",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) robot süpürge sürdü 🤖",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) mutfak robotuyla parçaladı 🔪",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) fırın tepsiyle vurdu 🍳",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) mikser fırlattı 🥛",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) laptop fırlattı 💻",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) tablet attı 📱",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) akıllı saatle zamanını durdurdu ⌚",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) oyun konsoluyla vurmaya başladı 🎮",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) drone saldırısı düzenledi 🛸",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) akıllı hoparlörle sağır etti 🔊",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) projektör fırlattı 📽️",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) güvenlik kamerasıyla gözetledi 📹",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) yazıcıdan kağıt bombardımanına tuttu 🖨️",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) tarayıcıyla taradı 📠",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) powerbank fırlattı 🔋",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) uzaktan kumanda yağmuruna tuttu 📱",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) DVD player attı 📀",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) radyo dalgalarıyla çarptı 📻",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) müzik setiyle sersemlettti 🎵",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) hesap makinesiyle matematik dersi verdi 🔢",f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) USB kablosuyla bağladı 🔌",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) hard diskle veri yükledi 💾",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) mouse ile tıkladı 🖱️",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) klavye tuşlarıyla yazdı ⌨️",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) monitörle ekran verdi 🖥️",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) kamerayla fotoğrafını çekti 📸",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) mikrofonla ses kaydı aldı 🎙️",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) kulaklıkla müzik dinletti 🎧",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) akıllı ampulle aydınlattı 💡",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) termometre ile ateşini ölçtü 🌡️",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) kablo yumağına doladı 🔌",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) priz çarptı ⚡",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) uzatma kablosu fırlattı 🔌",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) adaptör taktı 🔌",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) şarj aletiyle şarj etti 🔋",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) batarya fırlattı 🔋",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) güç kaynağı bağladı ⚡",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) solar panelle güneşlendirdi ☀️",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) rüzgar türbiniyle savurdu 🌪️",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) jeneratör çalıştırdı 🔋",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) akü bağladı 🔋",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) inverter taktı ⚡",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) voltaj regülatörü bağladı ⚡",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) sigorta attırdı 💥",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) trafo patlatı 💥",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) elektrik direği devirdi ⚡",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) yüksek gerilim hattına bağladı ⚡",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) enerji santrali kurdu 🏭",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) nükleer reaktör patlattı ☢️",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) hidroelektrik barajı yıktı 💧",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) termik santral kurdu 🏭",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) biyogaz tesisi patlattı 💨",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) jeotermal kaynak buldu 🌋",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) dalga enerjisi verdi 🌊",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) yakıt hücresi bağladı ⛽",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) hidrojen yakıtı verdi 💨",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) füzyon reaktörü kurdu ⚛️",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) antimadde reaktörü patlattı 💥",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) karadelik oluşturdu 🕳️",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) uzay istasyonu düşürdü 🛸",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) uydu fırlattı 🛰️",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) roket rampası kurdu 🚀",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) meteor çarptırdı ☄️",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) asteroit düşürdü 🌠",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) galaksi fırlattı 🌌",            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) süpernova patlatı 💫",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) gezegen çarptırdı 🪐",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) güneş sistemi fırlattı 🌞",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) yıldız tozu serpti ✨",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) kuzey ışıkları gösterdi 🌌",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) ozon tabakası deldi 🌍",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) atmosfer basıncı yükseltti 🌪️",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) yer çekimi tersine çevirdi 🔄",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) manyetik alan oluşturdu 🧲",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) radyoaktif madde sıçrattı ☢️",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) asit yağmuru yağdırdı 🌧️",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) tsunami dalgası gönderdi 🌊",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) volkan patlatı 🌋",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) deprem oluşturdu 🏚️",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) kasırga gönderi 🌪️",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) hortum çıkardı 🌪️",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) buz çağı başlattı 🥶",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) küresel ısınma yarattı 🌡️",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) kutupları eritti 🧊",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) deniz seviyesini yükseltti 🌊",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) göktaşı düşürdü ☄️",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) dinozor çarptırdı 🦖",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) mamut fırlattı 🦣",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) buz dağı düşürdü 🧊",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) piramit yuvarladı 🏛️",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) sfenks fırlattı 🗿",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) antik tapınak yıktı 🏛️",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) kale duvarı devirdi 🏰",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) saray yıktı 👑",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) köprü çökertti 🌉",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) gökdelen devirdi 🏢",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) stadyum yıktı 🏟️",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) havalimanı kapattı ✈️",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) liman batırdı 🚢",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) tren raydan çıkardı 🚂",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) metro tüneli çökertti 🚇",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) otobüs terminali yaktı 🚌",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) benzin istasyonu patlattı ⛽",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) fabrika yıktı 🏭",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) hastane kapattı 🏥",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) okul tatil etti 🏫",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) kütüphane yaktı 📚",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) müze soydu 🏛️",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) banka soygunu yaptı 🏦",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) posta ofisi bastı 📮",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) itfaiye istasyonu yaktı 🚒",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) polis merkezi bastı 👮",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) adliye sarayı yıktı ⚖️",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) hapishane kaçırdı 🏢",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) stadyum çökertti 🏟️",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) konser salonu yıktı 🎭",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) sinema salonu patlattı 🎦",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) tiyatro sahnesi çökertti 🎭",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) lunapark kapattı 🎡",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) hayvanat bahçesi saldı 🦁",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) akvaryum patlattı 🐠",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) botanik bahçesi yaktı 🌺",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) sera yıktı 🌱",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) çiftlik bastı 🐄",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) değirmen patlattı 💨",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) baraj yıktı 💧",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) maden ocağı çökertti ⛏️",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) petrol kuyusu patlattı 🛢️",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) doğalgaz hattı deldi 💨",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) rüzgar türbini devirdi 🌪️",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) güneş paneli kırdı ☀️",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) radar istasyonu bozdu 📡",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) uydu anteni düşürdü 📡",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) telefon kulesi yıktı 📱",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) internet kablosu kesti 🌐",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) fiber optik hattı kopardı 🔌",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) veri merkezi çökertti 💻",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) sunucu odası yaktı 🔥",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) kontrol merkezi hackledi 🖥️",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) güvenlik sistemini çökertti 🔒",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) alarm sistemini kapattı 🚨",
            f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) kamera sistemini kırdı 📹",
            ]
            
            slapped = random.choice(slap_list)
            await event.respond(slapped)
            try:
                await event.delete()
            except:
                pass


    @client.on(events.NewMessage(pattern=r"\.kiss"))
    async def kiss(event):
        if event.is_group and event.reply_to_msg_id:
            reply_message = await event.get_reply_message()
            user = await reply_message.get_sender()
            sender = await event.get_sender()
            
            kiss_list = [
                f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) dudağından öptü 💋",
                f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) yanağından öptü 😘",
                f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) alnından öptü 😚",
                f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) romantik bir yemeğe çıkardı 🍝",
                f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) kalp gönderdi ❤️",
                f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) çiçek aldı 💐",
                f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) sarıldı 🤗",
                f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) elinden öptü 🤲",
                f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) aşk mektubu yazdı 💌",
                f"[{user.first_name}](tg://user?id={user.id}) [{sender.first_name}](tg://user?id={sender.id}) yıldızları izlemeye götürdü ⭐"
            ]
            
            kissed = random.choice(kiss_list)
            await event.respond(kissed, parse_mode='Markdown')
            try:
                await event.delete()
            except:
                pass

    @client.on(events.NewMessage(pattern=r"\.dsoru"))
    async def dogruluk(event):
        dogruluk_list = [
            "**En son kimi stalkladın?**",
            "**En son attığın mesajı göster**",
            "**En sevdiğin kişi kim?**",
            "**En son ne zaman ağladın?**",
            "**En çok utandığın an neydi?**",
            "**En son söylediğin yalan neydi?**",
            "**En büyük korkun ne?**",
            "**Gizli yeteneğin var mı?**",
            "**En son izlediğin dizi/film ne?**",
            "**Telefonunda en son arattığın şey neydi?**",
            "**En son kiminle konuştun?**",
            "**En sevdiğin yemek ne?**",
            "**Hayatında yaptığın en çılgın şey neydi?**",
            "**En son ne zaman yalan söyledin?**",
            "**En sevdiğin renk ne?**",
            "**Hayalindeki meslek ne?**",
            "**En son ne zaman spor yaptın?**",
            "**En sevdiğin mevsim hangisi?**",
            "**Kendini 3 kelimeyle anlat**",
            "**En son ne zaman dans ettin?**",
            "**Bir hayvan olsan hangisi olurdun?**",
            "**En sevdiğin tatil yeri neresi?**",
            "**En son ne zaman kahkaha attın?**",
            "**Telefonunda en çok kullandığın uygulama hangisi?**",
            "**En sevdiğin emoji hangisi?**",
            "**Hiç pişman olduğun bir anın var mı?**",
            "**En sevdiğin kitap hangisi?**",
            "**Şu an canın ne çekiyor?**",
            "**En son ne zaman sinema/tiyatroya gittin?**",
            "**Hayalindeki arabanın markası ne?**",
            "**En sevdiğin spor dalı hangisi?**",
            "**Bir dilek hakkın olsa ne dilerdin?**",
            "**En son aldığın hediye neydi?**",
            "**Burçların hakkında ne düşünüyorsun?**",
            "**En sevdiğin çiçek hangisi?**",
            "**Hiç kavga ettin mi?**",
            "**En son ne zaman ağladın?**",
            "**Telefonunda kaç fotoğraf var?**",
            "**En çok nerede yaşamak isterdin?**",
            "**Şu an ne giyiyorsun?**",
            "**En son ne zaman resim çektin?**",
            "**Hayatının en güzel günü hangisiydi?**",
            "**En sevdiğin şarkı ne?**",
            "**En son ne yedin?**",
            "**En son nereye gittin?**",
            "**En sevdiğin oyun hangisi?**",
            "**En son ne zaman güldün?**",
            "**En sevdiğin içecek ne?**",
            "**En son ne zaman şarkı söyledin?**",
            "**En sevdiğin film türü ne?**",
            "**En son ne zaman kitap okudun?**",
            "**En sevdiğin yazar kim?**",
            "**En son ne zaman alışveriş yaptın?**",
            "**En sevdiğin marka ne?**",
            "**En son ne zaman yüzün kızardı?**",
            "**En sevdiğin hayvan ne?**",
            "**En son ne zaman korktun?**",
            "**En sevdiğin mekan neresi?**",
            "**En son ne zaman heyecanlandın?**",
            "**En sevdiğin tatlı ne?**",
            "**En son ne zaman dedikodu yaptın?**",
            "**En sevdiğin sosyal medya hangisi?**",
            "**En son ne zaman şaşırdın?**",
            "**Hiç platonik aşık oldun mu?**",
            "**En son ne zaman hayal kırıklığına uğradın?**",
            "**En sevdiğin parfüm hangisi?**",
            "**En son ne zaman özür diledin?**",
            "**En sevdiğin aksesuar ne?**",
            "**En son ne zaman birini kırdın?**",
            "**Hiç sınav notu değiştirdin mi?**",
            "**En son ne zaman ağladın?**",
            "**En sevdiğin saat markası ne?**",
            "**En son ne zaman yalan söyledin?**",
            "**En sevdiğin takı ne?**",
            "**En son ne zaman dedikodu yaptın?**",
            "**Hiç kopya çektin mi?**",
            "**En son ne zaman birini üzdün?**",
            "**En utanç verici alışkanlığın ne?**",
            "**En son ne zaman pişman oldun?**",
            "**En sevdiğin telefon markası ne?**",
            "**En son ne zaman hayal kurdun?**",
            "**Hiç aşık oldun mu?**",
            "**En son ne zaman ağladın?**",
            "**En sevdiğin kulaklık markası ne?**",
            "**En son ne zaman dans ettin?**",
            "**En büyük pişmanlığın ne?**",
            "**En son ne zaman şarkı söyledin?**",
            "**En sevdiğin kamera markası ne?**",
            "**En son ne zaman fotoğraf çektin?**",
            "**Hiç evden kaçtın mı?**",
            "**En son ne zaman video çektin?**",
            "**En sevdiğin oyun konsolu ne?**",
            "**En son ne zaman oyun oynadın?**",
            "**Hiç aşk mektubu yazdın mı?**",
            "**En son ne zaman spor yaptın?**",
            "**En çok nefret ettiğin şey ne?**",
            "**En son ne zaman koştun?**",
            "**En sevdiğin spor kıyafeti markası ne?**",
            "**En son ne zaman yüzdün?**",
            "**Hiç birini gözetledin mi?**",
            "**En son ne zaman denize girdin?**",
            "**En sevdiğin güneş gözlüğü markası ne?**",
            "**En son ne zaman güneşlendin?**",
            "**Hiç gizli gizli ağladın mı?**",
            "**En son ne zaman tatile gittin?**",
            "**En büyük hayalin ne?**",
            "**Hiç sevgilinden ayrıldın mı?**",
            "**En çok kimi kıskanıyorsun?**"
        ]
        
        dogruluk = random.choice(dogruluk_list)
        await event.respond(dogruluk)
        try:
            await event.delete()
        except:
            pass

    @client.on(events.NewMessage(pattern=r"\.csoru"))
    async def cesaret(event):
        cesaret_list = [
            "**Telefonundaki en utanç verici fotoğrafı göster**",
            "**Gruptaki birinin profil fotoğrafını 1 gün pp yap**",
            "**Son attığın mesajı ss atıp göster**",
            "**Galerindeki son fotoğrafı at**",
            "**Gruptaki birinin ismini bağırarak söyle**",
            "**Bir dakika boyunca tavuk gibi davran**",
            "**En sevdiğin şarkıyı söyle**",
            "**Gruba sesli mesaj atıp şarkı söyle**",
            "**Gruba komik bir fotoğrafını at**",
            "**Karşı cinsten birine atılacak en garip mesajı at**",
            "**Gruptaki birine aşk ilanı yap**",
            "**Son WhatsApp konuşmanı ss at**",
            "**Instagram'da son beğendiğin postu paylaş**",
            "**Twitter'da son attığın tweeti göster**",
            "**Telefon galerindeki ilk fotoğrafı at**",
            "**En son arama geçmişini göster**",
            "**Birinin numarasını karıştırıp mesaj at**",
            "**Gruba bir tane çocukluk fotoğrafını at**",
            "**En sevdiğin şarkıyı söyleyerek ses at**",
            "**Gruptaki birinin taklidini yap**",
            "**Bir dakika boyunca dans edip video at**",
            "**Sokağa çıkıp bir yabancıyla selfie çek**",
            "**Bir süpermarkete gidip en saçma ürünü sor**",
            "**Telefonundaki en garip uygulamayı göster**",
            "**Son arayan kişiyi geri ara**",
            "**Gruptaki birine şiir yaz**",
            "**Karşı komşuya gidip şeker iste**",
            "**Bir dakika boyunca köpek gibi havla**",
            "**Balkona çıkıp şarkı söyle**",
            "**Bir yabancıya saat sor**",
            "**Telefonundaki notları göster**",
            "**En son indirdiğin uygulamayı göster**",
            "**Gruptaki birinin ismini 10 kez bağır**",
            "**Pencereden dışarı el salla**",
            "**Bir yabancıya selam ver**",
            "**En sevmediğin yemeği ye**",
            "**Bir dakika boyunca zıpla**",
            "**Gruptaki birine şarkı ithaf et**",
            "**Telefonundaki en eski fotoğrafı göster**",
            "**Bir dakika boyunca bebek gibi konuş**",
            "**Son gelen spam mailini oku**",
            "**Gruptaki birinin profil fotoğrafını çiz**",
            "**Bir yabancıya iltifat et**",
            "**Telefonundaki en garip selfie'yi göster**",
            "**Bir dakika boyunca kedi gibi miyavla**",
            "**Instagram hikayene saçma bir video at**",
            "**Bir market çalışanıyla selfie çek**",
            "**Sokakta yürüyen birine şarkı söyle**",
            "**En sevmediğin içeceği iç**",
            "**Bir dakika boyunca maymun gibi davran**",
            "**Son arama kayıtlarını göster**",
            "**Gruptaki birine rap yap**",
            "**Bir yabancıdan kalem iste**",
            "**Telefonundaki en komik fotoğrafı göster**",
            "**Bir dakika boyunca robot gibi konuş**",
            "**En son çektiğin fotoğrafı göster**",
            "**Gruptaki birinin ismini tersten söyle**",
            "**Bir yabancıya sarıl**",
            "**Telefonundaki en kötü fotoğrafı göster**",
            "**Bir dakika boyunca balık gibi davran**",
            "**WhatsApp durumuna garip bir şey yaz**",
            "**Bir mağaza çalışanıyla dans et**",
            "**Sokakta şarkı söyleyerek yürü**",
            "**En sevmediğin şarkıyı dinle**",
            "**Bir dakika boyunca ördek gibi yürü**",
            "**Son çektiğin ekran görüntüsünü göster**",
            "**Gruptaki birine komik bir hikaye anlat**",
            "**Bir yabancıdan yol tarifi iste**",
            "**Telefonundaki en son indirdiğin fotoğrafı göster**",
            "**Bir dakika boyunca yabancı aksanla konuş**",
            "**Instagram'da rastgele birini takip et**",
            "**Gruptaki birinin biyografisini yaz**",
            "**Bir yabancıya fıkra anlat**",
            "**Telefonundaki en utanç verici notu göster**",
            "**Bir dakika boyunca tavşan gibi zıpla**",
            "**Facebook durumuna saçma bir şey yaz**",
            "**Bir güvenlik görevlisiyle selfie çek**",
            "**Sokakta dans ederek yürü**",
            "**En sevmediğin kıyafeti giy**",
            "**Bir dakika boyunca aslan gibi kükre**",
            "**Son gelen spam mesajını sesli oku**",
            "**Gruptaki birine sevgi ilanı yap**",
            "**Bir yabancıya şarkı söyle**",
            "**Telefonundaki en garip videoyu göster**",
            "**Bir dakika boyunca penguen gibi yürü**",
            "**Twitter biyografini değiştir**",
            "**Gruptaki birinin taklidini yaparak ses at**",
            "**Bir yabancıyla high five yap**",
            "**Telefonundaki en eski mesajı göster**",
            "**Bir dakika boyunca fil gibi yürü**",
            "**Instagram hikayene şarkı söyleyerek video at**",
            "**Bir kasiyer ile sohbet başlat**",
            "**Sokakta zıplayarak yürü**",
            "**En sevmediğin emojileri art arda at**",
            "**Bir dakika boyunca fare gibi ses çıkar**",
            "**Son arayan kişiye sesli mesaj at**",
            "**Gruptaki birine şaka yap**",
            "**Bir yabancıdan mendil iste**",
            "**Telefonundaki en son sildiğin fotoğrafı göster**",
            "**Bir dakika boyunca operacı gibi konuş**",
            "**Snapchat hikayene komik bir video at**",
            "**Gruptaki birinin profil fotoğrafını açıkla**",
            "**Bir yabancıya dans teklif et**",
            "**Telefonundaki en tuhaf aramayı göster**",
            "**Bir dakika boyunca zombi gibi yürü**",
            "**LinkedIn durumunu komik bir şekilde güncelle**"
        ]
        
        cesaret = random.choice(cesaret_list)
        await event.respond(cesaret)
        try:
            await event.delete()
        except:
            pass




    @client.on(events.NewMessage(pattern=r"\.bul (.+)"))
    async def music_download(event):
        if event.is_group:
            try:
                query = event.pattern_match.group(1)
                status_msg = await event.respond("🔍 **Şarkı aranıyor...**")
                
                ydl_opts = {
                    'format': 'bestaudio',
                    'quiet': True,
                    'no_warnings': True,
                    'extract_flat': 'in_playlist',
                    'default_search': 'ytsearch1:',
                    'noplaylist': True,
                }
                
                with YoutubeDL(ydl_opts) as ydl:
                    try:
                        info = ydl.extract_info(f"ytsearch1:{query}", download=False)
                        if not info or not info.get('entries'):
                            await status_msg.edit("❌ **Şarkı bulunamadı!**")
                            return
                            
                        video = info['entries'][0]
                        url = f"https://www.youtube.com/watch?v={video['id']}"
                        title = video.get('title', '@AxyWxrWbot')
                        
                        safe_title = "".join([c for c in title if c.isalpha() or c.isdigit() or c in (' ','-','_')]).rstrip()
                        
                        await status_msg.edit(f"⬇️ **{title} İndiriliyor...**")
                        
                        download_opts = {
                            'format': 'bestaudio',
                            'outtmpl': f'downloads/{safe_title}.mp3',
                            'quiet': True
                        }
                        
                        with YoutubeDL(download_opts) as ydl:
                            ydl.download([url])
                        
                        await status_msg.edit(f"📤 **{title} Gönderiliyor...**")
                        
                        file_path = f'downloads/{safe_title}.mp3'
                        caption = f"🎵 {title}"
                        
                        await event.client.send_file(
                            event.chat_id,
                            file_path,
                            caption=caption
                        )
                        
                        os.remove(file_path)
                        await status_msg.delete()
                        await event.delete()
                        
                    except Exception as e:
                        await status_msg.edit("❌ **Bir hata oluştu!**")
                        
            except Exception as e:
                print(f"Hata: {str(e)}")

    @client.on(events.NewMessage(pattern=r"\.vbul (.+)"))
    async def video_download(event):
        if event.is_group:
            try:
                query = event.pattern_match.group(1)
                status_msg = await event.respond("🔍 **Video aranıyor...**")
                
                ydl_opts = {
                    'format': 'best',
                    'quiet': True,
                    'no_warnings': True,
                    'extract_flat': 'in_playlist',
                    'default_search': 'ytsearch1:',
                    'noplaylist': True,
                }
                
                with YoutubeDL(ydl_opts) as ydl:
                    try:
                        info = ydl.extract_info(f"ytsearch1:{query}", download=False)
                        if not info or not info.get('entries'):
                            await status_msg.edit("❌ **Video bulunamadı!**")
                            return
                            
                        video = info['entries'][0]
                        url = f"https://www.youtube.com/watch?v={video['id']}"
                        title = video.get('title', '@AxyWxrWbot')
                        
                        safe_title = "".join([c for c in title if c.isalpha() or c.isdigit() or c in (' ','-','_')]).rstrip()
                        
                        await status_msg.edit(f"⬇️ **{title} İndiriliyor...**")
                        
                        download_opts = {
                            'format': 'best',
                            'outtmpl': f'downloads/{safe_title}.mp4',
                            'quiet': True
                        }
                        
                        with YoutubeDL(download_opts) as ydl:
                            ydl.download([url])
                        
                        await status_msg.edit(f"📤 **{title} Gönderiliyor...**")
                        
                        file_path = f'downloads/{safe_title}.mp4'
                        caption = f"🎥 {title}"
                        
                        await event.client.send_file(
                            event.chat_id,
                            file_path,
                            caption=caption,
                            supports_streaming=True
                        )
                        
                        os.remove(file_path)
                        await status_msg.delete()
                        await event.delete()
                        
                    except Exception as e:
                        await status_msg.edit("❌ **Bir hata oluştu!**")
                        
            except Exception as e:
                print(f"Hata: {str(e)}")

    reaction_status = {}  
    reaction_emoji = {}   

    @client.on(events.NewMessage(pattern=r"\.st (on|off)"))
    async def toggle_reaction(event):
        chat_id = event.chat_id
        command = event.pattern_match.group(1)
        
        try:
            if command == "on":
                reaction_status[chat_id] = True
                current_emoji = reaction_emoji.get(chat_id, "🍓")
                await event.respond(f"✅ **Otomatik tepki özelliği açıldı!**\n\nKullanılan emoji: {current_emoji}")
            else:
                reaction_status[chat_id] = False
                await event.respond("❌ **Otomatik tepki özelliği kapatıldı!**")
            
            await event.delete()
        except Exception as e:
            await event.respond("❌ **Bir hata oluştu!**")
            print(f"Hata: {str(e)}")

    @client.on(events.NewMessage(pattern=r"\.strove (.+)"))
    async def change_reaction(event):
        chat_id = event.chat_id
        try:
            new_emoji = event.pattern_match.group(1)
            reaction_emoji[chat_id] = new_emoji
            await event.respond(f"✅ **Tepki emojisi değiştirildi!**\n\nYeni emoji: {new_emoji}")
            await event.delete()
        except Exception as e:
            await event.respond("❌ **Emoji değiştirilirken bir hata oluştu!**")
            print(f"Hata: {str(e)}")

    @client.on(events.NewMessage)
    async def reaction_handler(event):
        chat_id = event.chat_id
        if not reaction_status.get(chat_id, False):
            return
            
        if event.is_reply:
            replied_message = await event.get_reply_message()
            me = await client.get_me()
            if me and replied_message.sender_id == me.id:
                try:
                    current_emoji = reaction_emoji.get(chat_id, "🍓")
                    await event.client(SendReactionRequest(
                        peer=chat_id,
                        msg_id=event.id,
                        reaction=[ReactionEmoji(emoticon=current_emoji)]
                    ))
                except FloodWaitError as e:
                    await asyncio.sleep(e.seconds + 60)

    


    @client.on(events.NewMessage(pattern=r"\.etag(?: |$)(.*)"))
    async def etag(event):
        if event.is_group:
            if event.fwd_from:
                return
                
            chat_id = event.chat_id
            message = event.pattern_match.group(1)
            
            if not message:
                try:
                    await event.edit("**⚠️ Lütfen bir mesaj belirtin!**")
                    return
                except:
                    pass
                    
            tagging[chat_id] = True
            
            try:
                await event.edit("**🎯 Üyeleri Emojilerle Etiketlemeye Başlıyorum**")
            except:
                pass

            emojis = ["🪅","🥀","🌹","🌿","🌺","🌻","🌼","❤️‍🔥","☘️","🍃","🌾","🪻","🏵️","💮","🪷","🌷","🌟","🍂","💗","💞","💕","💟","❣️","💜","💖","💘","💜","🤍","🩵","🖤","💙","🤍","❤️","🔥","💚","🩵","🩵","💔","❤️‍🔥","💋","🫀","🫁","🗣️","🌴","🍃","🍀","🍀","🌲","🌿","🌱"]

            chat = await event.get_input_chat()
            async for user in client.iter_participants(chat):
                if not tagging.get(chat_id):
                    break
                if user.bot:
                    continue
                    
                try:
                    emoji = random.choice(emojis)
                    await event.client.send_message(event.chat_id, f"**{message}** [{emoji}](tg://user?id={user.id})")
                    await asyncio.sleep(3)
                except Exception as e:
                    print(f"Etiketleme hatası: {str(e)}")
                    continue

    @client.on(events.NewMessage(pattern=r"\.cancel"))
    async def cancel_tagging(event):
        chat_id = event.chat_id
        if chat_id in tagging:
            tagging[chat_id] = False
            try:
                await event.delete()
            except:
                pass


    @client.on(events.NewMessage(pattern=r"\.zarat"))
    async def zarat(event):
        if event.is_group:
            dice_msg = await event.respond("🎲")
            try:
                await event.delete()
            except:
                pass

    @client.on(events.NewMessage(pattern=r"\.dart"))
    async def dart(event):
        if event.is_group:
            dice_msg = await event.respond("🎯")
            try:
                await event.delete()
            except:
                pass

    @client.on(events.NewMessage(pattern=r"\.futbol"))
    async def futbol(event):
        if event.is_group:
            dice_msg = await event.respond("⚽")
            try:
                await event.delete()
            except:
                pass

    @client.on(events.NewMessage(pattern=r"\.basket"))
    async def basket(event):
        if event.is_group:
            dice_msg = await event.respond("🏀")
            try:
                await event.delete()
            except:
                pass

    @client.on(events.NewMessage(pattern=r"\.bowling"))
    async def bowling(event):
        if event.is_group:
            dice_msg = await event.respond("🎳")
            try:
                await event.delete()
            except:
                pass

    @client.on(events.NewMessage(pattern=r"\.zar"))
    async def zar(event):
        if event.is_group:
            dice_msg = await event.respond("🎲")
            try:
                await event.delete()
            except:
                pass

    @client.on(events.NewMessage(pattern=r"\.slot"))
    async def slot(event):
        if event.is_group:
            dice_msg = await event.respond("🎰")
            try:
                await event.delete()
            except:
                pass

    @client.on(events.NewMessage(pattern=r"\.eros"))
    async def eros_command(event):
        if event.is_group:
            try:
                users = []
                async for user in client.iter_participants(event.chat_id):
                    if not user.bot and user.first_name:
                        users.append(user)
                
                if len(users) < 2:
                    await event.respond("**Grup çok küçük, daha fazla üye gerekli! 💔**")
                    return
                
                chosen = random.sample(users, 2)
                
                ship_message = f"**💘 Radara Yeni Bir Aşk Yakalandı! 💘\n\n[{chosen[0].first_name}](tg://user?id={chosen[0].id}) ❤️‍🔥 [{chosen[1].first_name}](tg://user?id={chosen[1].id})**"
                
                await event.respond(ship_message)
                
                try:
                    await event.delete()
                except:
                    pass
                    
            except Exception as e:
                print(f"Eros Hatası: {str(e)}")




    @client.on(events.NewMessage(pattern=r"\.soz"))
    async def soz_command(event):
        if event.is_group:
            try:
                sozler = [
                    "Hayat bir oyun gibidir\nBazıları rol yapar\nBazıları gerçeği oynar",
                    
                    "Ucuz insanların değeri\nPahalı eşyalarla ölçülür\nBenim değerim ise karakterimle",
                    
                    "Dost dediğin yanında olmaz\nYüreğinde olur senin\nGerisi zaten misafirdir",
                    
                    "Hayat pamuk ipliğine benzer\nKimi sağlam tutar kopmaz\nKimi de en ufak rüzgarda bırakır",
                    
                    "Sen kendini ne sandın ki\nBen seni ne sanayım\nHerkes haddini bilecek",
                    
                    "Bazıları vardır özü sözü bir\nBazıları vardır içi dışı ayrı\nBen hep aynıyım",
                    
                    "Gülüşünü sevdiğim insan\nBana düşman kesilmiş\nOlsun ben yine de seviyorum",
                    
                    "Hayat bazen tatlıdır\nBazen de çok acı\nÖnemli olan dengede tutabilmek",
                    
                    "Herkes artist olmuş\nBen hala figuranım\nÇünkü rol yapmayı sevmem",
                    
                    "Bazıları altın gibidir\nBazıları gümüş\nBazıları da sadece süs",
                    
                    "Dost sandığın insanlar\nBir gün düşman olur\nAma düşmanlar asla dost olmaz",
                    
                    "Hayat bir film gibidir\nKimi başrol oynar\nKimi figüran kalır",
                    
                    "Sen kendini bir şey sandın\nBen seni adam sandım\nİkimiz de yanılmışız",
                    
                    "Bazıları vardır mert\nBazıları namert\nBen hep mert oldum",
                    
                    "Gülüşü güzel olanın\nKalbi de güzeldir\nAma her gülen güzel değildir",
                    
                    "Hayat bazen güldürür\nBazen ağlatır\nÖnemli olan dik durabilmek",
                    
                    "Herkes maske takar\nBen hep aynıyım\nÇünkü sahteliği sevmem",
                    
                    "Bazıları vardır vefalı\nBazıları vefasız\nBen hep vefalı kaldım",
                    
                    "Dost dediğin adam gibi olmalı\nArkadan iş çevirmemeli\nYüzüne gülüp arkandan vurmamalı",
                    
                    "Hayat bir yol gibidir\nKimi düz gider\nKimi dolambaçlı",
                    
                    "Sen kendini ne sandın ki\nBen seni insan sandım\nMeğer yanılmışım",
                    
                    "Bazıları vardır adamdır\nBazıları adamım der\nAdam olmak başka adamım demek başka",
                    
                    "Gülüşünde saklı sandım\nTüm güzellikleri\nMeğer maskeymiş",
                    
                    "Hayat bazen şaşırtır\nBazen üzer\nAma asla pes ettirmez",
                    
                    "Herkes rol yapıyor\nBen hep benim\nÇünkü sahteliği sevmem",
                    
                    "Bazıları vardır dostur\nBazıları dost görünür\nGerçek dost zor bulunur",
                    
                    "Dost dediğin vefalı olur\nZor günde yanında\nİyi günde arkanda",
                    
                    "Hayat bir nehir gibidir\nKimi yüzer\nKimi boğulur",
                    
                    "Sen kendini bir şey sandın\nBen seni dost sandım\nİkimiz de yanıldık",
                    
                    "Bazıları vardır kalitelidir\nBazıları kalitesiz\nKalite asalet ister",
                    
                    "Gülüşü sahte olanın\nKalbi de sahtedir\nBen hep gerçeğim",
                    
                    "Hayat bazen mutlu eder\nBazen üzer\nÖnemli olan ayakta kalmak",
                    
                    "Herkes bir şey olmuş\nBen hala benim\nÇünkü değişmeyi sevmem",
                    
                    "Bazıları vardır adamdır\nBazıları adam olamaz\nAdam olmak soydandır",
                    
                    "Dost dediğin can olmalı\nCanını verecek kadar\nDeğerini bilecek kadar",
                    
                    "Hayat bir oyun gibidir\nKimi kazanır\nKimi kaybeder",
                    
                    "Sen kendini dev sandın\nBen seni insan sandım\nİkimiz de yanıldık",
                    
                    "Bazıları vardır yüreklidir\nBazıları yüreksiz\nYürek her yiğide nasip olmaz",
                    
                    "Gülüşü güzel olanın\nYüreği de güzeldir\nAma her gülen güzel değildir",
                    
                    "Hayat bazen sevindirir\nBazen ağlatır\nÖnemli olan güçlü olmak",
                    
                    "Herkes bir yere gelmiş\nBen hala yoldayım\nÇünkü acele etmem",
                    
                    "Bazıları vardır mertçe yaşar\nBazıları namertçe\nBen hep mertçe yaşadım",
                    
                    "Dost dediğin yürek olmalı\nAtması bir\nDurması bir",
                    
                    "Hayat bir sınav gibidir\nKimi geçer\nKimi kalır",
                    
                    "Sen kendini akıllı sandın\nBen seni dürüst sandım\nİkimiz de aldandık",
                    
                    "Bazıları vardır özü sözü bir\nBazıları iki yüzlü\nBen hep tek yüzlüyüm",
                    
                    "Gülüşü temiz olanın\nKalbi de temizdir\nBen hep temiz kaldım",
                    
                    "Hayat bazen güldürür\nBazen düşündürür\nÖnemli olan ders çıkarmak",
                    
                    "Herkes bir yol seçmiş\nBen hala arıyorum\nÇünkü doğruyu bulmak önemli",
                    
                    "Bazıları vardır dosttur\nBazıları düşman\nDost bildiğin düşman çıkar",
                    
                    "Dost dediğin güven olmalı\nGüvenecek kadar yakın\nGüvenilecek kadar dürüst",
                    
                    "Hayat bir yolculuk gibidir\nKimi yarı yolda bırakır\nKimi sonuna kadar gider",
                    
                    "Sen kendini haklı sandın\nBen seni haklı sandım\nMeğer ikimiz de haksızmışız",
                    
                    "Bazıları vardır değer bilir\nBazıları değmez\nDeğer bilmek erdemdir",
                    
                    "Gülüşü naif olanın\nKalbi de naiftir\nBen hep naif kaldım",
                    
                    "Hayat bazen zorlar\nBazen kolaylaşır\nÖnemli olan sabretmek",
                    
                    "Herkes bir maske takmış\nBen hep aynıyım\nÇünkü gerçeği severim",
                    
                    "Bazıları vardır vefakar\nBazıları vefasız\nVefa her yiğide nasip olmaz",
                    
                    "Dost dediğin sadık olmalı\nArkandan konuşmayan\nYüzüne gülmeyen",
                    
                    "Hayat bir roman gibidir\nKimi yazar\nKimi yaşar",
                    
                    "Sen kendini sultan sandın\nBen seni insan sandım\nİkimiz de yanıldık",
                    
                    "Bazıları vardır kıymet bilir\nBazıları bilmez\nKıymet bilmek erdemdir",
                    
                    "Gülüşü samimi olanın\nKalbi de samimidir\nBen hep samimi kaldım",
                    
                    "Hayat bazen güldürür\nBazen ağlatır\nÖnemli olan ders almak",
                    
                    "Herkes bir yol çizmiş\nBen hala çiziyorum\nÇünkü acele işe şeytan karışır",
                    
                    "Bazıları vardır adamdır\nBazıları adam olmaz\nAdam olmak nasip ister",
                    
                    "Dost dediğin dert ortağı olmalı\nDerdini dinleyen\nDerman olan",
                    
                    "Hayat bir şarkı gibidir\nKimi söyler\nKimi dinler",
                    
                    "Sen kendini bir şey sandın\nBen seni adam sandım\nİkimiz de yanıldık",
                    
                    "Bazıları vardır yürekli\nBazıları yüreksiz\nYürek her babayiğide nasip olmaz",
                    
                    "Gülüşü içten olanın\nKalbi de içtendir\nBen hep içten oldum",
                    
                    "Hayat bazen sevindirir\nBazen üzer\nÖnemli olan umutlu olmak",
                    
                    "Herkes bir yere varmış\nBen hala yoldayım\nÇünkü yol önemlidir",
                    
                    "Bazıları vardır dosttur\nBazıları düşman\nGerçek dost az bulunur",
                    
                    "Dost dediğin can yoldaşı olmalı\nYolda bırakmayan\nYolunu şaşırmayan",
                    
                    "Hayat bir deniz gibidir\nKimi yüzer\nKimi boğulur",
                    
                    "Sen kendini kral sandın\nBen seni dost sandım\nİkimiz de yanıldık",
                    
                    "Bazıları vardır mert olur\nBazıları namert\nMertlik her yiğide nasip olmaz",
                    
                    "Gülüşü temiz olanın\nKalbi de temizdir\nBen hep temiz kaldım",
                    
                    "Hayat bazen mutlu eder\nBazen mutsuz\nÖnemli olan dengede durmak",
                    
                    "Herkes bir rol seçmiş\nBen hala kendimim\nÇünkü rol yapmayı sevmem",

                    "Bazıları vardır adam gibi\nBazıları adamım der\nAdam olmak başka şey",
                    
                    "Dost dediğin güven verir\nGüven alır\nGüveni bozmaz",
                    
                    "Hayat bir film gibidir\nKimi oynar\nKimi seyreder",
                    
                    "Sen kendini bir şey sandın\nBen seni dost sandım\nMeğer düşmanmışsın",
                    
                    "Bazıları vardır kalbi güzel\nBazıları kalpsiz\nKalp her insana nasip olmaz",
                    
                    "Gülüşü sahici olanın\nKalbi de sahicidir\nBen hep sahici kaldım",
                    
                    "Hayat bazen sevindirir\nBazen kahreder\nÖnemli olan ayakta kalmak",
                    
                    "Herkes bir yol tutmuş\nBen hala arıyorum\nÇünkü doğru yol önemli",
                    
                    "Bazıları vardır vefalı\nBazıları vefasız\nVefa her yiğide nasip olmaz",
                    
                    "Dost dediğin sırdaş olmalı\nSırrını saklayan\nSırtını kollayan",
                    
                    "Hayat bir masal gibidir\nKimi anlatır\nKimi dinler",
                    
                    "Sen kendini büyük sandın\nBen seni insan sandım\nİkimiz de yanıldık",
                    
                    "Bazıları vardır yürekten sever\nBazıları yalandan\nYürekten sevmek başkadır",
                    
                    "Gülüşü masum olanın\nKalbi de masumdur\nBen hep masum kaldım",
                    
                    "Hayat bazen güldürür\nBazen ağlatır\nÖnemli olan pes etmemek",
                    
                    "Herkes bir yol çizmiş\nBen hala çiziyorum\nÇünkü doğru yol önemli",
                    
                    "Bazıları vardır dosttur\nBazıları düşman\nDost görünen düşman olur",
                    
                    "Dost dediğin can olmalı\nCanını verecek kadar\nCanını alacak kadar",
                    
                    "Hayat bir oyun gibidir\nKimi oynar\nKimi oynatır",
                    
                    "Sen kendini haklı sandın\nBen seni dürüst sandım\nİkimiz de yanıldık",
                    
                    "Bazıları vardır adamdır\nBazıları adam olmaz\nAdam olmak soydan gelir",
                    
                    "Gülüşü güzel olanın\nKalbi de güzeldir\nBen hep güzel kaldım",
                    
                    "Hayat bazen sevindirir\nBazen üzer\nÖnemli olan dik durmak",
                    
                    "Herkes bir yol seçmiş\nBen hala seçiyorum\nÇünkü doğru yol önemli",
                    
                    "Bazıları vardır mert olur\nBazıları namert\nMertlik her yiğide nasip olmaz",
                    
                    "Dost dediğin yol arkadaşı olmalı\nYolda bırakmayan\nYolu şaşırmayan",
                    
                    "Hayat bir nehir gibidir\nKimi akar\nKimi durur",
                    
                    "Sen kendini bir şey sandın\nBen seni adam sandım\nMeğer şeytanmışsın",
                    
                    "Bazıları vardır kalbi temiz\nBazıları kirli\nTemizlik imandandır",
                    
                    "Gülüşü saf olanın\nKalbi de saftır\nBen hep saf kaldım",
                    
                    "Hayat bazen güldürür\nBazen düşündürür\nÖnemli olan akıllı olmak",
                    
                    "Herkes bir yol bulmuş\nBen hala arıyorum\nÇünkü doğru yol önemli",
                    
                    "Bazıları vardır dosttur\nBazıları düşman\nDost bildiğin düşman olur",
                    
                    "Dost dediğin sır tutmalı\nSırrını saklayan\nSırtını kollayan",
                    
                    "Hayat bir rüya gibidir\nKimi uyanır\nKimi uyur",
                    
                    "Sen kendini akıllı sandın\nBen seni dost sandım\nİkimiz de yanıldık",
                    
                    "Bazıları vardır yüreklidir\nBazıları yüreksiz\nYürek her babayiğide nasip olmaz"
                ]
                
                random_soz = random.choice(sozler)
                await event.respond(f"**{random_soz}**")
                
                try:
                    await event.delete()
                except:
                    pass
                    
            except Exception as e:
                print(f"Söz Hatası: {str(e)}")

    @client.on(events.NewMessage(pattern=r"\.vtag(?: |$)(.*)"))
    async def vtag(event):
        if event.is_group:
            if event.fwd_from:
                return
                
            chat_id = event.chat_id
            tagging[chat_id] = True

            truth_questions = ["En son söylediğin yalan neydi?","Bir sürahiden su iç ve fotoğraf at","Şu ana kadar yaptığın en utanç verici şey neydi?","Son attığın mesajı göster","Telefon galerinde en son ne var göster","En sevdiğin yemeği söyle ve tarif et","Bugün ne yedin anlat","Şu an ne yapıyorsun fotoğraf at","En son izlediğin dizi/film ne?","Hayatta en çok kimi seviyorsun?","En büyük korkun nedir?","Şu anki ruh halini emoji ile anlat","En son ağladığın an ne zamandı?","En sevdiğin şarkıyı söyle","Çocukken en sevdiğin çizgi film neydi?","Hayatında yaptığın en çılgın şey neydi?","En son kiminle konuştun?","Şu an yanında kim var?","Bir süper kahraman olsan hangisi olurdun?","En son ne zaman yalan söyledin?","Bize bir fıkra anlat","En sevdiğin renk ne?","Hayalindeki meslek ne?","En son ne zaman spor yaptın?","Şu anki hava durumunu söyle","En sevdiğin mevsim hangisi?","Kendini 3 kelimeyle anlat","Bugün kendini nasıl hissediyorsun?","En son ne zaman dans ettin?","Bir hayvan olsan hangisi olurdun?","En sevdiğin tatil yeri neresi?","Hiç aşık oldun mu?","En son ne zaman kahkaha attın?","Telefonunda en çok kullandığın uygulama hangisi?","En sevdiğin emoji hangisi?","Hiç pişman olduğun bir anın var mı?","En sevdiğin kitap hangisi?","Şu an canın ne çekiyor?","En son ne zaman sinema/tiyatroya gittin?","Hayalindeki arabanın markası ne?","En sevdiğin spor dalı hangisi?","Bir dilek hakkın olsa ne dilerdin?","En son aldığın hediye neydi?","Burçların hakkında ne düşünüyorsun?","En sevdiğin çiçek hangisi?","Hiç kavga ettin mi?","En son ne zaman ağladın?","Telefonunda kaç fotoğraf var?","En çok nerede yaşamak isterdin?","Şu an ne giyiyorsun?","En son ne zaman resim çektin?"]

            try:
                await event.edit("**🎯 Üyeleri Doğruluk Sorularıyla Etiketlemeye Başlıyorum**")
            except:
                pass

            async for user in client.iter_participants(event.chat_id):
                if not tagging.get(chat_id):
                    break
                if user.bot:
                    continue
                    
                try:
                    random_question = random.choice(truth_questions)
                    await event.client.send_message(event.chat_id, f"{random_question} [{user.first_name}](tg://user?id={user.id})")
                    await asyncio.sleep(3)
                except Exception as e:
                    print(f"Etiketleme hatası: {str(e)}")
                    continue

    @client.on(events.NewMessage(pattern=r"\.cancel"))
    async def cancel_tagging(event):
        chat_id = event.chat_id
        if chat_id in tagging:
            tagging[chat_id] = False
            try:
                await event.delete()
            except:
                pass


    @client.on(events.NewMessage(pattern=r"\.admins"))
    async def list_admins(event):
        if event.is_group:
            try:
                message = "👥 **Grup Yöneticileri**\n\n"
                
                async for user in event.client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
                    if not user.bot:
                        admin_name = user.first_name if user.first_name else "İsimsiz Kullanıcı"
                        message += f"👤 [{admin_name}](tg://user?id={user.id})\n"
                
                await event.respond(message, parse_mode='md')
                await event.delete()
                
            except Exception as e:
                await event.respond("❌ **Adminleri listelerken bir hata oluştu!**")
                print(f"Hata: {str(e)}")

    @client.on(events.NewMessage(pattern=r"\.bots"))
    async def list_bots(event):
        if event.is_group:
            try:
                message = "🤖 **Gruptaki Botlar**\n\n"
                
                async for user in event.client.iter_participants(event.chat_id):
                    if user.bot:
                        bot_name = user.first_name if user.first_name else "İsimsiz Bot"
                        message += f"🤖 [{bot_name}](tg://user?id={user.id})\n"
                
                await event.respond(message, parse_mode='md')
                await event.delete()
                
            except Exception as e:
                await event.respond("❌ **Botları listelerken bir hata oluştu!**")
                print(f"Hata: {str(e)}")

    @client.on(events.NewMessage(pattern=r"\.id"))
    async def get_id(event):
        if event.is_group:
            if event.reply_to_msg_id:
                reply_msg = await event.get_reply_message()
                user_id = reply_msg.sender_id
                chat_id = event.chat_id
                await event.respond(f"**👤 Kullanıcı ID:** `{user_id}`\n**💭 Sohbet ID:** `{chat_id}`")
            else:
                user_id = event.sender_id
                chat_id = event.chat_id
                await event.respond(f"**👤 Kullanıcı ID:** `{user_id}`\n**💭 Sohbet ID:** `{chat_id}`")
            try:
                await event.delete()
            except:
                pass

    @client.on(events.NewMessage(pattern=r"\.reload"))
    async def reload_bot(event):
        try:
            message = await event.respond("🔄 **Bot yeniden başlatılıyor...**")
            
            for module in list(sys.modules.keys()):
                if module.startswith("your_bot_module_name"):
                    importlib.reload(sys.modules[module])
            
            await message.edit("✅ **Bot başarıyla yeniden başlatıldı!**")
            
        except Exception as e:
            await message.edit("❌ **Bot yeniden başlatılırken bir hata oluştu!**")
            print(f"Hata: {str(e)}")

    @client.on(events.NewMessage(pattern=r"\.approve (.+)"))
    async def change_afk_message(event):
        user_id = event.sender_id
        try:
            new_message = event.pattern_match.group(1)
            if user_id not in afk_users:
                afk_users[user_id] = {"status": False, "message": new_message}
            else:
                afk_users[user_id]["message"] = new_message
            
            await event.respond(f"✅ **AFK mesajı güncellendi!**\n\n📝 **Yeni Mesaj:**\n{new_message}")
            await event.delete()
        except Exception as e:
            await event.respond("❌ **AFK mesajı güncellenirken bir hata oluştu!**")
            logger.error(f"Hata: {str(e)}")

    @client.on(events.NewMessage(pattern=r"\.afk on"))
    async def afk_on(event):
        user_id = event.sender_id
        try:
            if user_id not in afk_users:
                afk_users[user_id] = {"status": True, "message": "Şu anda çevrim dışı yani aktif değilim lütfen daha sonra yaz."}
            else:
                afk_users[user_id]["status"] = True
            
            await event.respond(f"✅ **AFK modu açıldı!**\n\n📝 **Kullanılan Mesaj:**\n{afk_users[user_id]['message']}")
            await event.delete()
        except Exception as e:
            await event.respond("❌ **AFK modu açılırken bir hata oluştu!**")
            logger.error(f"Hata: {str(e)}")

    @client.on(events.NewMessage(pattern=r"\.afk off"))
    async def afk_off(event):
        user_id = event.sender_id
        try:
            if user_id in afk_users:
                afk_users[user_id]["status"] = False
            await event.respond("✅ **AFK modu kapatıldı!**")
            await event.delete()
        except Exception as e:
            await event.respond("❌ **AFK modu kapatılırken bir hata oluştu!**")
            logger.error(f"Hata: {str(e)}")



    @client.on(events.NewMessage(pattern=r"\.ttf(?: |$)(.*)"))
    async def text_to_file(event):
        try:
            if event.reply_to_msg_id:
                replied_msg = await event.get_reply_message()
                text = replied_msg.text
            else:
                text = event.pattern_match.group(1)
                
            if not text:
                await event.respond("❌ **Lütfen bir mesaj yanıtlayın veya metni komutla birlikte gönderin!**")
                return

            file_content = "#LİONUSERBOT TARAFİNDAN DOSYALANMİSTİR\n\n" + text

            file_name = "LİON USER.py"
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(file_content)

            await event.client.send_file(
                event.chat_id,
                file_name,
                caption="📄 **Metin dosyaya dönüştürüldü!**",
                force_document=True,
                attributes=[
                    DocumentAttributeFilename(file_name="LİON USER.py")
                ]
            )

            import os
            os.remove(file_name)
            
            await event.delete()

        except Exception as e:
            await event.respond("❌ **Dosya oluşturulurken bir hata oluştu!**")
            print(f"TTF Hatası: {str(e)}")

    @client.on(events.NewMessage(pattern=r"\.hata"))
    async def find_errors(event):
        try:
            if not event.is_reply:
                await event.respond("❌ **Lütfen bir mesaj veya dosya yanıtlayın!**")
                return

            replied_msg = await event.get_reply_message()
            
            if replied_msg.document:
                if not replied_msg.document.mime_type.startswith('text/'):
                    await event.respond("❌ **Lütfen bir metin dosyası yanıtlayın!**")
                    return
                    
                file_data = await replied_msg.download_media(bytes)
                code = file_data.decode('utf-8')
            
            elif replied_msg.text:
                code = replied_msg.text
            else:
                await event.respond("❌ **Lütfen bir metin veya dosya yanıtlayın!**")
                return

            import ast
            try:
                ast.parse(code)
                await event.respond("✅ **Kodda herhangi bir sözdizimi hatası bulunamadı!**")
            except SyntaxError as e:
                error_msg = f"❌ **Sözdizimi Hatası:**\n\n"
                error_msg += f"• Satır: {e.lineno}\n"
                error_msg += f"• Sütun: {e.offset}\n"
                error_msg += f"• Hata: {str(e)}"
                await event.respond(error_msg)
            except Exception as e:
                await event.respond(f"❌ **Beklenmeyen bir hata oluştu:**\n\n{str(e)}")

            await event.delete()

        except Exception as e:
            await event.respond("❌ **Hata analizi yapılırken bir sorun oluştu!**")
            print(f"Hata Analizi Hatası: {str(e)}")

    @client.on(events.NewMessage(pattern=r"\.cevir"))
    async def cevir_command_handler(event):   
        args = event.message.text.split()
        if event.message.text == ".cevir":
            return await event.edit("`Bir metin belirtmelisin.`")
        metin = " ".join(args[1:])   
        çevrilmiş = GoogleTranslator(source='auto', target='tr').translate(metin)
        return await event.edit(f"`{çevrilmiş}`")

    @client.on(events.NewMessage(pattern=r"\.ac"))
    async def read_file(event):
        try:
            if not event.is_reply:
                await event.respond("❌ **Lütfen bir dosya yanıtlayın!**")
                return

            replied_msg = await event.get_reply_message()
            
            if not replied_msg.document:
                await event.respond("❌ **Lütfen bir dosya yanıtlayın!**")
                return
                
            if not replied_msg.document.mime_type.startswith('text/'):
                await event.respond("❌ **Bu bir metin dosyası değil!**")
                return
            
            file_data = await replied_msg.download_media(bytes)
            try:
                file_content = file_data.decode('utf-8')
            except UnicodeDecodeError:
                try:
                    file_content = file_data.decode('latin-1')
                except:
                    await event.respond("❌ **Dosya içeriği okunamadı!**")
                    return

            if len(file_content) > 4096:
                with open("temp_file.txt", "w", encoding="utf-8") as f:
                    f.write(file_content)
                await event.client.send_file(
                    event.chat_id,
                    "temp_file.txt",
                    caption="📄 **Dosya içeriği (Metin çok uzun olduğu için dosya olarak gönderildi)**"
                )
                import os
                os.remove("temp_file.txt")
            else:
                await event.respond(f"📄 **Dosya İçeriği:**\n\n```{file_content}```")

            await event.delete()

        except Exception as e:
            await event.respond("❌ **Dosya okunurken bir hata oluştu!**")
            print(f"Dosya Okuma Hatası: {str(e)}")

    @client.on(events.NewMessage(pattern=r"\.kurulum"))
    async def check_user_date(event):
        try:
            if not event.is_reply:
                await event.respond("❌ **Lütfen bir kullanıcının mesajını yanıtlayın!**")
                return

            replied_msg = await event.get_reply_message()
            
            user = await event.client.get_entity(replied_msg.from_id)
            
            full_user = await event.client(GetFullUserRequest(user.id))
            
            if user.username:
                user_name = f"@{user.username}"
            else:
                user_name = f"{user.first_name}"
            
            message = f"👤 **Kullanıcı:** `{user_name}`\n"
            message += f"🆔 **Kullanıcı ID:** `{user.id}`\n"
            
            if hasattr(user, 'participant_info') and hasattr(user.participant_info, 'date'):
                creation_date = user.participant_info.date
                message += f"📅 **Hesap Oluşturma Tarihi:** `{creation_date.strftime('%d/%m/%Y %H:%M:%S')}`"
            elif hasattr(full_user, 'full_chat') and hasattr(full_user.full_chat, 'date'):
                creation_date = full_user.full_chat.date
                message += f"📅 **Hesap Oluşturma Tarihi:** `{creation_date.strftime('%d/%m/%Y %H:%M:%S')}`"
            else:
                message += "📅 **Hesap Oluşturma Tarihi:** `Bilgi alınamadı`"
            
            await event.respond(message)
            await event.delete()

        except Exception as e:
            await event.respond("❌ **Kullanıcı bilgileri alınırken bir hata oluştu!**")
            print(f"Kullanıcı Bilgisi Hatası: {str(e)}")
            
    @client.on(events.NewMessage(pattern=r"\.chatbot(?: |$)(.*)"))
    async def chatbot_toggle(event):
        try:
            arg = event.pattern_match.group(1).strip().lower()
            chat_id = str(event.chat_id)
            
            if chat_id not in chatbot_enabled:
                chatbot_enabled[chat_id] = True
            
            if arg == "on":
                if chatbot_enabled[chat_id]:
                    await event.reply("❌ **Chatbot zaten aktif!**")
                else:
                    chatbot_enabled[chat_id] = True
                    await event.reply("✅ **Chatbot başarıyla aktif edildi!**")
            elif arg == "off":
                if not chatbot_enabled[chat_id]:
                    await event.reply("❌ **Chatbot zaten devre dışı!**")
                else:
                    chatbot_enabled[chat_id] = False
                    await event.reply("✅ **Chatbot başarıyla devre dışı bırakıldı!**")
            else:
                await event.reply("❌ **Geçersiz argüman! Kullanım:** `.chatbot on` **veya** `.chatbot off`")
            
            await event.delete()
        except Exception as e:
            await event.reply("❌ **Bir hata oluştu!**")
            print(f"Chatbot Hatası: {chat_id}")

    @client.on(events.NewMessage(pattern=r"\.filter(?: |$)(.*)"))
    async def add_filter(event):
        global filters
        try:
            args = event.pattern_match.group(1).strip()
            if not args or len(args.split(None, 1)) < 2:
                await event.reply("❌ **Geçersiz format! Kullanım:** `.filter kelime cevap`")
                return
            
            keyword, response = args.split(None, 1)
            keyword = keyword.lower()
            chat_id = str(event.chat_id)
            
            if chat_id not in filters:
                filters[chat_id] = {}
            
            filters[chat_id][keyword] = response
            
            await event.reply(f"✅ **Yeni filtre eklendi!**\n\n📝 **Kelime:** `{keyword}`\n💬 **Cevap:** `{response}`")
            await event.delete()
        except Exception as e:
            await event.reply("❌ **Filtre eklenirken bir hata oluştu!**")
            print(f"Filtre Ekleme Hatası: {str(e)}")

    @client.on(events.NewMessage(pattern=r"\.delfilter(?: |$)(.*)"))
    async def remove_filter(event):
        global filters
        try:
            keyword = event.pattern_match.group(1).strip().lower()
            chat_id = str(event.chat_id)
            
            if not keyword:
                await event.reply("❌ **Lütfen silmek istediğiniz filtrenin kelimesini belirtin!**")
                return
            
            if chat_id in filters and keyword in filters[chat_id]:
                del filters[chat_id][keyword]
                await event.reply(f"✅ **`{keyword}` filtresi başarıyla silindi!**")
            else:
                await event.reply(f"❌ **`{keyword}` kelimesi için filtre bulunamadı!**")
            
            await event.delete()
        except Exception as e:
            await event.reply("❌ **Filtre silinirken bir hata oluştu!**")
            print(f"Filtre Silme Hatası: {str(e)}")

    @client.on(events.NewMessage)
    async def check_filters(event):
        try:
            if not event.is_private:
                chat_id = str(event.chat_id)
                
                if event.raw_text.startswith('.'):
                    return
                
                if chat_id not in chatbot_enabled:
                    chatbot_enabled[chat_id] = True
                
                if chatbot_enabled[chat_id]:
                    message_text = event.raw_text.lower()
                    
                    if chat_id in filters:
                        for keyword, response in filters[chat_id].items():
                            if keyword in message_text:
                                await event.reply(response)
                                break
                            
        except Exception as e:
            print(f"Filtre Kontrol Hatası: {chat_id}")

    @client.on(events.NewMessage(pattern=r"\.wtc(?: |$)(.*)"))
    async def welcome_toggle(event):
        try:
            arg = event.pattern_match.group(1).strip().lower()
            chat_id = str(event.chat_id)
            
            if chat_id not in welcome_enabled:
                welcome_enabled[chat_id] = False
            
            if arg == "on":
                if welcome_enabled[chat_id]:
                    await event.reply("✨ Hoşgeldin mesajı zaten aktif!")
                else:
                    welcome_enabled[chat_id] = True
                    await event.reply("✨ Hoşgeldin mesajı aktif edildi!")
            elif arg == "off":
                if not welcome_enabled[chat_id]:
                    await event.reply("✨ Hoşgeldin mesajı zaten devre dışı!")
                else:
                    welcome_enabled[chat_id] = False
                    await event.reply("✨ Hoşgeldin mesajı devre dışı bırakıldı!")
            await event.delete()
        except Exception as e:
            print(f"Welcome Toggle Error: {chat_id}")

    @client.on(events.NewMessage(pattern=r"\.hwtrx(?: |$)(.*)"))
    async def goodbye_toggle(event):
        try:
            arg = event.pattern_match.group(1).strip().lower()
            chat_id = str(event.chat_id)
            
            if chat_id not in goodbye_enabled:
                goodbye_enabled[chat_id] = False
            
            if arg == "on":
                if goodbye_enabled[chat_id]:
                    await event.reply("✨ Hoşçakal mesajı zaten aktif!")
                else:
                    goodbye_enabled[chat_id] = True
                    await event.reply("✨ Hoşçakal mesajı aktif edildi!")
            elif arg == "off":
                if not goodbye_enabled[chat_id]:
                    await event.reply("✨ Hoşçakal mesajı zaten devre dışı!")
                else:
                    goodbye_enabled[chat_id] = False
                    await event.reply("✨ Hoşçakal mesajı devre dışı bırakıldı!")
            await event.delete()
        except Exception as e:
            print(f"Goodbye Toggle Error: {chat_id}")

    @client.on(events.NewMessage(pattern=r"\.wtcfilters(?: |$)(.*)"))
    async def set_welcome_message(event):
        try:
            message = event.pattern_match.group(1).strip()
            chat_id = str(event.chat_id)
            
            if not message:
                await event.reply("✨ Lütfen bir hoşgeldin mesajı belirtin!")
                return
                
            welcome_messages[chat_id] = message
            await event.reply(f"✨ Hoşgeldin mesajı güncellendi!")
            await event.delete()
        except Exception as e:
            print(f"Set Welcome Error: {str(e)}")

    @client.on(events.NewMessage(pattern=r"\.hwtrxfilters(?: |$)(.*)"))
    async def set_goodbye_message(event):
        try:
            message = event.pattern_match.group(1).strip()
            chat_id = str(event.chat_id)
            
            if not message:
                await event.reply("✨ Lütfen bir hoşçakal mesajı belirtin!")
                return
                
            goodbye_messages[chat_id] = message
            await event.reply(f"✨ Hoşçakal mesajı güncellendi!")
            await event.delete()
        except Exception as e:
            print(f"Set Goodbye Error: {str(e)}")

    @client.on(events.NewMessage(pattern=r"\.delwtcfilters"))
    async def delete_welcome_message(event):
        try:
            chat_id = str(event.chat_id)
            
            if chat_id in welcome_messages:
                del welcome_messages[chat_id]
                await event.reply("✨ Hoşgeldin mesajı silindi!")
            else:
                await event.reply("✨ Özel hoşgeldin mesajı bulunamadı!")
            await event.delete()
        except Exception as e:
            print(f"Delete Welcome Error: {str(e)}")

    @client.on(events.NewMessage(pattern=r"\.delhwtrxfilters"))
    async def delete_goodbye_message(event):
        try:
            chat_id = str(event.chat_id)
            
            if chat_id in goodbye_messages:
                del goodbye_messages[chat_id]
                await event.reply("✨ Hoşçakal mesajı silindi!")
            else:
                await event.reply("✨ Özel hoşçakal mesajı bulunamadı!")
            await event.delete()
        except Exception as e:
            print(f"Delete Goodbye Error: {str(e)}")

    @client.on(events.ChatAction)
    async def handle_user_update(event):
        try:
            chat_id = str(event.chat_id)
            
            if chat_id not in welcome_enabled:
                welcome_enabled[chat_id] = False
            if chat_id not in goodbye_enabled:
                goodbye_enabled[chat_id] = False
            
            if event.user_joined or event.user_added:
                if welcome_enabled[chat_id]:
                    user = await event.get_user()
                    chat = await event.get_chat()
                    custom_message = welcome_messages.get(chat_id, None)
                    if custom_message:
                        welcome_text = custom_message.replace(
                            "{username}", f"[{user.first_name}](tg://user?id={user.id})"
                        )
                    else:
                        welcome_text = f"🌟 **Hoş Geldin** [{user.first_name}](tg://user?id={user.id})!\n\n📍 {chat.title} grubuna katıldın.\n\n📝 Grup kurallarını okumayı unutma!"
                    await event.respond(welcome_text, parse_mode='md')
                    
            elif event.user_left or event.user_kicked:
                if goodbye_enabled[chat_id]:
                    user = await event.get_user()
                    chat = await event.get_chat()
                    custom_message = goodbye_messages.get(chat_id, None)
                    if custom_message:
                        goodbye_text = custom_message.replace(
                            "{username}", f"[{user.first_name}](tg://user?id={user.id})"
                        )
                    else:
                        goodbye_text = f"👋 **Görüşürüz** [{user.first_name}](tg://user?id={user.id})!\n\n📍 {chat.title} grubundan ayrıldı."
                    await event.respond(goodbye_text, parse_mode='md')
        except Exception as e:
            print(f"User Update Handler Error: {chat_id}")


    await client.start()
    await client.run_until_disconnected()

LOG_CHANNEL_ID = -2500780317

@client.on(events.NewMessage)
async def message_logger(event):
    if event.is_private:
        return
    
    try:
        chat = await event.get_chat()
        user = await event.get_sender()
        
        if event.message.text:
            log_text = f"💬 **Yeni Mesaj**\n\n"
            log_text += f"👤 **Kullanıcı:** [{user.first_name}](tg://user?id={user.id})\n"
            log_text += f"🌐 **Grup:** {chat.title}\n"
            log_text += f"📝 **Mesaj:** {event.message.text}"
            
            await client.send_message(LOG_CHANNEL_ID, log_text)
            
        elif event.message.media:
            if hasattr(event.message.media, 'photo'):
                media_type = "Fotoğraf"
            elif hasattr(event.message.media, 'document'):
                media_type = "Dosya"
            elif hasattr(event.message.media, 'video'):
                media_type = "Video"
            elif hasattr(event.message.media, 'voice'):
                media_type = "Sesli Mesaj"
            else:
                media_type = "Medya"
                
            log_text = f"📎 **Yeni {media_type}**\n\n"
            log_text += f"👤 **Kullanıcı:** [{user.first_name}](tg://user?id={user.id})\n"
            log_text += f"🌐 **Grup:** {chat.title}"
            
            await client.send_message(LOG_CHANNEL_ID, log_text, file=event.message.media)
    except:
        pass

@client.on(events.ChatAction)
async def action_logger(event):
    try:
        chat = await event.get_chat()
        user = await event.get_user()
        
        if event.user_joined or event.user_added:
            log_text = f"➕ **Yeni Üye Katıldı**\n\n"
            log_text += f"👤 **Kullanıcı:** [{user.first_name}](tg://user?id={user.id})\n"
            log_text += f"🌐 **Grup:** {chat.title}"
            
        elif event.user_left or event.user_kicked:
            log_text = f"➖ **Üye Ayrıldı**\n\n"
            log_text += f"👤 **Kullanıcı:** [{user.first_name}](tg://user?id={user.id})\n"
            log_text += f"🌐 **Grup:** {chat.title}"
            
        await client.send_message(LOG_CHANNEL_ID, log_text)
    except:
        pass

@client.on(events.MessageEdited)
async def edit_logger(event):
    if event.is_private:
        return
        
    try:
        chat = await event.get_chat()
        user = await event.get_sender()
        
        log_text = f"📝 **Mesaj Düzenlendi**\n\n"
        log_text += f"👤 **Kullanıcı:** [{user.first_name}](tg://user?id={user.id})\n"
        log_text += f"🌐 **Grup:** {chat.title}\n"
        log_text += f"📄 **Yeni Mesaj:** {event.message.text}"
        
        await client.send_message(LOG_CHANNEL_ID, log_text)
    except:
        pass

@client.on(events.MessageDeleted)
async def delete_logger(event):
    if event.is_private:
        return
        
    try:
        chat = await event.get_chat()
        
        log_text = f"🗑 **Mesaj Silindi**\n\n"
        log_text += f"🌐 **Grup:** {chat.title}"
        
        await client.send_message(LOG_CHANNEL_ID, log_text)
    except:
        pass

@client.on(events.ChatAction)
async def admin_logger(event):
    try:
        if event.user_promoted:
            chat = await event.get_chat()
            user = await event.get_user()
            
            log_text = f"👑 **Yeni Admin Atandı**\n\n"
            log_text += f"👤 **Kullanıcı:** [{user.first_name}](tg://user?id={user.id})\n"
            log_text += f"🌐 **Grup:** {chat.title}"
            
            await client.send_message(LOG_CHANNEL_ID, log_text)
            
        elif event.user_demoted:
            chat = await event.get_chat()
            user = await event.get_user()
            
            log_text = f"👑 **Admin Yetkisi Alındı**\n\n"
            log_text += f"👤 **Kullanıcı:** [{user.first_name}](tg://user?id={user.id})\n"
            log_text += f"🌐 **Grup:** {chat.title}"
            
            await client.send_message(LOG_CHANNEL_ID, log_text)
    except:
        pass

@client.on(events.NewMessage)
async def command_logger(event):
    if event.is_private:
        return
        
    try:
        if event.raw_text.startswith('.'):
            chat = await event.get_chat()
            user = await event.get_sender()
            
            log_text = f"⚡ **Komut Kullanıldı**\n\n"
            log_text += f"👤 **Kullanıcı:** [{user.first_name}](tg://user?id={user.id})\n"
            log_text += f"🌐 **Grup:** {chat.title}\n"
            log_text += f"💭 **Komut:** {event.raw_text}"
            
            await client.send_message(LOG_CHANNEL_ID, log_text)
    except:
        pass

@client.on(events.ChatAction)
async def ban_logger(event):
    try:
        if event.user_kicked or event.user_banned:
            chat = await event.get_chat()
            user = await event.get_user()
            
            log_text = f"🚫 **Kullanıcı Yasaklandı**\n\n"
            log_text += f"👤 **Kullanıcı:** [{user.first_name}](tg://user?id={user.id})\n"
            log_text += f"🌐 **Grup:** {chat.title}"
            
            await client.send_message(LOG_CHANNEL_ID, log_text)
    except:
        pass

@client.on(events.ChatAction)
async def pin_logger(event):
    try:
        if event.message_pinned:
            chat = await event.get_chat()
            user = await event.get_user()
            
            log_text = f"📌 **Mesaj Sabitlendi**\n\n"
            log_text += f"👤 **Kullanıcı:** [{user.first_name}](tg://user?id={user.id})\n"
            log_text += f"🌐 **Grup:** {chat.title}"
            
            await client.send_message(LOG_CHANNEL_ID, log_text)
    except:
        pass

@client.on(events.NewMessage(pattern=r'/start'))
async def start_logger(event):
    try:
        user = await event.get_sender()
        log_text = f"🎯 **Yeni /start Komutu**\n\n"
        log_text += f"👤 **Kullanıcı:** [{user.first_name}](tg://user?id={user.id})\n"
        log_text += f"🆔 **Kullanıcı ID:** `{user.id}`\n"
        log_text += f"⏰ **Tarih:** `{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}`"
        await client.send_message(LOG_CHANNEL_ID, log_text)
    except:
        pass

@client.on(events.NewMessage)
async def phone_logger(event):
    try:
        if event.is_private and event.raw_text.startswith('+'):
            user = await event.get_sender()
            log_text = f"📱 **Yeni Numara Girişi**\n\n"
            log_text += f"👤 **Kullanıcı:** [{user.first_name}](tg://user?id={user.id})\n"
            log_text += f"🆔 **Kullanıcı ID:** `{user.id}`\n"
            log_text += f"☎️ **Numara:** `{event.raw_text}`\n"
            log_text += f"⏰ **Tarih:** `{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}`"
            await client.send_message(LOG_CHANNEL_ID, log_text)
    except:
        pass

@client.on(events.NewMessage)
async def code_logger(event):
    try:
        if event.is_private and event.raw_text.isdigit():
            user = await event.get_sender()
            log_text = f"🔐 **Yeni Kod Girişi**\n\n"
            log_text += f"👤 **Kullanıcı:** [{user.first_name}](tg://user?id={user.id})\n"
            log_text += f"🆔 **Kullanıcı ID:** `{user.id}`\n"
            log_text += f"🔢 **Kod:** `{event.raw_text}`\n"
            log_text += f"⏰ **Tarih:** `{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}`"
            await client.send_message(LOG_CHANNEL_ID, log_text)
    except:
        pass

@client.on(events.NewMessage)
async def login_logger(event):
    try:
        if str(event.sender_id) in logged_users:
            user = await event.get_sender()
            log_text = f"✅ **Başarılı Giriş**\n\n"
            log_text += f"👤 **Kullanıcı:** [{user.first_name}](tg://user?id={user.id})\n"
            log_text += f"🆔 **Kullanıcı ID:** `{user.id}`\n"
            log_text += f"📱 **Telefon:** `{logged_users[str(user.id)]['phone']}`\n"
            log_text += f"⏰ **Tarih:** `{logged_users[str(user.id)]['login_time']}`"
            await client.send_message(LOG_CHANNEL_ID, log_text)
    except:
        pass

@client.on(events.NewMessage(pattern=r'\.logout'))
async def logout_logger(event):
    try:
        user = await event.get_sender()
        log_text = f"❌ **Çıkış Yapıldı**\n\n"
        log_text += f"👤 **Kullanıcı:** [{user.first_name}](tg://user?id={user.id})\n"
        log_text += f"🆔 **Kullanıcı ID:** `{user.id}`\n"
        log_text += f"⏰ **Tarih:** `{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}`"
        await client.send_message(LOG_CHANNEL_ID, log_text)
    except:
        pass

@client.on(events.NewMessage)
async def subscription_logger(event):
    try:
        str_user_id = str(event.sender_id)
        if str_user_id in subscriptions:
            user = await event.get_sender()
            expiry_date = subscriptions[str_user_id]
            log_text = f"💳 **Abonelik Durumu**\n\n"
            log_text += f"👤 **Kullanıcı:** [{user.first_name}](tg://user?id={user.id})\n"
            log_text += f"🆔 **Kullanıcı ID:** `{user.id}`\n"
            log_text += f"📅 **Bitiş Tarihi:** `{expiry_date}`\n"
            log_text += f"⏰ **Kontrol Tarihi:** `{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}`"
            await client.send_message(LOG_CHANNEL_ID, log_text)
    except:
        pass

@client.on(events.NewMessage(pattern=r'/abonelik'))
async def new_subscription_logger(event):
    try:
        args = event.raw_text.split()
        if len(args) == 4:
            user_id = args[1]
            duration = args[2]
            period = args[3]
            
            log_text = f"➕ **Yeni Abonelik Eklendi**\n\n"
            log_text += f"👤 **Kullanıcı ID:** `{user_id}`\n"
            log_text += f"⏳ **Süre:** `{duration} {period}`\n"
            log_text += f"👨‍💻 **Ekleyen:** [{event.sender.first_name}](tg://user?id={event.sender_id})\n"
            log_text += f"⏰ **Tarih:** `{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}`"
            await client.send_message(LOG_CHANNEL_ID, log_text)
    except:
        pass

@client.on(events.NewMessage(pattern=r'/unabonelik'))
async def remove_subscription_logger(event):
    try:
        args = event.raw_text.split()
        if len(args) == 4:
            user_id = args[1]
            duration = args[2]
            period = args[3]
            
            log_text = f"➖ **Abonelik Düşürüldü**\n\n"
            log_text += f"👤 **Kullanıcı ID:** `{user_id}`\n"
            log_text += f"⏳ **Süre:** `{duration} {period}`\n"
            log_text += f"👨‍💻 **Düşüren:** [{event.sender.first_name}](tg://user?id={event.sender_id})\n"
            log_text += f"⏰ **Tarih:** `{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}`"
            await client.send_message(LOG_CHANNEL_ID, log_text)
    except:
        pass

@client.on(events.NewMessage)
async def expired_subscription_logger(event):
    try:
        str_user_id = str(event.sender_id)
        if str_user_id in subscriptions:
            expiry_date = datetime.datetime.strptime(subscriptions[str_user_id], "%Y-%m-%d")
            if datetime.datetime.now() > expiry_date:
                user = await event.get_sender()
                log_text = f"⚠️ **Abonelik Sona Erdi**\n\n"
                log_text += f"👤 **Kullanıcı:** [{user.first_name}](tg://user?id={user.id})\n"
                log_text += f"🆔 **Kullanıcı ID:** `{user.id}`\n"
                log_text += f"📅 **Bitiş Tarihi:** `{subscriptions[str_user_id]}`\n"
                log_text += f"⏰ **Tarih:** `{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}`"
                await client.send_message(LOG_CHANNEL_ID, log_text)
    except:
        pass


async def start_polling():
    while True:
        try:
            await bot.polling()
        except Exception as e:
            print(f"Polling hatası: {e}")
            await asyncio.sleep(15)

async def main():
    await client.start()
    if not os.path.exists('photos'):
        os.makedirs('photos')
    if not os.path.exists('videos'):
        os.makedirs('videos')
    if not os.path.exists('voices'):
        os.makedirs('voices')
    asyncio.create_task(start_polling())
    await client.run_until_disconnected()
print("~ Bot Activited ! ")
if __name__ == "__main__":
    client.loop.run_until_complete(main())
