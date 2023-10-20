from prisma import Prisma

class PrismaConnection:

    def __init__(self):
        self.prisma=Prisma()

    async def Connect(self):
        await self.prisma.connect()

    async def Disconnect(self):
        await self.prisma.disconnect()

prisma_connection = PrismaConnection()