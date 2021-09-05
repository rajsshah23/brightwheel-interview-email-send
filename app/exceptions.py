class SpendgridException(Exception):
    pass


class SpendgridSendException(SpendgridException):
    pass


class SpendgridSendNon200Response(SpendgridSendException):
    pass


class SnailgunException(Exception):
    pass


class SnailgunSendException(SnailgunException):
    pass


class SnailgunSendNon200Response(SnailgunSendException):
    pass
