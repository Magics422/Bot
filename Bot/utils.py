from telegram import ReplyKeyboardMarkup, KeyboardButton

import settings


def main_keyboard():
    return ReplyKeyboardMarkup([
    ['Температура', 'Боли в животе', "Травма"],
    ['Нарушение сердечного ритма', "Головная боль", "Боли в груди"],
    ['Боли в спине и конечностях', 'Сахарный диабет', 'Артериальное давление'],
    ['Судороги', 'Слабость', 'Нарушение речи, координации']
])

def temper_keyboard():
    return ReplyKeyboardMarkup([
    ['Температура больше 37°, но меньше 38.5°'],
    ["Температура больше 38.5°"],
])

def stomach_keyboard():
    return ReplyKeyboardMarkup([
    ['Боли в животе, рвота, жидкий стул, первый день'],
    ["Боли в животе с имеющиемися хроническими заболеваниями"],
])

def injury_keyboard():
    return ReplyKeyboardMarkup([
    ['Травма с кровотечением'],
    ["Травма без кровотечения"],
])

def arhythmia_keyboard():
    return ReplyKeyboardMarkup([
    ['Чувство сердебиения возникло впервые'],
    ["В жизни уже была аритмия"],
])

def headache_keyboard():
    return ReplyKeyboardMarkup([
    ['Острые боли в голове, начались внезапно'],
    ["Постоянные боли в голове, устаногвлено хр. заболевание"],
])

def chest_pain_keyboard():
    return ReplyKeyboardMarkup([
    ['Боли в области сердца (за грудиной)'],
    ["Боли в груди с боку"],
])

def backache_keyboard():
    return ReplyKeyboardMarkup([
    ['Боли в спине после физической нагрузки'],
    ["Боли в спине при налличии хр.заболеваний"],
])

def diabetes_keyboard():
    return ReplyKeyboardMarkup([
    ['Высокие сахара'],
    ["Низкие сахара"],
])

def pressure_keyboard():
    return ReplyKeyboardMarkup([
    ['Высокое аретриальное давление'],
    ["Низкое артериальное давление"],
])

def convulsions_keyboard():
    return ReplyKeyboardMarkup([
    ['Впервые возникшие судороги'],
    ["Судороги с имеющиемися хроническими заболеваниями"],
])

def weakness_keyboard():
    return ReplyKeyboardMarkup([
    ['Слабость возникшая внезапно первый день'],
    ["Слабость нарастающая постепенно"],
])

def stroke_keyboard():
    return ReplyKeyboardMarkup([
    ['Нарушилась речь, парализовало'],
    ['Головокружение'],
])
