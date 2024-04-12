#!/bin/bash

# Update package list
sudo apt update

# Upgrade all packages
sudo apt upgrade -y

# Update Flatpak apps
flatpak update --non-interactive