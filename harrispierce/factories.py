import factory

from harrispierce.models import Article, Journal, Section

class JournalFactory(factory.Factory):
    class Meta:
        model = Journal

    name = factory.sequence(lambda n: 'Journal%d'%n)

    @factory.post_generation
    def sections(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for section in extracted:
                self.sections.add(section)


class SectionFactory(factory.Factory):
    class Meta:
        model = Section

    name = factory.sequence(lambda n: 'Section%d'%n)