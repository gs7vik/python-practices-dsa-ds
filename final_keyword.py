from typing import Final, final

PI: Final = 3.14159
PI = 3  # ❌ Type checker (e.g., mypy) will warn about this (this will come only if you have installed mypy its not a runtime feature)
print(PI)  # 3

#final keyword is also used to prevent method overriding in classes 
from typing import final

class Base:
    @final
    def do_something(self):
        print("Doing something...")

class Derived(Base):
    def do_something(self):  # ❌ mypy will warn: Cannot override final method
        print("Trying to override")