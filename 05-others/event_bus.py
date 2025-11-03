import asyncio

class EventBus:
    subscribers = {}
    
    @classmethod
    def subscriber(cls, event_type, subcriber):
        if event_type not in cls.subscribers:
            cls.subscribers[event_type] = []
        cls.subscribers[event_type].append(subcriber)
    
    @classmethod
    async def publish(cls, event_type: str, data=None):
        if event_type in cls.subscribers:
            await asyncio.gather(*(s.handle_event(event_type, data)
                                   for s in cls.subscribers[event_type]))