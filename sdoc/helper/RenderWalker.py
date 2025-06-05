from typing import List


class RenderWalker:
    """
    Class for generating CSS class names when walking your representation of your HTML elements.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, module_class: str, sub_module_class: str | None = None):
        """
        Object constructor.

        :param module_class: The CSS module class.
        :param sub_module_class: The CSS submodule class.
        """
        self.module_class = module_class
        """
        The CSS module class.
        """

        self.sub_module_class = sub_module_class
        """
        The CSS submodule class.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def get_classes(self, sub_classes: str | List[str] | None = None,
                    additional_classes: str | List[str] | None = None) \
            -> List[str]:
        """
        Returns all applicable classes for an HTML element.

        :param sub_classes: The CSS subclasses with the CSS module class.
        :param additional_classes: Additional CSS classes.
        """
        classes = []

        if self.sub_module_class is not None:
            classes.append(self.sub_module_class)

        if sub_classes is not None:
            if isinstance(sub_classes, str):
                classes.append(self.module_class + '-' + sub_classes)
            elif isinstance(sub_classes, list):
                for sub_class in sub_classes:
                    classes.append(self.module_class + '-' + sub_class)
            else:
                raise TypeError(f'Argument sub_classes must be str, list or None, got {type(sub_classes)}.')

        if additional_classes is not None:
            if isinstance(additional_classes, str):
                classes.append(additional_classes)
            elif isinstance(additional_classes, list):
                classes.extend(additional_classes)
            else:
                raise TypeError(
                        f'Argument additional_classes must be str, list or None, got {type(additional_classes)}.')

        return classes

# ----------------------------------------------------------------------------------------------------------------------
