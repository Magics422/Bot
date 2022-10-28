import logging
from telegram.ext import ConversationHandler, Updater, CommandHandler, MessageHandler, Filters
import settings

from handlers import (greet_user, temperature, talk_to_me, subfebril_temper, hi_temper, stomach_ache, acute_stomach_ache, chronic_stomach_ache,
travma_krov, travma, travma_keyboard, heart_keyboard, arhythmia_acute, arhythmia_chron, headache_key, headache_chron, headache_acute,
chest_key, heart_pain, chest_pain, back_key, diabet_key, pressure_key, convulsii_key, weakness_key, stroke_key, back_hard, back_chron,
 hypoglycemia, hyperglycemia, low_pressure, hi_pressure, chron_convulsii, acute_convulsii, acute_weakness, chron_weakness, acute_stroke, chron_stroke   )


logging.basicConfig(filename='bot.log', level=logging.INFO)


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher


    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.regex('^(Температура)$'), temperature))
    dp.add_handler(MessageHandler(Filters.regex('^(Температура больше 37°, но меньше 38.5°)$'), subfebril_temper))
    dp.add_handler(MessageHandler(Filters.regex('^(Температура больше 38.5°)$'), hi_temper))
    dp.add_handler(MessageHandler(Filters.regex('^(Боли в животе)$'), stomach_ache))
    dp.add_handler(MessageHandler(Filters.regex('^(Боли в животе, рвота, жидкий стул, первый день)$'), acute_stomach_ache))
    dp.add_handler(MessageHandler(Filters.regex('^(Боли в животе с имеющиемися хроническими заболеваниями)$'), chronic_stomach_ache))
    dp.add_handler(MessageHandler(Filters.regex('^(Травма)$'), travma_keyboard))
    dp.add_handler(MessageHandler(Filters.regex('^(Травма с кровотечением)$'), travma_krov))
    dp.add_handler(MessageHandler(Filters.regex('^(Травма без кровотечения)$'), travma))
    dp.add_handler(MessageHandler(Filters.regex('^(Нарушение сердечного ритма)$'), heart_keyboard))
    dp.add_handler(MessageHandler(Filters.regex('^(Чувство сердебиения возникло впервые)$'), arhythmia_acute))
    dp.add_handler(MessageHandler(Filters.regex('^(В жизни уже была аритмия)$'), arhythmia_chron))
    dp.add_handler(MessageHandler(Filters.regex('^(Головная боль)$'), headache_key))
    dp.add_handler(MessageHandler(Filters.regex('^(Острые боли в голове, начались внезапно)$'), headache_acute))
    dp.add_handler(MessageHandler(Filters.regex('^(Постоянные боли в голове, устаногвлено хр. заболевание)$'), headache_chron))
    dp.add_handler(MessageHandler(Filters.regex('^(Боли в груди)$'), chest_key))
    dp.add_handler(MessageHandler(Filters.regex('^(Боли в области сердца)$'), heart_pain))
    dp.add_handler(MessageHandler(Filters.regex('^(Боли в груди с боку)$'), chest_pain))
    dp.add_handler(MessageHandler(Filters.regex('^(Боли в спине и конечностях)$'), back_key))
    dp.add_handler(MessageHandler(Filters.regex('^(Боли в спине после физической нагрузки)$'), back_hard))
    dp.add_handler(MessageHandler(Filters.regex('^(Боли в спине при налличии хр.заболеваний)$'), back_chron))
    dp.add_handler(MessageHandler(Filters.regex('^(Сахарный диабет)$'), diabet_key))
    dp.add_handler(MessageHandler(Filters.regex('^(Высокие сахара)$'), hyperglycemia))
    dp.add_handler(MessageHandler(Filters.regex('^(Низкие сахара)$'), hypoglycemia))
    dp.add_handler(MessageHandler(Filters.regex('^(Артериальное давление)$'), pressure_key))
    dp.add_handler(MessageHandler(Filters.regex('^(Высокое аретриальное давление)$'), hi_pressure))
    dp.add_handler(MessageHandler(Filters.regex('^(Низкое артериальное давление)$'), low_pressure))
    dp.add_handler(MessageHandler(Filters.regex('^(Судороги)$'), convulsii_key))
    dp.add_handler(MessageHandler(Filters.regex('^(Впервые возникшие судороги)$'), acute_convulsii))
    dp.add_handler(MessageHandler(Filters.regex('^(Судороги с имеющиемися хроническими заболеваниями)$'), chron_convulsii))
    dp.add_handler(MessageHandler(Filters.regex('^(Слабость)$'), weakness_key))
    dp.add_handler(MessageHandler(Filters.regex('^(Слабость возникшая внезапно первый день)$'), acute_weakness))
    dp.add_handler(MessageHandler(Filters.regex('^(Слабость нарастающая постепенно)$'), chron_weakness))
    dp.add_handler(MessageHandler(Filters.regex('^(Нарушение речи, координации)$'), stroke_key))
    dp.add_handler(MessageHandler(Filters.regex('^(Нарушилась речь, парализовало)$'), acute_stroke))
    dp.add_handler(MessageHandler(Filters.regex('^(Головокружение)$'), chron_stroke))

    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
   


    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()