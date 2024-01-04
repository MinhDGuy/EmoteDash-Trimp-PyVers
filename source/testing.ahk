$g::
	SendInput {g down} {g up}
	Sleep 100
    SendInput {Space down} {Space up}
    Sleep 50
    SendInput {3 down} {3 up}
	Sleep 100
	SendInput {LCtrl down}
Return

$h::SendInput {LCtrl up} {g down} {g up}