######################################################################################################
#                                 Auto-generated Metaflow stub file                                  #
# MF version: 2.14.0.1+obcheckpoint(0.1.8);ob(v1)                                                    #
# Generated on 2025-02-17T23:51:59.815639                                                            #
######################################################################################################

from __future__ import annotations

import typing
if typing.TYPE_CHECKING:
    import typing


class SerializationHandler(object, metaclass=type):
    def serialze(self, *args, **kwargs) -> typing.Union[str, bytes]:
        ...
    def deserialize(self, *args, **kwargs) -> typing.Any:
        ...
    ...

