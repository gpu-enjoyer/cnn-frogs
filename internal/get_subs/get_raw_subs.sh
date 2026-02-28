#!/bin/bash

yt-dlp \
    --skip-download \
    --write-auto-subs \
    --sub-lang en \
    --convert-subs srt \
    https://www.youtube.com/watch?v=jztwpsIzEGc
