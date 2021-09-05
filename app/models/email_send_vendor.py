import enum


class EmailSendVendor(str, enum.Enum):
    spendgrid = "spendgrid"
    snailgun = "snailgun"
