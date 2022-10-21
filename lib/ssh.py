import traceback
import time
import paramiko
from paramiko import SSHClient


class Ssh():
    def __init__(self, ip_address, username, port=22, password=None, pubkey=None):
        self.ip_address = ip_address
        self.username = username
        self.password = password
        self.port = port
        self.pubkey = pubkey

    def scp_file(self, source, destination, put=True, retry=3):
        try:
            session = None
            loop = 0
            while True:
                try:
                    success = True

                    session = SSHClient()
                    session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    session.connect(
                        self.ip_address,
                        port=self.port,
                        username=self.username,
                        password=self.password,
                        timeout=3
                    )

                    sftp = paramiko.SFTPClient.from_transport(session.get_transport())
                    if put:
                        sftp.put(source, destination)
                    else:
                        sftp.get(source, destination)
                    sftp.close()

                    session.close()
                except BaseException:
                    print(traceback.format_exc())
                    success = False
                finally:
                    if session is not None:
                        session.close()

                if success:
                    return True

                loop = loop + 1
                if loop > retry:
                    return False

                time.sleep(loop * 5)

        except BaseException:
            return False
