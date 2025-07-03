FROM quay.io/pypa/manylinux_2_34_x86_64

ENV PATH="/opt/python/cp313-cp313/bin:$PATH"
RUN /opt/python/cp313-cp313/bin/pip install --upgrade pip && pip install nuitka

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
RUN cd /opt/_internal && tar xf static-libs-for-embedding-only.tar.xz

COPY . /app

RUN nuitka --enable-plugin=pyside6 --output-file=anime_player --include-data-files=docs/GLSL_Instructions_Advanced.txt=docs/GLSL_Instructions_Advanced.txt --include-data-files=docs/GLSL_Instructions_Advanced_ru.txt=docs/GLSL_Instructions_Advanced_ru.txt --include-data-dir=images=images --include-data-dir=shaders=shaders --product-name="Anime Player" --product-version=2 --standalone main.py
