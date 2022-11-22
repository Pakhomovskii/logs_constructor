# Python structured logs construction (using context manager) IN_PROGRESS

## Description

This program can generate logs after your bash command execution. You can just fill in the json file and describe what commands and what the output you are going to logging

## Example

In default configuration you can use standard tamplate

If you what to use your own structure create json file (IN_PROGRESS)

```yaml
{
    "name_of_temp": "NetworkManagerInfo",
    "main_command": "sudo journalctl -u NetworkManager -S yesterday",
    "time": "local",
    "sourceInfo": true,
    "memoryInfo": true
}
```
>  ### Where  "`name_of_temp`"  the name of your file. Use "'command'" keyword in your keys if your want to execute the command and save output in logs
___

#### Then run the log_gen.py. Supposed output:

```yaml
NetworkManagerInfo

Filesystem
      Size  Used Avail Use% Mounted on\ntmpfs           
      1.5G  2.4M  1.5G   1% /run\n/dev/nvme0n1p2  
      468G   88G  357G  20% /\ntmpfs           
      7.5G  170M  7.4G   3% /dev/shm\ntmpfs           
      5.0M  4.0K  5.0M   1% /run/lock\n/dev/nvme0n1p1  
      511M  5.3M  506M   2% /boot/efi\ntmpfs          
      1.5G   13M  1.5G   1% /run/user/1000\n'

                      Nov 21 20:17:33 sawkay-laptop NetworkManager[1049]: <info>  
                      [1669036653.3776] modem-manager: ModemManager no longer available\nNov 21 20:17:34 sawkay-laptop systemd[1]: Stopping Network Manager...
                      \nNov 21 20:17:34 sawkay-laptop NetworkManager[1049]: <info>  
                      [1669036654.3056] caught SIGTERM, shutting down normally.
                      \nNov 21 20:17:34 sawkay-laptop NetworkManager[1049]: <info>  
                      [1669036654.5402] device (wlp3s0): state change: activated -> deactivating (reason \'unmanaged\', sys-iface-state: \'managed\')\nNov 21 20:17:34 sawkay-laptop NetworkManager[1049]: <warn> 

```

