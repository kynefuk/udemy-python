import enum

# enum.uniqueを付けると値の重複があるとエラーになる
@enum.unique
class Status(enum.Enum):
    # name, value
    ACTIVE = 1
    INACTIVE = 2
    RUNNNING = 3


print(Status.ACTIVE.name)
print(Status.ACTIVE.value)

# Status()にvalueを入れると対応するnameが返ってくる
print(Status(1))

# Falseになる
print(Status.ACTIVE == 1)


#######################

# IntEnumのメンバーは int型と比較することができる。基本的にはEnumを使った方が良い
class Status2(enum.IntEnum):
    # name, value
    ACTIVE = 1
    INACTIVE = 2
    RUNNNING = 3


# Trueとなる
print(Status2.ACTIVE == 1)

print(Status(1))


#######################

# Flagではビット演算子が使える
class Perm(enum.IntFlag):
    R = 4
    W = 2
    X = 1


# 論理和なので6となる
print(int(Perm.R | Perm.W))

RWX = Perm.R | Perm.W | Perm.X

# Trueが返ってくる
print(Perm.R in RWX)
