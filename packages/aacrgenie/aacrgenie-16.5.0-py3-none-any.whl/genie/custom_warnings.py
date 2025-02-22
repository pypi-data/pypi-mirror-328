class ProcessingWarning(Warning):
    """General warning for data processing"""

    pass


class RowMismatchWarning(ProcessingWarning):
    """Rows between these two datasets are not the same"""

    pass
