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
