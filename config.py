#!/usr/bin/Python3

from zeep import Client

IntegrationID = "IntegratorTxID"
Username = "Username"
Password = "Password"

Credentials = dict(
    IntegrationID=IntegrationID,
    Username=Username,
    Password=Password
)

client = Client(wsdl="https://swsim.testing.stamps.com/swsim/swsimv69.asmx?wsdl")
