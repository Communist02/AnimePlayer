import locale

en = {
    'File': 'File',
    'Open file': 'Open file',
    'Open URL': 'Open URL',
    'Open folder': 'Open folder',
    'Exit': 'Exit',
    'Playback': 'Playback',
    'Play | Pause': 'Play | Pause',
    'Fullscreen': 'Fullscreen',
    'Increasing image quality': 'Increasing image quality',
    'Disable': 'Disable',
    'Other': 'Other',
    'Reference': 'Reference',
    'About': 'About',
    'Quality': 'Quality',
    'Mode': 'Mode',
    'About program': 'Media player written in Python programming language using PySimpleGUI library, mpv media player and Anime4K scaling algorithm',
    'Activate SVP': 'Activate SVP',
    'Create config for Android': 'Create config for Android',
    'PLAY': 'PLAY',
    'PAUSE': 'PAUSE',
    'FULL': 'FULL',
    'MENU': 'MENU'
}

ru = {
    'File': 'Файл',
    'Open file': 'Открыть файл',
    'Open URL': 'Открыть URL-адрес',
    'Open folder': 'Открыть папку',
    'Exit': 'Выход',
    'Playback': 'Воспроизведение',
    'Play | Pause': 'Воспроизведение | Пауза',
    'Fullscreen': 'Полноэкранный режим',
    'Increasing image quality': 'Увеличение качества изображения',
    'Disable': 'Отключить',
    'Other': 'Другое',
    'Reference': 'Справка',
    'About': 'О программе',
    'Quality': 'Качество',
    'Mode': 'Режим',
    'About program': 'Медиаплеер, написанный на языке программирования Python с использованием библиотеки графического пользовательского интерфейса PySimpleGUI, мультимедийного проигрывателя mpv и алгоритма масштабирования Anime4K',
    'Activate SVP': 'Активировать SVP',
    'Create config for Android': 'Создать конфиг для Android',
    'PLAY': 'ИГРАТЬ',
    'PAUSE': 'ПАУЗА',
    'FULL': 'ПОЛН',
    'MENU': 'МЕНЮ'
}

match locale.getlocale()[0]:
    case 'Russian_Russia':
        strings = ru
    case _:
        strings = en
