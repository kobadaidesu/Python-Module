import random
import typing


players: list[str] = ["bob", "alice", "dylan", "charlie"]
actions: list[str] = ["run", "eat", "release", "climb", "use", "grab"]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        name: str = random.choice(players)
        action: str = random.choice(actions)
        yield (name, action)


def consume_event(
    event_list: list[tuple[str, str]],
) -> typing.Generator[tuple[str, str], None, None]:
    while len(event_list) > 0:
        index: int = random.randrange(0, len(event_list))
        yield event_list.pop(index)


def main() -> None:
    events: typing.Generator[tuple[str, str], None, None] = gen_event()
    print("=== Game Data Stream Processor ===")
    for index in range(1000):
        name, action = next(events)
        print(f"Event {index}: Player {name} did action {action}")
    event_list: list[tuple[str, str]] = []
    for _ in range(10):
        event_list.append(next(events))
    print(f"Built list of 10 events: {event_list}")
    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()
