from bitsets import bitset
from copy import copy
from collections import deque


class Concept:
    def __init__(self, extent, intent):
        self._extent = extent
        self._intent = intent

    def __repr__(self):
        return "Concept({}, {})".format(repr(self._extent), repr(self._intent))

    @property
    def extent(self):
        return self._extent

    @property
    def intent(self):
        return self._intent


class Context:
    def __init__(self, matrix, Objects, Attributes):
        self.rows = tuple(map(Attributes.frombools, matrix))
        self.columns = tuple(map(Objects.frombools, zip(*matrix)))

        self._Objects = Objects
        self._Attributes = Attributes

    @classmethod
    def from_fimi(cls, filename, objects_labels=None, attribute_labels=None):
        with open(filename, 'r') as file:
            max_attribute = 0
            rows = []

            for line in file:
                # remove '\n' from line
                line = line.strip()
                row_attributes = []

                for value in line.split():
                    attribute = int(value)
                    row_attributes.append(attribute)
                    max_attribute = max(attribute, max_attribute)

                rows.append(row_attributes)

            bools = [[True if i in row else False for i in range(max_attribute + 1)]
                     for row in rows]

        if objects_labels is None:
            objects_labels = range(len(bools))

        if attribute_labels is None:
            attribute_labels = range(len(bools[0]))

        return cls(bools, bitset("Objects", objects_labels), bitset("Attributes", attribute_labels))


def calculate_all_concepts(context, up):
    initial_concept = Concept(context._Objects.supremum,
                              up(context._Objects.supremum, context))

    Attributes = context._Attributes
    Objects = context._Objects

    attribute_count = context._Attributes.supremum.count()
    concepts = []
    attribute_sets = [0] * attribute_count

    def fast_generate_from(concept: Concept, attribute: int, attribute_sets):
        concepts.append(concept)

        if concept.intent.all() or attribute >= attribute_count:
            return

        concept_queue = deque()
        attribute_queue = deque()
        set_my = copy(attribute_sets)

        for j in range(attribute, attribute_count):
            yj = 2 ** j - 1
            b = concept.intent

            x = attribute_sets[j]
            x &= yj

            y = copy(b)
            y &= yj

            if not b & 2 ** j and x & y == x:
                c = context.columns[j]
                c &= concept.extent

                d = up(c, context)

                k = copy(b)
                k &= yj

                l = copy(d)
                l &= yj

                if k == l:
                    concept_queue.append(Concept(Objects.fromint(c),
                                                 Attributes.fromint(d)))
                    attribute_queue.append(j + 1)
                else:
                    set_my[j] = d

        while concept_queue:
            fast_generate_from(concept_queue.popleft(),
                               attribute_queue.popleft(),
                               set_my)

    fast_generate_from(initial_concept, 0, attribute_sets)
    return concepts
