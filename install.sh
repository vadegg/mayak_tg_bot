#!/bin/bash
pip3 install PyTelegramBotAPI==2.2.3
sqlite3 db/main.db < db/schemas.sql
