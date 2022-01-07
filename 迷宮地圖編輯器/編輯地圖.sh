#!/bin/sh

if [[ -x "Tiled-1.7.2-x86_64.AppImage" ]]
then
    ./Tiled-1.7.2-x86_64.AppImage MazeCar.tmx &
else
    xdg-open "https://thorbjorn.itch.io/tiled"
fi
