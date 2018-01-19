from kik_unofficial.message.message import Message


class AddToGroupMessage(Message):
    def __init__(self, group_jid, peer_jid):
        super().__init__()
        self.group_jid = group_jid
        self.peer_jid = peer_jid

    def serialize(self) -> bytes:
        data = ('<iq type="set" id="{}">'
                '<query xmlns="kik:groups:admin">'
                '<g jid="{}">'
                '<m>{}</m>'
                '</g>'
                '</query>'
                '</iq>').format(self.message_id, self.group_jid, self.peer_jid)
        return data.encode()


class RemoveFromGroupMessage(Message):
    def __init__(self, group_jid, peer_jid):
        super().__init__()
        self.group_jid = group_jid
        self.peer_jid = peer_jid

    def serialize(self) -> bytes:
        data = ('<iq type="set" id="{}">'
                '<query xmlns="kik:groups:admin">'
                '<g jid="{}">'
                '<m r="1">{}</m>'
                '</g>'
                '</query>'
                '</iq>').format(self.message_id, self.group_jid, self.peer_jid)
        return data.encode()


class UnbanMessage(Message):
    def __init__(self, group_jid, peer_jid):
        super().__init__()
        self.group_jid = group_jid
        self.peer_jid = peer_jid

    def serialize(self) -> bytes:
        data = ('<iq type="set" id="{}">'
                '<query xmlns="kik:groups:admin">'
                '<g jid="{}">'
                '<b r="1">{}</m>'
                '</g>'
                '</query>'
                '</iq>').format(self.message_id, self.group_jid, self.peer_jid)
        return data.encode()


class BanMessage(Message):
    def __init__(self, group_jid, peer_jid):
        super().__init__()
        self.group_jid = group_jid
        self.peer_jid = peer_jid

    def serialize(self) -> bytes:
        data = ('<iq type="set" id="{}">'
                '<query xmlns="kik:groups:admin">'
                '<g jid="{}">'
                '<b>{}</m>'
                '</g>'
                '</query>'
                '</iq>').format(self.message_id, self.group_jid, self.peer_jid)
        return data.encode()
