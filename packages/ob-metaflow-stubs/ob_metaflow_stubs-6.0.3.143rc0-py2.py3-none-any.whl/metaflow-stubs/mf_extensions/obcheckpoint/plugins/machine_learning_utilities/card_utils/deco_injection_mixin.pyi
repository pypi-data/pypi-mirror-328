######################################################################################################
#                                 Auto-generated Metaflow stub file                                  #
# MF version: 2.14.0.2rc0+obcheckpoint(0.1.8.1rc0);ob(v1)                                            #
# Generated on 2025-02-17T19:27:36.100559                                                            #
######################################################################################################

from __future__ import annotations


from ......exception import MetaflowException as MetaflowException

class CardDecoratorInjector(object, metaclass=type):
    """
    Mixin Useful for injecting @card decorators from other first class Metaflow decorators.
    """
    def attach_card_decorator(self, flow, step_name, card_id, card_type, refresh_interval = 5):
        """
        This method is called `step_init` in your StepDecorator code since
        this class is used as a Mixin
        """
        ...
    ...

