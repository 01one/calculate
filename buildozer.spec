[app]
title = Calculate
package.name = calculate
package.domain = org.pygame
source.dir = .

source.include_exts = 

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png


# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# version.regex = __version__ = ['"](.*)['"]
version.filename = %(source.dir)s/main.py


requirements = python3,pygame

icon.filename = %(source.dir)s/icon.png

orientation = portrait
author = © Copyright Mashiur Rahman

osx.python_version = 3

fullscreen = 0

android.whitelist = calculate/*

ndroid.add_activites = com.example.ExampleActivity

p4a.branch = develop



# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86
android.arch = armeabi-v7a


[buildozer]
