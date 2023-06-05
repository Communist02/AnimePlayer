import locale

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
    'About program': 'Media player written in Python programming language using PySimpleGUI library, mpv media player and Anime4K scaling algorithm\n\nSite: https://github.com/Communist02/AnimePlayer',
    'Activate SVP': 'Activate SVP',
    'Create config for Android': 'Create config for Android',
    'Play': 'Play',
    'Pause': 'Pause',
    'Menu': 'Menu',
    'Next file': 'Next file',
    'Previous file': 'Previous file',
    'Sound level': 'Sound level',
    'Frames lost': 'Frames lost',
    'Information': 'Information',
    'Clear': 'Clear',
    'Select': 'Select',
    'Cancel': 'Cancel',
    'Language selection (requires reboot)': 'Language selection (requires reboot)',
    'On startup, open the last opened file': 'On startup, open the last opened file',
    'Set the position of the last opened file': 'Set the position of the last opened file',
    'Dark theme (requires reboot)': 'Dark theme (requires reboot)',
    'Speed': 'Speed',
    'Playback speed': 'Playback speed'
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
    'About program': 'Видеоплеер, написанный на языке программирования Python с использованием библиотеки графического пользовательского интерфейса PySimpleGUI, мультимедийного проигрывателя mpv и алгоритма масштабирования Anime4K\n\nСайт: https://github.com/Communist02/AnimePlayer',
    'Activate SVP': 'Активировать SVP',
    'Create config for Android': 'Создать конфиг для Android',
    'Play': 'Играть',
    'Pause': 'Пауза',
    'Menu': 'Меню',
    'Next file': 'Следующий файл',
    'Previous file': 'Предыдущий файл',
    'Sound level': 'Уровень звука',
    'Frames lost': 'Потеряно кадров',
    'Information': 'Информация',
    'Clear': 'Очистить',
    'Select': 'Выбрать',
    'Cancel': 'Отмена',
    'Language selection (requires reboot)': 'Выбор языка (требуется перезагрузка)',
    'On startup, open the last opened file': 'При запуске открывать последний открытый файл',
    'Set the position of the last opened file': 'Устанавливать позицию последнего открытого файла',
    'Dark theme (requires reboot)': 'Темная тема (требуется перезагрузка)',
    'Speed': 'Скорость',
    'Playback speed': 'Скорость воспроизведения'
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
