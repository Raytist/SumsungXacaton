from aiogram.types import InlineKeyboardButton , InlineKeyboardMarkup , ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


menu_buttons = [[InlineKeyboardButton(text='статистика за день', callback_data='get_stats_for_day')],
            [InlineKeyboardButton(text='статистика за неделю',callback_data='get_stats_for_week')],
            [InlineKeyboardButton(text='статистика за месяц',callback_data='get_stats_for_month')]]

stats_buttons = [[InlineKeyboardButton(text='показать в виде графика',callback_data='show_graph')],
                 [InlineKeyboardButton(text='самый популярный',callback_data='show_most_popular_post'),InlineKeyboardButton(text='самый непопулярный',callback_data='show_most_unpopular_post')],
                 [InlineKeyboardButton(text='вернуться назад',callback_data='back')]]

back_button = [[InlineKeyboardButton(text="вернуться",callback_data='back_in stats')]]

back_grah = [[InlineKeyboardButton(text='вернуться',callback_data='back_out_grah')]]

greet_kb = InlineKeyboardMarkup(inline_keyboard=menu_buttons)
greet_kb_stats = InlineKeyboardMarkup(inline_keyboard=stats_buttons)
greet_kb_back = InlineKeyboardMarkup(inline_keyboard=back_button)
greet_kb_grah = InlineKeyboardMarkup(inline_keyboard=back_grah)