import subprocess
from datetime import datetime
from .models import OSUser


def get_linux_users():
    output = subprocess.check_output(
        "getent passwd | grep '/home/' | cut -d: -f1",
        shell=True,
        universal_newlines=True)
    return output.strip().split('\n')


def update_os_users():
    for username in get_linux_users():
        if OSUser.objects.filter(login=username).exists():
            continue
        os_user = OSUser(
            login=username,
            pass_number=username + datetime.now().strftime("%Y-%m-%d"),
            at_work=True,
        )
        os_user.save()
