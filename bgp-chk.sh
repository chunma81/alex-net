#!/usr/bin/expect -f
    set timeout 20
    set IPaddress [lindex $argv 0]
    set Username “alex"
    set Password “alex123"
    set Directory /home/alex/

    log_file -noappend $Directory/CHK_LINK_STATUS.log
    send_log "### /START-SSH-SESSION/ IP: $IPaddress @ [exec date] ###\r"

    spawn ssh -o "StrictHostKeyChecking no" $Username@hostname
    expect "*assword:"
    send "$Password\r"
    expect ">"
    send "show bgp summary | match 2914\r"
    expect "l>"
    send "show int desc | match NTT\r"
    expect "l>"
    send "show ospf neighbor\r"
    expect ">"
    send "exit\r"
    interact
    send_log "### /END-SSH-SESSION/ IP: $IPaddress @ [exec date] ###\r"
exit
