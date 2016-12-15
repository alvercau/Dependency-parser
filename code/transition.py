#!/usr/bin/python

class Transition(object):
    """
    This class defines a set of transitions which are applied to a
    configuration to get the next configuration.
    """
    # Define set of transitions
    LEFT_ARC = 'LEFTARC'
    RIGHT_ARC = 'RIGHTARC'
    SHIFT = 'SHIFT'
    REDUCE = 'REDUCE'

    def __init__(self):
        raise ValueError('Do not construct this object!')

    @staticmethod
    def left_arc(conf, relation):
        """
            :param conf: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
        """
        # precondition: there has to be a stack and a buffer, the left element may not be the ROOT and the left element
        # may not be a dependent itself
        if not conf.buffer or not conf.stack:
            return -1
        idx_wi = conf.stack[-1]
        if idx_wi == 0:
            return -1
            # idx_wi may not be z in any (x,y,z) in conf.arcs
        if idx_wi in [z for x, y, z in conf.arcs]:
            return -1

        idx_wi = conf.stack.pop(-1)
        idx_wj = conf.buffer[0]
        conf.arcs.append((idx_wj, relation, idx_wi))

    @staticmethod
    def right_arc(conf, relation):
        """
            :param conf: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
        """
        if not conf.buffer or not conf.stack:
            return -1

        # You get this one for free! Use it as an example.

        idx_wi = conf.stack[-1]
        idx_wj = conf.buffer.pop(0)

        conf.stack.append(idx_wj)
        conf.arcs.append((idx_wi, relation, idx_wj))

    @staticmethod
    def reduce(conf):
        """
            :param conf: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
        """
        # precondition: wi has to be in a head
        if not conf.stack:
            return -1
        idx_wi = conf.stack[-1]
        if idx_wi not in [z for x,y,z in conf.arcs]:
            return -1

        conf.stack.pop(-1)

    @staticmethod
    def shift(conf):
        """
            :param conf: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
        """
        if not conf.buffer:
            return -1
        idx_wj = conf.buffer.pop(0)
        conf.stack.append(idx_wj)
