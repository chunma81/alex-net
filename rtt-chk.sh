#!/usr/bin/expect -f
    set timeout 20
    set IPaddress [lindex $argv 0]
    set Username "alex"
    set Password "alex123"
    set Directory /home/alex/

    log_file -noappend $Directory/CHK_RTT.log
    send_log "### /START-SSH-SESSION/ IP: $IPaddress @ [exec date] ###\r"

    spawn ssh -o "StrictHostKeyChecking no" $Username@hostname
    expect "*assword:"
    send "$Password\r"
    expect ">"
    send "start shell\r"
    expect "%"
    send "mtr 8.8.8.8 -r -c 5 -n\r"
    expect "%"
    send "exit\r"
    expect ">"
    send "exit\r"
    interact
    send_log "### /END-SSH-SESSION/ IP: $IPaddress @ [exec date] ###\r"
exit
