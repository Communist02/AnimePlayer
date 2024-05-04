import locale
import ctypes
import os

en = {
    'lang': 'English',
    'File': 'File',
    'Open file': 'Open file',
    'Open URL': 'Open URL',
    'Open folder': 'Open folder',
    'Close': 'Close',
    'Exit': 'Exit',
    'Playback': 'Playback',
    'Play | Pause': 'Play | Pause',
    'Fullscreen': 'Fullscreen',
    'Increasing image quality': 'Increasing image quality',
    'Disable': 'Disable',
    'Other': 'Other',
    'Reference': 'Reference',
    'About': 'About',
    'Settings': 'Settings',
    'Quality': 'Quality',
    'Mode': 'Mode',
    'About program': 'Media player written in Python programming language using PySide 6 library, mpv media player and Anime4K scaling algorithm\n\nSite: https://github.com/Communist02/AnimePlayer',
    'Activate SVP': 'Activate SVP',
    'Create config for Android': 'Create config for Android',
    'Play': 'Play',
    'Pause': 'Pause',
    'Menu': 'Menu',
    'Next file': 'Next file',
    'Previous file': 'Previous file',
    'Volume level': 'Volume level',
    'Frames lost': 'Frames lost',
    'Information': 'Information',
    'Clear': 'Clear',
    'Select': 'Select',
    'Cancel': 'Cancel',
    'Language selection': 'Language selection (restart required)',
    'On startup open the last opened file': 'On startup open the last opened file',
    'Set the position of the last opened file': 'Set the position of the last opened file',
    'Dark theme': 'Dark theme',
    'Speed': 'Speed',
    'Playback speed': 'Playback speed',
    'Subtitles': 'Subtitles',
    'Soundtrack': 'Soundtrack',
    'Choose file': 'Choose file',
    'All supported files': 'All supported files',
    'Enter the URL': 'Enter the URL',
    'Opening a link': 'Opening a link',
    'Select a folder': 'Select a folder',
    'Opening a folder': 'Opening a folder',
    'You can use this config to use the Anime4K algorithm in the mpv video player on android': 'You can use this config to use the Anime4K algorithm in the mpv video player on android',
    'Enter the path to the shaders': 'Enter the path to the shaders',
    'Select the algorithm configuration': 'Select the algorithm configuration',
    'All': 'All',
    'Selected': 'Selected',
    'Off': 'Off',
    'Paste': 'Paste',
    'Screenshot': 'Screenshot',
    'Take a screenshot': 'Take a screenshot',
    'Enter folder path for screenshots': 'Enter folder path for screenshots',
    'Increase maximum volume up to 150%': 'Increase maximum volume up to 150%',
    'Launch parameters': 'Launch parameters',
    'Manual launch parameters': 'Use the mpv manual https://mpv.io/manual/\nBut keep in mind that Python syntax is required.\nAccess the "player" variable.\nFor example, instead of --volume=50 use player.volume = 50',
    'Apply': 'Apply',
    'Save': 'Save',
    'Error': 'Error',
    'Success': 'Success',
    'Volume +10': 'Volume +10',
    'Volume -10': 'Volume -10',
    'Rewind +5 sec': 'Rewind +5 sec',
    'Rewind -5 sec': 'Rewind -5 sec',
    'Zoom in': 'Zoom in',
    'Zoom out': 'Zoom out',
    'Playlist': 'Playlist',
    'Theme': 'Theme',
    'Light': 'Light',
    'Dark': 'Dark',
    'System': 'System'
}

ru = {
    'lang': 'Русский',
    'File': 'Файл',
    'Open file': 'Открыть файл',
    'Open URL': 'Открыть URL-адрес',
    'Open folder': 'Открыть папку',
    'Close': 'Закрыть',
    'Exit': 'Выход',
    'Playback': 'Воспроизведение',
    'Play | Pause': 'Воспроизведение | Пауза',
    'Fullscreen': 'Полноэкранный режим',
    'Increasing image quality': 'Увеличение качества изображения',
    'Disable': 'Отключить',
    'Other': 'Другое',
    'Reference': 'Справка',
    'About': 'О программе',
    'Settings': 'Настройки',
    'Quality': 'Качество',
    'Mode': 'Режим',
    'About program': 'Видеоплеер, написанный на языке программирования Python с использованием библиотеки графического пользовательского интерфейса PySide 6, мультимедийного проигрывателя mpv и алгоритма масштабирования Anime4K\n\nСайт: https://github.com/Communist02/AnimePlayer',
    'Activate SVP': 'Активировать SVP',
    'Create config for Android': 'Создать конфиг для Android',
    'Play': 'Играть',
    'Pause': 'Пауза',
    'Menu': 'Меню',
    'Next file': 'Следующий файл',
    'Previous file': 'Предыдущий файл',
    'Volume level': 'Уровень громкости',
    'Frames lost': 'Потеряно кадров',
    'Information': 'Информация',
    'Clear': 'Очистить',
    'Select': 'Выбрать',
    'Cancel': 'Отмена',
    'Language selection': 'Выбор языка (требуется перезапуск)',
    'On startup open the last opened file': 'При запуске открывать последний открытый файл',
    'Set the position of the last opened file': 'Устанавливать позицию последнего открытого файла',
    'Dark theme': 'Темная тема',
    'Speed': 'Скорость',
    'Playback speed': 'Скорость воспроизведения',
    'Subtitles': 'Субтитры',
    'Soundtrack': 'Звуковая дорожка',
    'Choose file': 'Выберите файл',
    'All supported files': 'Все поддерживаемые файлы',
    'Enter the URL': 'Введите URL-адрес',
    'Opening a link': 'Открытие ссылки',
    'Select a folder': 'Выберите папку',
    'Opening a folder': 'Открытие папки',
    'You can use this config to use the Anime4K algorithm in the mpv video player on android': 'Этот конфиг вы можете использовать для использования алгоритма Anime4K в видеоплеере mpv на Android',
    'Enter the path to the shaders': 'Введите путь до шейдеров',
    'Select the algorithm configuration': 'Выберите конфигурацию алгоритма',
    'All': 'Все',
    'Selected': 'Выбранный',
    'Off': 'Выкл.',
    'Paste': 'Вставить',
    'Screenshot': 'Cкриншот',
    'Take a screenshot': 'Сделать скриншот',
    'Enter folder path for screenshots': 'Введите путь до папки для скриншотов',
    'Increase maximum volume up to 150%': 'Увеличить максимальную громкость до 150%',
    'Launch parameters': 'Параметры запуска',
    'Manual launch parameters': 'Используйте руководство mpv https://mpv.io/manual/\nНо имейте ввиду, что требуется синтаксис языка Python.\nОбращайтесь к переменной player.\nНапример, вместо --volume=50 используйте player.volume = 50',
    'Apply': 'Применить',
    'Save': 'Сохранить',
    'Error': 'Ошибка',
    'Success': 'Успех',
    'Volume +10': 'Громкость +10',
    'Volume -10': 'Громкость -10',
    'Rewind +5 sec': 'Перемотка +5 сек',
    'Rewind -5 sec': 'Перемотка -5 сек',
    'Zoom in': 'Увеличить масштаб',
    'Zoom out': 'Уменьшить масштаб',
    'Playlist': 'Список воспроизведения',
    'Theme': 'Тема',
    'Light': 'Светлая',
    'Dark': 'Темная',
    'System': 'Системная'
}

match locale.getlocale()[0]:
    case 'Russian_Russia':
        strings = ru
    case _:
        strings = en


def set_locale(lang):
    global strings
    match lang:
        case 'Русский':
            strings = ru
        case 'English':
            strings = en
        case _:
            if os.name == 'nt':
                windll = ctypes.windll.kernel32
                windll.GetUserDefaultUILanguage()
                lang = locale.windows_locale[windll.GetUserDefaultUILanguage()]
            else:
                lang = locale.getlocale()[0]
            match lang:
                case 'Russian_Russia' | 'ru_RU':
                    strings = ru
                case _:
                    strings = en
