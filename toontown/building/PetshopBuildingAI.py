from panda3d.core import *
from direct.directnotify import DirectNotifyGlobal
from . import DistributedDoorAI
from . import DistributedPetshopInteriorAI
from . import FADoorCodes
from . import DoorTypes
from toontown.toon import NPCToons
from toontown.toonbase import ToontownGlobals
from toontown.quest import Quests
from toontown.pets import DistributedPetAI, PetTraits, PetUtil
from toontown.hood import ZoneUtil

class PetshopBuildingAI:

    def __init__(self, air, exteriorZone, interiorZone, blockNumber):
        self.air = air
        self.exteriorZone = exteriorZone
        self.interiorZone = interiorZone
        self.setup(blockNumber)

    def cleanup(self):
        for npc in self.npcs:
            npc.requestDelete()

        del self.npcs
        self.door.requestDelete()
        del self.door
        self.insideDoor.requestDelete()
        del self.insideDoor
        self.interior.requestDelete()
        del self.interior

    def setup(self, blockNumber):
        self.interior = DistributedPetshopInteriorAI.DistributedPetshopInteriorAI(blockNumber, self.air, self.interiorZone)
        self.npcs = NPCToons.createNpcsInZone(self.air, self.interiorZone)
        seeds = self.air.petMgr.getAvailablePets(1, len(self.npcs))
        self.interior.generateWithRequired(self.interiorZone)
        door = DistributedDoorAI.DistributedDoorAI(self.air, blockNumber, DoorTypes.EXT_STANDARD)
        insideDoor = DistributedDoorAI.DistributedDoorAI(self.air, blockNumber, DoorTypes.INT_STANDARD)
        door.setOtherDoor(insideDoor)
        insideDoor.setOtherDoor(door)
        door.zoneId = self.exteriorZone
        insideDoor.zoneId = self.interiorZone
        door.generateWithRequired(self.exteriorZone)
        insideDoor.generateWithRequired(self.interiorZone)
        self.door = door
        self.insideDoor = insideDoor