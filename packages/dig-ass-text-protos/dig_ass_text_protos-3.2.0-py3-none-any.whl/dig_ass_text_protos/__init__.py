__version__ = "3.2.0"

from .DigitalAssistantText_pb2 import (
    DigitalAssistantTextRequest,
    DigitalAssistantTextResponse,
    ChatItem,
    InnerContextItem,
    OuterContextItem,
    ReplicaItem,
)

from .DigitalAssistantText_pb2_grpc import DigitalAssistantTextStub
