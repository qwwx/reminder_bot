import sqlite3
from datetime import datetime


class BotDB:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exists(self, user_id):
        """Проверяем, есть ли юзер в базе"""
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return bool(len(result.fetchall()))

    def get_user_id(self, user_id):
        """Достаем id юзера в базе по его user_id"""
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return result.fetchone()[0]

    def add_user(self, user_id):
        """Добавляем юзера в базу"""
        self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))
        return self.conn.commit()

    def add_record(self, user_id, text, date):
        """Создаем запись """
        self.cursor.execute("INSERT INTO `records` (`users_id`, `text`, `date`) VALUES (?, ?, ?)",
                            (self.get_user_id(user_id), text, date))
        return self.conn.commit()

    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()

    def get_record(self):
        """Сравниваем время"""
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:00")
        self.cursor.execute(f"SELECT users_id, text FROM `records` WHERE date=?", (current_time,), )
        return self.cursor.fetchall()

    def tg_id(self, id):
        """Вытаскиваем id пользователя"""
        self.cursor.execute(f"SELECT user_id FROM `users` WHERE id=?", (id,), )
        return self.cursor.fetchall()
