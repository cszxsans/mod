# -*- coding: utf-8 -*-
from Preset.Model.PartBase import PartBase
from Preset.Model.GameObject import registerGenericClass


@registerGenericClass("EmptyPart")
class EmptyPart(PartBase):
	def __init__(self):
		PartBase.__init__(self)
		# 零件名称
		self.name = "空零件"

	def InitClient(self):
		"""
		@description 客户端的零件对象初始化入口
		"""
		pass

	def InitServer(self):
		import mod.server.extraServerApi as serverApi
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerChatEvent", self, self.OnServerChat)		

	def OnServerChat(self,args):
		import mod.server.extraServerApi as serverApi
		comp = serverApi.GetEngineCompFactory().CreateWeather(serverApi.GetLevelId())
		if args["message"] == "下雨":	
			comp.SetRaining(0.5,1000)
		elif args["message"] == "停雨":
			comp.SetRaining(0,1000)
		elif args["message"] == "打雷":
			comp.SetThunder(0.5,1000)

	def TickClient(self):
		"""
		@description 客户端的零件对象逻辑驱动入口
		"""
		pass

	def TickServer(self):
		"""
		@description 服务端的零件对象逻辑驱动入口
		"""
		pass

	def DestroyClient(self):
		"""
		@description 客户端的零件对象销毁逻辑入口
		"""
		pass

	def DestroyServer(self):
		"""
		@description 服务端的零件对象销毁逻辑入口
		"""
		pass


		
