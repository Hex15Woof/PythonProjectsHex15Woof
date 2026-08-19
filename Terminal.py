import os
from time import sleep
import sys
import shutil  # для удаления папок с файлами
import winsound

def main():
    data_path = "logs_data"  # основная папка для хранения
    current_language = 'en'  # язык по умолчанию

    # Словарь с переводами для разных языков
    translations = {
        'en': {
            'system_start': "System start, please wait.",
            'terminal_version': "HexOS Terminal",
            'enter_username': "Please enter your username: ",
            'enter_password': "Please enter your password: ",
            'login_success': "User {username} successfully logged in",
            'logout_message': "User {user} logged out",
            'no_user_logged': "No user is currently logged in",
            'unknown_command': "Unknown command: '{cmd}'. Type 'cmds' for help.",
            'commands_title': "\nCOMMANDS:",
            'cmd_cmds': "cmds - Shows all commands",
            'cmd_stop': "stop - System shutdown",
            'cmd_logout': "logout - Logout from system",
            'cmd_lang': "lang - Command not working now.",
            'cmd_logmode': "logmode - Enter log management mode",
            'lang_changed': "Language changed to English",
            'system_stop': "System stop, please wait.",
            'logmode_enter': "Entering log management mode...",
            'logmode_exit': "Exiting log management mode.",
            'log_created': "Log '{logname}' created.",
            'category_created': "Category '{catname}' created.",
            'log_already_exists': "Log '{logname}' already exists.",
            'category_already_exists': "Category '{catname}' already exists.",
            'log_not_found': "Log '{logname}' not found.",
            'category_not_found': "Category '{catname}' not found.",
            'log_deleted': "Log '{logname}' deleted.",
            'category_deleted': "Category '{catname}' deleted.",
            'entered_category': "Entered category '{catname}'.",
            'exited_category': "Exited category.",
            'input_log_content': "Enter content for log '{logname}': ",
            'log_updated': "Log '{logname}' updated.",
            'current_category': "Current category: {catname}",
            'no_current_category': "No current category (in root).",
            'logcmds_title': "\nLOG MODE COMMANDS:",
            'cmd_mklog': "mklog <logname> - Create a new log/note",
            'cmd_mkcat': "mkcat <catname> - Create a new category",
            'cmd_edit': "edit <logname> - Edit existing log",
            'cmd_enter': "enter <catname> - Enter category",
            'cmd_exitcat': "exitcat - Exit current category",
            'cmd_dellog': "dellog <logname> - Delete log",
            'cmd_delcat': "delcat <catname> - Delete category",
            'cmd_exit': "exit - Exit log mode",
            'cmd_logcmds': "logcmds - Show log mode commands",
            'cmd_viewlog': "viewlog <logname> - View log content",
            'log_content': "Content of log '{logname}':",
            'cmd_listlogs': "listlogs - List all logs",
            'logs_list': "Available logs:",
            'no_logs_found': "No logs found.",
            'cmd_listcats': "listcats - List all categories and logs",
            'categories_list': "Categories and logs:",
            'no_categories_found': "No categories found.",
            'cmd_rename': "rename <old_logname> <new_logname> - Rename a log",
            'log_renamed': "Log '{oldname}' renamed to '{newname}'."
        },
    }

    logs = {}  # словарь: имя лога → содержимое заметки
    categories = {}  # словарь: имя категории → список логов в ней
    current_category = None  # текущая активная категория (None — вне категорий)

    def get_text(key):
        """Получить текст на текущем языке"""
        return translations[current_language][key]

    def meow():
        print("meow")

    def sysstart():
        print(get_text('system_start'))
        sleep(1)
        print("Loading HexOS...")
        winsound.Beep(750, 150)
        sleep(3)
        print("Checking system memory...")
        winsound.Beep(750, 150)
        sleep(1)
        print("Checking servers...")
        winsound.Beep(750, 150)
        sleep(1)
        print("Checking networks...")
        winsound.Beep(750, 150)
        sleep(1)
        print("Checking storage...")
        winsound.Beep(750, 150)
        sleep(1)
        print("Checking disks...")
        winsound.Beep(750, 150)
        sleep(1)
        print("Checking CPU...")
        winsound.Beep(750, 150)
        sleep(1)
        print("Checking RAM...")
        winsound.Beep(750, 150)
        sleep(1)
        print("Checking Python...")
        winsound.Beep(750, 150)
        sleep(1)
        print("Importing module os...")
        winsound.Beep(750, 150)
        sleep(1)
        print("Importing module sys...")
        winsound.Beep(750, 150)
        sleep(1)
        print("Importing module shutil...")
        winsound.Beep(750, 150)
        sleep(1)
        print("Importing module winsound...")
        winsound.Beep(750, 150)
        sleep(1)
        print("Importing module time...")
        winsound.Beep(750, 150)
        sleep(1)
        print("Loading data...")
        winsound.Beep(750, 150)
        sleep(5)
        print("All systems working correct.")
        print("Initializing HexOS...")
        print(get_text('terminal_version'))
        print(f"Print 'cmds' to see all commands")
        winsound.Beep(500, 500)

    def sysstop():
        print(get_text('system_stop'))
        winsound.Beep(750, 150)
        sys.exit()

    def login():
        username = input(get_text('enter_username'))
        password = input(get_text('enter_password'))
        print(get_text('login_success').format(username=username))
        return username, password

    def logout(current_user):
        if current_user:
            print(get_text('logout_message').format(user=current_user))
        else:
            print(get_text('no_user_logged'))

    def show_commands():
        print(get_text('commands_title'))
        print(get_text('cmd_cmds'))
        print(get_text('cmd_stop'))
        print(get_text('cmd_logout'))
        print(get_text('cmd_lang'))
        print(get_text('cmd_logmode'))
        print(get_text('cmd_listlogs'))
        print(get_text('cmd_listcats'))
        print()

    def show_log_commands():
        """Показать команды лог‑режима"""
        print(get_text('logcmds_title'))
        print(get_text('cmd_mklog'))
        print(get_text('cmd_mkcat'))
        print(get_text('cmd_edit'))
        print(get_text('cmd_enter'))
        print(get_text('cmd_exitcat'))
        print(get_text('cmd_dellog'))
        print(get_text('cmd_delcat'))
        print(get_text('cmd_exit'))
        print(get_text('cmd_logcmds'))
        print(get_text('cmd_viewlog'))
        print(get_text('cmd_listlogs'))
        print(get_text('cmd_listcats'))
        print(get_text('cmd_rename'))
        print()

    def init_storage():
        """Создать основную папку для хранения, если её нет"""
        if not os.path.exists(data_path):
            os.makedirs(data_path)
            print(f"Created storage folder: {data_path}")

    def load_storage():
        """Загрузить существующие категории и логи из файловой системы"""
        if not os.path.exists(data_path):
            return

        for item in os.listdir(data_path):
            item_path = os.path.join(data_path, item)
            if os.path.isdir(item_path):  # это категория (папка)
                categories[item] = []
                # Загружаем логи внутри категории
                for file in os.listdir(item_path):
                    if file.endswith('.txt'):
                        logname = file[:-4]  # убираем .txt
                        logs[logname] = ""  # пока пустое содержимое
                        categories[item].append(logname)
            elif item.endswith('.txt'):  # логи в корне
                logname = item[:-4]
                logs[logname] = ""

    def listlogs():
        """Показать все заметки"""
        if not logs:
            print(get_text('no_logs_found'))
        else:
            print(get_text('logs_list'))
            for logname in logs:
                print(f"  - {logname}")
            print()

    def listcats():
        """Показать все категории и заметки в них"""
        if not categories:
            print(get_text('no_categories_found'))
        else:
            print(get_text('categories_list'))
            for catname in categories:
                print(f"  Category: {catname}")
                if categories[catname]:
                    for logname in categories[catname]:
                        print(f"    - {logname}")
                else:
                    print("    (no logs)")
            print()

    def viewlog(logname):
        """Просмотреть содержимое заметки (файла)"""
        if logname not in logs:
            print(get_text('log_not_found').format(logname=logname))
        else:
            # Определяем путь к файлу
            if current_category and logname in categories.get(current_category, []):
                log_path = os.path.join(data_path, current_category, f"{logname}.txt")
            else:
                log_path = os.path.join(data_path, f"{logname}.txt")
            # Читаем содержимое файла
            try:
                with open(log_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                print(get_text('log_content').format(logname=logname))
                print(content)
                print()  # пустая строка для читаемости
            except FileNotFoundError:
                print(get_text('log_not_found').format(logname=logname))

    def mklog(logname):
        """Создать новую заметку (файл)"""
        # Определяем путь
        if current_category:
            log_path = os.path.join(data_path, current_category, f"{logname}.txt")
        else:
            log_path = os.path.join(data_path, f"{logname}.txt")

        if os.path.exists(log_path):
            print(get_text('log_already_exists').format(logname=logname))
        else:
            # Создаём файл
            with open(log_path, 'w', encoding='utf-8') as f:
                f.write("")  # пустой файл
            logs[logname] = ""
            if current_category:
                if current_category not in categories:
                    categories[current_category] = []
                categories[current_category].append(logname)
            print(get_text('log_created').format(logname=logname))

    def mkcat(catname):
        """Создать новую категорию (папку)"""
        cat_path = os.path.join(data_path, catname)
        if os.path.exists(cat_path):
            print(get_text('category_already_exists').format(catname=catname))
        else:
            os.makedirs(cat_path)
            categories[catname] = []
            print(get_text('category_created').format(catname=catname))


    def edit(logname):
        """Редактировать заметку (файл)"""
        if logname not in logs:
            print(get_text('log_not_found').format(logname=logname))
        else:
            content = input(get_text('input_log_content').format(logname=logname))
            # Определяем путь к файлу
            if current_category and logname in categories.get(current_category, []):
                log_path = os.path.join(data_path, current_category, f"{logname}.txt")
            else:
                log_path = os.path.join(data_path, f"{logname}.txt")
            # Сохраняем содержимое в файл
            with open(log_path, 'w', encoding='utf-8') as f:
                f.write(content)
            logs[logname] = content
            print(get_text('log_updated').format(logname=logname))

    def enter_category(catname):
        """Войти в категорию"""
        nonlocal current_category
        if catname not in categories:
            print(get_text('category_not_found').format(catname=catname))
        else:
            current_category = catname
            print(get_text('entered_category').format(catname=catname))

    def exit_category():
        """Выйти из категории"""
        nonlocal current_category
        current_category = None
        print(get_text('exited_category'))

    def dellog(logname):
        """Удалить заметку (файл)"""
        if logname not in logs:
            print(get_text('log_not_found').format(logname=logname))
        else:
            # Определяем путь к файлу
            if current_category and logname in categories.get(current_category, []):
                log_path = os.path.join(data_path, current_category, f"{logname}.txt")
            else:
                log_path = os.path.join(data_path, f"{logname}.txt")
            # Удаляем файл
            try:
                os.remove(log_path)
                del logs[logname]
                # Удаляем из категории, если нужно
                if current_category and logname in categories.get(current_category, []):
                    categories[current_category].remove(logname)
                print(get_text('log_deleted').format(logname=logname))
            except OSError as e:
                print(f"Error deleting file: {e}")

    def delcat(catname):
        """Удалить категорию (папку)"""
        if catname not in categories:
            print(get_text('category_not_found').format(catname=catname))
        else:
            cat_path = os.path.join(data_path, catname)
            try:
                shutil.rmtree(cat_path)  # удаляем папку со всеми файлами
                # Удаляем все логи этой категории из памяти
                for logname in categories[catname]:
                    if logname in logs:
                        del logs[logname]
                del categories[catname]
                print(get_text('category_deleted').format(catname=catname))
            except OSError as e:
                print(f"Error deleting category: {e}")


    def rename_log(old_name, new_name):
        """Переименовать заметку (файл)"""
        if old_name not in logs:
            print(get_text('log_not_found').format(logname=old_name))
        elif new_name in logs:
            print(get_text('log_already_exists').format(logname=new_name))
        else:
            # Определяем старые и новые пути
            # Ищем, где лежит файл: в корне или в текущей категории
            old_path = None
            new_path = None

            # Проверяем внутри текущей категории
            if current_category and old_name in categories.get(current_category, []):
                old_path = os.path.join(data_path, current_category, f"{old_name}.txt")
                new_path = os.path.join(data_path, current_category, f"{new_name}.txt")
            # Проверяем в корне
            elif os.path.exists(os.path.join(data_path, f"{old_name}.txt")):
                old_path = os.path.join(data_path, f"{old_name}.txt")
                new_path = os.path.join(data_path, f"{new_name}.txt")

            if old_path and os.path.exists(old_path):
                os.rename(old_path, new_path)
                # Обновляем данные в памяти
                logs[new_name] = logs[old_name]
                del logs[old_name]

                # Обновляем ссылки в категориях
                for cat in categories:
                    if old_name in categories[cat]:
                        categories[cat].remove(old_name)
                        categories[cat].append(new_name)

                print(get_text('log_renamed').format(oldname=old_name, newname=new_name))
            else:
                print(get_text('log_not_found').format(logname=old_name))


    # Инициализация хранилища
    init_storage()
    load_storage()

    # Запуск системы
    meow()
    sysstart()

    # Авторизация
    current_user, _ = login()
    in_logmode = False  # флаг: находимся ли в режиме управления заметками

    # Основной цикл обработки команд
    while True:
        # Показываем текущую категорию, если в лог‑режиме
        if in_logmode and current_category:
            print(get_text('current_category').format(catname=current_category))
        elif in_logmode:
            print(get_text('no_current_category'))

        cmd_input = input("> ").strip().lower()
        parts = cmd_input.split()
        cmd = parts[0] if parts else ''
        args = parts[1:] if len(parts) > 1 else []

        if not in_logmode:
            # Обычный режим
            if cmd == "stop":
                sysstop()
            elif cmd == "logout":
                logout(current_user)
                current_user = None
            elif cmd == "cmds":
                show_commands()
            elif cmd == "lang" and args:
                print("This command not working.")
            elif cmd == "msg":
                msgtext = input(f"Input your message:")
                print(msgtext)
            elif cmd:
                print(get_text('unknown_command').format(cmd=cmd))
        else:
            # Режим управления заметками
            if cmd == "exit":
                in_logmode = False
                print(get_text('logmode_exit'))
            elif cmd == "mklog" and args:
                mklog(args[0])
            elif cmd == "mkcat" and args:
                mkcat(args[0])
            elif cmd == "edit" and args:
                edit(args[0])
            elif cmd == "enter" and args:
                enter_category(args[0])
            elif cmd == "exitcat":
                exit_category()
            elif cmd == "dellog" and args:
                dellog(args[0])
            elif cmd == "delcat" and args:
                delcat(args[0])
            elif cmd == "rename" and len(args) == 2:
                rename_log(args[0], args[1])
            elif cmd == "viewlog" and args:
                viewlog(args[0])
            elif cmd == "listlogs":
                listlogs()
            elif cmd == "listcats":
                listcats()
            elif cmd == "cmds":
                show_commands()  # показываем общие команды
            elif cmd == "logcmds":
                show_log_commands()  # показываем команды лог‑режима
            elif cmd:
                print(get_text('unknown_command').format(cmd=cmd))

if __name__ == "__main__":
    main()
