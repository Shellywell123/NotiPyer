#!/bin/bash

root="https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-linux"

if [[ $(uname -m) =~ "64" ]]; then
    echo "Fetching 64 bit geckodriver"
    url=$root"64.tar.gz"
else
    echo "Fetching 32 bit geckodriver"
    url=$root"32.tar.gz"
fi

curl -L $url | tar xfz -