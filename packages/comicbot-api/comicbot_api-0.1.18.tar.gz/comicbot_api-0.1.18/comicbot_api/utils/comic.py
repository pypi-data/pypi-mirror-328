from dataclasses import dataclass


@dataclass(init=False)
class Comic:
    title: str
    url: str

    def __init__(self, **kwargs):
        self.url = kwargs['url']
        self.title = kwargs['title']

    # def __repr__(self):
    #     return pprint.pformat(dataclasses.asdict(self))
