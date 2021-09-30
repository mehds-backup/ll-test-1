class Node:
    def __new__(cls, *args, **kwargs):
        if kwargs['type'] == 'Institution':
            return InstitutionNode.__new__(*args, **kwargs)
        if kwargs['type'] == 'Milestone':
            return MilestoneNode.__new__(*args, **kwargs)


class InstitutionNode:
    pass


class MilestoneNode:
    pass
