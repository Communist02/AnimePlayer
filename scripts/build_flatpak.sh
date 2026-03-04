cd ../
flatpak-builder build-dir flatpak.yaml --force-clean
flatpak build-export anime-player-repo build-dir
flatpak build-bundle anime-player-repo anime_player_x86_64.flatpak io.github.communist02.AnimePlayer
flatpak uninstall -y io.github.communist02.AnimePlayer
flatpak install -y --bundle --user anime_player_x86_64.flatpak
flatpak run io.github.communist02.AnimePlayer
