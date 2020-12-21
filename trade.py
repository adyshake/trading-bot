import robin_stocks as rs
import os

robin_username = os.environ.get("robin_username")
robin_password = os.environ.get("robin_password")

print(robin_username)
print(robin_password)

rs.login(username=robin_username,
         password=robin_password,
         expiresIn=86400,
         by_sms=True)

rs.logout()