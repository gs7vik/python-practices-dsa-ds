from typing_extensions import TypedDict
#typeddict is used for type hints (static checking)

class CheckTypeDict(TypedDict):
    id: int
    content: str
    timestamp: float
    
# message:CheckTypeDict={ even tho i mentioned id as int its working fine dont know why
#     "id":"hello",
#     "content":"hello world",
#     "timestamp":1
# }

message:CheckTypeDict={"id1":1,"content":"hello","timestamp":1.2}

print(message)