#!/usr/bin/expect -f
    set timeout 20
    set IPaddress [lindex $argv 0]
    set Username "alex"
    set Password "alex123"
    set Directory /home/alex/

    log_file -noappend $Directory/CHK_TRAFFIC.log
    send_log "### /START-SSH-SESSION/ IP: $IPaddress @ [exec date] ###\r"

    spawn ssh -o "StrictHostKeyChecking no" $Username@hostname
    expect "*assword:"
    send "$Password\r"
    expect ">"
    send "show int desc | match xe-0/0/0\r"
    expect ">"
    send "show int xe-0/0/0 | match rate\r"
    expect ">"
    send "exit\r"
    interact
    send_log "### /END-SSH-SESSION/ IP: $IPaddress @ [exec date] ###\r"

    spawn ssh -o "StrictHostKeyChecking no" $Username@hostname
    expect "*assword:"
    send "$Password\r"
    expect ">"
    send "show int desc | match xe-1/1/1\r"
    expect ">"
    send "show int xe-1/1/1 | match rate\r"
    expect ">"
    send "exit\r"
    interact
#    send_log "### /END-SSH-SESSION/ IP: $IPaddress @ [exec date] ###\r"
exit
