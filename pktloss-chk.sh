#!/usr/bin/expect -f
    set timeout 20
    set IPaddress [lindex $argv 0]
    set Username “alex"
    set Password “alex123"
    set Directory /home/alex/

    log_file -noappend $Directory/CHK_LOSS.log
    send_log "### /START-SSH-SESSION/ IP: $IPaddress @ [exec date] ###\r"

    spawn ssh -o "StrictHostKeyChecking no" $Username@hostname
    expect "*assword:"
    send "$Password\r"
    expect ">"
    send "show route 8.8.8.8\r"
    expect ">"
    send "ping 8.8.8.8 rapid count 50 size 1450\r"
    expect ">"
    send "start shell\r"
    expect "%"
    send "mtr 8.8.8.8 -r -c 1 -n\r"
    expect "%"
    send "exit\r"
    expect ">"
    send "exit\r"
    interact
    send_log "### /END-SSH-SESSION/ IP: $IPaddress @ [exec date] ###\r"
exit
