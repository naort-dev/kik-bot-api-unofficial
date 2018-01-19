import asyncio
import logging
import time
from asyncio import Transport, Protocol
from threading import Thread

from bs4 import BeautifulSoup
from kik_unofficial.callback import KikCallback
from kik_unofficial.handler import CheckUniqueHandler, RegisterHandler, RosterHandler, MessageHandler, \
    GroupMessageHandler, FriendMessageHandler
from kik_unofficial.kik_exceptions import KikApiException
from kik_unofficial.message.chat import GroupChatMessage, ChatMessage, ReadReceiptMessage, DeliveredReceiptMessage, \
    IsTypingMessage, GroupIsTypingMessage, GroupReceiptResponse
from kik_unofficial.message.group import AddToGroupMessage, RemoveFromGroupMessage, BanMessage, UnbanMessage
from kik_unofficial.message.message import Message
from kik_unofficial.message.roster import RosterMessage, BatchFriendMesssage, FriendMesssage, AddFriendMessage
from kik_unofficial.message.unauthorized.checkunique import CheckUniqueMessage
from kik_unofficial.message.unauthorized.register import LoginMessage, RegisterMessage, EstablishAuthConnectionMessage, \
    ConnectionFailedResponse

HOST, PORT = "talk1110an.kik.com", 5223


class KikApi:
    def __init__(self, callback: KikCallback, username=None, password=None, loglevel=logging.INFO):
        """
        Initializes a connection to Kik servers. Use username and password for logging in.

        :param callback: KikCallback containing callback implementation.
        :param username: username.
        :param password: password.
        :param loglevel: logging level.
        """
        logging_format = '%(asctime)-15s %(levelname)-6s %(threadName)-10s %(message)s'
        logging.basicConfig(format=logging_format, level=loglevel, datefmt='%Y-%m-%d %H:%M:%S', filename='kik.log',
                            filemode='w')
        self.callback = callback
        self.handlers = {
            'kik:iq:check-unique': CheckUniqueHandler(callback, self),
            'jabber:iq:register': RegisterHandler(callback, self),
            'jabber:iq:roster': RosterHandler(callback, self),
            'jabber:client': MessageHandler(callback, self),
            'kik:groups': GroupMessageHandler(callback, self),
            'kik:iq:friend': FriendMessageHandler(callback, self),
        }
        self.connected = False
        self.authenticated = False
        self.connection = None
        self.loop = asyncio.get_event_loop()
        self.node = None
        self.initial_connection_payload = '<k anon="">'.encode()
        self.username = username
        self.password = password
        if username and password:
            self.authenticate_on_connection = True
        self._connect()

    def _connect(self):
        self.kik_connection_thread = Thread(target=self._kik_connection_thread_function)
        self.kik_connection_thread.start()

    def login(self, username, password, captcha_result=None):
        self.username = username
        self.password = password
        login_message = LoginMessage(username, password, captcha_result)
        return self._send(login_message)

    def register(self, email, username, password, first_name, last_name, birthday="1974-11-20", captcha_result=None):
        self.username = username
        self.password = password
        register_message = RegisterMessage(email, username, password, first_name, last_name, birthday, captcha_result)
        return self._send(register_message)

    def check_unique(self, username):
        return self._send(CheckUniqueMessage(username))

    def request_roster(self):
        return self._send(RosterMessage())

    def send(self, peer_jid: str, message: str):
        if self.is_group_jid(peer_jid):
            return self._send(GroupChatMessage(peer_jid, message))
        else:
            return self._send(ChatMessage(peer_jid, message))

    @staticmethod
    def is_group_jid(jid):
        if '@talk.kik.com' in jid:
            return False
        elif '@groups.kik.com' in jid:
            return True
        else:
            raise KikApiException('Not a valid jid')

    def send_read_receipt(self, peer_jid: str, receipt_message_id: str):
        return self._send(ReadReceiptMessage(peer_jid, receipt_message_id))

    def send_delivered_receipt(self, peer_jid: str, receipt_message_id: str):
        return self._send(DeliveredReceiptMessage(peer_jid, receipt_message_id))

    def send_is_typing(self, peer_jid: str, is_typing: bool):
        if self.is_group_jid(peer_jid):
            return self._send(GroupIsTypingMessage(peer_jid, is_typing))
        else:
            return self._send(IsTypingMessage(peer_jid, is_typing))

    def request_info_from_jid(self, peer_jid: str):
        return self._send(BatchFriendMesssage(peer_jid))

    def request_info_from_username(self, username: str):
        return self._send(FriendMesssage(username))

    def add_friend(self, peer_jid):
        return self._send(AddFriendMessage(peer_jid))

    def add_to_group(self, group_jid, peer_jid):
        return self._send(AddToGroupMessage(group_jid, peer_jid))

    def remove_from_group(self, group_jid, peer_jid):
        return self._send(RemoveFromGroupMessage(group_jid, peer_jid))

    def ban(self, group_jid, peer_jid):
        return self._send(BanMessage(group_jid, peer_jid))

    def unban(self, group_jid, peer_jid):
        return self._send(UnbanMessage(group_jid, peer_jid))

    def _establish_auth_connection(self):
        self.connect_auth = True
        logging.debug("Establishing authenticated connection on node {}".format(self.node))
        self._connect()

    def _kik_connection_thread_function(self):
        """ Runs in Kik connection thread """
        if self.loop and self.loop.is_running():
            self.loop.call_soon_threadsafe(self.connection.close)
            while self.loop.is_running():
                time.sleep(0.1)
                logging.debug("Waiting for loop to stop.")
        self.connection = KikConnection(self.loop, self)
        coro = self.loop.create_connection(lambda: self.connection, HOST, PORT, ssl=True)
        self.loop.run_until_complete(coro)
        logging.debug("New connection made")
        self.loop.run_forever()

    def _send(self, message: Message):
        while not self.connected:
            logging.debug("Waiting for connection.")
            time.sleep(0.1)
        self.loop.call_soon_threadsafe(self.connection.send, (message.serialize()))
        return message.message_id

    def data_received(self, data: bytes):
        if data == b' ':
            # Happens every half hour. Disconnect after 10th time. Some kind of keep-alive? Let's send it back.
            self.loop.call_soon_threadsafe(self.connection.send, b' ')
        message = BeautifulSoup(data.decode(), features='xml')
        if len(message) > 0:
            message = next(iter(message))

        if message.name == "iq":
            self._handle_iq(message)
        elif message.name == "message":
            self._handle_message(message)
        elif message.name == "k":
            if message['ok'] == "1":
                self.connected = True
                if 'ts' in message.attrs:
                    self.authenticated = True
                    self.callback.on_authorized()
                elif self.authenticate_on_connection:
                    self.authenticate_on_connection = False
                    self.login(self.username, self.password)
            else:
                self.callback.on_connection_failed(ConnectionFailedResponse(message))

    def _handle_iq(self, message: BeautifulSoup):
        self._handle(message.query['xmlns'], message)

    def _handle_message(self, message: BeautifulSoup):
        if 'xmlns' in message.attrs:
            self._handle(message['xmlns'], message)
        elif message['type'] == 'receipt':
            self.callback.on_group_receipt(GroupReceiptResponse(message))

    def _handle(self, xmlns: str, message: BeautifulSoup):
        if xmlns not in self.handlers:
            raise NotImplementedError
        self.handlers[xmlns].handle(message)

    def connection_lost(self):
        self.connected = False

    def connection_made(self):
        if self.node:
            message = EstablishAuthConnectionMessage(self.node, self.username, self.password)
            self.initial_connection_payload = message.serialize()
        self.connection.send(self.initial_connection_payload)


class KikConnection(Protocol):
    def __init__(self, loop, api: KikApi):
        self.api = api
        self.loop = loop
        self.transport = None  # type: Transport

    def connection_made(self, transport: Transport):
        self.transport = transport
        logging.debug("Connection made")
        self.api.connection_made()

    def data_received(self, data: bytes):
        logging.debug("Received %s", data)
        self.loop.call_soon_threadsafe(self.api.data_received, data)

    def connection_lost(self, exc):
        logging.debug('Connection lost')
        self.loop.call_soon_threadsafe(self.api.connection_lost)
        self.loop.stop()

    def send(self, data: bytes):
        logging.debug("Sending %s", data)
        self.transport.write(data)

    def close(self):
        if self.transport:
            self.transport.write(b'</k>')
        logging.debug("Transport closed")
