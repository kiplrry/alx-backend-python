#!/usr/bin/python3

class User:
    name: str
    id: int

larry = User()
larry.names = 'larry'
print(larry.__dict__)