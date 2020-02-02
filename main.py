import questions
import telebot
from random import shuffle
from telebot import types
import random

bot = telebot.TeleBot('842578968:AAEqFwF8GFsIO3rf9N1_8xdPvAm5KqbZap4')

@bot.message_handler(commands=['start'])
def send_welcome(message):
	user = message.chat.first_name
	msg = 'Привет, %s! \n \nДля того, что бы начать игру нажми на кнопку "Начать игру", выбери компанию в которой находишься и система предложит тебе случайный вопрос. \n \nНе знаком с нашими правилами? Скорее жми "Правила" и внимательно читай :)\n \nЕсли хочешь познакомиться с авторами бота - жми "О проекте".\n\nИ помни, что цель игры - максимально открыто пообщаться и насладиться компанией друзей и близких."' % user
	bot.send_message(message.chat.id, msg)
	any_msg(message)

# create keyboard

@bot.message_handler(content_types=['text'])
def any_msg(message):
	keyboardmain = types.InlineKeyboardMarkup(row_width=2)
	start_game_button = types.InlineKeyboardButton(text='Начать игру', callback_data='start_game')
	rule_button = types.InlineKeyboardButton(text='Правила', callback_data='rule')
	about_button = types.InlineKeyboardButton(text='О проекте', callback_data='about')
	keyboardmain.add(start_game_button, rule_button, about_button)
	bot.send_message(message.chat.id, 'Выберите один из вариантов', reply_markup=keyboardmain)

# Отлов сообщений в кейборде

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
	
	# Сообщения с главного меню

	if call.data == 'start_game':
		keyboard_start_game = types.InlineKeyboardMarkup(row_width=2)
		love_questions_button = types.InlineKeyboardButton(text='Вопросы для пары', callback_data='love_questions')
		friends_questions_button = types.InlineKeyboardButton(text='Вопросы для компании', callback_data='friends_questions')
		back_button = types.InlineKeyboardButton(text='Вернуться назад', callback_data='back')
		keyboard_start_game.add(love_questions_button, friends_questions_button, back_button)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text="Вопросы для какой компании?", reply_markup=keyboard_start_game)

	elif call.data == 'rule':
		msg = "Friendbuilding - это концепция построения дружеских отношений на любом уровне! \n \nИгра Friendbuilding - это волшебные карточки, которые смогут позволить вам и окружающим вас людям очень сблизиться и открыть друг друга совсем с другой стороны! \n  \nВсё просто: ваша задача по очереди давать развёрнутые ответы на вопросы, которые предлагает вам система. \n  \nКак результат, вы получаете тёплые, искренние и глубокие разговоры друг с другом, тем самым поднимая эмпатию и укрепляя ваши взаимоотношения с окружающими."

		keyboard_rule = types.InlineKeyboardMarkup(row_width=1)	
		back_rule_button = types.InlineKeyboardButton(text='Вернуться назад', callback_data='back')
		keyboard_rule.add(back_rule_button)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text=msg, reply_markup=keyboard_rule)

	elif call.data == 'about':
		msg = 'Привет, меня зовут Дима и я  ̶а̶л̶к̶о̶г̶о̶л̶и̶к̶  разработчик этого бота ☺️ \n \nОткуда пришла идея? Саму концепцию "Friendbuilding" я узнал от Дмитрия Рожкова ( @rozhkov_networking ). Дмитрий занимается обучением  искусству создавать тёплые и крепкие отношения  любого уровня между людьми. Он выпустил свою настольную игру "Карточки Friendbuilding" . Данный бот как раз и сделан на основе этих карточек. \n \nБот не выступает заменой настольной игры, а является её дополнением, когда карточек нет под рукой. \n \nНадеюсь, что наш проект принесёт вам пользу и поможет ещё больше сблизиться с близкими для вас людьми! \n \nСвязаться с разработчиком можно здесь @Shkinder_dmitry.'

		keyboard_about= types.InlineKeyboardMarkup(row_width=1)	
		back_about_button = types.InlineKeyboardButton(text='Вернуться назад', callback_data='back')
		keyboard_about.add(back_about_button)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text=msg, reply_markup=keyboard_about)

	# Сообщения с начала игры	

	elif call.data == 'love_questions':
		i = random.randint(1,len(questions.love_questions))
		msg = questions.love_questions[i]

		keyboard_questions = types.InlineKeyboardMarkup(row_width=2)
		next_question_button = types.InlineKeyboardButton(text='Следующий вопрос', callback_data='love_questions')
		end_game_button = types.InlineKeyboardButton(text='Закончить игру', callback_data='end_game')
		keyboard_questions.add(next_question_button, end_game_button)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text= msg, reply_markup=keyboard_questions)

	elif call.data == 'friends_questions':
		i = random.randint(1,len(questions.love_questions))
		msg = questions.love_questions[i]

		keyboard_questions = types.InlineKeyboardMarkup(row_width=2)
		next_question_button = types.InlineKeyboardButton(text='Следующий вопрос', callback_data='friends_questions')
		end_game_button = types.InlineKeyboardButton(text='Закончить игру', callback_data='end_game')
		keyboard_questions.add(next_question_button, end_game_button)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text=msg, reply_markup=keyboard_questions)

	elif call.data == 'back':
		keyboardmain = types.InlineKeyboardMarkup(row_width=2)
		start_game_button = types.InlineKeyboardButton(text='Начать игру', callback_data='start_game')
		rule_button = types.InlineKeyboardButton(text='Правила', callback_data='rule')
		about_button = types.InlineKeyboardButton(text='О проекте', callback_data='about')
		keyboardmain.add(start_game_button, rule_button, about_button)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text="Выберите один из вариантов", reply_markup=keyboardmain)

	# Сообщения после выбора вопросов
	
	elif call.data == 'end_game':
		keyboardmain = types.InlineKeyboardMarkup(row_width=2)
		start_game_button = types.InlineKeyboardButton(text='Начать игру', callback_data='start_game')
		rule_button = types.InlineKeyboardButton(text='Правила', callback_data='rule')
		about_button = types.InlineKeyboardButton(text='О проекте', callback_data='about')
		keyboardmain.add(start_game_button, rule_button, about_button)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text="Выберите один из вариантов", reply_markup=keyboardmain)


if __name__ == '__main__':
	bot.polling(none_stop=True)