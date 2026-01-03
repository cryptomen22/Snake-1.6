[app]

title = Snake 1.6
package.name = snake16ultimate
package.domain = org.vseznaushchy

source.dir = .
source.include_exts = py,png,jpg,jpeg,gif,bmp,wav,mp3,ogg,ttf,otf

requirements = python3,kivy==2.1.0,pygame==2.1.0,android

version = 1.6

orientation = portrait
fullscreen = 1

android.permissions = INTERNET

android.api = 31
android.minapi = 21
android.ndk = 23c
android.sdk = 31
android.archs = arm64-v8a

android.accept_sdk_license = True

p4a.bootstrap = sdl2
p4a.branch = master

log_level = 2
warn_on_root = 1

[buildozer]

build_dir = ./.buildozer
bin_dir = ./bin
