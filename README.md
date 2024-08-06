# About

This is simply a collection of configuration files I use for my setup. The purpose of this repository is to have a backup of these files and an easy way to replicate my environment on different computers.

# Installing the extensions

```sh
cat <EXTENSIONSFILE> | awk '{print "--install-extension " $0}' | xargs code
```
