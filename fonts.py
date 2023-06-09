import os

if os.name == 'nt':
    from ctypes import windll, byref, create_unicode_buffer, create_string_buffer

    FR_PRIVATE = 0x10
    FR_NOT_ENUM = 0x20


    def load_font(font_path, private: bool = True, enumerable: bool = False):
        """
        Makes fonts located in file 'font_path' available to the font system
        :param font_path: font path
        :param private: if True, other processes cannot see this font, and this font will be unloaded when the process dies
        :param enumerable: if True, this font will appear when enumerating fonts
        :return: bool(num_fonts_added)
        """
        if isinstance(font_path, str):
            path_buf = create_unicode_buffer(font_path)
            add_font_resource_ex = windll.gdi32.AddFontResourceExW
        elif isinstance(font_path, bytes):
            path_buf = create_string_buffer(font_path)
            print(path_buf)
            add_font_resource_ex = windll.gdi32.AddFontResourceExA
        else:
            raise TypeError('font_path must be of type str or bytes')

        flags = (FR_PRIVATE if private else 0) | (FR_NOT_ENUM if not enumerable else 0)
        num_fonts_added = add_font_resource_ex(byref(path_buf), flags, 0)
        return bool(num_fonts_added)
else:
    def load_font(font_path):
        pass
