cd ../
flatpak-builder build-dir flatpak.yaml --force-clean
flatpak build-export anime-player-repo build-dir
flatpak build-bundle anime-player-repo AnimePlayer.flatpak com.mazur.AnimePlayer
flatpak uninstall -y com.mazur.AnimePlayer
flatpak install -y --bundle --user AnimePlayer.flatpak
flatpak run com.mazur.AnimePlayer