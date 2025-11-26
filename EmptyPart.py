# -*- coding: utf-8 -*-
from Preset.Model.PartBase import PartBase
from Preset.Model.GameObject import registerGenericClass

cntdead = 1
@registerGenericClass("EmptyPart")
class EmptyPart(PartBase):
	def __init__(self):
		PartBase.__init__(self)
		# 零件名称
		print("初始化")
		self.name = "空零件"

	def InitClient(self):
		"""
		@description 客户端的零件对象初始化入口
		"""
		print("客户端初始化")

	def InitServer(self):		
		print("服务端初始化")
		import mod.server.extraServerApi as serverApi
		serverSystem = serverApi.GetSystem("Minecraft", "preset")
		serverSystem.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "PlayerDieEvent", self, self.PlayerDie)


	def PlayerDie(self,args):
		print("玩家死亡")
		parent = self.GetParent()
		entityId = parent.GetEntityId()
		"""if args["id"] != entityId:
			return"""
		cntdead += 1
		print(cntdead)

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


		
