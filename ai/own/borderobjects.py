from uz.nuu.datamining.own.functions import Distance, Table, inf_object


def borderobjects(a, classes, types = None):
    """
    :param a: objects
    :param classes: class of objects
    :param types: types of features
    :return: index's of border objects
    """

    inf_table = inf_object(a, classes, types)
    m = len(a)
    