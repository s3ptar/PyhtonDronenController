#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""#####################################################################
#! @ file:                   util_configuration.py.py
#  @ projekt:                PyhtonDronenController
#  @ created on:             2026-07-27
#  @ author:                 R. Gräber
#  @ version:                1
#  @ history:                -
#  @ brief:                  Side Function
#                            logging handlings
#####################################################################"""

"""#####################################################################
# Includes
#####################################################################"""
import json
"""#####################################################################
# Informations
#####################################################################"""

"""#####################################################################
# Declarations
#####################################################################"""

"""#####################################################################
# Constant
#####################################################################"""

"""#####################################################################
# Global Variable
#####################################################################"""

"""#####################################################################
# local Variable
#####################################################################"""

"""#####################################################################
# Constant
#####################################################################"""

"""#####################################################################
# Local Funtions
#####################################################################"""



"""#####################################################################
#! @fn           load_config
#  @ brief       read the default config and override it with the override config
#  @ param       none
#  @ exception   none
#  @ return      dict with the merged configuration
#####################################################################"""
def load_config(config_name=None) -> dict:
    """Lädt die Default-Basis und überschreibt sie mit der Override-Config."""
    # Standardkonfiguration
    config = {}
    # 1. Default-Config laden
    try:
        with open("config/default_config.json", "r") as f:
            config = json.load(f)
    except Exception as e:
        print(f"Hinweis: default_config.json nicht gefunden. Nutze Hardcoded Defaults. Error {e}")

    # 2. Override-Config laden und Werte überschreiben
    try:
        with open("config/override_config.json", "r") as f:
            override = json.load(f)
            config.update(override)
    except Exception:
        # Falls keine Override-Datei existiert, ist das völlig okay
        pass

    if config_name is not None:
        return config[config_name]
    else:
        return config


"""#####################################################################
#! @fn           write_config(config_name, config_data)
#  @param        config_name - Name der Konfiguration, z.B. "Master_DEV"
#  @param        config_data - Dictionary mit den Konfigurationsdaten
#  @ brief       write the override config to the override file
#  @ param       none
#  @ exception   none
#  @ return      dict with the merged configuration
#####################################################################"""
def write_config(config_name, config_data):
    """Schreibt die Konfiguration in die Override-Datei."""
    try:
        # 1. Aktuelle Override-Config laden
        override = {}
        try:
            with open("config/override_config.json", "r") as f:
                override = json.load(f)
        except Exception:
            # Falls keine Override-Datei existiert, ist das völlig okay
            pass

        # 2. Neue Konfiguration setzen
        override[config_name] = config_data

        # 3. In die Datei schreiben
        with open("config/override_config.json", "w") as f:
            json.dump(override, f, indent=4)

        print(f"Konfiguration für {config_name} erfolgreich gespeichert.")
    except Exception as e:
        print(f"Fehler beim Speichern der Konfiguration: {e}")




"""#####################################################################
#! @fn           int main(){
#  @ brief       start up function
#  @ param       none
#  @ exception   none
#  @ return      none
#####################################################################"""

if __name__ == "__main__":
    print("Hello World!")

