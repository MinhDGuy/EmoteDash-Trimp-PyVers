3If WinActive("ahk_exe RobloxPlayerBeta.exe")

$g::
	SendInput {f down} {f up}
	Sleep 25
	SendInput {g down} {g up}
    SendInput {3 down} {3 up}
	Sleep 100
	SendInput {c down}
Return

$h::SendInput {c up} {g down} {g up}