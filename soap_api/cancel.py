#!/usr/bin/Python3

from config import client
from config import Credentials

TrackingNumber = "9461211899564690760126"


if __name__ == '__main__':
    print(client.service.CancelIndicium(Credentials=Credentials, TrackingNumber=TrackingNumber))
