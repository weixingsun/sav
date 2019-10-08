#!/bin/bash
. ./attach_dbus.sh unity
gsettings reset org.gnome.desktop.interface gtk-theme
gsettings reset org.gnome.desktop.interface icon-theme
