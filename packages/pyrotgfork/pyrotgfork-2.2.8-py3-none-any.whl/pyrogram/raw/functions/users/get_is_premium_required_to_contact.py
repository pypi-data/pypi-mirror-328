#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class GetIsPremiumRequiredToContact(TLObject):  # type: ignore
    """Check whether we can write to the specified user (this method can only be called by non-Premium users), see here » for more info on the full flow.


    Details:
        - Layer: ``199``
        - ID: ``A622AA10``

    Parameters:
        id (List of :obj:`InputUser <pyrogram.raw.base.InputUser>`):
            Users to fetch info about.

    Returns:
        List of ``bool``
    """

    __slots__: list[str] = ["id"]

    ID = 0xa622aa10
    QUALNAME = "functions.users.GetIsPremiumRequiredToContact"

    def __init__(self, *, id: list["raw.base.InputUser"]) -> None:
        self.id = id  # Vector<InputUser>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetIsPremiumRequiredToContact":
        # No flags
        
        id = TLObject.read(b)
        
        return GetIsPremiumRequiredToContact(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.id))
        
        return b.getvalue()
