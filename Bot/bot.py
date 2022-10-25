import logging
from telegram.ext import ConversationHandler, Updater, CommandHandler, MessageHandler, Filters
import settings

from handlers import (greet_user, temperature, talk_to_me, subfebril_temper, hi_temper, stomach_ache, acute_stomach_ache, chronic_stomach_ache,
travma_krov, travma, travma_keyboard, heart_keyboard, arhythmia_acute, arhythmia_chron, headache_key, headache_chron, headache_acute,
    )


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

    dp.add_handler(MessageHandler(Filters.regex('^(Боли в области сердца (за грудиной))$'), subfebril_temper))
    dp.add_handler(MessageHandler(Filters.regex('^(Боли в груди с боку)$'), hi_temper))
    dp.add_handler(MessageHandler(Filters.regex('^(Боли в спине после физической нагрузки)$'), stomach_ache))
    dp.add_handler(MessageHandler(Filters.regex('^(Боли в спине при налличии хр.заболеваний)$'), acute_stomach_ache))
    dp.add_handler(MessageHandler(Filters.regex('^(Высокие сахара)$'), chronic_stomach_ache))
    dp.add_handler(MessageHandler(Filters.regex('^(Низкие сахара)$'), temperature))
    dp.add_handler(MessageHandler(Filters.regex('^(Высокое аретриальное давление)$'), subfebril_temper))
    dp.add_handler(MessageHandler(Filters.regex('^(Низкое артериальное давление)$'), hi_temper))
    dp.add_handler(MessageHandler(Filters.regex('^(Впервые возникшие судороги)$'), stomach_ache))
    dp.add_handler(MessageHandler(Filters.regex('^(Судороги с имеющиемися хроническими заболеваниями)$'), acute_stomach_ache))
    dp.add_handler(MessageHandler(Filters.regex('^(Слабость возникшая внезапно первый день)$'), chronic_stomach_ache))    dp.add_handler(MessageHandler(Filters.regex('^(Боли в животе с имеющиемися хроническими заболеваниями)$'), chronic_stomach_ache))
    dp.add_handler(MessageHandler(Filters.regex('^(Слабость нарастающая постепенно)$'), temperature))
    dp.add_handler(MessageHandler(Filters.regex('^(Нарушилась речь, парализовало)$'), temperature))
    dp.add_handler(MessageHandler(Filters.regex('^(Головокружение)$'), temperature))
    dp.add_handler(MessageHandler(Filters.regex('^(Чувство онемения в руках, нога)$'), temperature))

    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
   


    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()