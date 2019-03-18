import logging
from bs4 import BeautifulSoup

from kik_unofficial.callbacks import KikClientCallback
from kik_unofficial.datatypes.xmpp.errors import SignUpError, LoginError
from kik_unofficial.datatypes.xmpp.chatting import IncomingMessageDeliveredEvent, IncomingMessageReadEvent, IncomingChatMessage, \
    IncomingGroupChatMessage, IncomingFriendAttribution, IncomingGroupStatus, IncomingIsTypingEvent, IncomingGroupIsTypingEvent, \
    IncomingStatusResponse, IncomingGroupSticker, IncomingGroupSysmsg, IncomingImageMessage, IncomingGroupReceiptsEvent, IncomingGifMessage, \
    IncomingVideoMessage
from kik_unofficial.datatypes.xmpp.roster import FetchRosterResponse, PeerInfoResponse, GroupSearchResponse
from kik_unofficial.datatypes.xmpp.sign_up import RegisterResponse, UsernameUniquenessResponse
from kik_unofficial.datatypes.xmpp.login import LoginResponse

log = logging.getLogger('kik_unofficial')


class XmlnsHandler:
    def __init__(self, callback: KikClientCallback, api):
        self.callback = callback
        self.api = api

    def handle(self, data: BeautifulSoup):
        raise NotImplementedError


class CheckUniqueHandler(XmlnsHandler):
    def handle(self, data: BeautifulSoup):
        self.callback.on_username_uniqueness_received(UsernameUniquenessResponse(data))


class RegisterHandler(XmlnsHandler):
    def handle(self, data: BeautifulSoup):
        message_type = data['type']

        if message_type == "error":
            if data.find('email'):
                # sign up
                sign_up_error = SignUpError(data)
                log.info("[-] Register error: {}".format(sign_up_error))
                self.callback.on_register_error(sign_up_error)

            else:
                login_error = LoginError(data)
                log.info("[-] Login error: {}".format(login_error))
                self.callback.on_login_error(login_error)

        elif message_type == "result":
            if data.find('node'):
                self.api.node = data.find('node').text
            if data.find('email'):
                # login successful
                response = LoginResponse(data)
                log.info("[+] Logged in as {}".format(response.username))
                self.callback.on_login_ended(response)
                self.api._establish_authenticated_session(response.kik_node)
            else:
                # sign up successful
                response = RegisterResponse(data)
                log.info("[+] Registered.")
                self.callback.on_sign_up_ended(response)
                self.api._establish_authenticated_session(response.kik_node)


class RosterHandler(XmlnsHandler):
    def handle(self, data: BeautifulSoup):
        self.callback.on_roster_received(FetchRosterResponse(data))


class MessageHandler(XmlnsHandler):
    def handle(self, data: BeautifulSoup):
        if data['type'] == 'chat':
            # what kind of chat message is it?
            if data.body and data.body.text:
                # regular text message
                self.callback.on_chat_message_received(IncomingChatMessage(data))
            elif data.find('friend-attribution'):
                # friend attribution
                self.callback.on_friend_attribution(IncomingFriendAttribution(data))
            elif data.find('status'):
                # status
                self.callback.on_status_message_received(IncomingStatusResponse(data))
            elif data.find('xiphias-mobileremote-call'):
                # usually SafetyNet-related (?)
                mobile_remote_call = data.find('xiphias-mobileremote-call')
                log.warning("[!] Received mobile-remote-call with method '{}' of service '{}'".format(
                                mobile_remote_call['method'], mobile_remote_call['service']))
            elif data.find('images'):
                # images
                self.callback.on_image_received(IncomingImageMessage(data))
            else:
                # what else? GIFs?
                log.debug("[-] Received unknown chat message. contents: {}".format(str(data)))
        elif data['type'] == 'receipt':
            if data.g:
                self.callback.on_group_receipts_received(IncomingGroupReceiptsEvent(data))
            elif data.receipt['type'] == 'delivered':
                self.callback.on_message_delivered(IncomingMessageDeliveredEvent(data))
            else:
                self.callback.on_message_read(IncomingMessageReadEvent(data))
        elif data['type'] == 'is-typing':
            self.callback.on_is_typing_event_received(IncomingIsTypingEvent(data))
        elif data['type'] == 'groupchat':
            if data.body:
                self.callback.on_group_message_received(IncomingGroupChatMessage(data))
            elif data.find('is-typing'):
                self.callback.on_group_is_typing_event_received(IncomingGroupIsTypingEvent(data))
            elif data.find('status'):
                self.callback.on_group_status_received(IncomingGroupStatus(data))
            elif data.find('sysmsg'):
                self.callback.on_group_sysmsg_received(IncomingGroupSysmsg(data))
            else:
                log.debug("[-] Received unknown groupchat message. contents: {}".format(str(data)))
        else:
            log.debug("[-] Received unknown message type. contents: {}".format(str(data)))


class GroupMessageHandler(XmlnsHandler):
    def handle(self, data: BeautifulSoup):
        if data.body:
            self.callback.on_group_message_received(IncomingGroupChatMessage(data))
        elif data.find('is-typing'):
            self.callback.on_group_is_typing_event_received(IncomingGroupIsTypingEvent(data))
        elif data.content and 'app-id' in data.content.attrs:
            app_id = data.content['app-id']
            if app_id == 'com.kik.ext.stickers':
                self.callback.on_group_sticker(IncomingGroupSticker(data))
            elif app_id == 'com.kik.ext.gallery':
                self.callback.on_image_received(IncomingImageMessage(data))
            elif app_id == 'com.kik.ext.camera':
                self.callback.on_image_received(IncomingImageMessage(data))
            elif app_id == 'com.kik.ext.gif':
                self.callback.on_gif_received(IncomingGifMessage(data))
            elif app_id == 'com.kik.ext.video-camera':
                self.callback.on_video_received(IncomingVideoMessage(data))

        else:
            log.debug("[-] Received unknown group message. contents: {}".format(str(data)))


class FriendMessageHandler(XmlnsHandler):
    def handle(self, data: BeautifulSoup):
        self.callback.on_peer_info_received(PeerInfoResponse(data))


class GroupSearchHandler(XmlnsHandler):
    def handle(self, data: BeautifulSoup):
        self.callback.on_group_search_response(GroupSearchResponse(data))
