{\rtf1\ansi\ansicpg1251\cocoartf2820
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww28600\viewh14940\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup\
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes\
import os\
\
TOKEN = os.getenv("BOT_TOKEN")\
\
COURSES = [\
    \{"title": "\uc0\u1050 \u1091 \u1088 \u1089  \u1087 \u1086  Python", "price": "1000", "details": "\u1048 \u1079 \u1091 \u1095 \u1080 \u1090 \u1077  Python \u1089  \u1085 \u1091 \u1083 \u1103 ."\},\
    \{"title": "\uc0\u1050 \u1091 \u1088 \u1089  \u1087 \u1086  Web-\u1088 \u1072 \u1079 \u1088 \u1072 \u1073 \u1086 \u1090 \u1082 \u1077 ", "price": "2000", "details": "\u1053 \u1072 \u1091 \u1095 \u1080 \u1090 \u1077 \u1089 \u1100  \u1089 \u1086 \u1079 \u1076 \u1072 \u1074 \u1072 \u1090 \u1100  \u1089 \u1072 \u1081 \u1090 \u1099 ."\},\
]\
\
def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:\
    keyboard = [[InlineKeyboardButton(course['title'], callback_data=f"course_\{i\}")]\
                for i, course in enumerate(COURSES)]\
    reply_markup = InlineKeyboardMarkup(keyboard)\
    update.message.reply_text("\uc0\u1044 \u1086 \u1073 \u1088 \u1086  \u1087 \u1086 \u1078 \u1072 \u1083 \u1086 \u1074 \u1072 \u1090 \u1100 ! \u1042 \u1099 \u1073 \u1077 \u1088 \u1080 \u1090 \u1077  \u1082 \u1091 \u1088 \u1089 :", reply_markup=reply_markup)\
\
def course_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:\
    query = update.callback_query\
    query.answer()\
    data = query.data\
    if data.startswith("course_"):\
        course_id = int(data.split("_")[1])\
        course = COURSES[course_id]\
        text = (f"**\{course['title']\}**\\n\uc0\u1062 \u1077 \u1085 \u1072 : \{course['price']\} \u1088 \u1091 \u1073 .\\n\\n"\
                f"\{course['details']\}\\n\\n"\
                f"\uc0\u1044 \u1083 \u1103  \u1086 \u1087 \u1083 \u1072 \u1090 \u1099  \u1087 \u1077 \u1088 \u1077 \u1074 \u1077 \u1076 \u1080 \u1090 \u1077  \u1076 \u1077 \u1085 \u1100 \u1075 \u1080  \u1085 \u1072  \u1082 \u1072 \u1088 \u1090 \u1091 : 1234 5678 9012 3456 \u1080  \u1086 \u1090 \u1087 \u1088 \u1072 \u1074 \u1100 \u1090 \u1077  \u1095 \u1077 \u1082 .")\
        query.edit_message_text(text, parse_mode="Markdown")\
\
def main():\
    if not TOKEN:\
        print("\uc0\u1054 \u1096 \u1080 \u1073 \u1082 \u1072 : \u1053 \u1077  \u1085 \u1072 \u1081 \u1076 \u1077 \u1085  \u1090 \u1086 \u1082 \u1077 \u1085  \u1073 \u1086 \u1090 \u1072  \u1074  \u1087 \u1077 \u1088 \u1077 \u1084 \u1077 \u1085 \u1085 \u1086 \u1081  \u1086 \u1082 \u1088 \u1091 \u1078 \u1077 \u1085 \u1080 \u1103  BOT_TOKEN")\
        return\
\
    application = Application.builder().token(TOKEN).build()\
\
    application.add_handler(CommandHandler("start", start))\
    application.add_handler(CallbackQueryHandler(course_callback))\
\
    application.run_polling()\
\
if __name__ == '__main__':\
    main()}