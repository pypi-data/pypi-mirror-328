import aiohttp
import asyncio
import json
from typing import Callable
class Robot:
    def __init__(self, auth: str):
        self.__auth = auth
        self.__base_url = "https://spius.ir/api/"
        self.handlers = {}

    @property
    def _auth(self):return self.__auth
    async def edit_bio(self, bio: str):
        """
        Edit the user's bio.

        ```python
        async def main():
            bot = Sina(token="your_token_here")
            edit_bio_response = await bot.edit_bio(bio="New bio text")
            print(edit_bio_response)
        asyncio.run(main())
        ```
        """
        return await self._post_request("EditBio.php", {'bio': bio})
    async def get_group_data(self, guid: str):
        """
        دریافت اطلاعات گروه با استفاده از شناسه گروه

        ```python
        async def main():
            bot = Sina(auth="bgmszbbwbwvsipffjvdmttqwohpfsnpo")
            group_data = await bot.get_group_data(guid="group_guid")
            print(group_data)
        asyncio.run(main())
        ```
        """
        return await self._post_request("GetGroup.php", {'guid': guid})

    async def send_group_message(self, guid: str, text: str):
        """
        ارسال پیام به گروه

        ```python
        async def main():
            bot = Sina(auth="bgmszbbwbwvsipffjvdmttqwohpfsnpo")
            response = await bot.send_group_message(guid="group_guid", text="پیام جدید")
            print(response)
        asyncio.run(main())
        ```
        """
        return await self._post_request("GroupSendMessage.php", {'guid': guid, 'text': text})

    async def edit_group(self, group_guid: str, group_name: str, description: str, group_image=None):
        """
        ویرایش اطلاعات گروه

        ```python
        async def main():
            bot = Sina(auth="bgmszbbwbwvsipffjvdmttqwohpfsnpo")
            response = await bot.edit_group(group_guid="group_guid", group_name="نام جدید", description="توضیحات جدید")
            print(response)
        asyncio.run(main())
        ```
        """
        return await self._post_request("EditGroup.php", {
            'group_guid': group_guid,
            'group_name': group_name,
            'description': description,
            'group_image': group_image
        })
    def on_group_update(self, func: Callable):
        """Decorator to handle group updates"""
        self.__handlers["group_update"] = func
        return func

    async def _post_request(self, endpoint: str, data: dict):
        url = f"{self.__base_url}{endpoint}"
        headers = {"Authorization": self._auth}
        data["auth"] = self._auth

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, data=data) as response:
                    response.raise_for_status()
                    response_text = await response.text()
                    return json.loads(response_text)
        except aiohttp.ClientError as e:
            return {"error": str(e)}

    async def get_group_data(self, guid: str):
        return await self._post_request("GetGroup.php", {'guid': guid})

    async def start(self):
        """Start the bot to listen for group updates"""
        while True:
            # Simulating getting group data as a new update
            group_data = await self.get_group_data("4d97b092e84d6c0")
            
            # Check if there's a handler for group_update event
            if "group_update" in self.__handlers:
                # Call the handler function with the group data
                await self.__handlers["group_update"](group_data)
            
            await asyncio.sleep(1)  # Delay to simulate receiving updates
    async def create_group(self, name: str, description: str, image=None):
        """
        ایجاد گروه جدید

        ```python
        async def main():
            bot = Sina(auth="bgmszbbwbwvsipffjvdmttqwohpfsnpo")
            response = await bot.create_group(name="گروه جدید", description="توضیحات گروه")
            print(response)
        asyncio.run(main())
        ```
        """
        return await self._post_request("CreateGroup.php", {
            'name': name,
            'description': description,
            'image': image
        })

    async def edit_name(self, name: str):
        """
        ویرایش نام کاربر

        ```python
        async def main():
            bot = Sina(auth="bgmszbbwbwvsipffjvdmttqwohpfsnpo")
            response = await bot.edit_name(name="نام جدید")
            print(response)
        asyncio.run(main())
        ```
        """
        return await self._post_request("EditName.php", {'name': name})

    async def edit_channel(self, channel_link: str, channel_name: str, channel_guid: str, description: str, channel_image=None):
        """
        ویرایش اطلاعات کانال

        ```python
        async def main():
            bot = Sina(auth="bgmszbbwbwvsipffjvdmttqwohpfsnpo")
            response = await bot.edit_channel(channel_link="لینک کانال", channel_name="نام کانال", channel_guid="guid کانال", description="توضیحات کانال")
            print(response)
        asyncio.run(main())
        ```
        """
        return await self._post_request("EditChannel.php", {
            'channel_link': channel_link,
            'channel_name': channel_name,
            'channel_guid': channel_guid,
            'description': description,
            'channel_image': channel_image
        })

    async def get_channel_data(self, guid: str):
        """
        دریافت اطلاعات کانال

        ```python
        async def main():
            bot = Sina(auth="bgmszbbwbwvsipffjvdmttqwohpfsnpo")
            channel_data = await bot.get_channel_data(guid="channel_guid")
            print(channel_data)
        asyncio.run(main())
        ```
        """
        return await self._post_request("GetChannel.php", {'guid': guid})

    async def send_channel_message(self, channel_guid: str, text: str):
        """
        ارسال پیام به کانال

        ```python
        async def main():
            bot = Sina(auth="bgmszbbwbwvsipffjvdmttqwohpfsnpo")
            response = await bot.send_channel_message(channel_guid="channel_guid", text="پیام به کانال")
            print(response)
        asyncio.run(main())
        ```
        """
        return await self._post_request("ChannelSendMessage.php", {
            'channel_guid': channel_guid,
            'text': text
        })

    async def show_devices(self):
        """
        نمایش اطلاعات دستگاه‌ها

        ```python
        async def main():
            bot = Sina(auth="bgmszbbwbwvsipffjvdmttqwohpfsnpo")
            devices = await bot.show_devices()
            print(devices)
        asyncio.run(main())
        ```
        """
        return await self._post_request("ShowDevices.php", {})

        return func
    async def start(self):
        while True:
            group_data = await self.get_group_data("4d97b092e84d6c0")
            
            if "message_update" in self.__handlers:
                for msg in group_data:
                    await self.__handlers["message_update"](msg)
            
            await asyncio.sleep(1)

    def run(self):
        asyncio.run(self.start())
    async def log_out(self):
        """
        Log out the user.

        ```python
        async def main():
            bot = Sina(token="your_token_here")
            log_out_response = await bot.log_out()
            print(log_out_response)
        asyncio.run(main())
        ```
        """
        return await self._post_request("LogOut.php", {})

    async def _post_request(self, endpoint: str, data: dict):
        url = f"{self.__base_url}{endpoint}"
        headers = {"Authorization": self._auth}
        data["auth"] = self._auth

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, data=data) as response:
                    response.raise_for_status()
                    response_text = await response.text()
                    return json.loads(response_text)
        except aiohttp.ClientError as e:
            return {"error": str(e)}

    async def get_group_data(self, guid: str):
        return await self._post_request("GetGroup.php", {'guid': guid})
    def on_message_updates_group(self, guid: str):
        def decorator(func: Callable):
            self.handlers[guid] = func
            return func
        return decorator
    async def start(self):
        last_seen_messages = {}
        while True:
            for guid, handler in self.handlers.items():
                group_data = await self.get_group_data(guid)
                if group_data:
                    last_message = group_data[-1]
                    message_id = last_message['id']
                    if last_seen_messages.get(guid) != message_id:
                        last_seen_messages[guid] = message_id
                        await handler(last_message)

    def run(self):asyncio.run(self.start())
    async def Get_username(self,username):
        data =  await self._post_request("SearchUser.php", {
            'search': username,
        })
        return data[0]
    async def SendMessageUser(self,guid,text):
        data = await self._post_request("SendMessage.php", {
            'guid': guid,
            'text': text
        })
        return data
    async def EditUsername(self,username):
        return await self._post_request("EditUser.php",{
            "username":username
        })
    async def Search_Id(self,text):
        return self._post_request("SearchUser.php",{
            'search': text,
        })
