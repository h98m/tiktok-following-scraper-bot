import telebot
import requests
import re
import os
import random

TOKEN = "هنا التوكن "
bot = telebot.TeleBot(TOKEN)

headers = {
    'User-Agent': 'com.zhiliaoapp.musically.go/370402 (Linux; U; Android 14; ar_EG; TECNO CL6; Build/UP1A.231005.007;tt-ok/3.12.13.27-ul)',
    'x-argus': 'nACUDEstLAyVsIIH2FWhr5B53PG5VL9E77ywN5oGIXYEG9nXz0AsSxa/...'  
}
cookies2 = {
    '_ttp': '2vgirjOnuSrSOnprbKT4f6H0h4U',
    'tt_chain_token': 'aI+tyWRBH/hxDwK2jQqVFg==',
}
headers2 = {
    'user-agent': 'Mozilla/5.0 ... Mobile Safari/537.36',
}

user_states = {}

def extract_ids(username, cookies2, headers2):
    url = f"https://www.tiktok.com/@{username}"
    response = requests.get(url, cookies=cookies2, headers=headers2)
    pattern = r'"webapp.user-detail":\{"userInfo":\{"user":\{"id":"(\d+)",.*?"secUid":"([^"]+)"'
    match = re.search(pattern, response.text, re.DOTALL)
    if match:
        return match.group(1), match.group(2)
    return None, None

def fetch_followings(user_id, sec_user_id, chat_id=None, message_id=None, username_display=""):
    c = '0123456789abcdef'
    session = ''.join(random.choices(c, k=32))
    cookies = {
        'sessionid': session,
        'sessionid_ss': session,
        'sid_tt': session,
    }

    cursor = "0"
    followings = []

    while True:
        url = f"https://api19-normal-c-alisg.tiktokv.com/lite/v2/relation/following/list/?user_id={user_id}&count=50&page_token={cursor}&sec_user_id={sec_user_id}"
        try:
            response = requests.get(url, headers=headers, cookies=cookies, timeout=15)
            data = response.json()
        except:
            break

        for user in data.get("followings", []):
            username = user.get("unique_id")
            follower_count = user.get("follower_count", 0)
            if username:
                followings.append((username, follower_count))

            if chat_id and message_id and len(followings) % 10 == 0:
                try:
                    bot.edit_message_text(
                        chat_id=chat_id,
                        message_id=message_id,
                        text=f"جارٍ استخراج المتابَعين للحساب @{username_display} 🔍\n📦 تم جمع {len(followings)} متابَعًا حتى الآن..."
                    )
                except Exception as e:
                    print(f"فشل في التحديث: {e}")

        cursor = data.get("next_page_token")
        has_more = data.get("rec_has_more", False)
        if not has_more or not cursor:
            break

    return followings


@bot.message_handler(commands=['start'])
def start(message):
    user_states[message.chat.id] = "WAIT_USERNAME"
    bot.send_message(message.chat.id, "أرسل اسم المستخدم (بدون @) لبدء استخراج المتابَعين ")

@bot.message_handler(func=lambda m: user_states.get(m.chat.id) == "WAIT_USERNAME")
def handle_username(message):
    username = str(message.text).strip().replace("@", "")
    user_states[message.chat.id] = None

    sent_msg = bot.send_message(message.chat.id, f"جارٍ استخراج المتابَعين للحساب @{username} ")

    user_id, sec_uid = extract_ids(username, cookies2, headers2)
    if not user_id or not sec_uid:
        bot.edit_message_text(" لم أتمكن من العثور على الحساب.", chat_id=message.chat.id, message_id=sent_msg.message_id)
        return

    followings = fetch_followings(
        user_id,
        sec_uid,
        chat_id=message.chat.id,
        message_id=sent_msg.message_id,
        username_display=username
    )

    if not followings:
        bot.edit_message_text(" لم يتم العثور على متابَعين.", chat_id=message.chat.id, message_id=sent_msg.message_id)
        return

    filename = f"{user_id}_followings.txt"
    with open(filename, "w", encoding="utf-8") as f:
        for username, count in followings:
            f.write(f"{username}\n")

    caption = f" تم العثور على {len(followings)} متابَعًا "
    with open(filename, "rb") as f:
        bot.edit_message_text(f" جاري إرسال النتائج ...", chat_id=message.chat.id, message_id=sent_msg.message_id)
        bot.send_document(message.chat.id, f, caption=caption)

    try:
        os.remove(filename)
    except Exception as e:
        print(f"خطأ حذف الملف: {e}")


@bot.message_handler(commands=['stop'])
def stop(message):
    user_states[message.chat.id] = None
    bot.send_message(message.chat.id, "تم إيقاف العملية. أرسل /start للبدء من جديد.")

print(" البوت يعمل الآن وسيسحب فقط المتابَعين بدون شروط ")
bot.infinity_polling()
