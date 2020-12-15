import re 
import os


class REPRLoop:
	"""Основной бесконечный оработчик"""
	def __init__(self, storage_file):
		self.PARSE_ERROR = -1
		self.storage_file = storage_file
		self.phone_pattern = re.compile(r"^\d\(\d{3}\)-\d{3}-\d{2}-\d{2}$")
		self.FIO_pattern = re.compile(r"^[А-я]+? [А-я]+? [А-я]+?$")

	def run(self):
		"""Запускает сам REPR цикл"""
		self.print_help_message()

		while True:
			action = self.read_action()

			if not self.validate_action(action):
				print("\nТакого действия не существует. ", end="")
				self.print_help_message()
				continue
			
			if action == 3:
				break
			elif action == 1:
				self.insert_user()
			else:
				self.list_users()
			
			print()

	def list_users(self):
		"""Выводит список пользователей, если файлик существует"""
		if not os.path.exists(self.storage_file):
			return
		
		print(*[f"\t{data}" for data in open(self.storage_file).readlines()])
			
	def insert_user(self):
		"""Добавляет пользователя в список"""
		# сначала считываем ФИО пользователя
		user_fio = input("Введите ФИО пользователя в формате: Xxxxx Xxxxxxx Xxx:\n\t> ")
		if not self.validate_user_fio(user_fio):
			print("Неверный формат ФИО пользователя\n")
			return

		# Затем считываем телефон пользователя
		phone_number = input("Введите телефонный номер в формате x(xxx)-xxx-xx-xx:\n\t> ")
		if not self.validate_phone_number(phone_number):
			print("Неверный формат номера телефона\n")
			return
		
		with open(self.storage_file, "a") as file:
			file.write(f"{user_fio} {phone_number}\n")
	
	def validate_user_fio(self, user_fio):
		"""Валидирует ФИО пользвателя"""
		return re.match(self.FIO_pattern, user_fio)	

	def validate_phone_number(self, phone_number):
		"""Валидирует номер телефона"""
		return re.match(self.phone_pattern, phone_number)

	def print_help_message(self):
		"""Выводите сообщение с подсказкой о всех командах"""
		print(
			"Подсказка:\n"
			"\t1 - добавить пользователя\n"
			"\t2 - вывести список пользователей\n"
			"\t3 - выход из программы\n"
		)

	def validate_action(self, action_type):
		"""Проверяет тип действия"""
		return action_type in [1, 2, 3]

	def read_action(self):
		"""Считываем действие пользователя"""
		try:
			return int(input("Введите номер желаемого действия: "))
		except:
			return self.PARSE_ERROR


loop = REPRLoop("contacts.txt")
loop.run()
