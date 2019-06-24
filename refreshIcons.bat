taskkill /IM explorer.exe /F
CD /d %userprofile%\AppData\Local
DEL IconCache.db /a
start explorer.exe
